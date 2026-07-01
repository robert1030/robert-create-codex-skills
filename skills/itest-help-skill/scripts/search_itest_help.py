#!/usr/bin/env python3
"""Search packaged iTest 26.2 help RAG chunks without external dependencies."""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG_ROOT = ROOT / "references" / "rag"
CHUNK_MANIFEST = RAG_ROOT / "chunk_manifest.jsonl"

TOKEN_RE = re.compile(r"[A-Za-z0-9_.$:-]+")


@dataclass
class Result:
    score: int
    record: dict
    snippet: str


def tokenize(text: str) -> list[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "") if len(t) > 1]


def load_records() -> list[dict]:
    if not CHUNK_MANIFEST.exists():
        raise SystemExit(f"Missing manifest: {CHUNK_MANIFEST}")
    records = []
    with CHUNK_MANIFEST.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                records.append(json.loads(line))
    return records


def chunk_path(record: dict) -> Path:
    if record.get("kind") == "text":
        return RAG_ROOT / "text" / f"{record['chunk_id']}.md"
    return RAG_ROOT / "images" / f"{record['image_chunk_id']}.md"


def read_body(path: Path, max_chars: int = 20000) -> str:
    text = path.read_text(encoding="utf-8", errors="replace")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            text = parts[2]
    return text[:max_chars]


def compact(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " > ".join(str(v) for v in value)
    return str(value)


def score_record(record: dict, query_tokens: list[str], phrase: str, include_images: bool) -> Result | None:
    if record.get("kind") == "image" and not include_images:
        return None

    path = chunk_path(record)
    if not path.exists():
        return None

    title_fields = " ".join([
        compact(record.get("heading_path")),
        compact(record.get("toc_path")),
        compact(record.get("index_keywords")),
        compact(record.get("index_keyword_paths")),
        compact(record.get("context_ids")),
        record.get("source_file", ""),
        record.get("source_original_path", ""),
    ]).lower()
    body = read_body(path)
    body_lower = body.lower()

    score = 0
    if phrase and phrase in title_fields:
        score += 80
    if phrase and phrase in body_lower:
        score += 25
    for token in query_tokens:
        if token in title_fields:
            score += 12
        if token in body_lower:
            score += 3
    if record.get("kind") == "text":
        score += 3
    if record.get("index_keywords"):
        score += 2
    if record.get("context_ids"):
        score += 2

    if score <= 0:
        return None

    snippet = make_snippet(body, query_tokens)
    return Result(score=score, record=record, snippet=snippet)


def make_snippet(body: str, query_tokens: list[str]) -> str:
    plain = re.sub(r"\s+", " ", body).strip()
    lower = plain.lower()
    pos = -1
    for token in query_tokens:
        pos = lower.find(token)
        if pos >= 0:
            break
    if pos < 0:
        return plain[:280]
    start = max(0, pos - 100)
    end = min(len(plain), pos + 220)
    prefix = "..." if start else ""
    suffix = "..." if end < len(plain) else ""
    return prefix + plain[start:end] + suffix


def format_result(index: int, result: Result) -> str:
    r = result.record
    chunk_id = r.get("chunk_id") or r.get("image_chunk_id")
    lines = [
        f"[{index}] score={result.score} kind={r.get('kind')} id={chunk_id}",
        f"source_file: {r.get('source_file') or r.get('image_path')}",
        f"toc_path: {compact(r.get('toc_path')) or '<none>'}",
        f"heading_path: {compact(r.get('heading_path')) or '<none>'}",
    ]
    if r.get("index_keywords"):
        lines.append(f"index_keywords: {compact(r.get('index_keywords'))}")
    if r.get("category"):
        lines.append(f"image_category: {r.get('category')} ocr_status={r.get('ocr_status')} has_ocr_text={r.get('has_ocr_text')}")
    lines.append(f"snippet: {result.snippet}")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Search packaged iTest 26.2 help chunks.")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--limit", type=int, default=8, help="Maximum results")
    parser.add_argument("--include-images", action="store_true", help="Include image OCR chunks")
    args = parser.parse_args(argv)

    query_tokens = tokenize(args.query)
    phrase = args.query.lower().strip()
    if not query_tokens:
        raise SystemExit("Query must contain at least one searchable token.")

    results = []
    for record in load_records():
        result = score_record(record, query_tokens, phrase, args.include_images)
        if result:
            results.append(result)

    results.sort(key=lambda item: item.score, reverse=True)
    for idx, result in enumerate(results[: max(0, args.limit)], 1):
        print(format_result(idx, result))
        print()
    if not results:
        print("No matching iTest help chunks found.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
