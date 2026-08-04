#!/usr/bin/env python3
"""對已驗證 iTest Help retrieval index 做可重現的本地文字檢索。"""

from __future__ import annotations

import argparse
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
        "chunk_id", "source_file", "document_version", "title", "heading_path", "locators",
        "source_sha256", "content_sha256", "rag_metadata_file", "rag_metadata_line", "rag_markdown_file"
    )}
    result["score"] = relevance
    result["text_length"] = len(record["text"])
    result["text"] = record["text"] if full else snippets(record["text"], query)
    result["text_truncated"] = len(result["text"]) < len(record["text"])
    return result


def main() -> int:
    force_utf8_stdout()
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    # 預設 10：分數常擠在很窄的區間，limit 5 會把切題但詞頻略低的來源擋在外面。
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--index", type=Path, default=Path(__file__).resolve().parents[1] / "knowledge" / "retrieval-index.jsonl")
    args = parser.parse_args()
    if not args.index.is_file():
        print(json.dumps({"status": "index_invalid", "error": f"Missing index: {args.index}"}, ensure_ascii=False))
        return 2
    scored = [(score(args.query, record), record) for record in load_index(args.index)]
    matches = [(value, record) for value, record in scored if value > 0]
    matches.sort(key=lambda item: (-item[0], item[1]["chunk_id"]))
    result = {
        "status": "ok" if matches else "no_results",
        "query": args.query,
        "results": [public_result(record, value, args.full, args.query) for value, record in matches[:max(1, args.limit)]],
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
