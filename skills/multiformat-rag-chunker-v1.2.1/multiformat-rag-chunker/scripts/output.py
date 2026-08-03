#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write the fixed per-source output contract and cryptographic manifest."""

from __future__ import annotations

import importlib.metadata
import json
import shutil
from pathlib import Path
from typing import Any

from constants import (
    CHUNKS_DIR,
    CHUNKS_JSONL,
    DOCUMENT_IR_JSONL,
    EXIT_FATAL,
    EXIT_PARTIAL_SUCCESS,
    EXIT_SUCCESS,
    FAILED_JSONL,
    MANIFEST_JSON,
    NORMALIZED_MD,
    REPORT_JSON,
    SKILL_VERSION,
)
from coverage import runtime_failure_category
from models import Chunk, DocumentIR, FailureItem
from utils import sha256_file, sha256_text, write_json, write_jsonl


def _version(package: str) -> str | None:
    try:
        return importlib.metadata.version(package)
    except importlib.metadata.PackageNotFoundError:
        return None


def status_exit_code(status: str) -> int:
    if status == "success":
        return EXIT_SUCCESS
    if status == "partial_success":
        return EXIT_PARTIAL_SUCCESS
    return EXIT_FATAL


def _next_action(reason: str | None) -> str:
    if reason == "needs_capability":
        return "agent_evaluate_safe_capability_fulfillment_or_equivalent"
    if reason == "needs_source":
        return "obtain_readable_source_or_required_attachment"
    return "retry_distinct_source_preserving_strategy"


def failure_records(document: DocumentIR) -> list[FailureItem]:
    failures: list[FailureItem] = []
    verified_blocks = [block.block_id for block in document.blocks if block.status == "success"]
    for block in document.blocks:
        if block.status not in {"failed", "low_quality"}:
            continue
        reason = block.metadata.get("reason") or ", ".join(block.metadata.get("quality_reasons", [])) or "content_quality_gate_failed"
        runtime_reason = runtime_failure_category([block])
        failures.append(FailureItem(
            source_id=document.source_id,
            source_file=document.provenance.user_specified_name,
            block_id=block.block_id,
            failure_stage="adapter_or_enrichment",
            failure_reason=runtime_reason or str(reason),
            attempts=len(block.attempts),
            required=block.required,
            critical=block.critical,
            location=block.location.to_dict(),
            details={
                "type": block.type,
                "content_origin": block.content_origin,
                "observed_failure_reason": str(reason),
                "completed_scope": {
                    "verified_block_count": len(verified_blocks),
                    "verified_block_ids": verified_blocks,
                },
                "missing_scope": {"block_id": block.block_id, "required": block.required, "critical": block.critical},
                "next_action": _next_action(runtime_reason),
                "metadata": block.metadata,
                "attempt_history": [attempt.to_dict() for attempt in block.attempts],
            },
        ))
    return failures


def _chunk_markdown(chunk: Chunk, content_sha256: str) -> str:
    try:
        import yaml
        frontmatter = yaml.safe_dump({
            "chunk_id": chunk.chunk_id,
            "source_id": chunk.source_id,
            "title": chunk.title,
            "heading_path": chunk.heading_path,
            "section_titles": chunk.section_titles,
            "source_block_ids": chunk.source_block_ids,
            "overlap_block_ids": chunk.overlap_block_ids,
            "overlap_token_count": chunk.overlap_token_count,
            "token_estimate": chunk.token_estimate,
            "source_hash": chunk.source_hash,
            "normalized_document_hash": chunk.normalized_document_hash,
            "content_status": chunk.content_status,
            "content_sha256": content_sha256,
        }, allow_unicode=True, sort_keys=False).strip()
    except Exception:
        frontmatter = json.dumps({
            "chunk_id": chunk.chunk_id,
            "source_id": chunk.source_id,
            "content_sha256": content_sha256,
        }, ensure_ascii=False)
    return f"---\n{frontmatter}\n---\n\n{chunk.markdown_body.rstrip()}\n"


def _clear_chunk_outputs(source_dir: Path) -> None:
    chunks_dir = source_dir / CHUNKS_DIR
    if chunks_dir.exists():
        shutil.rmtree(chunks_dir)
    chunks_jsonl = source_dir / CHUNKS_JSONL
    if chunks_jsonl.exists():
        chunks_jsonl.unlink()


