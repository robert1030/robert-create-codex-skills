#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Single adapter registry. Adapters parse formats and return Document IR only."""

from __future__ import annotations

from pathlib import Path
from typing import Callable

from adapters.base import AdapterContext
from models import DocumentIR

AdapterFunction = Callable[[Path, AdapterContext], DocumentIR]


def get_adapter(extension: str) -> tuple[str, AdapterFunction]:
    extension = extension.lower()
    if extension == ".pdf":
        from adapters.pdf_adapter import parse
        return "pdf_adapter", parse
    if extension == ".docx":
        from adapters.docx_adapter import parse
        return "docx_adapter", parse
    if extension == ".doc":
        from adapters.doc_adapter import parse
        return "doc_adapter", parse
    if extension in {".html", ".htm"}:
        from adapters.html_adapter import parse
        return "html_adapter", parse
    if extension == ".xml":
        from adapters.xml_adapter import parse
        return "xml_adapter", parse
    if extension == ".csv":
        from adapters.csv_adapter import parse
        return "csv_adapter", parse
    if extension in {".md", ".markdown"}:
        from adapters.markdown_adapter import parse
        return "markdown_adapter", parse
    if extension in {".jpg", ".jpeg", ".png", ".heif", ".heic"}:
        from adapters.image_adapter import parse
        return "image_adapter", parse
    if extension == ".mp4":
        from adapters.video_adapter import parse
        return "video_adapter", parse
    raise ValueError(f"unsupported_extension:{extension}")
