#!/usr/bin/env python3
"""對已驗證 iTest Help retrieval index 做可重現的本地文字檢索。"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path


def force_utf8_stdout() -> None:
    """Windows 主控台預設字碼頁可能是 CP950，強制 UTF-8 輸出以免 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


SNIPPET_WINDOW = 300
SNIPPET_MAX_WINDOWS = 5
SNIPPET_SEPARATOR = "\n…\n"
MAX_LIMIT = 100
MAX_OUTPUT_BYTES = 512 * 1024
NEXT_ACTION_COMMAND = "python scripts/inspect_chunk.py <chunk-id>"
# 檢索結果只帶代表性的位置資訊，完整 locators 由 inspect_chunk.py 提供。
LOCATORS_IN_SEARCH = 2


def verify_index(index: Path) -> tuple[bool, str | None]:
    """比對索引 SHA-256 與凍結 manifest，避免引用來自偽造索引的 Chunk ID。

    `--index` 指向非預設路徑時不硬擋，只回報未驗證，保留測試與除錯彈性。
    """
    manifest = index.parent / "retrieval-index-manifest.json"
    if not manifest.is_file():
        return False, "missing retrieval-index-manifest.json"
    expected = json.loads(manifest.read_text(encoding="utf-8")).get("index_sha256", "").upper()
    actual = hashlib.sha256(index.read_bytes()).hexdigest().upper()
    if actual != expected:
        return False, f"index SHA-256 {actual} does not match the frozen {expected}"
    return True, None


def tokenize(value: str) -> list[str]:
    return [term.casefold() for term in re.findall(r"[A-Za-z0-9_./]+|[\u4e00-\u9fff]+", value) if len(term) > 1]


def score(query: str, record: dict) -> int:
    query_terms = tokenize(query)
    searchable = "\n".join(
        [record["source_file"], record["title"], " ".join(record["heading_path"]), record["text"]]
    ).casefold()
    result = 0
    phrase = query.casefold().strip()
    if phrase and phrase in searchable:
        result += 20
    for term in query_terms:
        occurrences = searchable.count(term)
        if occurrences:
            result += min(occurrences, 5)
            if term in record["title"].casefold() or term in " ".join(record["heading_path"]).casefold():
                result += 4
            if term in record["source_file"].casefold():
                result += 2
    return result


