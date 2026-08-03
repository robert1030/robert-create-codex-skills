#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HTML and HTM adapter preserving DOM paths and local assets."""

from __future__ import annotations

import base64
import hashlib
import re
import warnings
from pathlib import Path
from urllib.parse import unquote, urlparse

from adapters.base import AdapterContext
from models import DocumentIR, Location
from ocr import ocr_image
from relationship_resolver import resolve_relationship
from utils import normalize_nfc
from visual import classify_visual, load_image


def _dom_path(tag) -> str:
    parts: list[str] = []
    current = tag
    while getattr(current, "name", None):
        parent = current.parent
        index = 1
        if parent is not None:
            siblings = [sibling for sibling in parent.find_all(current.name, recursive=False)]
            if current in siblings:
                index = siblings.index(current) + 1
        parts.append(f"{current.name}[{index}]")
        current = parent
    return "/" + "/".join(reversed(parts))


def _safe_local_image(base: Path, reference: str) -> Path | None:
    parsed = urlparse(reference)
    if parsed.scheme or parsed.netloc:
        return None
    candidate = (base.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(base.parent.resolve())
    except ValueError:
        return None
    return candidate if candidate.is_file() else None


def _image_bytes(base: Path, reference: str, context: AdapterContext) -> bytes | None:
    if reference.startswith("data:") and "," in reference:
        header, payload = reference.split(",", 1)
        try:
            return base64.b64decode(payload) if ";base64" in header else unquote(payload).encode("utf-8")
        except Exception:
            return None
    if context.collection_runtime is not None and context.collection_member_path:
        resolution = context.collection_runtime.resolve_relationship(
            context.collection_member_path,
            reference,
        )
        if resolution.status == "resolved" and resolution.target_member:
            local = context.collection_runtime.path_for(resolution.target_member)
            if local is not None and local.is_file():
                return local.read_bytes()
    local = _safe_local_image(base, reference)
    return local.read_bytes() if local else None


def _append_image(path: Path, tag, context: AdapterContext, blocks: list, heading_path: list[str], index: int) -> None:
    reference = str(tag.get("src", ""))
    asset_id = f"html-image-{index:03d}"
    data = _image_bytes(path, reference, context)
    if data is None:
        blocks.append(context.block(
            "image",
            "",
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="placeholder",
            required=bool(tag.get("alt")),
            status="failed" if tag.get("alt") else "skipped",
            verbatim=False,
            metadata={"asset_id": asset_id, "reference": reference, "reason": "remote_or_missing_local_image"},
        ))
        return
    image = load_image(data)
    inspection = classify_visual(image, name_hint=reference)
    asset_sha256 = hashlib.sha256(data).hexdigest()
    visual_review = (
        context.visual_semantics.lookup(reference, asset_sha256)
        if context.visual_semantics is not None
        else None
    )
    metadata = {
        "asset_id": asset_id,
        "reference": reference,
        "asset_sha256": asset_sha256,
        "visual_class": inspection.visual_class,
        "width": inspection.width,
        "height": inspection.height,
        "alt": normalize_nfc(str(tag.get("alt", ""))),
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
            "image",
            "\n".join(f"QR Code payload：{value}" for value in inspection.qr_payloads),
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="qr_decoder",
            required=True,
            critical=True,
            metadata={
                **metadata,
                "qr_payloads": inspection.qr_payloads,
                "machine_payloads": machine_payloads,
                "decoder_evidence": {"backend": "opencv_qrcode_detector", "verified": True},
            },
        ))
    elif inspection.visual_class == "screen_capture" and visual_review is not None:
        blocks.append(context.block(
            "image",
            visual_review.summary,
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="llm_visual_summary",
            required=True,
            verbatim=False,
            metadata={
                **metadata,
                "visual_summary_evidence": visual_review.evidence(),
            },
        ))
    elif inspection.visual_class == "screen_capture" and not tag.get("alt"):
        blocks.append(context.block(
            "image",
            "",
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="derived_normalization",
            required=False,
            status="skipped",
            verbatim=False,
            metadata={**metadata, "skip_reason": "no_verified_machine_payload"},
        ))
    elif inspection.visual_class == "barcode" and inspection.barcode_payloads:
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
            "image",
            "\n".join(f"Barcode payload：{value}" for value in inspection.barcode_payloads),
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="qr_decoder",
            required=True,
            critical=True,
            metadata={
                **metadata,
                "barcode_payloads": inspection.barcode_payloads,
                "machine_payloads": machine_payloads,
                "decoder_evidence": {
                    "backend": sorted({str(item["decoder"]) for item in barcode_details}),
                    "verified": True,
                },
            },
        ))
    elif inspection.visual_class in {"logo", "icon", "decorative", "photo"} and not tag.get("alt"):
        blocks.append(context.block(
            "image",
            "",
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="derived_normalization",
            required=False,
            status="skipped",
            verbatim=False,
            metadata={**metadata, "skip_reason": "non_required_visual"},
        ))
    elif tag.get("alt"):
        blocks.append(context.block(
            "image",
            normalize_nfc(str(tag.get("alt"))),
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="native_text",
            required=True,
            metadata=metadata,
        ))
    else:
        result = ocr_image(data, languages=context.ocr_languages)
        status = "success" if result.status == "success" else ("low_quality" if result.text else "failed")
        ocr_reasons = [str(reason) for reason in result.quality.get("reasons", [])]
        backend_unavailable = "ocr_backend_not_available" in ocr_reasons
        block = context.block(
            "image",
            result.text if result.status == "success" else "",
            location=Location(dom_path=_dom_path(tag), asset_id=asset_id),
            heading_path=list(heading_path),
            content_origin="ocr" if result.text else "placeholder",
            required=True,
            status=status,
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


def _relationship_records(soup, context: AdapterContext) -> list[dict[str, object]]:
    """Record every supported local or external relationship occurrence."""

    if context.collection_runtime is None or not context.collection_member_path:
        return []
    records: list[dict[str, object]] = []
    attributes = ("href", "src", "data")
    for tag in soup.find_all(True):
        for attribute in attributes:
            value = tag.get(attribute)
            if not isinstance(value, str) or not value.strip():
                continue
            semantic_hint = str(tag.get("title") or "").strip()
            resolution = context.collection_runtime.resolve_relationship(
                context.collection_member_path,
                value,
                semantic_hint=semantic_hint,
            )
            records.append({
                "raw_reference": resolution.raw_reference,
                "source_member": resolution.source_member,
                "location": _dom_path(tag),
                "relationship_type": f"html_{tag.name}_{attribute}",
                "target_member": resolution.target_member,
                "fragment": resolution.fragment,
                "status": resolution.status,
                "strategy": resolution.strategy,
                "evidence": resolution.evidence,
            })
    return records


def _append_paragraph(text: str, tag, context: AdapterContext, blocks: list, heading_path: list[str]) -> None:
    # A non-breaking-space-only inline node is present in the DOM but carries
    # no chunkable text.  Do not turn it into an empty required Block.
    compact = normalize_nfc(text).strip()
    if not compact:
        return
    critical = bool(re.search(r"\b20\d{2}[-/.]\d{1,2}[-/.]\d{1,2}\b|warning|禁止|不得|must not", compact, re.IGNORECASE))
    blocks.append(context.block(
        "paragraph", compact, location=Location(dom_path=_dom_path(tag)), heading_path=list(heading_path),
        content_origin="native_text", required=True, critical=critical,
    ))


def _direct_list_items(tag) -> tuple[list[str], int]:
    """Keep visible direct children of malformed lists in their DOM order."""

    from bs4.element import NavigableString, Tag

    items: list[str] = []
    non_li_count = 0
    for child in tag.contents:
        value = ""
        if isinstance(child, NavigableString):
            value = normalize_nfc(str(child)).strip()
            if value:
                non_li_count += 1
        elif isinstance(child, Tag):
            if child.name in {"script", "style", "noscript", "template", "br"}:
                continue
            value = normalize_nfc(child.get_text(" ", strip=True))
            if child.name != "li" and value:
                non_li_count += 1
        if value:
            items.append(value)
    return items, non_li_count


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
    from bs4.element import NavigableString, Tag

    data = path.read_bytes()
    # Some legacy ``.htm`` members contain XML-like markup.  Parsing remains
    # intentionally HTML-first, while the parser warning is not actionable for
    # the batch runtime and would otherwise corrupt machine-readable stderr.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", XMLParsedAsHTMLWarning)
        soup = BeautifulSoup(data, "lxml")
    relationships = _relationship_records(soup, context)
    for unwanted in soup(["script", "style", "noscript", "template"]):
        unwanted.decompose()
    title = normalize_nfc(soup.title.get_text(" ", strip=True)) if soup.title else path.stem
    blocks = []
    heading_path: list[str] = []
    image_index = 0
    semantic_containers = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "table", "pre", "code"}
    ignored_ancestors = {"head", "script", "style", "noscript", "template"}
    for node in soup.descendants:
        if isinstance(node, Tag):
            tag = node
        elif isinstance(node, NavigableString):
            parent = node.parent
            if parent is None or any(getattr(ancestor, "name", None) in ignored_ancestors for ancestor in node.parents):
                continue
            if any(getattr(ancestor, "name", None) in semantic_containers for ancestor in node.parents):
                continue
            text = normalize_nfc(str(node).strip())
            if text:
                _append_paragraph(text, parent, context, blocks, heading_path)
            continue
        else:
            continue
        if tag.name == "img":
            image_index += 1
            _append_image(path, tag, context, blocks, heading_path, image_index)
            continue
        if tag.name not in semantic_containers:
            continue
        if tag.name == "code" and tag.find_parent("pre"):
            continue
        if tag.find_parent(["pre", "table", "ul", "ol"]) and tag.name in {"p", "code"}:
            continue
        text = normalize_nfc(tag.get_text(" ", strip=True))
        if not text:
            continue
        location = Location(dom_path=_dom_path(tag))
        if re.fullmatch(r"h[1-6]", tag.name):
            level = int(tag.name[1])
            heading_path = heading_path[: level - 1] + [text]
            if level == 1:
                title = text
            blocks.append(context.block(
                "heading", text, location=location, heading_path=list(heading_path),
                content_origin="native_text", required=True, critical=True,
                metadata={"level": level},
            ))
        elif tag.name in {"ul", "ol"}:
            items, direct_non_li_count = _direct_list_items(tag)
            if items:
                ordered = tag.name == "ol"
                rendered = "\n".join(f"{index}. {item}" if ordered else f"- {item}" for index, item in enumerate(items, start=1))
                blocks.append(context.block(
                    "list", rendered, location=location, heading_path=list(heading_path),
                    content_origin="native_text", required=True,
                    metadata={
                        "ordered": ordered,
                        "items": items,
                        "item_count": len(items),
                        "direct_non_li_child_count": direct_non_li_count,
                    },
                ))
        elif tag.name == "table":
            caption_tag = tag.find("caption", recursive=False)
            caption = normalize_nfc(caption_tag.get_text(" ", strip=True)) if caption_tag else ""
            rows = []
            for row in tag.find_all("tr"):
                cells = [normalize_nfc(cell.get_text(" ", strip=True)) for cell in row.find_all(["th", "td"], recursive=False)]
                if cells:
                    rows.append(cells)
            if rows or caption:
                header = rows[0] if rows else []
                blocks.append(context.block(
                    "table", "", location=location, heading_path=list(heading_path),
                    content_origin="native_table", required=True, critical=True,
                    metadata={
                        "caption": caption,
                        "header": header,
                        "rows": rows[1:],
                        "logical_column_count": len(header),
                        "data_row_count": len(rows) - 1,
                        "heading_context": list(heading_path),
                    },
                ))
        elif tag.name in {"pre", "code"}:
            blocks.append(context.block(
                "code", tag.get_text("", strip=False).strip(), location=location,
                heading_path=list(heading_path), content_origin="native_text",
                required=True, critical=True, metadata={"language": tag.get("class", [])},
            ))
        else:
            _append_paragraph(text, tag, context, blocks, heading_path)
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={
            "adapter": "html_adapter",
            "dom_element_count": len(blocks),
            "relationships": relationships,
        },
    )
