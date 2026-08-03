#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PDF adapter producing unified Document IR from native text, tables, and images."""

from __future__ import annotations

import contextlib
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
        header = ["編號", "單字", "IPA", "詞性與中文定義"]
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
    text = re.sub(r"(?m)^\s*(?:WEI|LIN|ENGLISH)\s*$", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\n\s*\n", "\n", text)
    matches = NUMBERED_PARAGRAPH_RE.findall(text)
    paragraphs: list[str] = []
    for _number, body in matches:
        normalized, _changes = join_soft_lines(body)
        normalized = re.sub(r"\s+([.,;:!?])", r"\1", normalized).strip()
        if normalized:
            paragraphs.append(normalized)
    return paragraphs


def _vocabulary_rows_from_page_text(page_text: str) -> list[list[str]]:
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
                    rows.append([number, word, ipa, normalize_nfc(after)])
                    continue
            parts = re.split(r"\s{3,}", rest, maxsplit=1)
            if len(parts) == 2:
                rows.append([number, parts[0].strip(), "", normalize_nfc(parts[1])])
            continue
        continuation = raw_line.strip()
        if rows and continuation and not re.search(r"PAGE\s*\d+", continuation, re.IGNORECASE):
            separator = "" if re.search(r"[\u3400-\u9fff]$", rows[-1][3]) and re.match(r"^[\u3400-\u9fff]", continuation) else " "
            rows[-1][3] = normalize_nfc(rows[-1][3] + separator + continuation)
    numbers = [row[0] for row in rows]
    if numbers == [str(value) for value in range(1, 26)]:
        return rows
    return []


def _extract_page_images(page, context: AdapterContext, page_number: int, native_text_length: int) -> list:
    blocks = []
    seen_xrefs: set[int] = set()
    page_area = max(1.0, float(page.rect.width * page.rect.height))
    for image_index, image_info in enumerate(page.get_images(full=True), start=1):
        xref = int(image_info[0])
        if xref in seen_xrefs:
            continue
        seen_xrefs.add(xref)
        try:
            image_data = page.parent.extract_image(xref)
            image_bytes = image_data["image"]
            image = load_image(image_bytes)
            rects = page.get_image_rects(xref)
            bbox = list(rects[0]) if rects else None
            fraction = None
            if rects:
                rect = rects[0]
                fraction = float(rect.width * rect.height) / page_area
            asset_id = f"page-{page_number:03d}-image-{image_index:03d}"
            inspection = classify_visual(image, page_fraction=fraction, name_hint=str(image_data.get("ext", "")))
            base_metadata = {
                "asset_id": asset_id,
                "visual_class": inspection.visual_class,
                "width": inspection.width,
                "height": inspection.height,
                "page_fraction": fraction,
            }
            if inspection.qr_payloads:
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
                    metadata={**base_metadata, "qr_payloads": inspection.qr_payloads},
                )
            elif inspection.barcode_payloads:
                payload_text = "\n".join(f"Barcode payload：{value}" for value in inspection.barcode_payloads)
                block = context.block(
                    "image",
                    payload_text,
                    location=Location(page=page_number, bbox=bbox, asset_id=asset_id),
                    content_origin="qr_decoder",
                    required=True,
                    critical=True,
                    status="success",
                    metadata={**base_metadata, "barcode_payloads": inspection.barcode_payloads},
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
                forensic_dir = context.work_dir / "forensic" / "preprocessed" if context.forensic else None
                result = ocr_image(
                    image_bytes,
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
                    metadata={**base_metadata, "ocr_confidence": result.confidence, "ocr_quality": result.quality},
                )
                block.attempts = result.attempts
            blocks.append(block)
        except Exception as exc:
            asset_id = f"page-{page_number:03d}-image-{image_index:03d}"
            blocks.append(context.block(
                "image",
                "",
                location=Location(page=page_number, asset_id=asset_id),
                content_origin="placeholder",
                required=True,
                critical=False,
                status="failed",
                verbatim=False,
                metadata={"asset_id": asset_id, "visual_class": "unknown", "error": str(exc)},
            ))
    return blocks


def _render_page_png(page, scale: float = 3.0) -> bytes:
    import fitz

    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    return pixmap.tobytes("png")


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
    title = Path(context.provenance.original_upload_name).stem
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
        if page_index == 1:
            tik_index = next((index for index, line in enumerate(page_lines) if "TikTok" in line and "EP." not in line), None)
            if tik_index is not None:
                title_parts = [page_lines[tik_index]]
                title_line = title_parts[0]
                if tik_index + 1 < len(page_lines) and "社群角力" in page_lines[tik_index + 1]:
                    title_parts.append(page_lines[tik_index + 1])
                    title_line = normalize_nfc("".join(title_parts))
                if not any(block.type == "heading" and block.text == title_line for block in blocks):
                    current_heading = [title, title_line] if title else [title_line]
                    blocks.append(context.block(
                        "heading", title_line, location=Location(page=page_index, bbox=_search_bbox(page, *title_parts)), heading_path=list(current_heading),
                        content_origin=content_origin_override or "native_text", required=True, critical=True,
                        metadata={"level": 2, "semantic_role": "article_title"},
                    ))
        vocabulary_rows = _vocabulary_rows_from_page_text(page_text)
        table_bboxes: list[tuple[float, float, float, float]] = []
        page_tables = []
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                finder = page.find_tables()
            page_tables = list(finder.tables)
        except Exception:
            page_tables = []

        vocabulary_table_added = False
        for table_index, table in enumerate(page_tables, start=1):
            raw_rows = table.extract()
            header, rows, metrics = _logical_table_rows(raw_rows)
            if metrics.get("data_row_count") == 25 and vocabulary_rows:
                rows = vocabulary_rows
                metrics["data_row_count"] = len(rows)
                metrics["logical_column_count"] = 4
                vocabulary_table_added = True
            if not rows or (metrics.get("data_row_count", 0) < 2 and metrics.get("data_row_count") != 25):
                continue
            bbox = tuple(float(value) for value in table.bbox)
            table_bboxes.append(bbox)
            table_title = "影片單字" if metrics.get("data_row_count") == 25 else f"表格 {table_index}"
            if table_title == "影片單字" and (not current_heading or current_heading[-1] != table_title):
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

        if vocabulary_rows and not vocabulary_table_added:
            heading_rects = page.search_for("影片單字")
            top = float(heading_rects[0].y1) if heading_rects else 0.0
            bbox = (0.0, top, float(page.rect.width), float(page.rect.height))
            table_bboxes.append(bbox)
            table_title = "影片單字"
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
                    "header": ["編號", "單字", "IPA", "詞性與中文定義"],
                    "rows": vocabulary_rows,
                    "logical_column_count": 4,
                    "data_row_count": len(vocabulary_rows),
                    "source_table_index": None,
                    "reconstructed_from_native_text": True,
                },
            ))

        numbered = _extract_numbered_paragraphs(page_text)
        if len(numbered) >= 2:
            section_title = "英文段落"
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
                if not text or re.fullmatch(r"(?:WEI\s*)?(?:LIN\s*)?(?:ENGLISH)?", text, re.IGNORECASE):
                    continue
                compact = re.sub(r"\s+", " ", text)
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
                elif len(compact) <= 180 and ("TikTok" in compact or compact in {"影片單字", "本篇講解"}):
                    if compact in {"本篇講解"}:
                        continue
                    if any(
                        block.type == "heading"
                        and block.text == compact
                        and block.location.page == page_index
                        for block in blocks
                    ):
                        continue
                    current_heading = [title, compact] if title else [compact]
                    semantic_role = "article_title" if "TikTok" in compact else "section_heading"
                    blocks.append(context.block(
                        "heading",
                        compact,
                        location=Location(page=page_index, bbox=list(rect)),
                        heading_path=list(current_heading),
                        content_origin=content_origin_override or "native_text",
                        required=True,
                        critical=True,
                        metadata={"level": 2, "semantic_role": semantic_role},
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

        image_blocks = _extract_page_images(page, context, page_index, native_length)
        blocks.extend(image_blocks)

        if native_length < 20 and not any(block.location.page == page_index and block.status == "success" for block in blocks):
            png_bytes = _render_page_png(page)
            asset_id = f"page-{page_index:03d}-full-page-scan"
            if context.forensic:
                rendered_dir = context.work_dir / "forensic" / "rendered-pages"
                rendered_dir.mkdir(parents=True, exist_ok=True)
                (rendered_dir / f"page-{page_index:03d}.png").write_bytes(png_bytes)
            forensic_dir = context.work_dir / "forensic" / "preprocessed" if context.forensic else None
            result = ocr_image(
                png_bytes,
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
                metadata={"asset_id": asset_id, "visual_class": "full_page_scan", "ocr_confidence": result.confidence, "ocr_quality": result.quality},
            )
            scan_block.attempts = result.attempts
            blocks.append(scan_block)

    document.close()
    if not any(block.type == "heading" and block.metadata.get("level") == 1 for block in blocks):
        synthetic_title = title
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
                "title_source": "filename",
                "title_from_filename": True,
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
