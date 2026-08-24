"""Small common layer for v1.3 extraction adapters.

Adapters return blocks with text and source-location metadata.  This module
turns those blocks into the existing chunk contract without owning any
format-specific parsing logic.
"""
import re
from pathlib import Path
from typing import Any

import enc_compat
import preprocess


_ENC = enc_compat.get_encoding()


def count_tokens(text: str) -> int:
    return len(_ENC.encode(text))


def _split_long_text(text: str, chunk_size: int) -> list[str]:
    """Split by sentences first, then use token windows for one long sentence."""
    sentences = [s for s in re.split(r"(?<=[。！？.!?])\s*", text) if s]
    pieces: list[str] = []
    buf = ""
    for sentence in sentences:
        if count_tokens(sentence) > chunk_size:
            if buf.strip():
                pieces.append(buf.strip())
                buf = ""
            ids = _ENC.encode(sentence)
            for start in range(0, len(ids), chunk_size):
                part = _ENC.decode(ids[start:start + chunk_size]).strip()
                if part:
                    pieces.append(part)
            continue
        candidate = (buf + " " + sentence).strip() if buf else sentence
        if count_tokens(candidate) <= chunk_size:
            buf = candidate
        else:
            if buf.strip():
                pieces.append(buf.strip())
            buf = sentence
    if buf.strip():
        pieces.append(buf.strip())
    return pieces or [text.strip()]


def _merge_blocks(left: dict[str, Any], right: dict[str, Any]) -> dict[str, Any]:
    merged = dict(left)
    merged["text"] = (left.get("text", "") + " " + right.get("text", "")).strip()
    left_locator = left.get("source_locator")
    right_locator = right.get("source_locator")
    if left_locator and right_locator and left_locator != right_locator:
        merged["source_locator"] = f"{left_locator};{right_locator}"
    elif right_locator and not left_locator:
        merged["source_locator"] = right_locator
    return merged


def _safe_locator(value: str | None, page_number: int | None) -> str:
    if value:
        slug = re.sub(r"[^\w.-]+", "_", str(value)).strip("_")
        if slug:
            return slug[:48]
    if page_number is not None:
        return f"p{page_number:03d}"
    return "doc"


def blocks_to_chunks(
    blocks: list[dict[str, Any]],
    path: Path,
    file_type: str,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
    extraction_backend: str = "unknown",
) -> list[dict[str, Any]]:
    """Convert normalized adapter blocks to v1.3 chunks."""
    if chunk_size <= 0:
        raise ValueError("chunk_size 必須大於 0")
    if overlap < 0:
        raise ValueError("overlap 不可小於 0")
    if min_len < 0:
        raise ValueError("min_len 不可小於 0")
    slug = re.sub(r"[^\w]", "_", path.stem)[:40]
    fine_blocks: list[dict[str, Any]] = []
    for block in blocks:
        text = preprocess.normalize_text(str(block.get("text", "")).strip())
        if not text:
            continue
        base = dict(block)
        base["text"] = text
        if count_tokens(text) > chunk_size:
            for part in _split_long_text(text, chunk_size):
                fine_blocks.append({**base, "text": part})
        else:
            fine_blocks.append(base)

    merged: list[dict[str, Any]] = []
    pending: dict[str, Any] | None = None
    for block in fine_blocks:
        if pending is not None:
            candidate = _merge_blocks(pending, block)
            if count_tokens(candidate["text"]) <= chunk_size:
                block = candidate
                pending = None
            else:
                merged.append(pending)
                pending = None
        if count_tokens(block["text"]) < min_len:
            if merged:
                candidate = _merge_blocks(merged[-1], block)
                if count_tokens(candidate["text"]) <= chunk_size:
                    merged[-1] = candidate
                else:
                    merged.append(block)
            else:
                pending = block
        else:
            merged.append(block)
    if pending is not None:
        if merged:
            merged[-1] = _merge_blocks(merged[-1], pending)
        else:
            merged.append(pending)

    chunks: list[dict[str, Any]] = []
    prev_tail = ""
    for index, block in enumerate(merged):
        text = (prev_tail + " " + block["text"]).strip() if prev_tail else block["text"]
        ids = _ENC.encode(block["text"])
        if overlap == 0:
            prev_tail = ""
        else:
            prev_tail = _ENC.decode(ids[-overlap:]) if len(ids) > overlap else block["text"]

        page_number = block.get("page_number")
        locator = _safe_locator(block.get("source_locator"), page_number)
        chunk_id = f"{slug}_{locator}_{index:04d}"
        chunks.append({
            "chunk_id": chunk_id,
            "text": text,
            "source_file": path.name,
            "file_type": file_type,
            "chunk_index": index,
            "page_number": page_number,
            "start_time": block.get("start_time"),
            "end_time": block.get("end_time"),
            "section_title": block.get("section_title"),
            "token_count": count_tokens(text),
            "summary": "",
            "source_locator": block.get("source_locator"),
            "block_type": block.get("block_type", "text"),
            "extraction_backend": extraction_backend,
            "quality_status": "NOT_CHECKED",
        })

    for index, chunk in enumerate(chunks):
        chunk["prev_chunk_id"] = chunks[index - 1]["chunk_id"] if index else None
        chunk["next_chunk_id"] = chunks[index + 1]["chunk_id"] if index + 1 < len(chunks) else None
    return chunks
