#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hash-bound visual summaries and independently validated visual text units."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote, urlparse


SUMMARY_SCHEMA = "multiformat-rag-chunker.visual-semantics.v1"
DENSE_SCHEMA = "multiformat-rag-chunker.visual-semantics.v2"
VALIDATION_SCHEMA = "multiformat-rag-chunker.visual-text-validation.v1"
CAPABILITY_SCHEMA = "multiformat-rag-chunker.capability-evidence.v1"
REVIEW_METHOD = "native_visual_nonverbatim"
VALIDATION_METHOD = "independent_native_visual"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_UNIT_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,95}$")
_UNIT_TYPES = frozenset({
    "heading", "lexical_entry", "phrase", "example", "paragraph", "footer", "other",
})
_FIELD_NAMES = frozenset({
    "headword", "ipa", "part_of_speech", "definition_zh", "phrase",
    "example_en", "example_zh", "label", "body",
})
_CAPABILITY_STATUSES = frozenset({"available", "unavailable", "denied", "unsupported", "failed"})


@dataclass(frozen=True, slots=True)
class CapabilityEvidence:
    status: str = "unknown"
    evidence: tuple[str, ...] = ()
    llm_visual_attempted: bool = False
    failure_reason: str | None = None
    manifest_sha256: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "evidence": list(self.evidence),
            "llm_visual_attempted": self.llm_visual_attempted,
            "failure_reason": self.failure_reason,
            "manifest_sha256": self.manifest_sha256,
        }


def _reference_key(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        raise ValueError("visual_summary_reference_must_be_local")
    path = PurePosixPath(unquote(parsed.path))
    if path.is_absolute() or ".." in path.parts or str(path) in {"", "."}:
        raise ValueError("visual_summary_reference_invalid")
    return path.as_posix()


def _sha256(value: object, reason: str) -> str:
    normalized = str(value or "").lower()
    if not _SHA256.fullmatch(normalized):
        raise ValueError(reason)
    return normalized


@dataclass(frozen=True, slots=True)
class VisualTextUnit:
    unit_id: str
    unit_type: str
    reading_order: int
    text: str
    fields: dict[str, Any]


@dataclass(frozen=True, slots=True)
class VisualReview:
    reference: str
    source_asset_sha256: str
    review_mode: str
    required_review_mode: str
    summary: str
    text_units: tuple[VisualTextUnit, ...]
    density_metrics: dict[str, Any]
    manifest_sha256: str
    validation_manifest_sha256: str | None
    input_sha256: str

    def evidence(self) -> dict[str, Any]:
        evidence: dict[str, Any] = {
            "schema": DENSE_SCHEMA if self.review_mode == "dense_text" else SUMMARY_SCHEMA,
            "review_method": REVIEW_METHOD,
            "review_mode": self.review_mode,
            "required_review_mode": self.required_review_mode,
            "source_asset_sha256": self.source_asset_sha256,
            "input_sha256": self.input_sha256,
            "review_manifest_sha256": self.manifest_sha256,
        }
        if self.validation_manifest_sha256:
            evidence.update({
                "validation_schema": VALIDATION_SCHEMA,
                "validation_method": VALIDATION_METHOD,
                "validation_manifest_sha256": self.validation_manifest_sha256,
                "independent_validation_status": "passed",
            })
        return evidence


# Kept as a compatibility name for external imports from v1.2.2-dev-r1.
VisualSummaryReview = VisualReview


class VisualSemantics:
    def __init__(self, reviews: dict[tuple[str, str], VisualReview] | None = None) -> None:
        self._reviews = dict(reviews or {})

    def lookup(self, reference: str, source_asset_sha256: str) -> VisualReview | None:
        try:
            reference_key = _reference_key(reference)
        except ValueError:
            return None
        return self._reviews.get((reference_key, source_asset_sha256.lower()))

    @property
    def review_count(self) -> int:
        return len(self._reviews)

    @property
    def dense_review_count(self) -> int:
        return sum(review.review_mode == "dense_text" for review in self._reviews.values())


def _load_validation(
    path: Path | None,
    *,
    input_sha256: str,
    extraction_manifest_sha256: str,
) -> tuple[dict[tuple[str, str], dict[str, Any]], str | None]:
    if path is None:
        return {}, None
    try:
        raw = path.read_bytes()
        if len(raw) > 8 * 1024 * 1024:
            raise ValueError("visual_text_validation_too_large")
        payload = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"visual_text_validation_unreadable:{exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema") != VALIDATION_SCHEMA:
        raise ValueError("visual_text_validation_schema_invalid")
    if _sha256(payload.get("input_sha256"), "visual_text_validation_input_sha256_invalid") != input_sha256:
        raise ValueError("visual_text_validation_input_sha256_mismatch")
    if _sha256(
        payload.get("extraction_manifest_sha256"),
        "visual_text_validation_extraction_sha256_invalid",
    ) != extraction_manifest_sha256:
        raise ValueError("visual_text_validation_extraction_sha256_mismatch")
    items = payload.get("validations")
    if not isinstance(items, list) or not items or len(items) > 2000:
        raise ValueError("visual_text_validations_required")
    validations: dict[tuple[str, str], dict[str, Any]] = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("visual_text_validation_item_invalid")
        reference = _reference_key(str(item.get("reference") or ""))
        asset_sha256 = _sha256(item.get("source_asset_sha256"), "visual_text_validation_asset_sha256_invalid")
        key = (reference, asset_sha256)
        if key in validations:
            raise ValueError("visual_text_validation_duplicate_item")
        validations[key] = item
    return validations, hashlib.sha256(raw).hexdigest()


