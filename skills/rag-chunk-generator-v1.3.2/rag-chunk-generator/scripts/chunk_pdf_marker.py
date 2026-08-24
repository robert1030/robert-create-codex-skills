"""Optional Marker PDF adapter for pure text-layer comparison runs."""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

import bootstrap
import preprocess
from adapter_common import blocks_to_chunks


_PAGE_MARKER_RE = re.compile(r"^\s*(\d+)\s*$")
_DASH_LINE_RE = re.compile(r"^\s*-{3,}\s*$")
_INLINE_PAGE_MARKER_RE = re.compile(r"^\s*\{(\d+)\}\s*-{3,}\s*$")


def _marker_executable() -> str:
    names = ["marker_single.exe", "marker_single"] if sys.platform == "win32" else ["marker_single"]
    for name in names:
        local = Path(sys.executable).with_name(name)
        if local.exists():
            return str(local)
    found = shutil.which("marker_single")
    if found:
        return found
    raise RuntimeError("找不到 marker_single CLI，Marker 安裝可能未完成")


def _run_marker(
    path: Path,
    output_dir: Path,
    page_range: str | None = None,
) -> str:
    command = [
        _marker_executable(),
        str(path),
        "--output_dir", str(output_dir),
        "--output_format", "markdown",
        "--paginate_output",
        "--disable_ocr",
    ]
    if page_range:
        command.extend(["--page_range", page_range])
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()[-2000:]
        raise RuntimeError(f"Marker 轉換失敗：{detail}")
    candidates = [p for p in output_dir.rglob("*.md") if p.name.lower() != "index.md"]
    if not candidates:
        raise RuntimeError("Marker 未產生 Markdown 輸出")
    preferred = [p for p in candidates if p.stem.lower() == path.stem.lower()]
    return (preferred[0] if preferred else candidates[0]).read_text(encoding="utf-8")


def _marker_blocks(text: str) -> list[dict[str, Any]]:
    """Parse Marker pagination markers while retaining a stable source locator."""
    lines = text.splitlines()
    blocks: list[dict[str, Any]] = []
    current_lines: list[str] = []
    current_page: str | None = None
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
        content_lines = raw.splitlines()
        first = content_lines[0].strip()
        if first.startswith("|"):
            block_type = "table"
            value = "\n".join(content_lines)
        elif re.match(r"^(?:[-*+]\s+|\d+[.)]\s+)", first):
            block_type = "list"
            value = "\n".join(content_lines)
        else:
            block_type = "paragraph"
            value = " ".join(line.strip() for line in content_lines)
        page_label = current_page or "unknown"
        marker_page = int(current_page) + 1 if current_page and current_page.isdigit() else None
        blocks.append({
            "text": preprocess.normalize_text(value),
            "section_title": "｜".join(heading_stack) if heading_stack else None,
            "source_locator": f"marker-page:{page_label}:line:{start_line:04d}-{end_line:04d}",
            "block_type": block_type,
            "page_number": marker_page,
        })
        start_line = end_line + 1

    line_number = 0
    while line_number < len(lines):
        line = lines[line_number]
        inline_page_match = _INLINE_PAGE_MARKER_RE.match(line)
        if inline_page_match:
            flush(line_number)
            current_page = inline_page_match.group(1)
            line_number += 1
            start_line = line_number + 1
            continue
        page_match = _PAGE_MARKER_RE.match(line)
        next_line = lines[line_number + 1] if line_number + 1 < len(lines) else ""
        if page_match and _DASH_LINE_RE.match(next_line):
            flush(line_number)
            current_page = page_match.group(1)
            line_number += 2
            start_line = line_number + 1
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            flush(line_number)
            level = len(heading.group(1))
            title = preprocess.normalize_text(heading.group(2).strip())
            heading_stack[:] = heading_stack[:level - 1]
            heading_stack.append(title)
            marker_page = int(current_page) + 1 if current_page and current_page.isdigit() else None
            blocks.append({
                "text": title,
                "section_title": "｜".join(heading_stack),
                "source_locator": f"marker-page:{current_page or 'unknown'}:line:{line_number + 1:04d}",
                "block_type": "heading",
                "page_number": marker_page,
            })
            line_number += 1
            start_line = line_number + 1
            continue
        if line.strip():
            if not current_lines:
                start_line = line_number + 1
            current_lines.append(line)
        else:
            flush(line_number)
            start_line = line_number + 2
        line_number += 1
    flush(len(lines))
    return blocks


def chunk_pdf_marker(
    path: Path,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
    page_range: str | None = None,
) -> list[dict[str, Any]]:
    bootstrap.ensure_marker()
    with tempfile.TemporaryDirectory(prefix="rag_marker_") as temp_dir:
        text = _run_marker(path, Path(temp_dir), page_range=page_range)
    blocks = _marker_blocks(text)
    if not blocks:
        raise RuntimeError("Marker 未產生可切片文字")
    chunks = blocks_to_chunks(
        blocks,
        path,
        file_type="pdf",
        chunk_size=chunk_size,
        overlap=overlap,
        min_len=min_len,
        extraction_backend="marker",
    )
    if not chunks:
        raise RuntimeError("Marker 未產生可交付切片")
    return chunks
