#!/usr/bin/env python3
"""以 Chunk ID 取得完整可引用的 iTest Help 記錄。"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def force_utf8_stdout() -> None:
    """Windows 主控台預設字碼頁可能是 CP950，強制 UTF-8 輸出以免 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def verify_index(index: Path) -> tuple[bool, str | None]:
    """比對索引 SHA-256 與凍結 manifest，避免引用來自偽造索引的 Chunk ID。"""
    manifest = index.parent / "retrieval-index-manifest.json"
    if not manifest.is_file():
        return False, "missing retrieval-index-manifest.json"
    expected = json.loads(manifest.read_text(encoding="utf-8")).get("index_sha256", "").upper()
    actual = hashlib.sha256(index.read_bytes()).hexdigest().upper()
    if actual != expected:
        return False, f"index SHA-256 {actual} does not match the frozen {expected}"
    return True, None


def main() -> int:
    force_utf8_stdout()
    parser = argparse.ArgumentParser()
    parser.add_argument("chunk_id")
    parser.add_argument("--index", type=Path, default=Path(__file__).resolve().parents[1] / "knowledge" / "retrieval-index.jsonl")
    args = parser.parse_args()
    if not args.index.is_file():
        print(json.dumps({"status": "index_invalid", "error": f"Missing index: {args.index}"}, ensure_ascii=False))
        return 2
    verified, reason = verify_index(args.index)
    if args.index.resolve() == Path(parser.get_default("index")).resolve() and not verified:
        print(json.dumps({"status": "integrity_error", "error": reason}, ensure_ascii=False))
        return 3
    with args.index.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                record = json.loads(line)
                if record["chunk_id"] == args.chunk_id:
                    print(json.dumps({"status": "ok", "index_verified": verified, "record": record}, ensure_ascii=False))
                    return 0
    print(json.dumps({"status": "not_found", "chunk_id": args.chunk_id}, ensure_ascii=False))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
