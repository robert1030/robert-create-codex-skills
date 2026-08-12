#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PDF adapter producing unified Document IR from native text, tables, and images."""

from __future__ import annotations

import contextlib
import hashlib
import io
import re
from pathlib import Path
from typing import Any

from adapters.base import AdapterContext
from models import DocumentIR, Location
from normalize import join_soft_lines, remove_page_noise
from ocr import ocr_image
from utils import normalize_nfc
from visual import classify_visual, load_image
from visual_review import is_effectively_blank, pdf_page_reference, render_pdf_page_png

NUMBERED_PARAGRAPH_RE = re.compile(r"(?ms)(?:^|\n)\s*([1-9]\d*)\.\s*(.*?)(?=(?:\n\s*[1-9]\d*\.\s)|\Z)")
DATE_RE = re.compile(r"\b20\d{2}[-/.]\d{1,2}[-/.]\d{1,2}\b")
ID_RE = re.compile(r"\b(?:EP\.?\s*\d+|v\d+(?:\.\d+)+)\b", re.IGNORECASE)


def _union_bbox(rects: list[Any]) -> list[float] | None:
    if not rects:
        return None
    return [
        min(float(rect.x0) for rect in rects),
        min(float(rect.y0) for rect in rects),
        max(float(rect.x1) for rect in rects),
        max(float(rect.y1) for rect in rects),
    ]


def _search_bbox(page, *texts: str) -> list[float] | None:
    rects: list[Any] = []
    for text in texts:
        if not text:
            continue
        try:
            matches = page.search_for(text)
        except Exception:
            matches = []
        rects.extend(matches)
    return _union_bbox(rects)


def _numbered_content_bbox(page) -> list[float] | None:
    rects: list[tuple[float, float, float, float]] = []
    for block_tuple in page.get_text("blocks", sort=True):
        x0, y0, x1, y1, raw_text, *_rest = block_tuple
        if re.search(r"(?m)^\s*[1-9]\d*\.\s+", str(raw_text)):
            rects.append((float(x0), float(y0), float(x1), float(y1)))
    if not rects:
        return None
    return [
        min(rect[0] for rect in rects),
        min(rect[1] for rect in rects),
        max(rect[2] for rect in rects),
        max(rect[3] for rect in rects),
    ]


def _layout_sort_key(block, original_index: int) -> tuple[Any, ...]:
    visual_text_order = block.metadata.get("visual_text_reading_order")
    if block.content_origin == "llm_visual_text" and isinstance(visual_text_order, int):
        return (float(visual_text_order), 0.0, 2, 3, original_index)
    bbox = block.location.bbox
    positioned = isinstance(bbox, list) and len(bbox) == 4
    y0 = float(bbox[1]) if positioned else 10**12
    x0 = float(bbox[0]) if positioned else 10**12
    role = block.metadata.get("semantic_role")
    priority = 3
    if block.type == "heading":
        priority = 0
    elif block.type == "image":
        priority = 1
    elif block.type in {"table", "list", "paragraph"}:
        priority = 2
    role_priority = {
        "document_title": 0,
        "article_title": 1,
        "section_heading": 2,
    }.get(role, 3)
    return (y0, x0, priority, role_priority, original_index)


