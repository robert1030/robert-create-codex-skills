#!/usr/bin/env python
"""Inspect one bundled iTest Help RAG chunk by ID."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


DEFAULT_RAG_PATH = Path(__file__).resolve().parents[1] / "references" / "rag"


def load_rows(rag_path: Path) -> list[dict]:
    rows: list[dict] = []
    with (rag_path / "chunk_manifest.jsonl").open("r", encoding="utf-8") as raw:
        for line in raw:
            text = line.strip()
            if text:
                rows.append(json.loads(text))
    return rows


def inspect_chunk(chunk_id: str, rag_path: Path) -> tuple[dict, str]:
    if not rag_path.exists():
        raise FileNotFoundError(f"RAG path not found: {rag_path}")
    if not rag_path.is_dir():
        raise ValueError(f"RAG path must be an extracted directory: {rag_path}")
    rows = load_rows(rag_path)
    for row in rows:
        if row.get("chunk_id") == chunk_id:
            body_path = rag_path / "text" / row["source_file"]
            return row, body_path.read_text(encoding="utf-8", errors="replace")
        if row.get("image_chunk_id") == chunk_id:
            body_path = rag_path / "images" / row["source_file"]
            return row, body_path.read_text(encoding="utf-8", errors="replace")
    raise KeyError(f"Chunk not found: {chunk_id}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("chunk_id", help="A text chunk_id or image_chunk_id.")
    parser.add_argument("--rag-path", type=Path, default=DEFAULT_RAG_PATH)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        row, body = inspect_chunk(args.chunk_id, args.rag_path)
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({"metadata": row, "body": body}, ensure_ascii=False, indent=2))
        return 0

    print("metadata:")
    print(json.dumps(row, ensure_ascii=False, indent=2))
    print()
    print("body:")
    print(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
