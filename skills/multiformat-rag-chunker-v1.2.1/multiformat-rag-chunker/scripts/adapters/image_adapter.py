#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Standalone image adapter with dedicated QR or barcode decoding before OCR."""

from __future__ import annotations

import hashlib
from pathlib import Path

from adapters.base import AdapterContext
from models import DocumentIR, Location
from ocr import ocr_image
from visual import classify_visual, load_image


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    title = path.stem
    image = load_image(path)
    inspection = classify_visual(image, name_hint=path.name)
    asset_id = "image-001"
    asset_sha256 = hashlib.sha256(path.read_bytes()).hexdigest()
    blocks = [context.block(
        "heading", title, heading_path=[title], content_origin="derived_normalization",
        required=True, critical=True, verbatim=False, metadata={"level": 1, "title_from_filename": True},
    )]
    metadata = {
        "asset_id": asset_id,
        "visual_class": inspection.visual_class,
        "width": inspection.width,
        "height": inspection.height,
        "asset_sha256": asset_sha256,
        "machine_payloads": [],
        **inspection.metadata,
    }
    if inspection.qr_payloads:
        machine_payloads = [
            {
                "kind": "qr",
                "symbology": "QR_CODE",
                "payload": value,
                "source_asset_sha256": asset_sha256,
            }
            for value in inspection.qr_payloads
        ]
        blocks.append(context.block(
            "image", "\n".join(f"QR Code payload：{value}" for value in inspection.qr_payloads),
            location=Location(asset_id=asset_id), heading_path=[title], content_origin="qr_decoder",
            required=True, critical=True, metadata={
                **metadata,
                "qr_payloads": inspection.qr_payloads,
                "machine_payloads": machine_payloads,
                "decoder_evidence": {"backend": "opencv_qrcode_detector", "verified": True},
            },
        ))
    elif inspection.barcode_payloads:
        barcode_details = inspection.metadata.get("barcode_details", [])
        machine_payloads = [
            {
                "kind": "barcode",
                "symbology": str(item["symbology"]),
                "payload": str(item["payload"]),
                "source_asset_sha256": asset_sha256,
            }
            for item in barcode_details
        ]
        blocks.append(context.block(
            "image", "\n".join(f"Barcode payload：{value}" for value in inspection.barcode_payloads),
            location=Location(asset_id=asset_id), heading_path=[title], content_origin="qr_decoder",
            required=True, critical=True, metadata={
                **metadata,
                "barcode_payloads": inspection.barcode_payloads,
                "machine_payloads": machine_payloads,
                "decoder_evidence": {
                    "backend": sorted({str(item["decoder"]) for item in barcode_details}),
                    "verified": True,
                },
            },
        ))
    elif inspection.visual_class in {"screen_capture", "photo", "logo", "icon", "decorative"}:
        blocks.append(context.block(
            "image", "", location=Location(asset_id=asset_id), heading_path=[title],
            content_origin="derived_normalization", required=False, status="skipped", verbatim=False,
            metadata={**metadata, "skip_reason": "no_verified_machine_payload"},
        ))
    else:
        forensic_dir = context.work_dir / "forensic" / "preprocessed" if context.forensic else None
        result = ocr_image(path, languages=context.ocr_languages, forensic_dir=forensic_dir, unit_name=asset_id)
        status = "success" if result.status == "success" else ("low_quality" if result.text else "failed")
        ocr_reasons = [str(reason) for reason in result.quality.get("reasons", [])]
        backend_unavailable = "ocr_backend_not_available" in ocr_reasons
        block = context.block(
            "image", result.text if result.status == "success" else "",
            location=Location(asset_id=asset_id), heading_path=[title], content_origin="ocr" if result.text else "placeholder",
            required=True, critical=True, status=status,
            metadata={
                **metadata,
                "ocr_confidence": result.confidence,
                "ocr_quality": result.quality,
                "ocr_semantic_status": (
                    "accepted" if result.status == "success"
                    else "not_run" if backend_unavailable
                    else "rejected"
                ),
                **({"reason": "ocr_backend_not_available"} if backend_unavailable else {}),
            },
        )
        block.attempts = result.attempts
        blocks.append(block)
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={"adapter": "image_adapter", "width": inspection.width, "height": inspection.height},
    )
