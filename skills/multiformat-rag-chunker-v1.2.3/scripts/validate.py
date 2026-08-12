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
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


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


def _primary_content_evidence(records: list[dict[str, Any]]) -> dict[str, Any]:
    def verified(record: dict[str, Any]) -> bool:
        if record.get("status") != "success":
            return False
        if record.get("type") == "table":
            metadata = record.get("metadata", {})
            return bool(metadata.get("caption") or metadata.get("header") or metadata.get("rows"))
        return bool(str(record.get("text") or "").strip())

    successful_primary = [
        record for record in records
        if verified(record)
        and record.get("type") != "heading"
        and record.get("content_origin") != "qr_decoder"
        and record.get("metadata", {}).get("content_role") not in {"machine_payload", "supplementary", "blank"}
    ]
    unresolved_primary = [
        record for record in records
        if record.get("required") is True
        and record.get("status") in {"failed", "low_quality"}
        and record.get("metadata", {}).get("content_role") not in {"machine_payload", "supplementary", "blank"}
    ]
    machine_payloads = [
        record for record in records
        if verified(record) and record.get("content_origin") == "qr_decoder"
    ]
    machine_payload_only_source = bool(machine_payloads) and not successful_primary and not unresolved_primary
    return {
        "verified_primary_count": len(successful_primary),
        "unresolved_primary_count": len(unresolved_primary),
        "verified_machine_payload_count": len(machine_payloads),
        "machine_payload_only_source": machine_payload_only_source,
        "has_effective_main_content": bool(successful_primary) or machine_payload_only_source,
    }


def _dense_text_evidence(records: list[dict[str, Any]]) -> dict[str, Any]:
    dense = [record for record in records if record.get("metadata", {}).get("dense_text_required") is True]
    references = sorted({str(record.get("metadata", {}).get("reference") or "") for record in dense})
    verified: list[str] = []
    unresolved: list[str] = []
    for reference in references:
        page_records = [
            record for record in dense
            if str(record.get("metadata", {}).get("reference") or "") == reference
        ]
        accepted = bool(page_records) and all(
            record.get("status") == "success"
            and record.get("content_origin") == "llm_visual_text"
            and record.get("verbatim") is False
            and bool(str(record.get("text") or "").strip())
            and record.get("metadata", {}).get("visual_text_evidence", {}).get(
                "independent_validation_status"
            ) == "passed"
            for record in page_records
        )
        (verified if accepted else unresolved).append(reference)
    ratio = round(len(verified) / len(references), 6) if references else None
    return {
        "eligible_page_count": len(references),
        "verified_page_count": len(verified),
        "coverage_ratio": ratio,
        "metric_status": "measured" if references else "not_applicable",
        "unit_count": len(dense),
        "unresolved_references": unresolved,
    }


