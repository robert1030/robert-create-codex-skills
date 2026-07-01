#!/usr/bin/env python3
"""Validate the packaged iTest Help skill data contract."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG_ROOT = ROOT / "references" / "rag"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    skill_md = ROOT / "SKILL.md"
    if not skill_md.exists():
        fail("SKILL.md is missing")
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if "iTest Help 26.2.0" not in text:
        fail("SKILL.md does not mention iTest Help 26.2.0")
    if "name: itest-help-skill" not in text:
        fail("SKILL.md name is wrong")
    if not (ROOT / "agents" / "openai.yaml").exists():
        fail("agents/openai.yaml is missing")
    agent_text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8", errors="replace")
    if "$itest-help-skill" not in agent_text:
        fail("agents/openai.yaml default_prompt must contain $itest-help-skill")

    required = [
        "manifest.md",
        "validation_report.md",
        "chunk_manifest.jsonl",
        "index_manifest.jsonl",
        "inventory.json",
    ]
    for name in required:
        if not (RAG_ROOT / name).exists():
            fail(f"missing references/rag/{name}")
    if not (RAG_ROOT / "text").is_dir():
        fail("references/rag/text is missing")
    if not (RAG_ROOT / "images").is_dir():
        fail("references/rag/images is missing")

    text_count = image_count = missing = 0
    with (RAG_ROOT / "chunk_manifest.jsonl").open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            record = json.loads(line)
            if record.get("kind") == "text":
                text_count += 1
                path = RAG_ROOT / "text" / f"{record.get('chunk_id')}.md"
            elif record.get("kind") == "image":
                image_count += 1
                path = RAG_ROOT / "images" / f"{record.get('image_chunk_id')}.md"
            else:
                fail(f"unknown chunk kind: {record.get('kind')}")
            if not path.exists():
                missing += 1
    if text_count != 2891:
        fail(f"expected 2891 text chunks, found {text_count}")
    if image_count != 1221:
        fail(f"expected 1221 image chunks, found {image_count}")
    if missing:
        fail(f"manifest points to {missing} missing chunk files")

    print("OK: iTest Help skill data contract is valid")
    print(f"text_chunks={text_count} image_chunks={image_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
