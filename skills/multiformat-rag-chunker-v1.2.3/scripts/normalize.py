#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Central text and structure normalization for Document IR blocks."""

from __future__ import annotations

import re
from collections import Counter
from typing import Iterable

from models import Block
from utils import normalize_nfc, validate_text_quality

PAGE_FOOTER_RE = re.compile(r"^\s*(?:PAGE|PAG\s*E)\s*\d+\s*$", re.IGNORECASE)
ISOLATED_PAGE_RE = re.compile(r"^\s*\d+\s*$")
POS_SEPARATOR_RE = re.compile(
    r"\s*/\s*(?=(?:adj|adv|aux|conj|det|n|num|prep|pron|v)\.)",
    re.IGNORECASE,
)


def _normalize_general_table_text(value: object) -> str:
    text = normalize_nfc(str(value or ""))
    text = re.sub(r"\s+", " ", text).strip()
    return POS_SEPARATOR_RE.sub(" / ", text)


def _normalize_table_general_text(block: Block) -> list[str]:
    header = block.metadata.get("header")
    rows = block.metadata.get("rows")
    if not isinstance(header, list) or not isinstance(rows, list):
        return []
    normalized_header = [normalize_nfc(str(value or "")).strip() for value in header]
    target_columns = [
        index
        for index, value in enumerate(normalized_header)
        if "定義" in value or ("詞性" in value and "中文" in value)
    ]
    if not target_columns and len(normalized_header) == 4 and normalized_header[2].upper() == "IPA":
        target_columns = [3]
    changed = False
    for row in rows:
        if not isinstance(row, list):
            continue
        for index in target_columns:
            if index >= len(row):
                continue
            original = row[index]
            normalized = _normalize_general_table_text(original)
            if normalized != original:
                row[index] = normalized
                changed = True
    return ["table_general_text_whitespace_normalized"] if changed else []


def join_soft_lines(text: str) -> tuple[str, list[str]]:
    text = normalize_nfc(text)
    if "\n" not in text:
        return text, []
    lines = [line.strip() for line in text.splitlines()]
    output: list[str] = []
    changes: list[str] = []
    for line in lines:
        if not line:
            if output and output[-1] != "":
                output.append("")
            continue
        if not output or output[-1] == "":
            output.append(line)
            continue
        previous = output[-1]
        if previous.endswith("-") and re.search(r"[A-Za-z]-$", previous) and re.match(r"^[a-z]", line):
            output[-1] = previous[:-1] + line
            changes.append("english_soft_hyphen_joined")
        elif not re.search(r"[。！？.!?:;：；]$", previous) and not re.match(r"^(?:[-*+] |\d+[.)]\s)", line):
            separator = "" if re.search(r"[\u3400-\u9fff]$", previous) and re.match(r"^[\u3400-\u9fff]", line) else " "
            output[-1] = previous + separator + line
            changes.append("soft_line_joined")
        else:
            output.append(line)
    return normalize_nfc("\n".join(output)), sorted(set(changes))


def remove_page_noise(text: str) -> tuple[str, list[str]]:
    lines: list[str] = []
    changes: list[str] = []
    for line in normalize_nfc(text).splitlines():
        compact = re.sub(r"\s+", " ", line).strip()
        if PAGE_FOOTER_RE.match(compact):
            changes.append("page_footer_removed")
            continue
        lines.append(line)
    return normalize_nfc("\n".join(lines)), sorted(set(changes))


def normalize_block(block: Block) -> Block:
    raw = block.raw_text if block.raw_text is not None else block.text
    text, noise_changes = remove_page_noise(raw)
    if block.type in {"paragraph", "heading", "transcript"}:
        text, line_changes = join_soft_lines(text)
    else:
        line_changes = []
    table_changes = _normalize_table_general_text(block) if block.type == "table" else []
    block.raw_text = raw
    block.text = normalize_nfc(text)
    block.heading_path = [normalize_nfc(value) for value in block.heading_path if normalize_nfc(value)]
    block.transformation_summary = sorted(
        set(block.transformation_summary + noise_changes + line_changes + table_changes + ["unicode_nfc"])
    )
    # A block that consisted entirely of recognized page or repeated-header
    # noise remains in the IR for provenance, but is no longer a required
    # semantic unit.  Leaving it as required would create an empty block that
    # the chunk completeness gate must correctly reject.
    if not block.text.strip() and noise_changes and "collection_occurrence" in block.metadata:
        block.required = False
        block.status = "skipped"
        block.metadata["skip_reason"] = "normalization_only_noise"
    valid, reasons, metrics = validate_text_quality(block.text, ocr=block.content_origin == "ocr")
    block.metadata.setdefault("quality", {}).update(metrics)
    if not valid and block.status == "success":
        block.status = "low_quality"
        block.metadata["quality_reasons"] = reasons
    return block


def _is_admitted_dense_visual_text(block: Block) -> bool:
    return (
        block.content_origin == "llm_visual_text"
        and block.metadata.get("dense_text_required") is True
    )


def _remove_repeated_headers(blocks: list[Block]) -> None:
    candidates = [
        block.text.strip()
        for block in blocks
        if block.location.page
        and block.type in {"heading", "paragraph"}
        and len(block.text.strip()) <= 80
        and not _is_admitted_dense_visual_text(block)
    ]
    counts = Counter(candidates)
    repeated = {value for value, count in counts.items() if value and count >= 2}
    for block in blocks:
        if _is_admitted_dense_visual_text(block):
            continue
        if block.text.strip() in repeated:
            block.status = "skipped"
            block.required = False
            block.metadata["skip_reason"] = "repeated_header"


def normalize_document_blocks(blocks: Iterable[Block]) -> list[Block]:
    normalized = [normalize_block(block) for block in blocks]
    _remove_repeated_headers(normalized)
    seen: set[tuple[str, str, int | None]] = set()
    for block in normalized:
        if block.status != "success" or not block.text:
            continue
        if _is_admitted_dense_visual_text(block):
            # Each admitted dense-text unit must remain independently
            # addressable even when its text repeats elsewhere.
            continue
        if "collection_occurrence" in block.metadata:
            # In a collection the source path and occurrence are semantic data.
            # Equal text at distinct DOM or XML positions must remain auditable.
            continue
        key = (block.type, block.text, block.location.page)
        if key in seen and block.type not in {"table", "image", "code"}:
            block.status = "skipped"
            block.required = False
            block.metadata["skip_reason"] = "duplicate_text"
        else:
            seen.add(key)
    return normalized
