#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CSV adapter preserving native row and column structure."""

from __future__ import annotations

import csv
from pathlib import Path

from adapters.base import AdapterContext
from models import DocumentIR, Location
from utils import normalize_nfc


def _decode(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    for encoding in ("utf-8-sig", "utf-8", "cp950", "big5", "gb18030", "windows-1252"):
        try:
            return data.decode(encoding), encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError("csv", data, 0, 1, "unable_to_decode_csv")


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    text, encoding = _decode(path)
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample)
    except csv.Error:
        dialect = csv.excel
    rows = [[normalize_nfc(cell) for cell in row] for row in csv.reader(text.splitlines(), dialect)]
    rows = [row for row in rows if any(cell for cell in row)]
    title = path.stem
    blocks = [context.block(
        "heading", title, heading_path=[title], content_origin="derived_normalization",
        required=True, critical=True, verbatim=False, metadata={"level": 1, "title_from_filename": True},
    )]
    if rows:
        width = max(len(row) for row in rows)
        padded = [row + [""] * (width - len(row)) for row in rows]
        header = padded[0]
        blocks.append(context.block(
            "table", "", location=Location(row_start=1, row_end=len(padded)), heading_path=[title],
            content_origin="native_table", required=True, critical=True,
            metadata={"header": header, "rows": padded[1:], "logical_column_count": width, "data_row_count": len(padded) - 1, "encoding": encoding},
        ))
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={"adapter": "csv_adapter", "row_count": len(rows), "column_count": max((len(row) for row in rows), default=0), "encoding": encoding},
    )
