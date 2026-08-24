"""MarkItDown, Trafilatura and safe XML adapters for v1.3.2."""
import codecs
import re
from pathlib import Path
from typing import Any

import bootstrap
import preprocess
from adapter_common import blocks_to_chunks


# These limits bound local parsing work without changing the output contract.
_MAX_HTML_BYTES = 20 * 1024 * 1024
_MAX_XML_BYTES = 10 * 1024 * 1024
_MAX_XML_ELEMENTS = 100_000
_MAX_XML_DEPTH = 128
_HTML_HEAD_BYTES = 64 * 1024
_HTML_CHARSET_RE = re.compile(
    rb"charset\s*=\s*['\"]?\s*([A-Za-z0-9._:-]+)", re.IGNORECASE
)


def _read_html_source(path: Path) -> str:
    """Decode HTML explicitly so an unknown encoding never becomes U+FFFD."""
    raw = path.read_bytes()
    if len(raw) > _MAX_HTML_BYTES:
        raise RuntimeError(
            f"HTML 檔案超過安全大小上限：{len(raw)} bytes > {_MAX_HTML_BYTES} bytes"
        )

    if raw.startswith(codecs.BOM_UTF32_LE) or raw.startswith(codecs.BOM_UTF32_BE):
        encoding = "utf-32"
    elif raw.startswith(codecs.BOM_UTF16_LE) or raw.startswith(codecs.BOM_UTF16_BE):
        encoding = "utf-16"
    elif raw.startswith(codecs.BOM_UTF8):
        encoding = "utf-8-sig"
    else:
        match = _HTML_CHARSET_RE.search(raw[:_HTML_HEAD_BYTES])
        encoding = match.group(1).decode("ascii") if match else "utf-8"

    try:
        codecs.lookup(encoding)
        text = raw.decode(encoding)
    except (LookupError, UnicodeDecodeError) as exc:
        raise RuntimeError(
            f"HTML 編碼無法嚴格解碼：{encoding}。請提供正確的 meta charset 或 BOM"
        ) from exc
    if "\ufffd" in text:
        raise RuntimeError("HTML 解碼產生 replacement character，停止避免資料遺失")
    return text


def _heading_stack_title(stack: list[str]) -> str | None:
    return "｜".join(stack) if stack else None


