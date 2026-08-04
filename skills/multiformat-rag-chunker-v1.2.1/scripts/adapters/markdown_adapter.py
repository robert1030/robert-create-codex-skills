#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown adapter preserving headings, tables, lists, code, and local images."""

from __future__ import annotations

import re
from pathlib import Path

from adapters.base import AdapterContext
from models import DocumentIR, Location
from ocr import ocr_image
from utils import normalize_nfc
from visual import classify_visual, load_image

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
LIST_RE = re.compile(r"^\s*(?:([-*+])|(\d+)[.)])\s+(.*)$")
IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<src>[^)\s]+)(?:\s+['\"].*?['\"])?\)")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?\s*$")


def _split_table_row(line: str) -> list[str]:
    stripped = line.strip().strip("|")
    return [normalize_nfc(cell.strip().replace("\\|", "|")) for cell in re.split(r"(?<!\\)\|", stripped)]


def _append_image(path: Path, alt: str, reference: str, context: AdapterContext, blocks: list, heading_path: list[str], line_number: int, index: int) -> None:
    asset_id = f"markdown-image-{index:03d}"
    candidate = (path.parent / reference).resolve()
    try:
        candidate.relative_to(path.parent.resolve())
    except ValueError:
        candidate = Path("/__invalid__")
    if not candidate.is_file():
        blocks.append(context.block(
            "image", alt, location=Location(element_index=line_number, asset_id=asset_id),
            heading_path=list(heading_path), content_origin="native_text" if alt else "placeholder",
            required=bool(alt), status="success" if alt else "failed", verbatim=bool(alt),
            metadata={"asset_id": asset_id, "reference": reference, "reason": "missing_local_image"},
        ))
        return
    data = candidate.read_bytes()
    image = load_image(data)
    inspection = classify_visual(image, name_hint=reference)
    metadata = {"asset_id": asset_id, "reference": reference, "visual_class": inspection.visual_class, "width": inspection.width, "height": inspection.height, "alt": alt}
    if inspection.qr_payloads:
        blocks.append(context.block(
            "image", "\n".join(f"QR Code payload：{value}" for value in inspection.qr_payloads),
            location=Location(element_index=line_number, asset_id=asset_id), heading_path=list(heading_path),
            content_origin="qr_decoder", required=True, critical=True, metadata={**metadata, "qr_payloads": inspection.qr_payloads},
        ))
    elif alt:
        blocks.append(context.block(
            "image", alt, location=Location(element_index=line_number, asset_id=asset_id), heading_path=list(heading_path),
            content_origin="native_text", required=True, metadata=metadata,
        ))
    elif inspection.visual_class in {"logo", "icon", "photo", "decorative"}:
        blocks.append(context.block(
            "image", "", location=Location(element_index=line_number, asset_id=asset_id), heading_path=list(heading_path),
            content_origin="derived_normalization", required=False, status="skipped", verbatim=False,
            metadata={**metadata, "skip_reason": "non_required_visual"},
        ))
    else:
        result = ocr_image(data, languages=context.ocr_languages)
        status = "success" if result.status == "success" else ("low_quality" if result.text else "failed")
        block = context.block(
            "image", result.text if result.status == "success" else "",
            location=Location(element_index=line_number, asset_id=asset_id), heading_path=list(heading_path),
            content_origin="ocr" if result.text else "placeholder", required=True, status=status,
            metadata={**metadata, "ocr_confidence": result.confidence, "ocr_quality": result.quality},
        )
        block.attempts = result.attempts
        blocks.append(block)


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    text = path.read_text(encoding="utf-8-sig")
    lines = text.splitlines()
    blocks = []
    heading_path: list[str] = []
    title = path.stem
    image_index = 0
    index = 0
    paragraph_lines: list[str] = []
    paragraph_start = 1

    def flush_paragraph() -> None:
        nonlocal paragraph_lines, paragraph_start
        value = normalize_nfc("\n".join(paragraph_lines))
        if value:
            blocks.append(context.block(
                "paragraph", value, location=Location(element_index=paragraph_start),
                heading_path=list(heading_path), content_origin="native_text", required=True,
            ))
        paragraph_lines = []

    while index < len(lines):
        line = lines[index]
        line_number = index + 1
        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush_paragraph()
            level = len(heading_match.group(1))
            value = normalize_nfc(heading_match.group(2))
            heading_path = heading_path[: level - 1] + [value]
            if level == 1:
                title = value
            blocks.append(context.block(
                "heading", value, location=Location(element_index=line_number), heading_path=list(heading_path),
                content_origin="native_text", required=True, critical=True, metadata={"level": level},
            ))
            index += 1
            continue
        if line.strip().startswith("```") or line.strip().startswith("~~~"):
            flush_paragraph()
            fence = line.strip()[:3]
            language = line.strip()[3:].strip()
            code_lines: list[str] = []
            index += 1
            while index < len(lines) and not lines[index].strip().startswith(fence):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            blocks.append(context.block(
                "code", "\n".join(code_lines), location=Location(element_index=line_number),
                heading_path=list(heading_path), content_origin="native_text", required=True, critical=True,
                metadata={"language": language},
            ))
            continue
        if index + 1 < len(lines) and "|" in line and TABLE_SEPARATOR_RE.match(lines[index + 1]):
            flush_paragraph()
            header = _split_table_row(line)
            index += 2
            rows: list[list[str]] = []
            while index < len(lines) and "|" in lines[index] and lines[index].strip():
                rows.append(_split_table_row(lines[index]))
                index += 1
            blocks.append(context.block(
                "table", "", location=Location(element_index=line_number), heading_path=list(heading_path),
                content_origin="native_table", required=True, critical=True,
                metadata={"header": header, "rows": rows, "logical_column_count": len(header), "data_row_count": len(rows)},
            ))
            continue
        list_match = LIST_RE.match(line)
        if list_match:
            flush_paragraph()
            ordered = bool(list_match.group(2))
            items: list[str] = []
            while index < len(lines):
                current = LIST_RE.match(lines[index])
                if not current or bool(current.group(2)) != ordered:
                    break
                items.append(normalize_nfc(current.group(3)))
                index += 1
            rendered = "\n".join(f"{position}. {item}" if ordered else f"- {item}" for position, item in enumerate(items, start=1))
            blocks.append(context.block(
                "list", rendered, location=Location(element_index=line_number), heading_path=list(heading_path),
                content_origin="native_text", required=True,
                metadata={"ordered": ordered, "items": items, "item_count": len(items)},
            ))
            continue
        image_matches = list(IMAGE_RE.finditer(line))
        if image_matches:
            flush_paragraph()
            for match in image_matches:
                image_index += 1
                _append_image(path, normalize_nfc(match.group("alt")), match.group("src"), context, blocks, heading_path, line_number, image_index)
            remaining = IMAGE_RE.sub("", line).strip()
            if remaining:
                paragraph_start = line_number
                paragraph_lines.append(remaining)
            index += 1
            continue
        if not line.strip():
            flush_paragraph()
            index += 1
            continue
        if not paragraph_lines:
            paragraph_start = line_number
        paragraph_lines.append(line)
        index += 1
    flush_paragraph()
    if not any(block.type == "heading" for block in blocks):
        blocks.insert(0, context.block(
            "heading", title, heading_path=[title], content_origin="derived_normalization",
            required=True, critical=True, verbatim=False, metadata={"level": 1, "title_from_filename": True},
        ))
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={"adapter": "markdown_adapter", "line_count": len(lines)},
    )
