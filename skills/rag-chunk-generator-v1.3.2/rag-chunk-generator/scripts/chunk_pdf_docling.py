"""Docling PDF adapter with page provenance required for delivery."""
from pathlib import Path
from typing import Any, Iterable

import bootstrap
import preprocess
from adapter_common import blocks_to_chunks


def _value(value: Any) -> str:
    return str(getattr(value, "value", value))


def _iter_items(document: Any) -> Iterable[Any]:
    seen: set[int] = set()
    iterator = getattr(document, "iterate_items", None)
    if callable(iterator):
        try:
            result = iterator(with_groups=False)
        except TypeError:
            result = iterator()
        for entry in result:
            item = entry[0] if isinstance(entry, tuple) else entry
            if id(item) not in seen:
                seen.add(id(item))
                yield item
    for attr in ("texts", "tables"):
        for item in getattr(document, attr, []) or []:
            if id(item) not in seen:
                seen.add(id(item))
                yield item


def _item_text(item: Any, document: Any) -> str:
    text = getattr(item, "text", None)
    if isinstance(text, str) and text.strip():
        return text.strip()
    for method_name in ("export_to_markdown", "export_to_text"):
        method = getattr(item, method_name, None)
        if not callable(method):
            continue
        for args in ((), (document,)):
            try:
                value = method(*args)
            except TypeError:
                continue
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def _provenance(item: Any) -> tuple[int | None, str | None]:
    prov = getattr(item, "prov", None) or []
    first = prov[0] if prov else None
    page_number = getattr(first, "page_no", None) if first is not None else None
    if page_number is None:
        return None, None
    page_number = int(page_number)
    locator = f"p{page_number:03d}"
    bbox = getattr(first, "bbox", None)
    if bbox is not None:
        coords = []
        for name in ("l", "t", "r", "b"):
            value = getattr(bbox, name, None)
            if value is not None:
                coords.append(f"{name}={float(value):.1f}")
        if coords:
            locator += ":" + ",".join(coords)
    return page_number, locator


def chunk_pdf_docling(
    path: Path,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
) -> list[dict[str, Any]]:
    bootstrap.ensure_docling()
    from docling.document_converter import DocumentConverter

    result = DocumentConverter().convert(str(path))
    document = result.document
    blocks: list[dict[str, Any]] = []
    heading_stack: dict[int, str] = {}
    unlocated_text = False

    for item in _iter_items(document):
        text = _item_text(item, document)
        if not text:
            continue
        page_number, locator = _provenance(item)
        if page_number is None:
            unlocated_text = True
        label = _value(getattr(item, "label", "text")).lower()
        is_heading = "header" in label or label in {"title", "section_header"}
        if is_heading:
            level = int(getattr(item, "level", 1) or 1)
            heading_stack = {k: v for k, v in heading_stack.items() if k < level}
            heading_stack[level] = preprocess.normalize_text(text)
        section_title = "｜".join(heading_stack[k] for k in sorted(heading_stack)) or None
        blocks.append({
            "text": preprocess.normalize_text(text),
            "section_title": section_title,
            "source_locator": locator,
            "block_type": label or "text",
            "page_number": page_number,
        })

    if not blocks:
        raise RuntimeError("Docling 未產生可切片文字")
    if unlocated_text:
        raise RuntimeError("Docling 產生了沒有 page provenance 的文字，為避免失去 PDF 定位而停止")
    return blocks_to_chunks(
        blocks,
        path,
        file_type="pdf",
        chunk_size=chunk_size,
        overlap=overlap,
        min_len=min_len,
        extraction_backend="docling",
    )