def load_index(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def snippets(text: str, query: str) -> str:
    """以查詢詞的命中位置為中心取窗，而不是取前綴。

    知識庫近半數 chunk 長於單次回傳預算，且定義性敘述常落在文件深處。取前綴會讓來源看起來
    只有開頭那段概述，導致「文件明明檢索到了，關鍵定義卻讀不到」。
    """
    if len(text) <= SNIPPET_WINDOW * SNIPPET_MAX_WINDOWS:
        return text
    lowered = text.casefold()
    terms = set(tokenize(query))
    if not terms:
        return text[:SNIPPET_WINDOW * SNIPPET_MAX_WINDOWS]
    # 全 chunk 出現次數用來壓低高頻詞的權重，否則開頭的常見字會把所有視窗吃光。
    weights = {term: 1.0 / math.sqrt(lowered.count(term)) for term in terms if lowered.count(term)}
    blocks = [lowered[start:start + SNIPPET_WINDOW] for start in range(0, len(lowered), SNIPPET_WINDOW)]
    ranked = sorted(
        range(1, len(blocks)),
        key=lambda index: (-sum(weight for term, weight in weights.items() if term in blocks[index]), index),
    )
    chosen = sorted({0, *ranked[: SNIPPET_MAX_WINDOWS - 1]})
    # 相鄰視窗必須併成連續一段，否則分隔符會把跨界的詞句攔腰切斷。
    runs: list[list[int]] = []
    for index in chosen:
        if runs and index == runs[-1][-1] + 1:
            runs[-1].append(index)
        else:
            runs.append([index])
    parts = [text[run[0] * SNIPPET_WINDOW:(run[-1] + 1) * SNIPPET_WINDOW] for run in runs]
    return SNIPPET_SEPARATOR.join(parts)


def public_result(record: dict, relevance: int, full: bool, query: str) -> dict:
    result = {key: record[key] for key in (
        "chunk_id", "source_file", "document_version", "title", "heading_path",
        "source_sha256", "content_sha256", "rag_metadata_file", "rag_metadata_line", "rag_markdown_file"
    )}
    # locators 佔整份輸出的 59%，但檢索階段只需要能標示位置的代表項；完整清單留給 inspect_chunk.py。
    result["locators"] = record["locators"][:LOCATORS_IN_SEARCH]
    result["locators_total"] = len(record["locators"])
    result["score"] = relevance
    result["text_length"] = len(record["text"])
    result["text"] = record["text"] if full else snippets(record["text"], query)
    result["text_truncated"] = len(result["text"]) < len(record["text"])
    return result


def result_index(results: list[dict]) -> list[str]:
    """一行一筆的結果索引，放在 results 之前。

    大輸出會被 agent 環境截成前 2KB 預覽，而單筆結果就超過 2KB，導致第二名以後
    在預覽中完全不可見。把名次、分數、是否為片段、來源與 chunk_id 壓成一行，
    整份索引約 1.3KB，可完整落在預覽內。

    曾經在此加上頁面 title，想讓分支限定詞在掃描階段就可見，A/B 實測 4 輪顯示
    沒有可觀測效益，已退回，理由見 FROZEN.md 的 v1.3.5 第三批條目。
    """
    return [
        f"{position}. score {entry['score']} "
        f"{'snippet' if entry['text_truncated'] else 'full'} "
        f"{entry['source_file']} :: {entry['chunk_id']}"
        for position, entry in enumerate(results, 1)
    ]


def resolve_query(args: argparse.Namespace) -> str | None:
    """`--query-file` 讓不可信文字不必經過 shell 展開就能送進檢索。

    設備錯誤訊息與日誌片段是攻擊者可控輸入，填進指令列會被 shell 做指令替換。
    位置參數保留，供 agent 自行構造的技術詞使用，行為與過去完全相同。
    """
    if args.query_file is not None:
        if not args.query_file.is_file():
            return None
        return args.query_file.read_text(encoding="utf-8").strip()
    return args.query


def main() -> int:
    force_utf8_stdout()
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="?")
    parser.add_argument("--query-file", type=Path, default=None,
                        help="從檔案讀取查詢字串，供不可信文字使用，避免 shell 指令替換")
    # 預設 10：分數常擠在很窄的區間，limit 5 會把切題但詞頻略低的來源擋在外面。
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--index", type=Path, default=Path(__file__).resolve().parents[1] / "knowledge" / "retrieval-index.jsonl")
    args = parser.parse_args()
    if args.query is not None and args.query_file is not None:
        print(json.dumps({"status": "invalid_arguments", "error": "Pass either a positional query or --query-file, not both"}, ensure_ascii=False))
        return 2
    query = resolve_query(args)
    if query is None:
        detail = f"Missing query file: {args.query_file}" if args.query_file is not None else "No query supplied"
        print(json.dumps({"status": "invalid_arguments", "error": detail}, ensure_ascii=False))
        return 2
    args.query = query
    if not args.index.is_file():
        print(json.dumps({"status": "index_invalid", "error": f"Missing index: {args.index}"}, ensure_ascii=False))
        return 2
    default_index = parser.get_default("index")
    is_default = args.index.resolve() == Path(default_index).resolve()
    verified, reason = verify_index(args.index)
    if is_default and not verified:
        print(json.dumps({"status": "integrity_error", "error": reason}, ensure_ascii=False))
        return 3
    limit = max(1, min(args.limit, MAX_LIMIT))
    scored = [(score(args.query, record), record) for record in load_index(args.index)]
    matches = [(value, record) for value, record in scored if value > 0]
    matches.sort(key=lambda item: (-item[0], item[1]["chunk_id"]))
    results = [public_result(record, value, args.full, args.query) for value, record in matches[:limit]]
    budget = MAX_OUTPUT_BYTES
    kept = []
    for entry in results:
        budget -= len(json.dumps(entry, ensure_ascii=False))
        if budget < 0 and kept:
            break
        kept.append(entry)
    truncated = [entry["chunk_id"] for entry in kept if entry["text_truncated"]]
    result = {
        "status": "ok" if matches else "no_results",
        "index_verified": verified,
        "limit_clamped": args.limit > MAX_LIMIT,
        "output_truncated": len(kept) < len(results),
        "truncated_count": len(truncated),
    }
    if kept:
        # 必須排在 results 之前，否則被預覽截斷就失去意義。
        result["result_index"] = result_index(kept)
    # query 回顯排在索引之後：貼上的錯誤訊息可能長達數百字元，放在前面會把
    # 索引的末幾筆推出 2KB 預覽，而回顯本身對掃描階段沒有價值。
    result["query"] = args.query
    result["results"] = kept
    if truncated:
        # 只放相對路徑，不寫絕對路徑：檢索輸出可能被轉貼，不應帶上使用者家目錄結構。
        result["next_action"] = (
            f"{len(truncated)} of {len(kept)} results are snippets, not full text. "
            "Before concluding the knowledge base lacks something, run "
            f"`{NEXT_ACTION_COMMAND}` on the relevant chunk_id."
        )
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