def _annotate_pdf_layout(blocks: list, document_title: str) -> list:
    """Reorder PDF blocks by logical layout and attach auditable semantics."""
    indexed = {id(block): index for index, block in enumerate(blocks)}
    ordered: list = []
    page_numbers = sorted({block.location.page for block in blocks if block.location.page is not None})

    unpaged = [block for block in blocks if block.location.page is None]
    ordered.extend(sorted(unpaged, key=lambda block: indexed[id(block)]))

    for page_number in page_numbers:
        page_blocks = [block for block in blocks if block.location.page == page_number]
        header_headings = [
            block for block in page_blocks
            if block.status == "success"
            and block.type == "heading"
            and block.metadata.get("semantic_role") in {"document_title", "article_title"}
        ]
        header_headings.sort(
            key=lambda block: (
                {"document_title": 0, "article_title": 1}.get(block.metadata.get("semantic_role"), 2),
                _layout_sort_key(block, indexed[id(block)]),
            )
        )

        body_y_values = [
            float(block.location.bbox[1])
            for block in page_blocks
            if block.status == "success"
            and isinstance(block.location.bbox, list)
            and len(block.location.bbox) == 4
            and (
                block.metadata.get("semantic_role") == "section_heading"
                or block.type in {"table", "list", "paragraph"}
            )
        ]
        first_body_y = min(body_y_values) if body_y_values else None
        header_visuals = [
            block for block in page_blocks
            if block.status == "success"
            and block.type == "image"
            and isinstance(block.location.bbox, list)
            and len(block.location.bbox) == 4
            and (block.metadata.get("qr_payloads") or block.metadata.get("barcode_payloads"))
            and (first_body_y is None or float(block.location.bbox[1]) < first_body_y)
        ]
        header_visuals.sort(key=lambda block: _layout_sort_key(block, indexed[id(block)]))
        for block in header_visuals:
            block.metadata["reading_order_adjustment"] = "header_visual_after_heading_cluster"
            block.metadata["association_method"] = "pdf_layout_header_cluster"

        reserved = {id(block) for block in header_headings + header_visuals}
        remaining = [block for block in page_blocks if id(block) not in reserved]
        remaining.sort(key=lambda block: _layout_sort_key(block, indexed[id(block)]))
        ordered.extend(header_headings)
        ordered.extend(header_visuals)
        ordered.extend(remaining)

    heading_text: list[str] = []
    heading_ids: list[str | None] = []
    for source_order, block in enumerate(ordered, start=1):
        block.metadata["source_order"] = source_order
        if block.location.element_index is None:
            block.location.element_index = source_order
        if block.type == "heading" and block.status == "success":
            level = max(1, min(6, int(block.metadata.get("level", 1))))
            if level == 1:
                heading_text = [block.text]
                heading_ids = [block.block_id]
            else:
                if not heading_text and document_title:
                    heading_text = [document_title]
                    heading_ids = [None]
                heading_text = heading_text[: level - 1]
                heading_ids = heading_ids[: level - 1]
                while len(heading_text) < level - 1:
                    heading_text.append(document_title)
                    heading_ids.append(None)
                heading_text.append(block.text)
                heading_ids.append(block.block_id)
            block.heading_path = list(heading_text)
            parent_id = next((value for value in reversed(heading_ids[:-1]) if value), None)
            if parent_id:
                block.metadata["parent_heading_block_id"] = parent_id
            continue
        block.heading_path = list(heading_text or ([document_title] if document_title else []))
        nearest_heading_id = next((value for value in reversed(heading_ids) if value), None)
        if nearest_heading_id:
            block.metadata["associated_heading_block_id"] = nearest_heading_id
            block.metadata["associated_heading_path"] = list(block.heading_path)
        if block.type == "image":
            block.metadata.setdefault("association_method", "nearest_preceding_heading")
    return ordered


def _vertical_overlap_ratio(first: list[float], second: list[float]) -> float:
    overlap = max(0.0, min(first[3], second[3]) - max(first[1], second[1]))
    shorter = min(max(0.0, first[3] - first[1]), max(0.0, second[3] - second[1]))
    return overlap / shorter if shorter > 0 else 0.0


def _detect_multicolumn_pages(blocks: list, page_widths: dict[int, float]) -> list[int]:
    """Return pages whose substantial text blocks form overlapping left and right columns."""
    risky_pages: list[int] = []
    for page_number, page_width in page_widths.items():
        candidates = [
            block for block in blocks
            if block.status == "success"
            and block.location.page == page_number
            and block.type in {"paragraph", "list"}
            and isinstance(block.location.bbox, list)
            and len(block.location.bbox) == 4
            and len(block.text.strip()) >= 20
            and float(block.location.bbox[2]) - float(block.location.bbox[0]) < page_width * 0.65
        ]
        left = [block for block in candidates if (block.location.bbox[0] + block.location.bbox[2]) / 2 < page_width * 0.48]
        right = [block for block in candidates if (block.location.bbox[0] + block.location.bbox[2]) / 2 > page_width * 0.52]
        if len(left) < 2 or len(right) < 2:
            continue
        overlap_pairs = sum(
            _vertical_overlap_ratio(left_block.location.bbox, right_block.location.bbox) >= 0.25
            for left_block in left
            for right_block in right
        )
        if overlap_pairs >= 2:
            risky_pages.append(page_number)
    return risky_pages


def _rect_intersection_ratio(rect: tuple[float, float, float, float], table_bbox: tuple[float, float, float, float]) -> float:
    x0, y0, x1, y1 = rect
    a0, b0, a1, b1 = table_bbox
    ix0, iy0 = max(x0, a0), max(y0, b0)
    ix1, iy1 = min(x1, a1), min(y1, b1)
    if ix1 <= ix0 or iy1 <= iy0:
        return 0.0
    intersection = (ix1 - ix0) * (iy1 - iy0)
    area = max(1.0, (x1 - x0) * (y1 - y0))
    return intersection / area


def _clean_cell(value: Any) -> str:
    if value is None:
        return ""
    text = normalize_nfc(str(value))
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([ˈˌ])", r"\1", text)
    text = re.sub(r"([ˈˌ])\s+", r"\1", text)
    return text.strip()


def _normalize_definition_separators(text: str) -> str:
    return re.sub(
        r"\s*/\s*(?=(?:adj|adv|n|v|prep|conj|pron)\.)",
        " / ",
        text,
        flags=re.IGNORECASE,
    )