def _validate_fields(value: object) -> dict[str, Any]:
    if value is None:
        return {}
    if not isinstance(value, dict) or not set(value).issubset(_FIELD_NAMES):
        raise ValueError("visual_text_unit_fields_invalid")
    result: dict[str, Any] = {}
    for field, raw in value.items():
        if isinstance(raw, str):
            normalized: Any = raw.strip()
            if not normalized or len(normalized) > 2000:
                raise ValueError("visual_text_unit_field_value_invalid")
        elif isinstance(raw, list) and raw and len(raw) <= 50:
            normalized = [str(item).strip() for item in raw]
            if any(not item or len(item) > 2000 for item in normalized):
                raise ValueError("visual_text_unit_field_value_invalid")
        else:
            raise ValueError("visual_text_unit_field_value_invalid")
        result[field] = normalized
    return result


def _load_text_units(item: dict[str, Any]) -> tuple[VisualTextUnit, ...]:
    raw_units = item.get("text_units")
    if not isinstance(raw_units, list) or not raw_units or len(raw_units) > 2000:
        raise ValueError("visual_text_units_required")
    units: list[VisualTextUnit] = []
    seen: set[str] = set()
    for raw in raw_units:
        if not isinstance(raw, dict):
            raise ValueError("visual_text_unit_invalid")
        unit_id = str(raw.get("unit_id") or "")
        unit_type = str(raw.get("unit_type") or "")
        reading_order = raw.get("reading_order")
        text = str(raw.get("text") or "").strip()
        uncertain = raw.get("uncertain_spans", [])
        if not _UNIT_ID.fullmatch(unit_id) or unit_id in seen:
            raise ValueError("visual_text_unit_id_invalid_or_duplicate")
        if unit_type not in _UNIT_TYPES:
            raise ValueError("visual_text_unit_type_invalid")
        if not isinstance(reading_order, int) or reading_order < 1:
            raise ValueError("visual_text_unit_reading_order_invalid")
        if not 1 <= len(text) <= 4000:
            raise ValueError("visual_text_unit_text_length_invalid")
        if uncertain != []:
            raise ValueError("visual_text_unit_uncertainty_unresolved")
        units.append(VisualTextUnit(
            unit_id=unit_id,
            unit_type=unit_type,
            reading_order=reading_order,
            text=text,
            fields=_validate_fields(raw.get("fields")),
        ))
        field_values = [
            item
            for value in units[-1].fields.values()
            for item in (value if isinstance(value, list) else [value])
        ]
        if any(value not in text for value in field_values):
            raise ValueError("visual_text_unit_field_not_in_text")
        if unit_type == "lexical_entry" and "headword" not in units[-1].fields:
            raise ValueError("visual_text_lexical_entry_headword_required")
        seen.add(unit_id)
    if sorted(unit.reading_order for unit in units) != list(range(1, len(units) + 1)):
        raise ValueError("visual_text_unit_reading_order_not_contiguous")
    return tuple(sorted(units, key=lambda unit: unit.reading_order))


