#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate the fixed output contract, content gates, hashes, and chunk mapping."""

from __future__ import annotations

import argparse
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
    FAILED_JSONL,
    MANIFEST_JSON,
    NORMALIZED_MD,
    REPORT_JSON,
)
from utils import common_heading_path, read_jsonl, sha256_file, sha256_text, validate_text_quality

FRONTMATTER_RE = re.compile(r"^---\n(?P<frontmatter>.*?)\n---\n\n(?P<body>.*)\Z", re.DOTALL)


def _parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_RE.match(text)
    if not match:
        raise ValueError("missing_or_invalid_frontmatter")
    try:
        import yaml
        data = yaml.safe_load(match.group("frontmatter"))
    except Exception as exc:
        raise ValueError(f"frontmatter_parse_failed:{exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("frontmatter_not_mapping")
    return data, match.group("body").rstrip() + "\n"



def _ordered_ir_records(
    ir_records: list[dict[str, Any]],
    source_metadata: dict[str, Any],
) -> tuple[list[dict[str, Any]], int]:
    eligible = [
        record for record in ir_records
        if record.get("status") == "success" and record.get("type") != "placeholder"
    ]
    source_orders = [record.get("metadata", {}).get("source_order") for record in eligible]
    layout_required = _layout_semantics_applicable(source_metadata)
    if not any(value is not None for value in source_orders) and not layout_required:
        return eligible, 0
    violations = sum(value is None or not isinstance(value, int) for value in source_orders)
    valid_orders = [value for value in source_orders if isinstance(value, int)]
    violations += len(valid_orders) - len(set(valid_orders))
    violations += sum(current >= following for current, following in zip(valid_orders, valid_orders[1:]))
    indexed = {id(record): index for index, record in enumerate(ir_records)}
    ordered = sorted(
        eligible,
        key=lambda record: (
            record.get("metadata", {}).get("source_order")
            if isinstance(record.get("metadata", {}).get("source_order"), int)
            else 10**12,
            indexed[id(record)],
        ),
    )
    return ordered, violations


def _sequence_mismatch_count(expected: list[str], actual: list[str]) -> int:
    shared = min(len(expected), len(actual))
    return sum(expected[index] != actual[index] for index in range(shared)) + abs(len(expected) - len(actual))


def _layout_semantics_applicable(source_metadata: dict[str, Any]) -> bool:
    return source_metadata.get("layout_semantics_status") == "reliable"


def _title_semantics_applicable(source_metadata: dict[str, Any]) -> bool:
    return source_metadata.get("document_title_semantics_status") == "reliable"


def _visual_relation_errors(ir_records: list[dict[str, Any]], source_metadata: dict[str, Any]) -> list[dict[str, Any]]:
    if not _layout_semantics_applicable(source_metadata):
        return []
    indexed = {id(record): index for index, record in enumerate(ir_records)}
    ordered = sorted(
        ir_records,
        key=lambda record: (
            record.get("metadata", {}).get("source_order")
            if isinstance(record.get("metadata", {}).get("source_order"), int)
            else 10**12,
            indexed[id(record)],
        ),
    )
    nearest_heading: dict[str, Any] | None = None
    errors: list[dict[str, Any]] = []
    for record in ordered:
        if record.get("status") != "success":
            continue
        if record.get("type") == "heading":
            nearest_heading = record
            continue
        if record.get("type") != "image":
            continue
        metadata = record.get("metadata", {})
        actual = metadata.get("associated_heading_block_id")
        expected = nearest_heading.get("block_id") if nearest_heading else None
        if not actual or actual != expected:
            errors.append({
                "block_id": record.get("block_id"),
                "reason": "visual_heading_relation_mismatch",
                "expected": expected,
                "actual": actual,
            })
            continue
        expected_path = nearest_heading.get("heading_path", []) if nearest_heading else []
        if record.get("heading_path", []) != expected_path:
            errors.append({
                "block_id": record.get("block_id"),
                "reason": "visual_heading_path_mismatch",
                "expected": expected_path,
                "actual": record.get("heading_path", []),
            })
        associated_path = metadata.get("associated_heading_path")
        if associated_path != expected_path:
            errors.append({
                "block_id": record.get("block_id"),
                "reason": "associated_heading_path_mismatch",
                "expected": expected_path,
                "actual": associated_path,
            })
        association_method = metadata.get("association_method")
        if not isinstance(association_method, str) or not association_method.strip():
            errors.append({
                "block_id": record.get("block_id"),
                "reason": "association_method_missing",
            })
    return errors


def _document_title_errors(
    ir_records: list[dict[str, Any]],
    source_metadata: dict[str, Any],
    chunk_records: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    if not _title_semantics_applicable(source_metadata):
        return []
    expected_title = str(source_metadata.get("document_title") or "")
    if not expected_title and chunk_records:
        expected_title = str(chunk_records[0].get("title") or "")
    title_blocks = [
        record for record in ir_records
        if record.get("status") == "success"
        and record.get("type") == "heading"
        and record.get("metadata", {}).get("semantic_role") == "document_title"
    ]
    errors: list[dict[str, Any]] = []
    if len(title_blocks) != 1:
        errors.append({"reason": "document_title_mismatch", "expected_count": 1, "actual_count": len(title_blocks)})
        return errors
    title_block = title_blocks[0]
    if not expected_title or title_block.get("text") != expected_title:
        errors.append({
            "block_id": title_block.get("block_id"),
            "reason": "document_title_mismatch",
            "expected": expected_title,
            "actual": title_block.get("text"),
        })
    if title_block.get("metadata", {}).get("level") != 1:
        errors.append({"block_id": title_block.get("block_id"), "reason": "document_title_level_not_one"})
    if title_block.get("heading_path", []) != [expected_title]:
        errors.append({
            "block_id": title_block.get("block_id"),
            "reason": "document_title_heading_path_mismatch",
            "expected": [expected_title],
            "actual": title_block.get("heading_path", []),
        })
    if any(str(record.get("title") or "") != expected_title for record in chunk_records):
        errors.append({"reason": "chunk_title_document_title_mismatch", "expected": expected_title})
    return errors


def validate_source_output(source_dir: Path) -> tuple[int, dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    required_files = [NORMALIZED_MD, DOCUMENT_IR_JSONL, CHUNKS_JSONL, FAILED_JSONL, REPORT_JSON, MANIFEST_JSON]
    for name in required_files:
        if not (source_dir / name).is_file():
            errors.append({"file": name, "reason": "missing_required_output"})
    if errors:
        return EXIT_FATAL, {"status": "fatal_error", "errors": errors, "warnings": warnings}

    try:
        normalized = (source_dir / NORMALIZED_MD).read_text(encoding="utf-8")
        ir_records = read_jsonl(source_dir / DOCUMENT_IR_JSONL)
        chunk_records = read_jsonl(source_dir / CHUNKS_JSONL)
        failure_records = read_jsonl(source_dir / FAILED_JSONL)
        report = json.loads((source_dir / REPORT_JSON).read_text(encoding="utf-8"))
        manifest = json.loads((source_dir / MANIFEST_JSON).read_text(encoding="utf-8"))
    except Exception as exc:
        return EXIT_FATAL, {"status": "fatal_error", "errors": [{"reason": str(exc)}], "warnings": warnings}

    valid_text, reasons, _metrics = validate_text_quality(normalized)
    if not valid_text:
        errors.append({"file": NORMALIZED_MD, "reason": "invalid_text_quality", "details": reasons})
    if re.search(r"(?mi)^\s*(?:PAGE|PAG\s*E)\s*\d+\s*$", normalized):
        errors.append({"file": NORMALIZED_MD, "reason": "page_footer_pollution"})
    block_ids = [str(record.get("block_id", "")) for record in ir_records]
    if any(not value for value in block_ids):
        errors.append({"file": DOCUMENT_IR_JSONL, "reason": "missing_block_id"})
    if len(set(block_ids)) != len(block_ids):
        errors.append({"file": DOCUMENT_IR_JSONL, "reason": "duplicate_block_id"})
    for record in ir_records:
        if record.get("content_origin") == "llm_visual_summary" and record.get("verbatim") is not False:
            errors.append({"block_id": record.get("block_id"), "reason": "llm_summary_mislabeled_as_verbatim"})

    coverage = report.get("chunk_pre_validation", {})
    if coverage.get("source_unit_accounting_ratio") != 1.0:
        errors.append({"reason": "source_unit_accounting_ratio_not_one"})
    for metric_name in ("text", "table", "visual", "structural"):
        metric = coverage.get(metric_name, {})
        if metric.get("eligible_count") == 0 and metric.get("coverage_ratio") == 1.0:
            errors.append({"reason": "zero_over_zero_must_not_equal_one", "metric": metric_name})
    if manifest.get("normalized_document_hash") != sha256_text(normalized):
        errors.append({"file": MANIFEST_JSON, "reason": "normalized_document_hash_mismatch"})
    for relative, expected in manifest.get("output_file_hashes", {}).items():
        target = source_dir / relative
        if not target.is_file() or sha256_file(target) != expected:
            errors.append({"file": relative, "reason": "output_hash_mismatch"})

    ir_by_id = {str(record.get("block_id", "")): record for record in ir_records if record.get("block_id")}
    source_metadata = report.get("source_metadata", {})
    source_semantic_audit = source_metadata.get("source_semantic_audit", {})
    adapter_candidates = [
        str(value)
        for value in (
            source_metadata.get("adapter"),
            report.get("adapter"),
            manifest.get("provenance", {}).get("actual_adapter"),
        )
        if value
    ]
    distinct_adapters = set(adapter_candidates)
    if len(distinct_adapters) > 1:
        errors.append({
            "reason": "adapter_identity_mismatch",
            "values": sorted(distinct_adapters),
        })
    adapter_name = adapter_candidates[0] if adapter_candidates else ""
    document_adapter = adapter_name in {"docx_adapter", "doc_adapter", "pdf_adapter"}
    if document_adapter:
        for field in ("layout_semantics_status", "document_title_semantics_status"):
            if field not in source_metadata:
                errors.append({"reason": "source_semantics_status_missing", "field": field})
    ordered_ir, source_order_metadata_violations = _ordered_ir_records(ir_records, source_metadata)
    expected_source_block_order = [str(record.get("block_id")) for record in ordered_ir]
    seen_chunk_ids: set[str] = set()
    for record in chunk_records:
        chunk_id = str(record.get("chunk_id", ""))
        if not chunk_id or chunk_id in seen_chunk_ids:
            errors.append({"chunk_id": chunk_id, "reason": "missing_or_duplicate_chunk_id"})
        seen_chunk_ids.add(chunk_id)
        markdown_file = str(record.get("markdown_file", ""))
        markdown_path = (source_dir / markdown_file).resolve()
        try:
            markdown_path.relative_to(source_dir.resolve())
        except ValueError:
            errors.append({"chunk_id": chunk_id, "reason": "chunk_path_escape"})
            continue
        if not markdown_path.is_file():
            errors.append({"chunk_id": chunk_id, "reason": "chunk_markdown_missing"})
            continue
        try:
            frontmatter, body = _parse_frontmatter(markdown_path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append({"chunk_id": chunk_id, "reason": str(exc)})
            continue
        if frontmatter.get("chunk_id") != chunk_id:
            errors.append({"chunk_id": chunk_id, "reason": "frontmatter_chunk_id_mismatch"})
        for field in ("title", "heading_path", "source_block_ids", "content_sha256"):
            if frontmatter.get(field) != record.get(field):
                errors.append({"chunk_id": chunk_id, "reason": f"frontmatter_{field}_mismatch"})
        if body.rstrip() != str(record.get("markdown_body", "")).rstrip():
            errors.append({"chunk_id": chunk_id, "reason": "chunk_body_mismatch"})
        if str(record.get("content_sha256")) != sha256_text(str(record.get("text", ""))):
            errors.append({"chunk_id": chunk_id, "reason": "chunk_content_hash_mismatch"})
        source_block_ids = [str(value) for value in record.get("source_block_ids", [])]
        mapped_records = [ir_by_id[block_id] for block_id in source_block_ids if block_id in ir_by_id]
        fallback_heading = [str(record.get("title"))] if record.get("title") else []
        expected_heading = common_heading_path(
            (mapped.get("heading_path", []) for mapped in mapped_records),
            fallback_heading,
        )
        actual_heading = [str(value) for value in record.get("heading_path", [])]
        if actual_heading != expected_heading:
            errors.append({
                "chunk_id": chunk_id,
                "reason": "chunk_heading_path_mismatch",
                "expected": expected_heading,
                "actual": actual_heading,
            })

    actual_source_block_order = [
        str(block_id)
        for record in chunk_records
        for block_id in record.get("source_block_ids", [])
    ]
    reading_order_violations = (
        _sequence_mismatch_count(expected_source_block_order, actual_source_block_order)
        if chunk_records
        else 0
    )
    if source_order_metadata_violations:
        errors.append({
            "reason": "source_order_metadata_invalid",
            "violation_count": source_order_metadata_violations,
        })
    if reading_order_violations:
        errors.append({
            "reason": "chunk_reading_order_mismatch",
            "violation_count": reading_order_violations,
            "expected": expected_source_block_order,
            "actual": actual_source_block_order,
        })
    visual_errors = _visual_relation_errors(ir_records, source_metadata)
    errors.extend(visual_errors)
    title_errors = _document_title_errors(ir_records, source_metadata, chunk_records)
    errors.extend(title_errors)

    final_status = str(report.get("final_status", "fatal_error"))
    post = report.get("chunk_post_validation", {})
    measured_post = {
        "reading_order_violation_count": reading_order_violations,
        "source_order_metadata_violation_count": source_order_metadata_violations,
        "visual_heading_relation_violation_count": len(visual_errors),
        "document_title_mismatch_count": len(title_errors),
    }
    for metric_name, measured_value in measured_post.items():
        reported_value = post.get(metric_name)
        if reported_value is None:
            errors.append({
                "reason": "chunk_post_validation_metric_missing",
                "metric": metric_name,
            })
        elif reported_value != measured_value:
            errors.append({
                "reason": "chunk_post_validation_metric_mismatch",
                "metric": metric_name,
                "reported": reported_value,
                "measured": measured_value,
            })
    if final_status == "success":
        if source_semantic_audit.get("status") not in {"passed", "not_applicable"}:
            errors.append({"reason": "success_with_failed_source_semantic_audit"})
        if source_semantic_audit.get("expected_total") not in (None, source_semantic_audit.get("verified_total")):
            errors.append({"reason": "success_with_source_semantic_gap"})
        critical_expected = source_semantic_audit.get("critical_expected_total")
        critical_verified = source_semantic_audit.get("critical_verified_total")
        if critical_expected is not None and critical_expected != critical_verified:
            errors.append({"reason": "success_with_critical_source_semantic_gap"})
        if document_adapter:
            if source_metadata.get("layout_semantics_status") != "reliable":
                errors.append({"reason": "success_without_reliable_layout_semantics"})
            if source_metadata.get("document_title_semantics_status") != "reliable":
                errors.append({"reason": "success_without_reliable_document_title_semantics"})
        if not chunk_records:
            errors.append({"reason": "success_without_chunks"})
        if coverage.get("required_content_coverage_ratio", 0) < 0.95:
            errors.append({"reason": "success_below_required_coverage"})
        critical_metric_status = coverage.get("critical_metric_status")
        if critical_metric_status == "measured":
            if coverage.get("critical_content_coverage_ratio") != 1.0:
                errors.append({"reason": "success_with_critical_gap"})
        elif critical_metric_status != "not_applicable":
            errors.append({"reason": "success_with_critical_metric_missing_or_invalid"})
        if post.get("chunk_validation_status") != "passed":
            errors.append({"reason": "success_with_failed_chunk_validation"})
        if any(record.get("required") and record.get("failure_reason") for record in failure_records):
            errors.append({"reason": "success_with_required_failure"})
    elif final_status == "partial_success":
        if chunk_records and any(record.get("content_status") != "partial_success" for record in chunk_records):
            errors.append({"reason": "partial_chunks_not_labeled_partial"})
    elif final_status != "fatal_error":
        errors.append({"reason": "unknown_final_status", "value": final_status})

    if errors:
        return EXIT_FATAL, {"status": "fatal_error", "errors": errors, "warnings": warnings, "reported_status": final_status}
    if final_status == "partial_success":
        return EXIT_PARTIAL_SUCCESS, {"status": "partial_success", "errors": [], "warnings": warnings, "chunk_count": len(chunk_records), "failure_count": len(failure_records)}
    if final_status == "fatal_error":
        return EXIT_FATAL, {"status": "fatal_error", "errors": [], "warnings": warnings, "chunk_count": len(chunk_records), "failure_count": len(failure_records)}
    return EXIT_SUCCESS, {"status": "success", "errors": [], "warnings": warnings, "chunk_count": len(chunk_records), "failure_count": len(failure_records)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate one per-source multiformat RAG output directory.")
    parser.add_argument("source_output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    code, result = validate_source_output(args.source_output.resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"status={result['status']} errors={len(result.get('errors', []))} warnings={len(result.get('warnings', []))}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