def _logical_table_rows(raw_rows: list[list[Any]]) -> tuple[list[str], list[list[str]], dict[str, Any]]:
    cleaned = [[_clean_cell(cell) for cell in row] for row in raw_rows]
    numeric_rows = [row for row in cleaned if row and re.fullmatch(r"\d+", row[0] or "")]
    if len(numeric_rows) >= 3:
        logical: list[list[str]] = []
        for row in cleaned:
            nonempty = [cell for cell in row if cell]
            first = row[0] if row else ""
            if re.fullmatch(r"\d+", first or ""):
                number = first
                word = row[1] if len(row) > 1 else ""
                ipa = row[2] if len(row) > 2 else ""
                definition_parts = [cell for cell in row[3:] if cell]
                logical.append([number, word, ipa, " ".join(definition_parts)])
            elif logical and nonempty:
                continuation = " ".join(nonempty)
                logical[-1][3] = normalize_nfc(f"{logical[-1][3]} {continuation}")
        header = [f"欄位 {index}" for index in range(1, 5)]
        return header, logical, {
            "logical_column_count": 4,
            "data_row_count": len(logical),
            "header_origin": "derived_normalization",
        }
    width = max((len(row) for row in cleaned), default=0)
    if not cleaned or width == 0:
        return [], [], {"logical_column_count": 0, "data_row_count": 0}
    header = cleaned[0]
    data = cleaned[1:]
    return header, data, {"logical_column_count": width, "data_row_count": len(data)}


def _extract_numbered_paragraphs(text: str) -> list[str]:
    text, _ = remove_page_noise(text)
    text = re.sub(r"\n\s*\n", "\n", text)
    matches = NUMBERED_PARAGRAPH_RE.findall(text)
    paragraphs: list[str] = []
    for _number, body in matches:
        normalized, _changes = join_soft_lines(body)
        normalized = re.sub(r"\s+([.,;:!?])", r"\1", normalized).strip()
        if normalized:
            paragraphs.append(normalized)
    return paragraphs


