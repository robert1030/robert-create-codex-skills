#!/usr/bin/env python
"""Search bundled iTest Help 26.2.0 RAG chunks."""

from __future__ import annotations

import argparse
import json
import re
import sys
import textwrap
from pathlib import Path


DEFAULT_RAG_PATH = Path(__file__).resolve().parents[1] / "references" / "rag"


def tokenize(query: str) -> list[str]:
    return [part.lower() for part in re.findall(r"[A-Za-z0-9_./#-]+", query) if len(part) > 1]


def load_manifest(rag_path: Path) -> list[dict]:
    rows: list[dict] = []
    manifest_path = rag_path / "chunk_manifest.jsonl"
    with manifest_path.open("r", encoding="utf-8") as raw:
        for line in raw:
            line_text = line.strip()
            if line_text:
                rows.append(json.loads(line_text))
    return rows


def metadata_text(row: dict) -> str:
    fields = [
        row.get("chunk_id", ""),
        row.get("source_original_path", ""),
        " ".join(row.get("toc_path") or []),
        " ".join(row.get("heading_path") or []),
        row.get("breadcrumb", ""),
        " ".join(row.get("context_ids") or []),
        " ".join(row.get("index_keywords") or []),
        " ".join(" > ".join(path) for path in (row.get("index_keyword_paths") or [])),
    ]
    return " ".join(str(field) for field in fields if field)


def score_row(query: str, terms: list[str], row: dict, body: str) -> int:
    query_lower = query.lower()
    body_lower = body.lower()
    meta_lower = metadata_text(row).lower()
    score = 0
    if query_lower and query_lower in body_lower:
        score += 80
    if query_lower and query_lower in meta_lower:
        score += 120
    for term in terms:
        body_hits = body_lower.count(term)
        meta_hits = meta_lower.count(term)
        score += min(body_hits, 8) * 8
        score += min(meta_hits, 5) * 20
    if row.get("index_keywords"):
        score += 4
    if row.get("context_ids"):
        score += 3
    return score


def compact_preview(text: str, query_terms: list[str], width: int = 420) -> str:
    collapsed = re.sub(r"\s+", " ", text).strip()
    lower = collapsed.lower()
    start = 0
    for term in query_terms:
        idx = lower.find(term)
        if idx >= 0:
            start = max(0, idx - 120)
            break
    preview = collapsed[start : start + width]
    return textwrap.shorten(preview, width=width, placeholder=" ...")


def search(query: str, rag_path: Path, limit: int) -> list[dict]:
    terms = tokenize(query)
    if not terms:
        raise ValueError("Query must contain at least one searchable term.")
    if not rag_path.exists():
        raise FileNotFoundError(f"RAG path not found: {rag_path}")
    if not rag_path.is_dir():
        raise ValueError(f"RAG path must be an extracted directory: {rag_path}")

    results: list[dict] = []
    for row in load_manifest(rag_path):
        source_file = row.get("source_file")
        if not source_file:
            continue
        body_path = rag_path / "text" / source_file
        if not body_path.exists():
            continue
        body = body_path.read_text(encoding="utf-8", errors="replace")
        score = score_row(query, terms, row, body)
        if score <= 0:
            continue
        results.append(
            {
                "score": score,
                "chunk_id": row.get("chunk_id"),
                "source_original_path": row.get("source_original_path"),
                "toc_path": row.get("toc_path") or [],
                "heading_path": row.get("heading_path") or [],
                "char_count": row.get("char_count"),
                "preview": compact_preview(body, terms),
            }
        )
    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:limit]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Search query, for example: itest python driver")
    parser.add_argument("--rag-path", type=Path, default=DEFAULT_RAG_PATH)
    parser.add_argument("--limit", type=int, default=8)
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    args = parser.parse_args(argv)

    try:
        results = search(args.query, args.rag_path, args.limit)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return 0 if results else 1

    if not results:
        print("No local iTest Help RAG results found.")
        print("Next step: use external lookup if tools are available, and label the source as External source.")
        return 1

    for idx, item in enumerate(results, 1):
        toc = " > ".join(item["toc_path"])
        heading = " > ".join(item["heading_path"])
        print(f"[{idx}] score={item['score']} chunk_id={item['chunk_id']}")
        print(f"source_original_path: {item['source_original_path']}")
        print(f"toc_path: {toc}")
        print(f"heading_path: {heading}")
        print(f"preview: {item['preview']}")
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
