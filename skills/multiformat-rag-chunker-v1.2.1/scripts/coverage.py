#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chunk-pre source accounting and content completeness gate."""

from __future__ import annotations

import re
from typing import Any

from constants import REQUIRED_COVERAGE_THRESHOLD
from models import Block, DocumentIR
from utils import validate_text_quality


_CAPABILITY_FAILURE_MARKERS = (
    "_not_available",
    "_unavailable",
    "missing_system_dependency",
    "no module named",
    "modulenotfounderror",
)
_SOURCE_FAILURE_MARKERS = (
    "encrypted",
    "password_protected",
    "corrupt",
    "damaged",
    "unreadable",
    "missing_source",
    "missing_related_media",
)


def runtime_failure_category(blocks: list[Block]) -> str | None:
    """Map observable failed-unit evidence to the frozen reason vocabulary."""

    reasons = []
    for block in blocks:
        if block.status not in {"failed", "low_quality"}:
            continue
        reason = block.metadata.get("reason") or block.metadata.get("error") or ""
        reasons.append(str(reason).lower())
    if any(marker in reason for reason in reasons for marker in _CAPABILITY_FAILURE_MARKERS):
        return "needs_capability"
    if any(marker in reason for reason in reasons for marker in _SOURCE_FAILURE_MARKERS):
        return "needs_source"
    return None


def _ratio(numerator: int, denominator: int) -> tuple[float | None, str]:
    if denominator == 0:
        return None, "not_applicable"
    return round(numerator / denominator, 6), "measured"


def _is_verified(block: Block) -> bool:
    if block.status != "success":
        return False
    if block.type == "table":
        return bool(block.metadata.get("caption") or block.metadata.get("header") or block.metadata.get("rows"))
    return bool(block.text.strip())


def _metric_for_types(blocks: list[Block], types: set[str]) -> dict[str, Any]:
    eligible = [block for block in blocks if block.type in types and block.required]
    verified = [block for block in eligible if _is_verified(block)]
    ratio, metric_status = _ratio(len(verified), len(eligible))
    return {
        "eligible_count": len(eligible),
        "verified_count": len(verified),
        "coverage_ratio": ratio,
        "metric_status": metric_status,
    }


def validate_normalized_markdown(text: str) -> tuple[bool, list[str]]:
    reasons: list[str] = []
    valid, quality_reasons, _metrics = validate_text_quality(text)
    if not valid:
        reasons.extend(quality_reasons)
    if not text.strip():
        reasons.append("normalized_document_empty")
    if re.search(r"(?mi)^\s*(?:PAGE|PAG\s*E)\s*\d+\s*$", text):
        reasons.append("page_footer_pollution_detected")
    return not reasons, reasons


def evaluate_source_coverage(
    document: DocumentIR,
    normalized_markdown: str,
    *,
    require_original_binary: bool = False,
    source_semantic_audit: dict[str, Any] | None = None,
) -> dict[str, Any]:
    blocks = document.blocks
    source_total = len(blocks)
    accounted = sum(block.status in {"success", "skipped", "low_quality", "failed"} for block in blocks)
    source_ratio, _ = _ratio(accounted, source_total)
    required = [block for block in blocks if block.required]
    required_verified = [block for block in required if _is_verified(block)]
    required_ratio, required_status = _ratio(len(required_verified), len(required))
    critical = [block for block in blocks if block.critical and block.required]
    critical_verified = [block for block in critical if _is_verified(block)]
    critical_ratio, critical_status = _ratio(len(critical_verified), len(critical))
    normalized_ok, normalized_reasons = validate_normalized_markdown(normalized_markdown)
    undisclosed_required_failures = [
        block.block_id for block in required
        if block.status in {"failed", "low_quality"} and block.block_id not in normalized_markdown
    ]
    metrics = {
        "source_unit_total": source_total,
        "source_unit_accounted": accounted,
        "source_unit_accounting_ratio": source_ratio,
        "required_unit_total": len(required),
        "required_unit_verified": len(required_verified),
        "required_content_coverage_ratio": required_ratio,
        "required_metric_status": required_status,
        "critical_unit_total": len(critical),
        "critical_unit_verified": len(critical_verified),
        "critical_content_coverage_ratio": critical_ratio,
        "critical_metric_status": critical_status,
        "text": _metric_for_types(blocks, {"heading", "paragraph", "list", "code", "transcript"}),
        "table": _metric_for_types(blocks, {"table"}),
        "visual": _metric_for_types(blocks, {"image"}),
        "structural": _metric_for_types(blocks, {"heading", "list", "table", "code"}),
        "undisclosed_required_failures": undisclosed_required_failures,
        "normalized_document_valid": normalized_ok,
        "normalized_document_validation_reasons": normalized_reasons,
        "source_semantic_audit": source_semantic_audit or {
            "status": "not_run",
            "expected_total": None,
            "verified_total": None,
            "critical_expected_total": None,
            "critical_verified_total": None,
        },
    }
    useful_blocks = [block for block in blocks if _is_verified(block) and block.type not in {"heading"}]
    fatal_reasons: list[str] = []
    partial_reasons: list[str] = []
    adapter_name = str(document.metadata.get("adapter") or "")
    layout_status = str(document.metadata.get("layout_semantics_status") or "")
    title_status = str(document.metadata.get("document_title_semantics_status") or "")
    if source_ratio != 1.0:
        fatal_reasons.append("source_units_not_fully_accounted")
    if critical and critical_ratio != 1.0:
        fatal_reasons.append("critical_content_incomplete")
    if not useful_blocks:
        fatal_reasons.append("no_effective_main_content")
    if not normalized_ok:
        fatal_reasons.append("normalized_document_invalid")
    if undisclosed_required_failures:
        fatal_reasons.append("undisclosed_required_failures")
    semantic_audit = source_semantic_audit or {}
    if semantic_audit.get("status") == "failed":
        if int(semantic_audit.get("critical_expected_total") or 0) != int(semantic_audit.get("critical_verified_total") or 0):
            fatal_reasons.append("critical_source_semantic_content_incomplete")
        else:
            partial_reasons.append("source_semantic_content_incomplete")
    if document.provenance.derived_snapshot:
        reason = "derived_snapshot_instead_of_original_binary"
        if require_original_binary:
            fatal_reasons.append(reason)
        else:
            partial_reasons.append(reason)
    if adapter_name in {"docx_adapter", "doc_adapter", "pdf_adapter"}:
        if layout_status != "reliable":
            partial_reasons.append("layout_semantics_not_reliable")
        if title_status != "reliable":
            partial_reasons.append("document_title_semantics_not_reliable")
    if required_ratio is None or required_ratio < REQUIRED_COVERAGE_THRESHOLD:
        partial_reasons.append("required_content_coverage_below_0.95")
    runtime_reason = runtime_failure_category(blocks)
    if runtime_reason:
        if fatal_reasons:
            fatal_reasons.append(runtime_reason)
        else:
            partial_reasons.append(runtime_reason)
    if fatal_reasons:
        status = "fatal_error"
    elif partial_reasons:
        status = "partial_success"
    else:
        status = "success"
    metrics["content_completeness_status"] = status
    metrics["layout_semantics_status"] = layout_status or None
    metrics["document_title_semantics_status"] = title_status or None
    metrics["fatal_reasons"] = fatal_reasons
    metrics["partial_reasons"] = partial_reasons
    return metrics
