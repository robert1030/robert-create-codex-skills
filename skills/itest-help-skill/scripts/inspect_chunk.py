#!/usr/bin/env python3
"""Print one packaged iTest help chunk by text chunk id or image chunk id."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG_ROOT = ROOT / "references" / "rag"
CHUNK_MANIFEST = RAG_ROOT / "chunk_manifest.jsonl"


def load_manifest() -> dict[str, dict]:
    records = {}
    with CHUNK_MANIFEST.open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            record = json.loads(line)
            key = record.get("chunk_id") or record.get("image_chunk_id")
            if key:
                records[key] = record
    return records


def chunk_path(record: dict) -> Path:
    if record.get("kind") == "text":
        return RAG_ROOT / "text" / f"{record['chunk_id']}.md"
    return RAG_ROOT / "images" / f"{record['image_chunk_id']}.md"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Inspect a packaged iTest help chunk.")
    parser.add_argument("chunk_id", help="Text chunk_id or image_chunk_id")
    args = parser.parse_args(argv)

    records = load_manifest()
    record = records.get(args.chunk_id)
    if not record:
        print(f"Chunk not found: {args.chunk_id}", file=sys.stderr)
        return 1
    path = chunk_path(record)
    if not path.exists():
        print(f"Chunk file missing: {path}", file=sys.stderr)
        return 1
    print(path.read_text(encoding="utf-8", errors="replace"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
