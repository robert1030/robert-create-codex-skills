#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adapter context and deterministic block-id allocation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from models import Block, DocumentIR, Location, Provenance
from ocr import OCRAdmission
from visual_semantics import CapabilityEvidence


_OCR_REASON = {
    "unavailable": "native_multimodal_unavailable",
    "denied": "native_multimodal_denied",
    "unsupported": "native_multimodal_unsupported",
    "failed": "native_multimodal_failed_after_attempt",
}


@dataclass(slots=True)
class AdapterContext:
    provenance: Provenance
    work_dir: Path
    ocr_languages: str
    forensic: bool = False
    collection_runtime: Any | None = None
    collection_member_path: str | None = None
    visual_semantics: Any | None = None
    capability_evidence: CapabilityEvidence = field(default_factory=CapabilityEvidence)
    _counter: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)
    _routing_events: list[dict[str, Any]] = field(default_factory=list)

    def next_block_id(self) -> str:
        self._counter += 1
        return f"{self.provenance.source_id}-block-{self._counter:04d}"

    def visual_route(
        self,
        reference: str,
        asset_sha256: str,
        *,
        review_present: bool,
        visual_class: str,
        native_structured_parser_status: str = "not_applicable",
        specialized_decoder_status: str = "insufficient",
    ) -> tuple[dict[str, Any], OCRAdmission]:
        capability = self.capability_evidence
        evidence = list(capability.evidence)
        if review_present:
            status = "available"
            evidence = evidence or ["hash_bound_visual_semantics_sidecar"]
            attempted = True
            selected_lane = "native_llm_multimodal"
            admitted = False
            reason = "native_multimodal_review_supplied"
        elif capability.status == "available":
            status = capability.status
            attempted = capability.llm_visual_attempted
            selected_lane = "native_llm_multimodal"
            admitted = False
            reason = "native_visual_review_required"
        elif capability.status in _OCR_REASON:
            status = capability.status
            attempted = capability.llm_visual_attempted
            selected_lane = "ocr_fallback"
            admitted = True
            reason = _OCR_REASON[status]
        else:
            status = "unknown"
            attempted = False
            selected_lane = "capability_evidence_required"
            admitted = False
            reason = "native_multimodal_capability_evidence_required"
        event = {
            "event_id": f"route-{len(self._routing_events) + 1:04d}",
            "reference": reference,
            "source_asset_sha256": asset_sha256.lower(),
            "visual_class": visual_class,
            "native_llm_multimodal_status": status,
            "native_llm_multimodal_evidence": evidence,
            "native_structured_parser_status": native_structured_parser_status,
            "specialized_decoder_status": specialized_decoder_status,
            "selected_lane": selected_lane,
            "llm_visual_attempted": attempted,
            "ocr_admitted": admitted,
            "ocr_admission_reason": reason,
        }
        self._routing_events.append(event)
        admission = OCRAdmission(
            admitted=admitted,
            reason=reason,
            capability_status=status,
            evidence=tuple(evidence),
            llm_visual_attempted=attempted,
        )
        return dict(event), admission

    def capability_routing_summary(self) -> dict[str, Any]:
        events = [dict(event) for event in self._routing_events]
        return {
            "schema": "multiformat-rag-chunker.capability-routing.v1",
            "native_llm_multimodal": self.capability_evidence.to_dict(),
            "routing_events": events,
            "selected_lanes": sorted({str(event["selected_lane"]) for event in events}),
            "llm_visual_attempted": any(bool(event["llm_visual_attempted"]) for event in events),
            "ocr_admitted": any(bool(event["ocr_admitted"]) for event in events),
        }

    def block(
        self,
        block_type: str,
        text: str,
        *,
        location: Location | None = None,
        heading_path: list[str] | None = None,
        content_origin: str = "native_text",
        required: bool = True,
        critical: bool = False,
        status: str = "success",
        verbatim: bool = True,
        raw_text: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Block:
        return Block(
            block_id=self.next_block_id(),
            type=block_type,
            text=text,
            location=location or Location(),
            heading_path=list(heading_path or []),
            content_origin=content_origin,
            required=required,
            critical=critical,
            status=status,
            verbatim=verbatim,
            raw_text=raw_text,
            metadata=dict(metadata or {}),
        )


def empty_document(context: AdapterContext, title: str) -> DocumentIR:
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=[],
        metadata=dict(context.metadata),
    )
