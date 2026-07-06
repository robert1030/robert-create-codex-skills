#!/usr/bin/env python
"""Validate the iTest Help Skill package contract."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_ROOT / "SKILL.md"
OPENAI_YAML = SKILL_ROOT / "agents" / "openai.yaml"
RAG_DIR = SKILL_ROOT / "references" / "rag"

EXPECTED_TEXT_CHUNKS = 3012
EXPECTED_IMAGE_CHUNKS = 1799
REQUIRED_TRIGGER_TERMS = [
    "itest help",
    "itest gui",
    "itest tcl",
    "itest python",
    "itest analysis",
]


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)
    print(f"FAIL: {message}")


def ok(message: str) -> None:
    print(f"OK: {message}")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def parse_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    if not match:
        raise ValueError("SKILL.md has no YAML frontmatter at byte zero.")
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_skill_text(failures: list[str]) -> None:
    if not SKILL_MD.exists():
        fail("SKILL.md is missing.", failures)
        return
    text = read_text(SKILL_MD)
    try:
        meta = parse_frontmatter(text)
    except Exception as exc:
        fail(str(exc), failures)
        return
    if meta.get("name") != "itest-help-skill":
        fail("SKILL.md name must be itest-help-skill.", failures)
    else:
        ok("SKILL.md name is itest-help-skill.")
    description = meta.get("description", "")
    if len(description) > 1024:
        fail("SKILL.md description exceeds 1024 characters.", failures)
    else:
        ok("SKILL.md description length is within 1024 characters.")
    lower_text = text.lower()
    for term in REQUIRED_TRIGGER_TERMS:
        if term not in lower_text:
            fail(f"Required trigger term missing from SKILL.md: {term}", failures)
        else:
            ok(f"Required trigger term present: {term}")
    if "External source" not in text:
        fail("External-source fallback rule is missing.", failures)
    else:
        ok("External-source fallback rule is present.")


def validate_openai_yaml(failures: list[str]) -> None:
    if not OPENAI_YAML.exists():
        fail("agents/openai.yaml is missing.", failures)
        return
    text = read_text(OPENAI_YAML)
    for required in ["display_name:", "short_description:", "default_prompt:"]:
        if required not in text:
            fail(f"agents/openai.yaml missing {required}", failures)
        else:
            ok(f"agents/openai.yaml contains {required}")
    if "$itest-help-skill" not in text:
        fail("agents/openai.yaml must preserve literal $itest-help-skill.", failures)
    else:
        ok("agents/openai.yaml preserves literal $itest-help-skill.")
    if "allow_implicit_invocation: true" not in text:
        fail("agents/openai.yaml must set allow_implicit_invocation: true.", failures)
    else:
        ok("agents/openai.yaml allows implicit invocation.")


def validate_rag_zip(failures: list[str]) -> None:
    if not RAG_DIR.exists():
        fail("Bundled extracted RAG directory is missing.", failures)
        return
    if not RAG_DIR.is_dir():
        fail("Bundled RAG path must be an extracted directory.", failures)
        return
    for required in [
        "manifest.md",
        "validation_report.md",
        "inventory.json",
        "index_manifest.jsonl",
        "chunk_manifest.jsonl",
    ]:
        if not (RAG_DIR / required).exists():
            fail(f"RAG directory missing {required}.", failures)
        else:
            ok(f"RAG directory contains {required}.")

    text_chunks = list((RAG_DIR / "text").glob("*.md"))
    image_chunks = list((RAG_DIR / "images").glob("*.md"))
    if len(text_chunks) != EXPECTED_TEXT_CHUNKS:
        fail(f"Expected {EXPECTED_TEXT_CHUNKS} text chunks, found {len(text_chunks)}.", failures)
    else:
        ok(f"Text chunk count is {EXPECTED_TEXT_CHUNKS}.")
    if len(image_chunks) != EXPECTED_IMAGE_CHUNKS:
        fail(f"Expected {EXPECTED_IMAGE_CHUNKS} image chunks, found {len(image_chunks)}.", failures)
    else:
        ok(f"Image chunk count is {EXPECTED_IMAGE_CHUNKS}.")

    chunk_lines = 0
    source_paths: set[str] = set()
    with (RAG_DIR / "chunk_manifest.jsonl").open("r", encoding="utf-8") as raw:
        for line in raw:
            if not line.strip():
                continue
            chunk_lines += 1
            row = json.loads(line)
            if row.get("source_original_path"):
                source_paths.add(row["source_original_path"])
    if chunk_lines != EXPECTED_TEXT_CHUNKS:
        fail(f"Expected {EXPECTED_TEXT_CHUNKS} chunk manifest rows, found {chunk_lines}.", failures)
    else:
        ok(f"Chunk manifest row count is {EXPECTED_TEXT_CHUNKS}.")
    if not source_paths:
        fail("No source_original_path values found in chunk manifest.", failures)
    else:
        ok(f"Chunk manifest has {len(source_paths)} unique source_original_path values.")


def main() -> int:
    failures: list[str] = []
    validate_skill_text(failures)
    validate_openai_yaml(failures)
    validate_rag_zip(failures)
    if failures:
        print()
        print(f"Validation failed with {len(failures)} issue(s).")
        return 1
    print()
    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