def _require_independent_validation(
    validation: dict[str, Any] | None,
    units: tuple[VisualTextUnit, ...],
) -> None:
    if validation is None:
        raise ValueError("visual_text_independent_validation_required")
    if validation.get("validation_method") != VALIDATION_METHOD:
        raise ValueError("visual_text_validation_method_invalid")
    if validation.get("status") != "passed":
        raise ValueError("visual_text_validation_not_passed")
    checked = validation.get("checked_unit_ids")
    expected = [unit.unit_id for unit in units]
    if checked != expected:
        raise ValueError("visual_text_validation_checked_units_mismatch")
    for field in ("missing_units", "unexpected_units", "mismatched_units"):
        if validation.get(field) != []:
            raise ValueError(f"visual_text_validation_{field}_not_empty")
    if validation.get("reading_order_status") != "passed":
        raise ValueError("visual_text_validation_reading_order_failed")
    if validation.get("mode_appropriate") is not True:
        raise ValueError("visual_text_validation_mode_inappropriate")


def load_capability_evidence(path: Path | None) -> CapabilityEvidence:
    """Load an Agent-to-script feature-detection record without guessing capability absence."""

    if path is None:
        return CapabilityEvidence()
    try:
        raw = path.read_bytes()
        if len(raw) > 1024 * 1024:
            raise ValueError("capability_evidence_too_large")
        payload = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"capability_evidence_unreadable:{exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema") != CAPABILITY_SCHEMA:
        raise ValueError("capability_evidence_schema_invalid")
    native = payload.get("native_llm_multimodal")
    if not isinstance(native, dict):
        raise ValueError("native_multimodal_capability_required")
    status = str(native.get("status") or "")
    if status not in _CAPABILITY_STATUSES:
        raise ValueError("native_multimodal_capability_status_invalid")
    raw_evidence = native.get("evidence")
    if isinstance(raw_evidence, str):
        evidence = (raw_evidence.strip(),) if raw_evidence.strip() else ()
    elif isinstance(raw_evidence, list):
        evidence = tuple(str(item).strip() for item in raw_evidence if str(item).strip())
    else:
        evidence = ()
    if not evidence or any(len(item) > 1000 for item in evidence):
        raise ValueError("native_multimodal_capability_evidence_required")
    attempted = native.get("llm_visual_attempted")
    if not isinstance(attempted, bool):
        raise ValueError("native_multimodal_attempt_status_required")
    failure_reason = str(native.get("failure_reason") or "").strip() or None
    if status == "failed" and (not attempted or not failure_reason):
        raise ValueError("native_multimodal_failed_attempt_evidence_required")
    if status in {"unavailable", "denied", "unsupported"} and not failure_reason:
        raise ValueError("native_multimodal_fallback_reason_required")
    if status == "available" and failure_reason:
        raise ValueError("native_multimodal_available_with_failure_reason")
    return CapabilityEvidence(
        status=status,
        evidence=evidence,
        llm_visual_attempted=attempted,
        failure_reason=failure_reason,
        manifest_sha256=hashlib.sha256(raw).hexdigest(),
    )


