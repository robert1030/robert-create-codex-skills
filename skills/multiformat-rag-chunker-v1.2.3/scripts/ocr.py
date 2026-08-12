#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transparent OCR with three distinct strategies and quality validation."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from constants import MAX_RETRIES, OCR_LANGUAGES
from models import AttemptRecord
from utils import normalize_nfc, validate_text_quality
from visual import load_image


@dataclass(frozen=True, slots=True)
class OCRAdmission:
    admitted: bool
    reason: str
    capability_status: str
    evidence: tuple[str, ...] = ()
    llm_visual_attempted: bool = False


@dataclass(slots=True)
class OCRResult:
    text: str
    status: str
    attempts: list[AttemptRecord] = field(default_factory=list)
    confidence: float | None = None
    backend: str = "tesseract"
    quality: dict[str, Any] = field(default_factory=dict)


def _preprocess(image, attempt: int):
    from PIL import ImageEnhance, ImageFilter, ImageOps

    if attempt == 1:
        return image, {"resolution_scale": 1.0, "preprocessing": "none", "psm": 6}
    if attempt == 2:
        grayscale = ImageOps.grayscale(image)
        grayscale = ImageOps.autocontrast(grayscale)
        grayscale = grayscale.resize((grayscale.width * 2, grayscale.height * 2))
        return grayscale, {
            "resolution_scale": 2.0,
            "preprocessing": "grayscale_autocontrast_upscale",
            "psm": 6,
        }
    grayscale = ImageOps.grayscale(image)
    grayscale = ImageEnhance.Contrast(grayscale).enhance(2.0)
    grayscale = grayscale.filter(ImageFilter.MedianFilter(size=3))
    threshold = 170
    binary = grayscale.point(lambda value: 255 if value > threshold else 0)
    binary = binary.resize((binary.width * 2, binary.height * 2))
    return binary, {
        "resolution_scale": 2.0,
        "preprocessing": "contrast_median_adaptive_like_threshold",
        "threshold": threshold,
        "psm": 4,
    }


def _ocr_once(image, languages: str, psm: int) -> tuple[str, float | None, dict[str, Any]]:
    import pytesseract

    config = f"--psm {psm}"
    data = pytesseract.image_to_data(image, lang=languages, config=config, output_type=pytesseract.Output.DICT)
    tokens: list[str] = []
    confidences: list[float] = []
    line_map: dict[tuple[int, int, int], list[str]] = {}
    count = len(data.get("text", []))
    for index in range(count):
        token = str(data["text"][index]).strip()
        if not token:
            continue
        key = (
            int(data.get("block_num", [0] * count)[index]),
            int(data.get("par_num", [0] * count)[index]),
            int(data.get("line_num", [0] * count)[index]),
        )
        line_map.setdefault(key, []).append(token)
        tokens.append(token)
        try:
            confidence = float(data["conf"][index])
            if confidence >= 0:
                confidences.append(confidence)
        except Exception:
            pass
    lines = [" ".join(values) for _key, values in sorted(line_map.items())]
    text = normalize_nfc("\n".join(lines))
    confidence = sum(confidences) / len(confidences) if confidences else None
    return text, confidence, {"token_count": len(tokens), "line_count": len(lines)}


def _content_consistency(text: str) -> dict[str, Any]:
    visible = [ch for ch in text if not ch.isspace()]
    alnum = sum(ch.isalnum() for ch in visible)
    punctuation = sum(re.match(r"[^\w\s]", ch, flags=re.UNICODE) is not None for ch in visible)
    stack: list[str] = []
    opener_for = {")": "(", "]": "[", "}": "{"}
    unmatched_closer_count = 0
    for character in text:
        if character in "([{":
            stack.append(character)
        elif character in opener_for:
            if stack and stack[-1] == opener_for[character]:
                stack.pop()
            else:
                unmatched_closer_count += 1
    quote_count = sum(text.count(character) for character in ('"', "'", "“", "”", "‘", "’"))
    return {
        "alphanumeric_ratio": round(alnum / len(visible), 6) if visible else 0.0,
        "punctuation_ratio": round(punctuation / len(visible), 6) if visible else 0.0,
        "unmatched_delimiter_count": unmatched_closer_count + len(stack),
        "odd_quote_count": quote_count % 2,
    }


