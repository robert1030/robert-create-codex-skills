#!/usr/bin/env python3
"""以 Chunk ID 取得完整可引用的 iTest Help 記錄。"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def force_utf8_stdout() -> None:
    """Windows 主控台預設字碼頁可能是 CP950，強制 UTF-8 輸出以免 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def main() -> int:
    force_utf8_stdout()
    parser = argparse.ArgumentParser()
    parser.add_argument("chunk_id")
    parser.add_argument("--index", type=Path, default=Path(__file__).resolve().parents[1] / "knowledge" / "retrieval-index.jsonl")
    args = parser.parse_args()
    if not args.index.is_file():
        print(json.dumps({"status": "index_invalid", "error": f"Missing index: {args.index}"}, ensure_ascii=False))
        return 2
    with args.index.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record = json.loads(line)
                if record["chunk_id"] == args.chunk_id:
                    print(json.dumps({"status": "ok", "record": record}, ensure_ascii=False))
                    return 0
    print(json.dumps({"status": "not_found", "chunk_id": args.chunk_id}, ensure_ascii=False))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
