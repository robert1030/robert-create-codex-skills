#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small deterministic helpers shared across adapters and validators."""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import unicodedata
from pathlib import Path
from typing import Any, Iterable

CJK_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
LATIN_WORD_RE = re.compile(r"[A-Za-z0-9_]+(?:['-][A-Za-z0-9_]+)*")
SLUG_RE = re.compile(r"[^a-zA-Z0-9._-]+")
REPLACEMENT_CHARACTER = "\ufffd"
MOJIBAKE_MARKERS = ("Ã", "Â", "â€™", "â€œ", "â€", "ðŸ", "ï¿½")
CONTROL_ALLOWED = {"\n", "\r", "\t"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def slugify(value: str, fallback: str = "source") -> str:
    value = value.strip().replace(os.sep, "-")
    value = SLUG_RE.sub("-", value).strip("-._").lower()
    return value[:96] or fallback


def estimate_tokens(text: str) -> int:
    if not text:
        return 0
    cjk = len(CJK_RE.findall(text))
    words = len(LATIN_WORD_RE.findall(text))
    residual = CJK_RE.sub("", text)
    residual = LATIN_WORD_RE.sub("", residual)
    punctuation = len(re.findall(r"[^\s]", residual))
    return max(1, cjk + math.ceil(words * 1.25) + math.ceil(punctuation * 0.35))


def common_heading_path(paths: Iterable[Iterable[str]], fallback: Iterable[str] = ()) -> list[str]:
    """Return the longest common heading prefix, or a stable document fallback."""
    normalized = [list(path) for path in paths if path]
    if not normalized:
        return list(fallback)
    common = normalized[0]
    for path in normalized[1:]:
        length = 0
        for left, right in zip(common, path):
            if left != right:
                break
            length += 1
        common = common[:length]
        if not common:
            break
    return common or list(fallback)


def normalize_nfc(text: str) -> str:
    text = unicodedata.normalize("NFC", text or "")
    text = text.replace("\r\n", "\n").replace("\r", "\n").replace("\x00", "")
    text = "\n".join(re.sub(r"[ \t]+$", "", line) for line in text.split("\n"))
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def validate_text_quality(text: str, *, ocr: bool = False) -> tuple[bool, list[str], dict[str, Any]]:
    reasons: list[str] = []
    if REPLACEMENT_CHARACTER in text:
        reasons.append("replacement_character_detected")
    bad_controls = [ch for ch in text if unicodedata.category(ch) == "Cc" and ch not in CONTROL_ALLOWED]
    if bad_controls:
        reasons.append("control_character_detected")
    marker_hits = sum(text.count(marker) for marker in MOJIBAKE_MARKERS)
    if marker_hits >= max(2, len(text) // 500):
        reasons.append("probable_mojibake")
    visible = [ch for ch in text if not ch.isspace()]
    unknown_ratio = 0.0
    symbol_ratio = 0.0
    if visible:
        unknown_ratio = sum(ch in {"?", "□", "�", "▯"} for ch in visible) / len(visible)
        symbol_ratio = sum(unicodedata.category(ch).startswith("S") for ch in visible) / len(visible)
    if ocr and unknown_ratio > 0.08:
        reasons.append("ocr_unknown_character_ratio_high")
    if ocr and len(visible) >= 20 and symbol_ratio > 0.35:
        reasons.append("ocr_symbol_ratio_high")
    metrics = {
        "visible_character_count": len(visible),
        "unknown_character_ratio": round(unknown_ratio, 6),
        "symbol_ratio": round(symbol_ratio, 6),
    }
    return not reasons, reasons, metrics


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid_jsonl:{path.name}:{number}:{exc}") from exc
            if not isinstance(value, dict):
                raise ValueError(f"jsonl_record_not_object:{path.name}:{number}")
            records.append(value)
    return records