def write_source_output(
    source_dir: Path,
    document: DocumentIR,
    normalized_markdown: str,
    chunks: list[Chunk],
    coverage: dict[str, Any],
    chunk_validation: dict[str, Any],
    final_status: str,
    *,
    parameters: dict[str, Any],
    validation_summary: dict[str, Any] | None = None,
    forensic_dir: Path | None = None,
) -> None:
    source_dir.mkdir(parents=True, exist_ok=True)
    if forensic_dir is not None:
        forensic_target = source_dir / "forensic"
        forensic_target.mkdir(parents=True, exist_ok=True)
        if forensic_dir.exists():
            shutil.copytree(forensic_dir, forensic_target, dirs_exist_ok=True)
        for name in ("source-assets", "rendered-pages", "crops", "preprocessed", "ocr-candidates", "overlays"):
            (forensic_target / name).mkdir(parents=True, exist_ok=True)
        forensic_files = sorted(
            path.relative_to(forensic_target).as_posix()
            for path in forensic_target.rglob("*")
            if path.is_file() and path.name != "debug-report.json"
        )
        write_json(forensic_target / "debug-report.json", {
            "mode": "forensic",
            "available_files": forensic_files,
            "notes": ["Only artifacts produced by executed backends are populated. Empty directories do not imply a backend ran."],
        })
    (source_dir / NORMALIZED_MD).write_text(normalized_markdown, encoding="utf-8", newline="\n")
    write_jsonl(source_dir / DOCUMENT_IR_JSONL, [block.to_dict() for block in document.blocks])
    failures = failure_records(document)
    write_jsonl(source_dir / FAILED_JSONL, [failure.to_dict() for failure in failures])

    _clear_chunk_outputs(source_dir)
    chunk_records: list[dict[str, Any]] = []
    if chunks:
        chunks_dir = source_dir / CHUNKS_DIR
        chunks_dir.mkdir(parents=True, exist_ok=True)
        for chunk in chunks:
            content_hash = sha256_text(chunk.text)
            markdown_file = f"{CHUNKS_DIR}/{chunk.chunk_id}.md"
            (source_dir / markdown_file).write_text(_chunk_markdown(chunk, content_hash), encoding="utf-8", newline="\n")
            record = chunk.to_dict()
            record["content_sha256"] = content_hash
            record["markdown_file"] = markdown_file
            chunk_records.append(record)
    write_jsonl(source_dir / CHUNKS_JSONL, chunk_records)

    report = {
        "skill_version": SKILL_VERSION,
        "source_id": document.source_id,
        "source_file": document.provenance.user_specified_name,
        "adapter": document.metadata.get("adapter", document.provenance.actual_adapter),
        "execution_summary": {
            "block_count": len(document.blocks),
            "chunk_count": len(chunks),
            "failure_count": len(failures),
        },
        "source_metadata": document.metadata,
        "ocr_fallback_statistics": {
            "ocr_block_count": sum(block.content_origin == "ocr" for block in document.blocks),
            "qr_decoder_block_count": sum(block.content_origin == "qr_decoder" for block in document.blocks),
            "total_backend_attempts": sum(len(block.attempts) for block in document.blocks),
        },
        "chunk_pre_validation": coverage,
        "chunk_post_validation": chunk_validation,
        "final_status": final_status,
        "warnings": document.warnings,
        "errors": document.errors,
        "parameters": parameters,
        "validation": validation_summary,
    }
    write_json(source_dir / REPORT_JSON, report)

    output_files = [
        source_dir / NORMALIZED_MD,
        source_dir / DOCUMENT_IR_JSONL,
        source_dir / CHUNKS_JSONL,
        source_dir / FAILED_JSONL,
        source_dir / REPORT_JSON,
    ]
    output_files.extend(sorted((source_dir / CHUNKS_DIR).glob("*.md")) if (source_dir / CHUNKS_DIR).exists() else [])
    if (source_dir / "forensic").exists():
        output_files.extend(sorted(path for path in (source_dir / "forensic").rglob("*") if path.is_file()))
    hashes = {path.relative_to(source_dir).as_posix(): sha256_file(path) for path in output_files if path.is_file()}
    manifest = {
        "skill_version": SKILL_VERSION,
        "provenance": document.provenance.to_dict(),
        "derived_files": sorted(hashes),
        "parser_ocr_versions": {
            "pymupdf": _version("PyMuPDF"),
            "python-docx": _version("python-docx"),
            "pytesseract": _version("pytesseract"),
            "pillow": _version("Pillow"),
            "beautifulsoup4": _version("beautifulsoup4"),
            "lxml": _version("lxml"),
        },
        "parameters": parameters,
        "output_file_hashes": hashes,
        "final_exit_code": status_exit_code(final_status),
        "normalized_document_hash": sha256_text(normalized_markdown),
    }
    write_json(source_dir / MANIFEST_JSON, manifest)
