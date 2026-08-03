#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validated, non-verbatim visual review sidecars for linked HTML assets."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse


SCHEMA = "multiformat-rag-chunker.visual-semantics.v1"
REVIEW_METHOD = "native_visual_nonverbatim"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _reference_key(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme or parsed.netloc:
        raise ValueError("visual_summary_reference_must_be_local")
    path = PurePosixPath(unquote(parsed.path))
    if path.is_absolute() or ".." in path.parts or str(path) in {"", "."}:
        raise ValueError("visual_summary_reference_invalid")
    return path.as_posix()


@dataclass(frozen=True, slots=True)
class VisualSummaryReview:
    reference: str
    source_asset_sha256: str
    summary: str
    manifest_sha256: str
    input_sha256: str

    def evidence(self) -> dict[str, str]:
        return {
            "schema": SCHEMA,
            "review_method": REVIEW_METHOD,
            "source_asset_sha256": self.source_asset_sha256,
            "input_sha256": self.input_sha256,
            "review_manifest_sha256": self.manifest_sha256,
        }


class VisualSemantics:
    def __init__(self, reviews: dict[tuple[str, str], VisualSummaryReview] | None = None) -> None:
        self._reviews = dict(reviews or {})

    def lookup(self, reference: str, source_asset_sha256: str) -> VisualSummaryReview | None:
        try:
            reference_key = _reference_key(reference)
        except ValueError:
            return None
        return self._reviews.get((reference_key, source_asset_sha256.lower()))

    @property
    def review_count(self) -> int:
        return len(self._reviews)


def load_visual_semantics(path: Path | None, source_input: Path) -> VisualSemantics:
    """Load a sidecar only when it is bound to this exact input artifact."""

    if path is None:
        return VisualSemantics()
    try:
        raw = path.read_bytes()
        payload = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"visual_semantics_unreadable:{exc}") from exc
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise ValueError("visual_semantics_schema_invalid")
    input_sha256 = str(payload.get("input_sha256") or "").lower()
    if not _SHA256.fullmatch(input_sha256):
        raise ValueError("visual_semantics_input_sha256_invalid")
    actual_input_sha256 = hashlib.sha256(source_input.read_bytes()).hexdigest()
    if input_sha256 != actual_input_sha256:
        raise ValueError("visual_semantics_input_sha256_mismatch")
    items = payload.get("reviews")
    if not isinstance(items, list) or not items:
        raise ValueError("visual_semantics_reviews_required")
    manifest_sha256 = hashlib.sha256(raw).hexdigest()
    reviews: dict[tuple[str, str], VisualSummaryReview] = {}
    for item in items:
        if not isinstance(item, dict):
            raise ValueError("visual_semantics_review_invalid")
        if item.get("review_method") != REVIEW_METHOD:
            raise ValueError("visual_semantics_review_method_invalid")
        reference = _reference_key(str(item.get("reference") or ""))
        source_asset_sha256 = str(item.get("source_asset_sha256") or "").lower()
        if not _SHA256.fullmatch(source_asset_sha256):
            raise ValueError("visual_semantics_asset_sha256_invalid")
        summary = str(item.get("summary") or "").strip()
        if not 20 <= len(summary) <= 600:
            raise ValueError("visual_semantics_summary_length_invalid")
        key = (reference, source_asset_sha256)
        if key in reviews:
            raise ValueError("visual_semantics_duplicate_review")
        reviews[key] = VisualSummaryReview(
            reference=reference,
            source_asset_sha256=source_asset_sha256,
            summary=summary,
            manifest_sha256=manifest_sha256,
            input_sha256=input_sha256,
        )
    return VisualSemantics(reviews)
