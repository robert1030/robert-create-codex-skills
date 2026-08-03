#!/usr/bin/env python3
"""Build a path-shortened derivative of the verified itest-help skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path


RAG_VERSION = "v1.2.1-full-visual-semantics-20260730"


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest().upper()


def replace_text(path: Path, replacements: tuple[tuple[str, str], ...]) -> None:
    text = path.read_text(encoding="utf-8")
    for old, new in replacements:
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8", newline="\n")


def move_chunks(root: Path) -> int:
    moved = 0
    for path in sorted(root.rglob("chunks"), key=lambda item: len(item.parts), reverse=True):
        if path.is_dir():
            target = path.with_name("c")
            path.rename(target)
            moved += 1
    for metadata in root.rglob("chunks.jsonl"):
        replace_text(metadata, (("\"markdown_file\": \"chunks/", "\"markdown_file\": \"c/"),))
    return moved


def run(command: list[str], cwd: Path) -> None:
    completed = subprocess.run(command, cwd=cwd, text=True, encoding="utf-8")
    if completed.returncode:
        raise RuntimeError("Command failed: " + " ".join(command))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    args = parser.parse_args()
    source = args.source.resolve()
    target = args.target.resolve()
    if not (source / "SKILL.md").is_file():
        raise ValueError(f"Missing source SKILL.md: {source}")
    if target.exists():
        raise ValueError(f"Refusing to overwrite target: {target}")

    shutil.copytree(source, target)
    knowledge = target / "knowledge"
    compact_knowledge = target / "k"
    knowledge.rename(compact_knowledge)
    old_rag = compact_knowledge / "rag" / RAG_VERSION
    compact_rag = compact_knowledge / "r" / "r"
    compact_rag.parent.mkdir(parents=True, exist_ok=True)
    old_rag.rename(compact_rag)
    (compact_knowledge / "rag").rmdir()
    renamed_chunk_dirs = move_chunks(compact_rag)

    for script_name in ("build_retrieval_index.py", "search_itest_help.py", "inspect_chunk.py", "validate_itest_help.py"):
        replace_text(target / "scripts" / script_name, (
            ('"knowledge"', '"k"'),
            ("knowledge/", "k/"),
            ('"rag" / "v1.2.1-full-visual-semantics-20260730"', '"r" / "r"'),
            ('root / "k" / "rag"', 'root / "k" / "r" / "r"'),
        ))
    for document in (target / "SKILL.md", target / "README.md"):
        replace_text(document, (("knowledge/", "k/"),))

    manifest_path = target / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["skill_version"] = "1.1.0-windows-portable"
    manifest["deployment_targets"]["windows_portable_agent"] = "ready_after_path_and_regression_validation"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    frozen = target / "FROZEN.md"
    frozen.write_text(
        frozen.read_text(encoding="utf-8")
        + "\n## v1.1.0-windows-portable\n\n"
        + "- 此為衍生發行版，不修改 v1.0.0 原始 skill 或原始 ZIP。\n"
        + "- RAG 檔案內容、Chunk ID、來源 SHA-256 與內容 SHA-256 保持；僅縮短目錄名稱並重建索引的實體路徑。\n"
        + "- portable RAG 根目錄固定為 `k/r/r`，Chunk 目錄固定為 `c`。\n",
        encoding="utf-8", newline="\n",
    )
    layout = {
        "format": "itest-help-windows-portable-1",
        "source_skill_sha256": digest(source / "manifest.json"),
        "source_rag_root": f"knowledge/rag/{RAG_VERSION}",
        "portable_rag_root": "k/r/r",
        "renamed_chunks_directories": renamed_chunk_dirs,
        "payload_file_count": sum(1 for path in compact_rag.rglob("*") if path.is_file()),
        "contract": "RAG payload bytes are preserved except chunks.jsonl markdown_file paths, which point to renamed c directories.",
    }
    (compact_knowledge / "portable-layout.json").write_text(
        json.dumps(layout, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    run([sys.executable, "scripts/build_retrieval_index.py", "."], target)
    run([sys.executable, "scripts/validate_itest_help.py", "."], target)
    run([sys.executable, "scripts/run_regression_tests.py", "."], target)
    print(json.dumps(layout, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