def _markdown_blocks(text: str) -> list[dict[str, Any]]:
    """Parse converter Markdown into coarse semantic blocks with line locators."""
    blocks: list[dict[str, Any]] = []
    current_lines: list[str] = []
    start_line = 1
    heading_stack: list[str] = []

    def flush(end_line: int) -> None:
        nonlocal current_lines, start_line
        if not current_lines:
            return
        raw = "\n".join(current_lines).strip()
        current_lines = []
        if not raw:
            start_line = end_line + 1
            return
        lines = raw.splitlines()
        first = lines[0].strip()
        if first.startswith("|"):
            block_type = "table"
            value = "\n".join(lines)
        elif re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", first):
            block_type = "list"
            value = "\n".join(lines)
        else:
            block_type = "paragraph"
            value = " ".join(line.strip() for line in lines)
        blocks.append({
            "text": preprocess.normalize_text(value),
            "section_title": _heading_stack_title(heading_stack),
            "source_locator": f"converted-line:{start_line:04d}-{end_line:04d}",
            "block_type": block_type,
            "page_number": None,
        })
        start_line = end_line + 1

    lines = text.splitlines()
    for line_number, line in enumerate(lines, 1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            flush(line_number - 1)
            level = len(match.group(1))
            title = preprocess.normalize_text(match.group(2).strip())
            heading_stack[:] = heading_stack[:level - 1]
            heading_stack.append(title)
            blocks.append({
                "text": title,
                "section_title": _heading_stack_title(heading_stack),
                "source_locator": f"converted-line:{line_number:04d}",
                "block_type": "heading",
                "page_number": None,
            })
            start_line = line_number + 1
        elif line.strip():
            if not current_lines:
                start_line = line_number
            current_lines.append(line)
        else:
            flush(line_number - 1)
            start_line = line_number + 1
    flush(len(lines))
    return blocks


def _convert_markitdown(path: Path, file_type: str) -> str:
    if file_type == "html":
        # MarkItDown reads the path itself.  Preflight with the same source
        # bytes first so an encoding failure is explicit rather than silent.
        _read_html_source(path)
    if file_type == "docx":
        bootstrap.ensure_markitdown_docx()
    else:
        bootstrap.ensure_markitdown()
    from markitdown import MarkItDown

    result = MarkItDown().convert(str(path))
    text = getattr(result, "text_content", None)
    if not isinstance(text, str) or not text.strip():
        raise RuntimeError("MarkItDown 未產生可切片文字")
    return text


def _convert_trafilatura(path: Path) -> str:
    bootstrap.ensure_trafilatura()
    import trafilatura

    html = _read_html_source(path)
    text = trafilatura.extract(
        html,
        output_format="markdown",
        include_comments=False,
        include_tables=True,
        favor_precision=True,
    )
    if not isinstance(text, str) or not text.strip():
        raise RuntimeError("Trafilatura 未辨識出 HTML 主文")
    return text


def _xml_blocks(path: Path) -> list[dict[str, Any]]:
    """Parse bounded XML without DTD, entity expansion or network access."""
    bootstrap.ensure_lxml()
    from lxml import etree

    raw = path.read_bytes()
    if len(raw) > _MAX_XML_BYTES:
        raise RuntimeError(
            f"XML 檔案超過安全大小上限：{len(raw)} bytes > {_MAX_XML_BYTES} bytes"
        )
    if re.search(rb"<!DOCTYPE\b|<!ENTITY\b", raw, re.IGNORECASE):
        raise RuntimeError("XML safe 路由不接受 DOCTYPE 或 ENTITY 宣告")

    parser = etree.XMLParser(
        resolve_entities=False,
        no_network=True,
        load_dtd=False,
        dtd_validation=False,
        recover=False,
        huge_tree=False,
    )
    try:
        root = etree.fromstring(raw, parser)
    except etree.XMLSyntaxError as exc:
        raise RuntimeError(f"XML 解析失敗：{exc}") from exc

    stack = [(root, 1)]
    element_count = 0
    while stack:
        element, depth = stack.pop()
        if not isinstance(element.tag, str):
            continue
        element_count += 1
        if element_count > _MAX_XML_ELEMENTS:
            raise RuntimeError(
                f"XML 元素數超過安全上限：>{_MAX_XML_ELEMENTS} 個"
            )
        if depth > _MAX_XML_DEPTH:
            raise RuntimeError(
                f"XML 巢狀深度超過安全上限：>{_MAX_XML_DEPTH} 層"
            )
        stack.extend(
            (child, depth + 1)
            for child in reversed(list(element))
            if isinstance(child.tag, str)
        )

    blocks: list[dict[str, Any]] = []

    def tag_identity(node: Any) -> tuple[str, str] | None:
        try:
            if not isinstance(node.tag, str):
                return None
            qname = etree.QName(node)
            return qname.namespace or "", qname.localname
        except (TypeError, ValueError):
            return None

    def display_name(node: Any) -> str:
        identity = tag_identity(node)
        if identity is None:
            return ""
        namespace, local = identity
        return f"{{{namespace}}}{local}" if namespace else local

    def display_attribute(key: str) -> str:
        qname = etree.QName(key)
        if qname.namespace:
            return f"@{{{qname.namespace}}}{qname.localname}"
        return f"@{qname.localname}"

    def visit(element, path_text: str) -> None:
        identity = tag_identity(element)
        tag = display_name(element)
        if not tag:
            return
        current_path = f"{path_text}/{tag}" if path_text else f"/{tag}"
        siblings = (
            [s for s in element.getparent() if tag_identity(s) == identity]
            if element.getparent() is not None
            else []
        )
        if len(siblings) > 1:
            current_path += f"[{siblings.index(element) + 1}]"
        lines = [current_path]
        for key, value in element.attrib.items():
            lines.append(f"{display_attribute(key)}={value}")
        direct_segments = [element.text or ""]
        direct_segments.extend(child.tail or "" for child in element)
        has_mixed_context = any(segment.strip() for segment in direct_segments)
        if has_mixed_context:
            mixed_text = " ".join(
                part.strip() for part in element.itertext() if part.strip()
            )
            if mixed_text:
                lines.append(mixed_text)
        if len(lines) > 1:
            blocks.append({
                "text": preprocess.normalize_text("\n".join(lines)),
                "section_title": current_path,
                "source_locator": current_path,
                "block_type": "xml_element",
                "page_number": None,
            })
        for child in element:
            visit(child, current_path)

    visit(root, "")
    if not blocks:
        raise RuntimeError("XML 未產生可切片的元素文字或屬性")
    return blocks


def chunk_markup(
    path: Path,
    file_type: str,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
    html_mode: str = "document",
    xml_backend: str = "safe",
) -> list[dict[str, Any]]:
    if file_type == "xml" and xml_backend == "safe":
        blocks = _xml_blocks(path)
        backend = "lxml-safe"
    else:
        if file_type == "html" and html_mode == "article":
            text = _convert_trafilatura(path)
            backend = "trafilatura"
        else:
            text = _convert_markitdown(path, file_type)
            backend = "markitdown"
        blocks = _markdown_blocks(text)
    chunks = blocks_to_chunks(
        blocks,
        path,
        file_type=file_type,
        chunk_size=chunk_size,
        overlap=overlap,
        min_len=min_len,
        extraction_backend=backend,
    )
    if not chunks:
        raise RuntimeError(f"{file_type.upper()} adapter 未產生可切片內容")
    return chunks