def _pdf_dense_text_contract_errors(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for record in records:
        if record.get("content_origin") != "llm_visual_text":
            continue
        block_id = record.get("block_id")
        metadata = record.get("metadata")
        if not isinstance(metadata, dict):
            errors.append({"block_id": block_id, "reason": "visual_text_metadata_missing"})
            continue
        reference = str(metadata.get("reference") or "")
        asset_sha256 = str(metadata.get("asset_sha256") or "").lower()
        if not reference:
            errors.append({"block_id": block_id, "reason": "visual_text_reference_missing"})
        if not SHA256_RE.fullmatch(asset_sha256):
            errors.append({"block_id": block_id, "reason": "visual_text_asset_sha256_invalid"})
        if record.get("type") not in {"heading", "paragraph"}:
            errors.append({"block_id": block_id, "reason": "visual_text_block_type_invalid"})
        if record.get("status") != "success" or record.get("required") is not True:
            errors.append({"block_id": block_id, "reason": "visual_text_not_required_success"})
        if record.get("verbatim") is not False:
            errors.append({"block_id": block_id, "reason": "visual_text_must_be_nonverbatim"})
        if metadata.get("dense_text_required") is not True:
            errors.append({"block_id": block_id, "reason": "visual_text_dense_requirement_missing"})
        unit_id = metadata.get("visual_text_unit_id")
        unit_type = metadata.get("visual_text_unit_type")
        reading_order = metadata.get("visual_text_reading_order")
        if not isinstance(unit_id, str) or not unit_id:
            errors.append({"block_id": block_id, "reason": "visual_text_unit_id_invalid"})
        if not isinstance(unit_type, str) or not unit_type:
            errors.append({"block_id": block_id, "reason": "visual_text_unit_type_invalid"})
        if not isinstance(reading_order, int) or reading_order < 1:
            errors.append({"block_id": block_id, "reason": "visual_text_reading_order_invalid"})
        if not isinstance(metadata.get("visual_text_fields"), dict):
            errors.append({"block_id": block_id, "reason": "visual_text_fields_invalid"})
        evidence = metadata.get("visual_text_evidence")
        if not isinstance(evidence, dict):
            errors.append({"block_id": block_id, "reason": "visual_text_evidence_missing"})
        else:
            expected_values = {
                "schema": "multiformat-rag-chunker.visual-semantics.v2",
                "review_method": "native_visual_nonverbatim",
                "review_mode": "dense_text",
                "required_review_mode": "dense_text",
                "validation_schema": "multiformat-rag-chunker.visual-text-validation.v1",
                "validation_method": "independent_native_visual",
                "independent_validation_status": "passed",
            }
            for field, expected in expected_values.items():
                if evidence.get(field) != expected:
                    errors.append({
                        "block_id": block_id,
                        "reason": "visual_text_evidence_field_invalid",
                        "field": field,
                    })
            if str(evidence.get("source_asset_sha256") or "").lower() != asset_sha256:
                errors.append({"block_id": block_id, "reason": "visual_text_evidence_asset_sha256_mismatch"})
            for field in ("input_sha256", "review_manifest_sha256", "validation_manifest_sha256"):
                if not SHA256_RE.fullmatch(str(evidence.get(field) or "").lower()):
                    errors.append({"block_id": block_id, "reason": "visual_text_evidence_sha256_invalid", "field": field})
        groups.setdefault((reference, asset_sha256), []).append(record)
    for (reference, _asset_sha256), group in groups.items():
        unit_ids = [record.get("metadata", {}).get("visual_text_unit_id") for record in group]
        orders = [record.get("metadata", {}).get("visual_text_reading_order") for record in group]
        if len(unit_ids) != len(set(unit_ids)):
            errors.append({"reference": reference, "reason": "visual_text_unit_id_duplicate"})
        if sorted(value for value in orders if isinstance(value, int)) != list(range(1, len(group) + 1)):
            errors.append({"reference": reference, "reason": "visual_text_reading_order_not_contiguous"})
    return errors


def _pdf_image_contract_errors(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    required_metadata = ("asset_id", "visual_class", "width", "height", "asset_sha256", "machine_payloads")
    for record in records:
        if record.get("type") != "image":
            continue
        block_id = record.get("block_id")
        metadata = record.get("metadata")
        if not isinstance(metadata, dict):
            errors.append({"block_id": block_id, "reason": "image_metadata_missing"})
            continue
        for field in required_metadata:
            if field not in metadata or metadata.get(field) is None:
                errors.append({"block_id": block_id, "reason": "image_metadata_field_missing", "field": field})
        asset_sha256 = str(metadata.get("asset_sha256") or "").lower()
        if not SHA256_RE.fullmatch(asset_sha256):
            errors.append({"block_id": block_id, "reason": "image_asset_sha256_invalid"})
        machine_payloads = metadata.get("machine_payloads")
        if not isinstance(machine_payloads, list):
            errors.append({"block_id": block_id, "reason": "image_machine_payloads_not_list"})
            machine_payloads = []
        if record.get("content_origin") == "qr_decoder":
            decoder_evidence = metadata.get("decoder_evidence")
            if not machine_payloads:
                errors.append({"block_id": block_id, "reason": "decoder_block_without_machine_payload"})
            if not isinstance(decoder_evidence, dict) or decoder_evidence.get("verified") is not True or not decoder_evidence.get("backend"):
                errors.append({"block_id": block_id, "reason": "decoder_evidence_missing_or_unverified"})
            for payload in machine_payloads:
                if not isinstance(payload, dict):
                    errors.append({"block_id": block_id, "reason": "machine_payload_invalid"})
                    continue
                for field in ("kind", "symbology", "payload", "source_asset_sha256"):
                    if not payload.get(field):
                        errors.append({"block_id": block_id, "reason": "machine_payload_field_missing", "field": field})
                if str(payload.get("source_asset_sha256") or "").lower() != asset_sha256:
                    errors.append({"block_id": block_id, "reason": "machine_payload_asset_sha256_mismatch"})
        visual_class = metadata.get("visual_class")
        attempts = record.get("attempts", [])
        if visual_class == "screen_capture" and attempts:
            errors.append({"block_id": block_id, "reason": "screen_capture_must_not_use_ocr"})
        if visual_class == "screen_capture" and record.get("content_origin") != "llm_visual_summary":
            if record.get("status") != "skipped" or record.get("required") is not False:
                errors.append({"block_id": block_id, "reason": "unreviewed_screen_capture_not_safely_skipped"})
            if metadata.get("skip_reason") not in {"no_verified_machine_payload", "covered_by_full_page_processing"}:
                errors.append({"block_id": block_id, "reason": "screen_capture_skip_reason_invalid"})
        if metadata.get("skip_reason") == "blank_page":
            if record.get("status") != "skipped" or record.get("required") is not False:
                errors.append({"block_id": block_id, "reason": "blank_page_must_be_nonrequired_skipped"})
        if record.get("content_origin") == "llm_visual_summary":
            evidence = metadata.get("visual_summary_evidence")
            if not isinstance(evidence, dict):
                errors.append({"block_id": block_id, "reason": "visual_summary_evidence_missing"})
            else:
                if evidence.get("review_method") != "native_visual_nonverbatim":
                    errors.append({"block_id": block_id, "reason": "visual_summary_review_method_invalid"})
                if str(evidence.get("source_asset_sha256") or "").lower() != asset_sha256:
                    errors.append({"block_id": block_id, "reason": "visual_summary_asset_sha256_mismatch"})
                if not SHA256_RE.fullmatch(str(evidence.get("input_sha256") or "").lower()):
                    errors.append({"block_id": block_id, "reason": "visual_summary_input_sha256_invalid"})
                if not SHA256_RE.fullmatch(str(evidence.get("review_manifest_sha256") or "").lower()):
                    errors.append({"block_id": block_id, "reason": "visual_summary_manifest_sha256_invalid"})
            if record.get("verbatim") is not False:
                errors.append({"block_id": block_id, "reason": "visual_summary_must_be_nonverbatim"})
        if record.get("content_origin") == "ocr" and record.get("status") == "success":
            if metadata.get("ocr_semantic_status") != "accepted":
                errors.append({"block_id": block_id, "reason": "successful_ocr_without_semantic_acceptance"})
    return errors


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


def _capability_routing_errors(
    ir_records: list[dict[str, Any]],
    source_metadata: dict[str, Any],
) -> list[dict[str, Any]]:
    errors: list[dict[str, Any]] = []
    routing = source_metadata.get("capability_routing")
    if not isinstance(routing, dict) or routing.get("schema") != "multiformat-rag-chunker.capability-routing.v1":
        return [{"reason": "capability_routing_missing_or_invalid"}]
    native = routing.get("native_llm_multimodal")
    if not isinstance(native, dict) or native.get("status") not in {
        "unknown", "available", "unavailable", "denied", "unsupported", "failed",
    }:
        errors.append({"reason": "native_multimodal_capability_summary_invalid"})
        native = {}
    native_status = str(native.get("status") or "")
    native_evidence = native.get("evidence")
    if native_status != "unknown" and (
        not isinstance(native_evidence, list)
        or not native_evidence
        or any(not isinstance(item, str) or not item.strip() for item in native_evidence)
    ):
        errors.append({"reason": "native_multimodal_capability_evidence_missing"})
    if native_status == "failed" and (
        native.get("llm_visual_attempted") is not True or not str(native.get("failure_reason") or "").strip()
    ):
        errors.append({"reason": "native_multimodal_failed_attempt_evidence_missing"})
    events = routing.get("routing_events")
    if not isinstance(events, list):
        return [*errors, {"reason": "capability_routing_events_invalid"}]
    by_id: dict[str, dict[str, Any]] = {}
    fallback_reasons = {
        "unavailable": "native_multimodal_unavailable",
        "denied": "native_multimodal_denied",
        "unsupported": "native_multimodal_unsupported",
        "failed": "native_multimodal_failed_after_attempt",
    }
    for event in events:
        if not isinstance(event, dict):
            errors.append({"reason": "capability_routing_event_invalid"})
            continue
        event_id = str(event.get("event_id") or "")
        if not event_id or event_id in by_id:
            errors.append({"reason": "capability_routing_event_id_missing_or_duplicate", "event_id": event_id})
            continue
        by_id[event_id] = event
        status = str(event.get("native_llm_multimodal_status") or "")
        admitted = event.get("ocr_admitted")
        attempted = event.get("llm_visual_attempted")
        reason = str(event.get("ocr_admission_reason") or "")
        event_evidence = event.get("native_llm_multimodal_evidence")
        asset_sha256 = str(event.get("source_asset_sha256") or "")
        if not SHA256_RE.fullmatch(asset_sha256):
            errors.append({"reason": "capability_routing_asset_sha256_invalid", "event_id": event_id})
        if not isinstance(admitted, bool) or not isinstance(attempted, bool):
            errors.append({"reason": "capability_routing_boolean_invalid", "event_id": event_id})
            continue
        if status != "unknown" and (
            not isinstance(event_evidence, list)
            or not event_evidence
            or any(not isinstance(item, str) or not item.strip() for item in event_evidence)
        ):
            errors.append({"reason": "capability_routing_event_evidence_missing", "event_id": event_id})
        if admitted:
            if status not in fallback_reasons or reason != fallback_reasons.get(status):
                errors.append({"reason": "ocr_admission_evidence_invalid", "event_id": event_id})
            if status == "failed" and not attempted:
                errors.append({"reason": "ocr_admitted_without_prior_llm_attempt", "event_id": event_id})
            if (
                status != native_status
                or event_evidence != native_evidence
                or attempted != native.get("llm_visual_attempted")
            ):
                errors.append({"reason": "ocr_admission_not_bound_to_capability_manifest", "event_id": event_id})
        elif status in fallback_reasons and event.get("selected_lane") == "ocr_fallback":
            errors.append({"reason": "ocr_fallback_lane_without_admission", "event_id": event_id})
        if status == "available" and admitted:
            errors.append({"reason": "capability_priority_violation", "event_id": event_id})
    measured_lanes = sorted({str(event.get("selected_lane")) for event in events if isinstance(event, dict)})
    if routing.get("selected_lanes") != measured_lanes:
        errors.append({"reason": "capability_selected_lanes_mismatch"})
    if routing.get("ocr_admitted") is not any(bool(event.get("ocr_admitted")) for event in events if isinstance(event, dict)):
        errors.append({"reason": "capability_ocr_admission_summary_mismatch"})
    if routing.get("llm_visual_attempted") is not any(bool(event.get("llm_visual_attempted")) for event in events if isinstance(event, dict)):
        errors.append({"reason": "capability_llm_attempt_summary_mismatch"})
    for record in ir_records:
        metadata = record.get("metadata", {})
        route = metadata.get("capability_route")
        tesseract_attempts = [
            attempt for attempt in record.get("attempts", [])
            if attempt.get("backend") == "tesseract"
        ]
        uses_ocr = record.get("content_origin") == "ocr" or bool(tesseract_attempts)
        uses_llm_visual = record.get("content_origin") in {"llm_visual_summary", "llm_visual_text"}
        ocr_unavailable_explanation = (
            metadata.get("reason") == "ocr_backend_not_available"
            or "ocr_backend_not_available" in metadata.get("ocr_quality", {}).get("reasons", [])
        )
        if ocr_unavailable_explanation and isinstance(route, dict):
            event = by_id.get(str(route.get("event_id") or ""))
            if event is not None and event.get("native_llm_multimodal_status") == "available":
                errors.append({"reason": "capability_priority_violation", "block_id": record.get("block_id")})
        if not uses_ocr and not uses_llm_visual:
            continue
        if not isinstance(route, dict):
            errors.append({"reason": "visual_block_capability_route_missing", "block_id": record.get("block_id")})
            continue
        event = by_id.get(str(route.get("event_id") or ""))
        if event != route:
            errors.append({"reason": "visual_block_capability_route_mismatch", "block_id": record.get("block_id")})
            continue
        record_asset_sha256 = str(metadata.get("asset_sha256") or "")
        if record_asset_sha256 and record_asset_sha256 != str(event.get("source_asset_sha256") or ""):
            errors.append({"reason": "visual_block_capability_asset_mismatch", "block_id": record.get("block_id")})
        if uses_ocr and event.get("ocr_admitted") is not True:
            errors.append({"reason": "ocr_used_without_admission", "block_id": record.get("block_id")})
        if tesseract_attempts and event.get("native_llm_multimodal_status") == "available":
            errors.append({"reason": "capability_priority_violation", "block_id": record.get("block_id")})
        if uses_llm_visual and (
            event.get("selected_lane") != "native_llm_multimodal"
            or event.get("llm_visual_attempted") is not True
            or event.get("ocr_admitted") is not False
        ):
            errors.append({"reason": "llm_visual_route_evidence_invalid", "block_id": record.get("block_id")})
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
        if record.get("content_origin") in {"llm_visual_summary", "llm_visual_text"} and record.get("verbatim") is not False:
            errors.append({"block_id": record.get("block_id"), "reason": "llm_visual_content_mislabeled_as_verbatim"})

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
    errors.extend(_capability_routing_errors(ir_records, source_metadata))
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
    if adapter_name == "pdf_adapter":
        errors.extend(_pdf_image_contract_errors(ir_records))
        errors.extend(_pdf_dense_text_contract_errors(ir_records))
    measured_primary = _primary_content_evidence(ir_records)
    reported_primary = coverage.get("primary_content")
    if reported_primary != measured_primary:
        errors.append({
            "reason": "primary_content_evidence_mismatch",
            "reported": reported_primary,
            "measured": measured_primary,
        })
    measured_dense = _dense_text_evidence(ir_records)
    if coverage.get("dense_text") != measured_dense:
        errors.append({
            "reason": "dense_text_evidence_mismatch",
            "reported": coverage.get("dense_text"),
            "measured": measured_dense,
        })
    source_sha256 = str(manifest.get("provenance", {}).get("sha256") or "").lower()
    for record in ir_records:
        if record.get("content_origin") != "llm_visual_text":
            continue
        evidence = record.get("metadata", {}).get("visual_text_evidence", {})
        if str(evidence.get("input_sha256") or "").lower() != source_sha256:
            errors.append({"block_id": record.get("block_id"), "reason": "visual_text_source_input_sha256_mismatch"})
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
    parameters = report.get("parameters", {})
    allow_partial_chunks = parameters.get("allow_partial_chunks") is True
    partial_authorization = parameters.get("partial_authorization")
    if allow_partial_chunks and partial_authorization != "explicit_user_request":
        errors.append({"reason": "partial_chunks_without_explicit_user_authorization"})
    if partial_authorization and not allow_partial_chunks:
        errors.append({"reason": "partial_authorization_without_partial_chunks"})
    if chunk_records and final_status == "partial_success" and not allow_partial_chunks:
        errors.append({"reason": "partial_chunks_without_enabled_partial_mode"})
    if not measured_primary["has_effective_main_content"]:
        if final_status != "fatal_error":
            errors.append({"reason": "nonfatal_status_without_effective_main_content"})
        if chunk_records:
            errors.append({"reason": "chunks_created_without_effective_main_content"})
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
