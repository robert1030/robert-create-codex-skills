#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare hash-bound PDF page assets for native AI visual review."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from pathlib import Path
from typing import Any

from visual_review import (
    dense_text_metrics,
    image_sha256,
    is_effectively_blank,
    pdf_page_reference,
    render_pdf_page_png,
)


REQUEST_SCHEMA = "multiformat-rag-chunker.visual-review-request.v2"
RESPONSE_SCHEMA = "multiformat-rag-chunker.visual-semantics.v2"
REVIEW_METHOD = "native_visual_nonverbatim"


def _prepare_output(output_dir: Path, overwrite: bool) -> None:
    if output_dir.exists():
        if not overwrite:
            raise ValueError(f"visual_review_output_exists:{output_dir}")
        resolved = output_dir.resolve()
        if resolved.parent == resolved or len(resolved.parts) < 3:
            raise ValueError("visual_review_output_refuses_broad_delete")
        marker = resolved / "visual-review-request.json"
        try:
            marker_payload = json.loads(marker.read_text(encoding="utf-8"))
        except Exception as exc:
            raise ValueError("visual_review_output_missing_owned_marker") from exc
        if marker_payload.get("schema") != REQUEST_SCHEMA:
            raise ValueError("visual_review_output_marker_schema_invalid")
        shutil.rmtree(resolved)
    output_dir.mkdir(parents=True, exist_ok=False)


def prepare_pdf_review(
    source: Path,
    output_dir: Path,
    *,
    overwrite: bool = False,
    profile: str = "auto",
) -> dict[str, Any]:
    import fitz

    if profile not in {"auto", "dense_text", "semantic_summary"}:
        raise ValueError("visual_review_profile_invalid")
    source = source.resolve()
    if not source.is_file() or source.suffix.lower() != ".pdf":
        raise ValueError("visual_review_requires_pdf_source")
    _prepare_output(output_dir.resolve(), overwrite)
    source_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
    items: list[dict[str, Any]] = []
    skipped_pages: list[dict[str, Any]] = []
    document = fitz.open(source)
    try:
        for page_number, page in enumerate(document, start=1):
            native_text_length = len(page.get_text("text", sort=True).strip())
            if native_text_length >= 80:
                skipped_pages.append({
                    "page": page_number,
                    "reason": "native_text_sufficient",
                    "native_text_length": native_text_length,
                })
                continue
            image_bytes = render_pdf_page_png(page)
            blank, blank_metrics = is_effectively_blank(image_bytes)
            if blank:
                skipped_pages.append({
                    "page": page_number,
                    "reason": "blank_page",
                    "blank_metrics": blank_metrics,
                })
                continue
            reference = pdf_page_reference(page_number)
            target = output_dir / reference
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(image_bytes)
            density = dense_text_metrics(image_bytes)
            required_review_mode = (
                "dense_text"
                if profile == "dense_text" or (profile == "auto" and density["dense_text_candidate"])
                else "semantic_summary"
            )
            items.append({
                "reference": reference,
                "source_asset_sha256": image_sha256(image_bytes),
                "page": page_number,
                "asset_path": str(target.resolve()),
                "visual_class": "full_page_scan",
                "required": True,
                "review_method": REVIEW_METHOD,
                "density_metrics": density,
                "required_review_mode": required_review_mode,
                "summary_contract": {
                    "content_origin": "llm_visual_summary",
                    "verbatim": False,
                    "minimum_characters": 20,
                    "maximum_characters": 600,
                },
                "dense_text_contract": {
                    "content_origin": "llm_visual_text",
                    "verbatim": False,
                    "independent_validation_required": True,
                    "reading_order": "contiguous_one_based",
                    "uncertain_spans_allowed_for_success": False,
                },
            })
    finally:
        document.close()
    request = {
        "schema": REQUEST_SCHEMA,
        "response_schema": RESPONSE_SCHEMA,
        "input_path": str(source),
        "input_sha256": source_sha256,
        "review_method": REVIEW_METHOD,
        "profile": profile,
        "items": items,
        "skipped_pages": skipped_pages,
    }
    request_path = output_dir / "visual-review-request.json"
    request_path.write_text(
        json.dumps(request, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return {**request, "request_path": str(request_path.resolve())}


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare exact PDF page assets for native visual review.")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument(
        "--profile",
        choices=("auto", "dense_text", "semantic_summary"),
        default="auto",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()
    try:
        result = prepare_pdf_review(
            args.input,
            args.output,
            overwrite=args.overwrite,
            profile=args.profile,
        )
    except Exception as exc:
        result = {"status": "fatal_error", "error": str(exc)}
        if args.json_output:
            print(json.dumps(result, ensure_ascii=False, sort_keys=True))
        else:
            print(str(exc), file=sys.stderr)
        return 1
    result["status"] = "review_required" if result["items"] else "not_applicable"
    if args.json_output:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(result["request_path"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
