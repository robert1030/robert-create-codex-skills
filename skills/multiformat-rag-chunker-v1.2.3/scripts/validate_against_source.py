#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independently compare one PDF source with one per-source RAG output directory."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from constants import (
    CHUNKS_JSONL,
    DOCUMENT_IR_JSONL,
    EXIT_FATAL,
    EXIT_PARTIAL_SUCCESS,
    EXIT_SUCCESS,
    MANIFEST_JSON,
    REPORT_JSON,
)
from utils import read_jsonl
from validate import validate_source_output


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def _independent_page_render(page: Any, scale: float = 2.0) -> bytes:
    import fitz

    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    return pixmap.tobytes("png")


def _independent_blank_check(image_bytes: bytes) -> bool:
    import io
    from PIL import Image, ImageStat

    with Image.open(io.BytesIO(image_bytes)) as opened:
        grayscale = opened.convert("L")
        grayscale.thumbnail((512, 512))
        histogram = grayscale.histogram()
        total = max(1, sum(histogram))
        nonwhite_ratio = sum(histogram[:245]) / total
        stats = ImageStat.Stat(grayscale)
        mean = float(stats.mean[0])
        stddev = float(stats.stddev[0])
    return mean >= 250.0 and stddev <= 3.0 and nonwhite_ratio <= 0.002


def _verified_scan_pages(records: list[dict[str, Any]]) -> set[int]:
    return {
        int(record.get("location", {}).get("page"))
        for record in records
        if record.get("status") == "success"
        and record.get("content_origin") in {"ocr", "llm_visual_summary", "llm_visual_text"}
        and record.get("metadata", {}).get("visual_class") == "full_page_scan"
        and isinstance(record.get("location", {}).get("page"), int)
    }