def load_visual_semantics(
    path: Path | None,
    source_input: Path,
    validation_path: Path | None = None,
) -> VisualSemantics:
    """Load sidecars only when they are bound to this exact input artifact."""

    if path is None:
        if validation_path is not None:
            raise ValueError("visual_text_validation_without_extraction")
        return VisualSemantics()
    try:
        raw = path.read_bytes()
        if len(raw) > 16 * 1024 * 1024:
            raise ValueError("visual_semantics_too_large")
        payload = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"visual_semantics_unreadable:{exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema") not in {SUMMARY_SCHEMA, DENSE_SCHEMA}:
        raise ValueError("visual_semantics_schema_invalid")
    schema = str(payload["schema"])
    input_sha256 = _sha256(payload.get("input_sha256"), "visual_semantics_input_sha256_invalid")
    actual_input_sha256 = hashlib.sha256(source_input.read_bytes()).hexdigest()
    if input_sha256 != actual_input_sha256:
        raise ValueError("visual_semantics_input_sha256_mismatch")
    items = payload.get("reviews")
    if not isinstance(items, list) or not items:
        raise ValueError("visual_semantics_reviews_required")
    manifest_sha256 = hashlib.sha256(raw).hexdigest()
    validations, validation_manifest_sha256 = _load_validation(
        validation_path,
        input_sha256=input_sha256,
        extraction_manifest_sha256=manifest_sha256,
    )
    reviews: dict[tuple[str, str], VisualReview] = {}
    dense_keys: set[tuple[str, str]] = set()
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("visual_semantics_review_invalid")
        if item.get("review_method") != REVIEW_METHOD:
            raise ValueError("visual_semantics_review_method_invalid")
        reference = _reference_key(str(item.get("reference") or ""))
        source_asset_sha256 = _sha256(item.get("source_asset_sha256"), "visual_semantics_asset_sha256_invalid")
        key = (reference, source_asset_sha256)
        if key in reviews:
            raise ValueError("visual_semantics_duplicate_review")
        if schema == SUMMARY_SCHEMA:
            review_mode = required_mode = "semantic_summary"
        else:
            review_mode = str(item.get("review_mode") or "")
            required_mode = str(item.get("required_review_mode") or "")
            if review_mode not in {"semantic_summary", "dense_text"}:
                raise ValueError("visual_semantics_review_mode_invalid")
            if required_mode not in {"semantic_summary", "dense_text"}:
                raise ValueError("visual_semantics_required_review_mode_invalid")
            if review_mode != required_mode:
                raise ValueError("visual_semantics_required_review_mode_mismatch")
        density_metrics = item.get("density_metrics", {})
        if schema == DENSE_SCHEMA and not isinstance(density_metrics, dict):
            raise ValueError("visual_semantics_density_metrics_invalid")
        summary = str(item.get("summary") or "").strip()
        units: tuple[VisualTextUnit, ...] = ()
        if review_mode == "semantic_summary":
            if not 20 <= len(summary) <= 600:
                raise ValueError("visual_semantics_summary_length_invalid")
        else:
            units = _load_text_units(item)
            _require_independent_validation(validations.get(key), units)
            dense_keys.add(key)
        reviews[key] = VisualReview(
            reference=reference,
            source_asset_sha256=source_asset_sha256,
            review_mode=review_mode,
            required_review_mode=required_mode,
            summary=summary,
            text_units=units,
            density_metrics=dict(density_metrics),
            manifest_sha256=manifest_sha256,
            validation_manifest_sha256=validation_manifest_sha256 if review_mode == "dense_text" else None,
            input_sha256=input_sha256,
        )
    if set(validations) != dense_keys:
        raise ValueError("visual_text_validation_scope_mismatch")
    return VisualSemantics(reviews)