def _obvious_ocr_garbage(consistency: dict[str, Any], confidence: float | None) -> bool:
    """Reject only a low-confidence candidate with independent structural junk signals."""

    return bool(
        confidence is not None
        and confidence < 20.0
        and float(consistency.get("punctuation_ratio") or 0.0) >= 0.2
        and (
            int(consistency.get("unmatched_delimiter_count") or 0) > 0
            or int(consistency.get("odd_quote_count") or 0) > 0
        )
    )


def _ocr_backend_unavailable(error: Exception) -> bool:
    """Recognize an unavailable OCR runtime without naming it as a quality failure."""

    message = str(error).lower()
    return any(marker in message for marker in (
        "tesseract is not installed",
        "not in your path",
        "tesseractnotfounderror",
        "no module named 'pytesseract'",
    ))


def ocr_image(
    source: Path | bytes,
    *,
    admission: OCRAdmission,
    languages: str = OCR_LANGUAGES,
    max_attempts: int = MAX_RETRIES,
    forensic_dir: Path | None = None,
    unit_name: str = "image",
) -> OCRResult:
    if not admission.admitted:
        return OCRResult(
            "",
            "blocked",
            [],
            backend="not_invoked",
            quality={
                "reasons": [admission.reason],
                "capability_status": admission.capability_status,
                "llm_visual_attempted": admission.llm_visual_attempted,
            },
        )
    try:
        image = load_image(source)
    except Exception as exc:
        attempt = AttemptRecord(1, "pillow", "load_image", "failed", error=str(exc))
        return OCRResult("", "failed", [attempt], quality={"reasons": ["image_load_failed"]})

    attempts: list[AttemptRecord] = []
    best: tuple[float, str, float | None, dict[str, Any]] | None = None
    backend_unavailable = False
    for attempt_number in range(1, min(max_attempts, MAX_RETRIES) + 1):
        processed, parameters = _preprocess(image, attempt_number)
        if forensic_dir is not None:
            forensic_dir.mkdir(parents=True, exist_ok=True)
            processed.save(forensic_dir / f"{unit_name}-attempt-{attempt_number}.png")
        try:
            text, confidence, engine_metrics = _ocr_once(processed, languages, int(parameters["psm"]))
            if forensic_dir is not None:
                candidate_dir = forensic_dir.parent / "ocr-candidates"
                candidate_dir.mkdir(parents=True, exist_ok=True)
                (candidate_dir / f"{unit_name}-attempt-{attempt_number}.txt").write_text(text, encoding="utf-8")
            valid, reasons, quality_metrics = validate_text_quality(text, ocr=True)
            consistency = _content_consistency(text)
            garbage = _obvious_ocr_garbage(consistency, confidence)
            if garbage:
                reasons = [*reasons, "ocr_structural_garbage_detected"]
            quality = {**engine_metrics, **quality_metrics, **consistency, "reasons": reasons}
            enough_text = quality_metrics["visible_character_count"] >= 3
            consistency_ok = consistency["alphanumeric_ratio"] >= 0.25 or quality_metrics["visible_character_count"] < 12
            status = "success" if valid and enough_text and consistency_ok and not garbage else "low_quality"
            attempts.append(AttemptRecord(
                attempt=attempt_number,
                backend="tesseract",
                strategy=f"attempt_{attempt_number}",
                status=status,
                parameters={**parameters, "languages": languages},
                quality={**quality, "mean_confidence": confidence},
            ))
            score = (
                quality_metrics["visible_character_count"]
                + (confidence or 0.0) * 0.25
                + consistency["alphanumeric_ratio"] * 50.0
                - len(reasons) * 100.0
            )
            if best is None or score > best[0]:
                best = (score, text, confidence, quality)
            if status == "success":
                return OCRResult(text, "success", attempts, confidence, quality=quality)
        except Exception as exc:
            backend_unavailable = backend_unavailable or _ocr_backend_unavailable(exc)
            attempts.append(AttemptRecord(
                attempt=attempt_number,
                backend="tesseract",
                strategy=f"attempt_{attempt_number}",
                status="failed",
                parameters={**parameters, "languages": languages},
                error=str(exc),
            ))
    if best and best[1]:
        return OCRResult(best[1], "low_quality", attempts, best[2], quality=best[3])
    reason = "ocr_backend_not_available" if backend_unavailable else "no_ocr_text"
    return OCRResult("", "failed", attempts, quality={"reasons": [reason]})