def validate_against_source(
    source: Path,
    source_output: Path,
    *,
    require_complete: bool = False,
) -> tuple[int, dict[str, Any]]:
    import fitz

    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    source = source.resolve()
    source_output = source_output.resolve()
    internal_code, internal_result = validate_source_output(source_output)
    if internal_result.get("errors"):
        errors.append({"reason": "internal_output_validation_failed", "details": internal_result["errors"]})
    if not source.is_file() or source.suffix.lower() != ".pdf":
        errors.append({"reason": "source_must_be_existing_pdf", "path": str(source)})
        return EXIT_FATAL, {"status": "fatal_error", "errors": errors, "warnings": warnings}
    try:
        manifest = json.loads((source_output / MANIFEST_JSON).read_text(encoding="utf-8"))
        report = json.loads((source_output / REPORT_JSON).read_text(encoding="utf-8"))
        ir_records = read_jsonl(source_output / DOCUMENT_IR_JSONL)
        chunk_records = read_jsonl(source_output / CHUNKS_JSONL)
    except Exception as exc:
        errors.append({"reason": "output_unreadable", "details": str(exc)})
        return EXIT_FATAL, {"status": "fatal_error", "errors": errors, "warnings": warnings}

    source_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
    manifest_sha256 = str(manifest.get("provenance", {}).get("sha256") or "").lower()
    if manifest_sha256 != source_sha256:
        errors.append({"reason": "source_sha256_mismatch", "expected": source_sha256, "actual": manifest_sha256})

    document = fitz.open(source)
    required_scan_pages: list[int] = []
    blank_pages: list[int] = []
    page_asset_sha256: dict[int, str] = {}
    try:
        for page_number, page in enumerate(document, start=1):
            native_length = len(page.get_text("text", sort=True).strip())
            if native_length >= 80:
                continue
            rendered = _independent_page_render(page)
            if _independent_blank_check(rendered):
                blank_pages.append(page_number)
            else:
                required_scan_pages.append(page_number)
                page_asset_sha256[page_number] = hashlib.sha256(rendered).hexdigest()
        page_count = document.page_count
    finally:
        document.close()

    reported_page_count = report.get("source_metadata", {}).get("page_count")
    if reported_page_count != page_count:
        errors.append({"reason": "source_page_count_mismatch", "expected": page_count, "actual": reported_page_count})
    verified_scan_pages = _verified_scan_pages(ir_records)
    missing_scan_pages = sorted(set(required_scan_pages) - verified_scan_pages)
    if missing_scan_pages:
        errors.append({"reason": "required_scan_pages_not_verified", "pages": missing_scan_pages})
    for page_number in blank_pages:
        if any(
            record.get("location", {}).get("page") == page_number
            and record.get("metadata", {}).get("visual_class") == "full_page_scan"
            and record.get("required") is True
            and record.get("status") in {"failed", "low_quality"}
            for record in ir_records
        ):
            errors.append({"reason": "blank_page_marked_required_failure", "page": page_number})

    mapped_ids = {
        str(block_id)
        for chunk in chunk_records
        for block_id in chunk.get("source_block_ids", [])
    }
    verified_primary_ids = {
        str(record.get("block_id"))
        for record in ir_records
        if record.get("status") == "success"
        and record.get("type") != "heading"
        and record.get("content_origin") != "qr_decoder"
        and record.get("metadata", {}).get("content_role") not in {"machine_payload", "supplementary", "blank"}
    }
    omitted_primary = sorted(verified_primary_ids - mapped_ids)
    if chunk_records and omitted_primary:
        errors.append({"reason": "verified_primary_blocks_missing_from_chunks", "block_ids": omitted_primary})

    for record in ir_records:
        if record.get("content_origin") == "llm_visual_text":
            metadata = record.get("metadata", {})
            page_number = record.get("location", {}).get("page")
            expected_asset_sha256 = page_asset_sha256.get(page_number)
            asset_sha256 = str(metadata.get("asset_sha256") or "").lower()
            evidence = metadata.get("visual_text_evidence", {})
            if expected_asset_sha256 and asset_sha256 != expected_asset_sha256:
                errors.append({
                    "block_id": record.get("block_id"),
                    "reason": "visual_text_source_page_sha256_mismatch",
                    "expected": expected_asset_sha256,
                    "actual": asset_sha256,
                })
            if str(evidence.get("input_sha256") or "").lower() != source_sha256:
                errors.append({
                    "block_id": record.get("block_id"),
                    "reason": "visual_text_source_input_sha256_mismatch",
                })
            if evidence.get("independent_validation_status") != "passed":
                errors.append({
                    "block_id": record.get("block_id"),
                    "reason": "visual_text_independent_validation_missing",
                })
            continue
        if record.get("type") != "image":
            continue
        metadata = record.get("metadata", {})
        asset_sha256 = str(metadata.get("asset_sha256") or "").lower()
        if not SHA256_RE.fullmatch(asset_sha256):
            errors.append({"block_id": record.get("block_id"), "reason": "image_asset_sha256_invalid"})
        if not isinstance(metadata.get("machine_payloads"), list):
            errors.append({"block_id": record.get("block_id"), "reason": "image_machine_payloads_invalid"})
        if metadata.get("visual_class") == "screen_capture" and record.get("attempts"):
            errors.append({"block_id": record.get("block_id"), "reason": "screen_capture_has_ocr_attempts"})
        if record.get("content_origin") == "qr_decoder":
            evidence = metadata.get("decoder_evidence")
            if not isinstance(evidence, dict) or evidence.get("verified") is not True:
                errors.append({"block_id": record.get("block_id"), "reason": "qr_decoder_evidence_missing"})
        if record.get("content_origin") == "llm_visual_summary" and metadata.get("visual_class") == "full_page_scan":
            page_number = record.get("location", {}).get("page")
            expected_asset_sha256 = page_asset_sha256.get(page_number)
            evidence = metadata.get("visual_summary_evidence", {})
            if expected_asset_sha256 and asset_sha256 != expected_asset_sha256:
                errors.append({
                    "block_id": record.get("block_id"),
                    "reason": "visual_summary_source_page_sha256_mismatch",
                    "expected": expected_asset_sha256,
                    "actual": asset_sha256,
                })
            if str(evidence.get("input_sha256") or "").lower() != source_sha256:
                errors.append({
                    "block_id": record.get("block_id"),
                    "reason": "visual_summary_source_input_sha256_mismatch",
                    "expected": source_sha256,
                    "actual": evidence.get("input_sha256"),
                })
            if not SHA256_RE.fullmatch(str(evidence.get("review_manifest_sha256") or "").lower()):
                errors.append({
                    "block_id": record.get("block_id"),
                    "reason": "visual_summary_manifest_sha256_invalid",
                })

    final_status = str(report.get("final_status") or "fatal_error")
    if require_complete and final_status != "success":
        errors.append({"reason": "complete_result_required", "actual_status": final_status})
    if require_complete and not chunk_records:
        errors.append({"reason": "complete_result_without_chunks"})

    result = {
        "status": "fatal_error" if errors else final_status,
        "errors": errors,
        "warnings": warnings,
        "source_sha256": source_sha256,
        "page_count": page_count,
        "required_scan_pages": required_scan_pages,
        "verified_scan_pages": sorted(verified_scan_pages),
        "verified_dense_text_pages": sorted({
            int(record.get("location", {}).get("page"))
            for record in ir_records
            if record.get("content_origin") == "llm_visual_text"
            and record.get("status") == "success"
            and isinstance(record.get("location", {}).get("page"), int)
        }),
        "blank_pages": blank_pages,
        "chunk_count": len(chunk_records),
        "internal_validator_exit_code": internal_code,
    }
    if errors or final_status == "fatal_error":
        return EXIT_FATAL, result
    if final_status == "partial_success":
        return EXIT_PARTIAL_SUCCESS, result
    return EXIT_SUCCESS, result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate PDF RAG output against the original source.")
    parser.add_argument("source", type=Path)
    parser.add_argument("source_output", type=Path)
    parser.add_argument("--require-complete", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    code, result = validate_against_source(
        args.source,
        args.source_output,
        require_complete=args.require_complete,
    )
    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
