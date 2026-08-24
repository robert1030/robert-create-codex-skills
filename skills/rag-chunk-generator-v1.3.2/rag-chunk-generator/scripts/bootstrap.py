"""
bootstrap.py — rag-chunk-generator 相依自動安裝
每個 ensure_* 在對應的 import 之前呼叫，裝過秒跳過。
pip 一律帶 --break-system-packages。
"""
import subprocess
import sys
import importlib
import tempfile
import zipfile
from collections.abc import Callable
from pathlib import Path


def _ready(import_name: str, verify: Callable[[], bool] | None = None) -> tuple[bool, str | None]:
    try:
        importlib.import_module(import_name)
    except ImportError as exc:
        return False, f"import {import_name} 失敗：{exc}"
    if verify is None:
        return True, None
    try:
        if verify():
            return True, None
        return False, "安裝後功能驗證回傳 False"
    except Exception as exc:
        return False, f"功能驗證例外：{type(exc).__name__}: {exc}"


def _pip(
    pkg: str,
    import_name: str | None = None,
    verify: Callable[[], bool] | None = None,
) -> None:
    """安裝 pkg，並在安裝前後執行 import 與可選功能驗證。"""
    check = import_name or pkg.split("[")[0].replace("-", "_")
    ready, reason = _ready(check, verify)
    if ready:
        return
    if reason:
        print(f"[bootstrap] {pkg} 需要安裝或重新驗證：{reason}", flush=True)
    print(f"[bootstrap] 安裝 {pkg} ...", flush=True)
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", pkg, "--break-system-packages", "-q"]
    )
    # pip may create a new package directory while this process already has
    # a cached FileFinder result for site-packages.
    importlib.invalidate_caches()
    ready, reason = _ready(check, verify)
    if not ready:
        raise RuntimeError(f"{pkg} 安裝後仍不可用：{reason}")


def ensure_pdf() -> None:
    """Legacy PDF diagnostic route：pdfplumber。"""
    _pip("pdfplumber")


def ensure_docling() -> None:
    """PDF primary route：Docling。"""
    _pip("docling", verify=_verify_docling)


def ensure_marker() -> None:
    """Optional PDF text-layer comparison route：Marker。"""
    _pip("marker-pdf", "marker", verify=_verify_marker)


def ensure_docx() -> None:
    """Legacy DOCX compatibility route：python-docx。"""
    _pip("python-docx", "docx")


def ensure_markitdown() -> None:
    """DOCX／HTML／general XML route：MarkItDown。"""
    _pip("markitdown", "markitdown", verify=_verify_markitdown)


def ensure_markitdown_docx() -> None:
    """DOCX route：MarkItDown base package plus DOCX extra smoke test。"""
    _pip("markitdown[docx]", "markitdown", verify=_verify_markitdown_docx)


def ensure_trafilatura() -> None:
    """HTML article route：Trafilatura。"""
    _pip("trafilatura", verify=_verify_trafilatura)


def ensure_lxml() -> None:
    """Safe XML route：lxml with network and entity expansion disabled by code."""
    _pip("lxml", verify=_verify_lxml)


def ensure_mp4() -> None:
    """MP4 切片相依：openai-whisper、pydub、ffmpeg-python"""
    _pip("openai-whisper", "whisper")
    _pip("pydub")
    _pip("ffmpeg-python", "ffmpeg")


def ensure_tiktoken() -> None:
    """Token 計數相依：tiktoken"""
    _pip("tiktoken")


def ensure_all() -> None:
    """安裝全部相依。"""
    ensure_tiktoken()
    ensure_docling()
    ensure_marker()
    ensure_pdf()
    ensure_markitdown_docx()
    ensure_trafilatura()
    ensure_lxml()
    ensure_docx()
    ensure_mp4()


def _verify_docling() -> bool:
    try:
        from docling.document_converter import DocumentConverter
        return callable(DocumentConverter)
    except Exception:
        return False


def _verify_marker() -> bool:
    try:
        import marker
        return marker is not None
    except Exception:
        return False


def _verify_markitdown() -> bool:
    try:
        from markitdown import MarkItDown
        return callable(MarkItDown)
    except Exception:
        return False


def _write_docx_probe(path: Path) -> None:
    """Write a tiny valid DOCX without adding python-docx as a probe dependency."""
    content_types = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>"""
    relationships = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>"""
    document = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:body><w:p><w:r><w:t>rag chunk bootstrap probe</w:t></w:r></w:p>
<w:sectPr><w:pgSz w:w="11906" w:h="16838"/></w:sectPr></w:body>
</w:document>"""
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types)
        archive.writestr("_rels/.rels", relationships)
        archive.writestr("word/document.xml", document)


def _verify_markitdown_docx() -> bool:
    if not _verify_markitdown():
        return False
    try:
        from markitdown import MarkItDown
        with tempfile.TemporaryDirectory(prefix="rag_markitdown_probe_") as temp_dir:
            probe = Path(temp_dir) / "probe.docx"
            _write_docx_probe(probe)
            result = MarkItDown().convert(str(probe))
            text = getattr(result, "text_content", "")
            return "rag chunk bootstrap probe" in text
    except Exception:
        return False


def _verify_trafilatura() -> bool:
    try:
        import trafilatura
        text = trafilatura.extract("<html><body><p>bootstrap probe</p></body></html>")
        return isinstance(text, str) and "bootstrap probe" in text
    except Exception:
        return False


def _verify_lxml() -> bool:
    try:
        from lxml import etree
        return etree.fromstring(b"<probe/>").tag == "probe"
    except Exception:
        return False
