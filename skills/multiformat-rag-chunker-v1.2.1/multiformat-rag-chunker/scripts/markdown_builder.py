#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build a human-readable normalized-document.md from verified Document IR blocks."""

from __future__ import annotations

from typing import Any

from models import Block, DocumentIR
from utils import normalize_nfc


def _escape_cell(value: Any) -> str:
    return normalize_nfc(str(value or "")).replace("|", "\\|").replace("\n", "<br>")


def _table_markdown(caption: str, header: list[Any], rows: list[list[Any]]) -> str:
    width = max(len(header), max((len(row) for row in rows), default=0))
    if width == 0:
        return caption.strip()
    normalized_header = [_escape_cell(header[index] if index < len(header) else "") for index in range(width)]
    normalized_rows = [
        [_escape_cell(row[index] if index < len(row) else "") for index in range(width)]
        for row in rows
    ]
    lines = [
        "| " + " | ".join(normalized_header) + " |",
        "| " + " | ".join("---" for _ in range(width)) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in normalized_rows)
    table = "\n".join(lines)
    return f"{caption.strip()}\n\n{table}" if caption.strip() else table


def _timestamp(seconds: float | None) -> str:
    if seconds is None:
        return "00:00:00.000"
    milliseconds = int(round(seconds * 1000))
    hours, remainder = divmod(milliseconds, 3600000)
    minutes, remainder = divmod(remainder, 60000)
    secs, millis = divmod(remainder, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}.{millis:03d}"


def placeholder_markdown(block: Block) -> str:
    location = block.location.to_dict()
    position = "未知位置"
    if location.get("page") is not None:
        position = f"第 {location['page']} 頁"
    elif location.get("dom_path"):
        position = location["dom_path"]
    elif location.get("xml_path"):
        position = location["xml_path"]
    elif location.get("time_start") is not None:
        position = _timestamp(float(location["time_start"]))
    reason = block.metadata.get("reason") or ", ".join(block.metadata.get("quality_reasons", [])) or "內容品質未達門檻"
    visual_class = block.metadata.get("visual_class") or block.type
    return "\n".join([
        "> [內容擷取未完成]",
        ">",
        f"> - 來源位置：{position}",
        f"> - 單元：{block.block_id}",
        f"> - 類型：{visual_class}",
        f"> - 狀態：{block.status}",
        f"> - 嘗試次數：{len(block.attempts)}",
        f"> - 原因：{reason}",
        "> - 詳細紀錄：failed-items.jsonl",
    ])


def block_to_markdown(block: Block) -> str:
    if block.status in {"failed", "low_quality"}:
        return placeholder_markdown(block) if block.required else ""
    if block.status == "skipped":
        return ""
    if block.type == "heading":
        level = int(block.metadata.get("level", max(1, len(block.heading_path))))
        level = max(1, min(6, level))
        return f"{'#' * level} {block.text.strip()}"
    if block.type == "paragraph":
        return block.text.strip()
    if block.type == "list":
        items = block.metadata.get("items")
        ordered = bool(block.metadata.get("ordered"))
        if isinstance(items, list) and items:
            return "\n".join(
                f"{index}. {normalize_nfc(str(item))}" if ordered else f"- {normalize_nfc(str(item))}"
                for index, item in enumerate(items, start=1)
            )
        return block.text.strip()
    if block.type == "table":
        return _table_markdown(
            str(block.metadata.get("caption", "")),
            list(block.metadata.get("header", [])),
            list(block.metadata.get("rows", [])),
        )
    if block.type == "code":
        language = block.metadata.get("language", "")
        if isinstance(language, list):
            language = language[0] if language else ""
        return f"```{language}\n{block.text.rstrip()}\n```"
    if block.type == "image":
        asset_id = block.location.asset_id or block.metadata.get("asset_id", "unknown")
        visual_class = block.metadata.get("visual_class", "image")
        return f"> [圖片內容：{asset_id}；分類：{visual_class}]\n>\n" + "\n".join(f"> {line}" for line in block.text.splitlines())
    if block.type == "transcript":
        start = _timestamp(block.location.time_start)
        end = _timestamp(block.location.time_end)
        return f"> [{start} 至 {end}] {block.text.strip()}"
    if block.type == "placeholder":
        return placeholder_markdown(block)
    return block.text.strip()


def build_normalized_markdown(document: DocumentIR) -> tuple[str, dict[str, str]]:
    parts: list[str] = []
    mapping: dict[str, str] = {}
    for block in document.blocks:
        markdown = block_to_markdown(block)
        if not markdown:
            continue
        mapping[block.block_id] = markdown
        parts.append(markdown)
    text = normalize_nfc("\n\n".join(parts)) + "\n"
    return text, mapping
