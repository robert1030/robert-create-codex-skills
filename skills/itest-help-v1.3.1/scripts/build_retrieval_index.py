#!/usr/bin/env python3
"""從已驗證 RAG Chunk metadata 建立 Agent 與 Chat Web 的查詢載荷。"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def load_collection_members(rag_root: Path) -> dict[str, dict]:
    reports = list(rag_root.glob("collection-report-*.json"))
    if len(reports) != 1:
        raise ValueError(f"Expected one collection report in {rag_root}, found {len(reports)}")
    report = json.loads(reports[0].read_text(encoding="utf-8"))
    return {member["source_id"]: member for member in report["members"] if member.get("source_id")}


def iter_raw_chunks(rag_root: Path):
    for metadata_path in sorted(rag_root.rglob("chunks.jsonl")):
        with metadata_path.open(encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, 1):
                if line.strip():
                    yield metadata_path, line_number, json.loads(line)


def build_records(skill_root: Path) -> list[dict]:
    rag_root = skill_root / "knowledge" / "rag" / "v1.2.1-full-visual-semantics-20260730"
    members = load_collection_members(rag_root)
    records: list[dict] = []
    for metadata_path, line_number, chunk in iter_raw_chunks(rag_root):
        source_id = chunk["source_id"]
        member = members.get(source_id)
        if member is None:
            raise ValueError(f"Chunk references unknown source_id: {source_id}")
        text = chunk.get("text") or chunk.get("markdown_body") or ""
        records.append(
            {
                "chunk_id": chunk["chunk_id"],
                "source_file": member["relative_path"],
                "document_version": "26.2.0",
                "title": chunk.get("title", ""),
                "heading_path": chunk.get("heading_path", []),
                "locators": chunk.get("locators", []),
                "source_sha256": chunk["source_hash"],
                "content_sha256": chunk["content_sha256"],
                "rag_metadata_file": metadata_path.relative_to(skill_root).as_posix(),
                "rag_metadata_line": line_number,
                "rag_markdown_file": (metadata_path.parent / chunk["markdown_file"]).relative_to(skill_root).as_posix(),
                "text": text,
            }
        )
    chunk_ids = [record["chunk_id"] for record in records]
    if len(chunk_ids) != len(set(chunk_ids)):
        raise ValueError("Duplicate chunk_id detected while building retrieval index")
    return records


def write_jsonl(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def write_chat_web_knowledge(path: Path, records: list[dict]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write("# iTest Help 26.2.0 verified knowledge\n\n")
        handle.write("Only answer from records that directly support the claim. Preserve the source fields in citations.\n")
        for record in records:
            heading = " / ".join(record["heading_path"]) or record["title"] or "Untitled"
            location = json.dumps(record["locators"], ensure_ascii=False, separators=(",", ":"))
            handle.write("\n## Chunk ID: " + record["chunk_id"] + "\n")
            handle.write("- Source file: " + record["source_file"] + "\n")
            handle.write("- Document version: " + record["document_version"] + "\n")
            handle.write("- Section: " + heading + "\n")
            handle.write("- Location: " + location + "\n")
            handle.write("- Source SHA-256: " + record["source_sha256"] + "\n")
            handle.write("- Content SHA-256: " + record["content_sha256"] + "\n\n")
            handle.write(record["text"].rstrip() + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_root", nargs="?", default=Path(__file__).resolve().parents[1], type=Path)
    args = parser.parse_args()
    skill_root = args.skill_root.resolve()
    knowledge_root = skill_root / "knowledge"
    records = build_records(skill_root)
    index_path = knowledge_root / "retrieval-index.jsonl"
    chat_path = knowledge_root / "chat-web-knowledge.md"
    write_jsonl(index_path, records)
    write_chat_web_knowledge(chat_path, records)
    manifest = {
        "record_count": len(records),
        "index_file": index_path.name,
        "index_sha256": sha256_file(index_path),
        "chat_web_file": chat_path.name,
        "chat_web_sha256": sha256_file(chat_path),
        "derivation": "chunks.jsonl plus collection member metadata only",
    }
    (knowledge_root / "retrieval-index-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps(manifest, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