def _numbered_lexical_rows_from_page_text(page_text: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in page_text.splitlines():
        match = re.match(r"^\s*(\d{1,2})\s+(.+)$", raw_line)
        if match:
            number = match.group(1)
            rest = match.group(2).rstrip()
            if "/" in rest:
                first = rest.find("/")
                second = rest.find("/", first + 1)
                if second > first:
                    word = rest[:first].strip()
                    ipa = rest[first:second + 1].strip()
                    after = rest[second + 1:].strip()
                    if after.startswith("(n)"):
                        ipa = f"{ipa} (n)"
                        after = after[3:].strip()
                    rows.append([number, word, ipa, _normalize_definition_separators(normalize_nfc(after))])
                    continue
            parts = re.split(r"\s{3,}", rest, maxsplit=1)
            if len(parts) == 2:
                rows.append([
                    number,
                    parts[0].strip(),
                    "",
                    _normalize_definition_separators(normalize_nfc(parts[1])),
                ])
            continue
        continuation = raw_line.strip()
        if rows and continuation and not re.search(r"PAGE\s*\d+", continuation, re.IGNORECASE):
            separator = "" if re.search(r"[\u3400-\u9fff]$", rows[-1][3]) and re.match(r"^[\u3400-\u9fff]", continuation) else " "
            rows[-1][3] = normalize_nfc(rows[-1][3] + separator + continuation)
    numbers = [int(row[0]) for row in rows]
    if len(numbers) >= 3 and all(current == previous + 1 for previous, current in zip(numbers, numbers[1:])):
        return rows
    return []


def _numeric_row_sequence(rows: list[list[str]]) -> list[int]:
    sequence: list[int] = []
    for row in rows:
        if not row or not re.fullmatch(r"\d+", str(row[0]).strip()):
            return []
        sequence.append(int(str(row[0]).strip()))
    return sequence


def _same_numeric_rows(first: list[list[str]], second: list[list[str]]) -> bool:
    first_sequence = _numeric_row_sequence(first)
    second_sequence = _numeric_row_sequence(second)
    return bool(first_sequence and first_sequence == second_sequence)


def _page_structural_labels(
    page_lines: list[str],
    document_title_line: str | None,
) -> tuple[list[str], str | None]:
    """Infer an article title and a numbered-section label from source order."""
    numbered_index = next(
        (index for index, line in enumerate(page_lines) if re.match(r"^\d+\s+\S", line)),
        None,
    )
    section_label: str | None = None
    if numbered_index is not None:
        for index in range(numbered_index - 1, -1, -1):
            candidate = page_lines[index].strip()
            if not candidate:
                continue
            if len(candidate) <= 80 and not DATE_RE.search(candidate) and not ID_RE.search(candidate):
                section_label = candidate
            break

    article_parts: list[str] = []
    if document_title_line and document_title_line in page_lines:
        start = page_lines.index(document_title_line) + 1
        stop = page_lines.index(section_label, start) if section_label in page_lines[start:] else len(page_lines)
        for candidate in page_lines[start:stop]:
            if re.match(r"^\d+\s+\S", candidate):
                break
            if re.fullmatch(r"(?:PAGE|PAG\s*E?)\s*\d+", candidate, re.IGNORECASE):
                continue
            if 3 <= len(candidate) <= 180:
                article_parts.append(candidate)
    return article_parts, section_label


def _extract_page_images(
    page,
    context: AdapterContext,
    page_number: int,
    native_text_length: int,
    *,
    scan_dominant: bool = False,
) -> list:
    blocks = []
    seen_xrefs: set[int] = set()
    page_area = max(1.0, float(page.rect.width * page.rect.height))
    for image_index, image_info in enumerate(page.get_images(full=True), start=1):
        xref = int(image_info[0])
        if xref in seen_xrefs:
            continue
        seen_xrefs.add(xref)
        asset_id = f"page-{page_number:03d}-image-{image_index:03d}"
        asset_sha256 = ""
        source_width = int(image_info[2] or 0)
        source_height = int(image_info[3] or 0)
        try:
            image_data = page.parent.extract_image(xref)
            image_bytes = image_data["image"]
            asset_sha256 = hashlib.sha256(image_bytes).hexdigest()
            source_width = int(image_data.get("width") or source_width)
            source_height = int(image_data.get("height") or source_height)
            image = load_image(image_bytes)
            rects = page.get_image_rects(xref)
            bbox = list(rects[0]) if rects else None
            fraction = None
            if rects:
                rect = rects[0]
                fraction = float(rect.width * rect.height) / page_area
            inspection = classify_visual(image, page_fraction=fraction, name_hint=str(image_data.get("ext", "")))
            base_metadata = {
                "asset_id": asset_id,
                "visual_class": inspection.visual_class,
                "width": inspection.width,
                "height": inspection.height,
                "page_fraction": fraction,
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
                payload_text = "\n".join(f"QR Code payload：{value}" for value in inspection.qr_payloads)
                block = context.block(
                    "image",
                    payload_text,
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="qr_decoder",
                    required=True,
                    critical=True,
                    status="success",
                    verbatim=True,
                    metadata={
                        **base_metadata,
                        "qr_payloads": inspection.qr_payloads,
                        "machine_payloads": machine_payloads,
                        "decoder_evidence": {"backend": "opencv_qrcode_detector", "verified": True},
                        "content_role": "machine_payload",
                    },
                )
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
                payload_text = "\n".join(f"Barcode payload：{value}" for value in inspection.barcode_payloads)
                block = context.block(
                    "image",
                    payload_text,
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="qr_decoder",
                    required=True,
                    critical=True,
                    status="success",
                    metadata={
                        **base_metadata,
                        "barcode_payloads": inspection.barcode_payloads,
                        "machine_payloads": machine_payloads,
                        "decoder_evidence": {
                            "backend": sorted({str(item["decoder"]) for item in barcode_details}),
                            "verified": True,
                        },
                        "content_role": "machine_payload",
                    },
                )
            elif scan_dominant:
                block = context.block(
                    "image",
                    "",
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="derived_normalization",
                    required=False,
                    critical=False,
                    status="skipped",
                    verbatim=False,
                    metadata={**base_metadata, "skip_reason": "covered_by_full_page_processing"},
                )
            elif inspection.visual_class == "screen_capture":
                block = context.block(
                    "image",
                    "",
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="derived_normalization",
                    required=False,
                    critical=False,
                    status="skipped",
                    verbatim=False,
                    metadata={**base_metadata, "skip_reason": "no_verified_machine_payload"},
                )
            elif inspection.visual_class in {"logo", "icon", "decorative", "photo"} or native_text_length >= 80:
                block = context.block(
                    "image",
                    "",
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="derived_normalization",
                    required=False,
                    critical=False,
                    status="skipped",
                    verbatim=False,
                    metadata={**base_metadata, "skip_reason": "non_required_visual_or_native_text_already_covers_content"},
                )
            else:
                route, admission = context.visual_route(
                    f"page-{page_number:03d}/image-{image_index:03d}",
                    asset_sha256,
                    review_present=False,
                    visual_class=inspection.visual_class,
                    native_structured_parser_status="insufficient",
                )
                forensic_dir = context.work_dir / "forensic" / "preprocessed" if context.forensic else None
                result = ocr_image(
                    image_bytes,
                    admission=admission,
                    languages=context.ocr_languages,
                    forensic_dir=forensic_dir,
                    unit_name=asset_id,
                )
                status = "success" if result.status == "success" else ("low_quality" if result.text else "failed")
                block = context.block(
                    "image",
                    result.text if result.status == "success" else "",
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="ocr" if result.text else "placeholder",
                    required=True,
                    critical=False,
                    status=status,
                    metadata={
                        **base_metadata,
                        "ocr_confidence": result.confidence,
                        "ocr_quality": result.quality,
                        "ocr_semantic_status": "accepted" if result.status == "success" else "rejected",
                        "reason": result.quality.get("reasons", [None])[0] if result.status != "success" else None,
                        "capability_route": route,
                        "content_role": "primary",
                    },
                )
                block.attempts = result.attempts
            blocks.append(block)
        except Exception as exc:
            blocks.append(context.block(
                "image",
                "",
                location=Location(page=page_number, asset_id=asset_id),
                content_origin="placeholder",
                required=True,
                critical=False,
                status="failed",
                verbatim=False,
                metadata={
                    "asset_id": asset_id,
                    "visual_class": "unknown",
                    "width": source_width,
                    "height": source_height,
                    "asset_sha256": asset_sha256,
                    "machine_payloads": [],
                    "error": str(exc),
                    "content_role": "primary",
                },
            ))
    return blocks


def _render_page_png(page, scale: float = 3.0) -> bytes:
    return render_pdf_page_png(page, scale=scale)


def parse_pdf_document(
    path: Path,
    context: AdapterContext,
    *,
    content_origin_override: str | None = None,
    derived_from: str | None = None,
) -> DocumentIR:
    import fitz

    document = fitz.open(path)
    context.provenance.source_dimensions["page_count"] = document.page_count
    if derived_from:
        context.provenance.derivation_chain.append({
            "operation": "render_to_pdf",
            "source": derived_from,
            "derived_path": str(path),
        })
    blocks = []
    pdf_metadata_title = normalize_nfc(str(document.metadata.get("title") or "").strip())
    title = pdf_metadata_title or Path(context.provenance.original_upload_name).stem
    current_heading: list[str] = []
    page_widths: dict[int, float] = {}

    for page_index, page in enumerate(document, start=1):
        page_widths[page_index] = float(page.rect.width)
        if context.forensic:
            rendered_dir = context.work_dir / "forensic" / "rendered-pages"
            rendered_dir.mkdir(parents=True, exist_ok=True)
            rendered_path = rendered_dir / f"page-{page_index:03d}.png"
            if not rendered_path.exists():
                rendered_path.write_bytes(_render_page_png(page, scale=2.0))
        page_text = page.get_text("text", sort=True)
        cleaned_page_text, _ = remove_page_noise(page_text)
        native_length = len(cleaned_page_text.strip())
        page_lines = [normalize_nfc(line.strip()) for line in page_text.splitlines() if line.strip()]
        episode_line = next((line for line in page_lines if "EP." in line and DATE_RE.search(line)), None)
        if episode_line and not any(block.type == "heading" and block.text == episode_line for block in blocks):
            title = episode_line
            current_heading = [episode_line]
            blocks.append(context.block(
                "heading", episode_line, location=Location(page=page_index, bbox=_search_bbox(page, episode_line)), heading_path=list(current_heading),
                content_origin=content_origin_override or "native_text", required=True, critical=True,
                metadata={
                    "level": 1,
                    "contains_date": True,
                    "contains_identifier": True,
                    "semantic_role": "document_title",
                    "title_source": "pdf_native_text",
                },
            ))
        article_parts, numbered_section_label = _page_structural_labels(page_lines, episode_line)
        if page_index == 1 and article_parts:
            article_title = normalize_nfc("".join(article_parts))
            if not any(block.type == "heading" and block.text == article_title for block in blocks):
                current_heading = [title, article_title] if title else [article_title]
                blocks.append(context.block(
                    "heading", article_title,
                    location=Location(page=page_index, bbox=_search_bbox(page, *article_parts)),
                    heading_path=list(current_heading),
                    content_origin=content_origin_override or "native_text",
                    required=True,
                    critical=True,
                    metadata={
                        "level": 2,
                        "semantic_role": "article_title",
                        "inference": "source_order_between_document_title_and_numbered_section",
                    },
                ))
        numbered_lexical_rows = _numbered_lexical_rows_from_page_text(page_text)
        table_bboxes: list[tuple[float, float, float, float]] = []
        page_tables = []
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                finder = page.find_tables()
            page_tables = list(finder.tables)
        except Exception:
            page_tables = []

        numbered_table_added = False
        for table_index, table in enumerate(page_tables, start=1):
            raw_rows = table.extract()
            header, rows, metrics = _logical_table_rows(raw_rows)
            if numbered_lexical_rows and _same_numeric_rows(rows, numbered_lexical_rows):
                rows = numbered_lexical_rows
                metrics["data_row_count"] = len(rows)
                metrics["logical_column_count"] = 4
                header = [f"欄位 {index}" for index in range(1, 5)]
                numbered_table_added = True
            if not rows or metrics.get("data_row_count", 0) < 2:
                continue
            bbox = tuple(float(value) for value in table.bbox)
            table_bboxes.append(bbox)
            numeric_table = bool(_numeric_row_sequence(rows))
            table_title = numbered_section_label if numeric_table and numbered_section_label else f"表格 {table_index}"
            if numbered_section_label and table_title == numbered_section_label and (not current_heading or current_heading[-1] != table_title):
                current_heading = [current_heading[0]] if current_heading else []
                current_heading.append(table_title)
                heading_bbox = _search_bbox(page, table_title) or list(bbox)
                blocks.append(context.block(
                    "heading",
                    table_title,
                    location=Location(page=page_index, bbox=heading_bbox),
                    heading_path=list(current_heading),
                    content_origin=content_origin_override or "native_text",
                    required=True,
                    critical=True,
                    metadata={"level": 2, "semantic_role": "section_heading"},
                ))
            blocks.append(context.block(
                "table",
                "",
                location=Location(page=page_index, bbox=list(bbox)),
                heading_path=list(current_heading),
                content_origin=content_origin_override or "native_table",
                required=True,
                critical=True,
                metadata={
                    "header": header,
                    "rows": rows,
                    **metrics,
                    "source_table_index": table_index,
                },
            ))

        if numbered_lexical_rows and not numbered_table_added:
            heading_rects = page.search_for(numbered_section_label) if numbered_section_label else []
            top = float(heading_rects[0].y1) if heading_rects else 0.0
            bbox = (0.0, top, float(page.rect.width), float(page.rect.height))
            table_bboxes.append(bbox)
            table_title = numbered_section_label or f"表格 {len(page_tables) + 1}"
            if not current_heading or current_heading[-1] != table_title:
                current_heading = [current_heading[0]] if current_heading else []
                current_heading.append(table_title)
                blocks.append(context.block(
                    "heading",
                    table_title,
                    location=Location(page=page_index, bbox=_union_bbox(heading_rects) or list(bbox)),
                    heading_path=list(current_heading),
                    content_origin=content_origin_override or "native_text",
                    required=True,
                    critical=True,
                    metadata={
                        "level": 2,
                        "semantic_role": "section_heading",
                        "derived_from_native_text_rows": True,
                    },
                ))
            blocks.append(context.block(
                "table",
                "",
                location=Location(page=page_index, bbox=list(bbox)),
                heading_path=list(current_heading),
                content_origin=content_origin_override or "native_table",
                required=True,
                critical=True,
                metadata={
                    "header": [f"欄位 {index}" for index in range(1, 5)],
                    "rows": numbered_lexical_rows,
                    "logical_column_count": 4,
                    "data_row_count": len(numbered_lexical_rows),
                    "source_table_index": None,
                    "reconstructed_from_native_text": True,
                },
            ))

        numbered = _extract_numbered_paragraphs(page_text)
        if len(numbered) >= 2:
            latin_characters = len(re.findall(r"[A-Za-z]", " ".join(numbered)))
            source_characters = len(re.findall(r"\S", " ".join(numbered)))
            section_title = "英文段落" if source_characters and latin_characters / source_characters >= 0.6 else "編號段落"
            current_heading = [title, section_title] if title else [section_title]
            numbered_bbox = _numbered_content_bbox(page)
            blocks.append(context.block(
                "heading",
                section_title,
                location=Location(page=page_index, bbox=numbered_bbox),
                heading_path=list(current_heading),
                content_origin="derived_normalization",
                required=True,
                critical=False,
                verbatim=False,
                metadata={
                    "level": 2,
                    "semantic_role": "section_heading",
                    "derived": True,
                    "derivation_type": "synthetic_section_heading",
                    "derived_from_numbered_text_origin": content_origin_override or "native_text",
                },
            ))
            blocks.append(context.block(
                "list",
                "\n".join(f"{index}. {value}" for index, value in enumerate(numbered, start=1)),
                location=Location(page=page_index, bbox=numbered_bbox),
                heading_path=list(current_heading),
                content_origin=content_origin_override or "native_text",
                required=True,
                critical=True,
                metadata={"ordered": True, "items": numbered, "item_count": len(numbered)},
            ))
        else:
            for block_tuple in page.get_text("blocks", sort=True):
                x0, y0, x1, y1, raw_text, *_rest = block_tuple
                rect = (float(x0), float(y0), float(x1), float(y1))
                if any(_rect_intersection_ratio(rect, bbox) >= 0.35 for bbox in table_bboxes):
                    continue
                text, _ = remove_page_noise(str(raw_text))
                text, _ = join_soft_lines(text)
                text = normalize_nfc(text)
                if not text:
                    continue
                compact = re.sub(r"\s+", " ", text)
                document_title_bbox = _search_bbox(page, episode_line) if episode_line else None
                pretitle_callout = bool(
                    document_title_bbox
                    and rect[3] <= float(document_title_bbox[1])
                    and rect[0] >= float(page.rect.width) * 0.7
                    and len(compact) <= 60
                )
                if pretitle_callout:
                    continue
                if any(
                    block.type == "heading"
                    and block.text == compact
                    and block.location.page == page_index
                    for block in blocks
                ):
                    continue
                if len(compact) <= 160 and ("EP." in compact or DATE_RE.search(compact)):
                    if any(
                        block.type == "heading"
                        and block.text == compact
                        and block.location.page == page_index
                        for block in blocks
                    ):
                        continue
                    title = compact
                    current_heading = [compact]
                    blocks.append(context.block(
                        "heading",
                        compact,
                        location=Location(page=page_index, bbox=list(rect)),
                        heading_path=list(current_heading),
                        content_origin=content_origin_override or "native_text",
                        required=True,
                        critical=True,
                        metadata={
                            "level": 1,
                            "contains_date": bool(DATE_RE.search(compact)),
                            "contains_identifier": bool(ID_RE.search(compact)),
                            "semantic_role": "document_title",
                            "title_source": "pdf_native_text_block",
                        },
                    ))
                elif len(compact) > 20:
                    blocks.append(context.block(
                        "paragraph",
                        compact,
                        location=Location(page=page_index, bbox=list(rect)),
                        heading_path=list(current_heading),
                        content_origin=content_origin_override or "native_text",
                        required=True,
                        critical=bool(DATE_RE.search(compact) or ID_RE.search(compact)),
                    ))

        scan_dominant = native_length < 80
        review_png = _render_page_png(page, scale=2.0) if scan_dominant else b""
        page_blank, blank_metrics = is_effectively_blank(review_png) if review_png else (False, {})
        review_reference = pdf_page_reference(page_index)
        review_asset_sha256 = hashlib.sha256(review_png).hexdigest() if review_png else ""
        page_review = (
            context.visual_semantics.lookup(review_reference, review_asset_sha256)
            if scan_dominant and not page_blank
            else None
        )
        page_route = None
        page_admission = None
        if scan_dominant and not page_blank:
            page_route, page_admission = context.visual_route(
                review_reference,
                review_asset_sha256,
                review_present=page_review is not None,
                visual_class="full_page_scan",
                native_structured_parser_status="insufficient",
            )
        if scan_dominant and page_blank:
            asset_id = f"page-{page_index:03d}-full-page-scan"
            blocks.append(context.block(
                "image",
                "",
                location=Location(page=page_index, bbox=list(page.rect), asset_id=asset_id),
                heading_path=list(current_heading),
                content_origin="derived_normalization",
                required=False,
                critical=False,
                status="skipped",
                verbatim=False,
                metadata={
                    "asset_id": asset_id,
                    "visual_class": "full_page_scan",
                    "width": int(page.rect.width * 2.0),
                    "height": int(page.rect.height * 2.0),
                    "asset_sha256": review_asset_sha256,
                    "machine_payloads": [],
                    "skip_reason": "blank_page",
                    "blank_metrics": blank_metrics,
                    "content_role": "blank",
                },
            ))
        elif page_review is not None and page_review.review_mode == "semantic_summary":
            asset_id = f"page-{page_index:03d}-full-page-scan"
            blocks.append(context.block(
                "image",
                page_review.summary,
                location=Location(page=page_index, bbox=list(page.rect), asset_id=asset_id),
                heading_path=list(current_heading),
                content_origin="llm_visual_summary",
                required=True,
                critical=page_index == 1,
                status="success",
                verbatim=False,
                metadata={
                    "asset_id": asset_id,
                    "reference": review_reference,
                    "visual_class": "full_page_scan",
                    "width": int(page.rect.width * 2.0),
                    "height": int(page.rect.height * 2.0),
                    "asset_sha256": review_asset_sha256,
                    "machine_payloads": [],
                    "visual_summary_evidence": page_review.evidence(),
                    "capability_route": page_route,
                    "content_role": "primary",
                },
            ))
        elif page_review is not None and page_review.review_mode == "dense_text":
            asset_id = f"page-{page_index:03d}-full-page-scan"
            for unit in page_review.text_units:
                blocks.append(context.block(
                    "heading" if unit.unit_type == "heading" else "paragraph",
                    unit.text,
                    location=Location(page=page_index, bbox=list(page.rect), asset_id=asset_id),
                    heading_path=list(current_heading),
                    content_origin="llm_visual_text",
                    required=True,
                    critical=page_index == 1 or unit.unit_type in {"heading", "lexical_entry"},
                    status="success",
                    verbatim=False,
                    metadata={
                        "asset_id": asset_id,
                        "reference": review_reference,
                        "visual_class": "full_page_scan",
                        "asset_sha256": review_asset_sha256,
                        "visual_text_evidence": page_review.evidence(),
                        "capability_route": page_route,
                        "visual_text_unit_id": unit.unit_id,
                        "visual_text_unit_type": unit.unit_type,
                        "visual_text_reading_order": unit.reading_order,
                        "visual_text_fields": unit.fields,
                        "level": 2 if unit.unit_type == "heading" else None,
                        "semantic_role": "section_heading" if unit.unit_type == "heading" else None,
                        "density_metrics": page_review.density_metrics,
                        "dense_text_required": True,
                        "content_role": "primary",
                    },
                ))

        image_blocks = _extract_page_images(
            page,
            context,
            page_index,
            native_length,
            scan_dominant=scan_dominant,
        )
        blocks.extend(image_blocks)

        if scan_dominant and not page_blank and page_review is None:
            png_bytes = _render_page_png(page)
            asset_id = f"page-{page_index:03d}-full-page-scan"
            if context.forensic:
                rendered_dir = context.work_dir / "forensic" / "rendered-pages"
                rendered_dir.mkdir(parents=True, exist_ok=True)
                (rendered_dir / f"page-{page_index:03d}.png").write_bytes(png_bytes)
            forensic_dir = context.work_dir / "forensic" / "preprocessed" if context.forensic else None
            assert page_admission is not None
            result = ocr_image(
                png_bytes,
                admission=page_admission,
                languages=context.ocr_languages,
                forensic_dir=forensic_dir,
                unit_name=asset_id,
            )
            status = "success" if result.status == "success" else ("low_quality" if result.text else "failed")
            scan_block = context.block(
                "image",
                result.text if result.status == "success" else "",
                location=Location(page=page_index, bbox=list(page.rect), asset_id=asset_id),
                heading_path=list(current_heading),
                content_origin="ocr" if result.text else "placeholder",
                required=True,
                critical=page_index == 1,
                status=status,
                metadata={
                    "asset_id": asset_id,
                    "reference": review_reference,
                    "visual_class": "full_page_scan",
                    "width": int(page.rect.width * 3.0),
                    "height": int(page.rect.height * 3.0),
                    "asset_sha256": hashlib.sha256(png_bytes).hexdigest(),
                    "machine_payloads": [],
                    "ocr_confidence": result.confidence,
                    "ocr_quality": result.quality,
                    "ocr_semantic_status": "accepted" if result.status == "success" else "rejected",
                    "reason": result.quality.get("reasons", [None])[0] if result.status != "success" else None,
                    "capability_route": page_route,
                    "content_role": "primary",
                },
            )
            scan_block.attempts = result.attempts
            blocks.append(scan_block)

    document.close()
    if not any(block.type == "heading" and block.metadata.get("level") == 1 for block in blocks):
        synthetic_title = title
        synthetic_title_source = "pdf_metadata" if pdf_metadata_title else "filename"
        blocks.insert(0, context.block(
            "heading",
            synthetic_title,
            heading_path=[synthetic_title],
            content_origin="derived_normalization",
            required=True,
            critical=True,
            verbatim=False,
            metadata={
                "level": 1,
                "semantic_role": "document_title",
                "title_source": synthetic_title_source,
                "title_from_filename": synthetic_title_source == "filename",
                "title_from_pdf_metadata": synthetic_title_source == "pdf_metadata",
            },
        ))
    blocks = _annotate_pdf_layout(blocks, title)
    multicolumn_pages = _detect_multicolumn_pages(blocks, page_widths)
    title_source = next(
        (
            block.metadata.get("title_source")
            for block in blocks
            if block.type == "heading" and block.metadata.get("semantic_role") == "document_title"
        ),
        "filename",
    )
    title_semantics_status = "reliable" if title_source != "filename" else "inferred"
    warnings: list[str] = []
    if multicolumn_pages:
        warnings.append("pdf_multicolumn_layout_caution")
    if title_semantics_status != "reliable":
        warnings.append("document_title_inferred_from_filename")
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={
            "page_count": context.provenance.source_dimensions.get("page_count"),
            "adapter": "pdf_adapter",
            "derived_from": derived_from,
            "document_title": title,
            "title_source": title_source,
            "layout_semantics_status": "needs_review" if multicolumn_pages else "reliable",
            "document_title_semantics_status": title_semantics_status,
            "multicolumn_pages": multicolumn_pages,
        },
        warnings=warnings,
    )


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    return parse_pdf_document(path, context)
