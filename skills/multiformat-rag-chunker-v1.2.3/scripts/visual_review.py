#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deterministic assets and evidence helpers for native visual review."""

from __future__ import annotations

import hashlib
import io
from typing import Any


VISUAL_REVIEW_RENDER_SCALE = 2.0


def render_pdf_page_png(page: Any, scale: float = VISUAL_REVIEW_RENDER_SCALE) -> bytes:
    import fitz

    pixmap = page.get_pixmap(matrix=fitz.Matrix(scale, scale), alpha=False)
    return pixmap.tobytes("png")


def pdf_page_reference(page_number: int) -> str:
    return f"pages/page-{page_number:03d}.png"


def image_sha256(image_bytes: bytes) -> str:
    return hashlib.sha256(image_bytes).hexdigest()


def blank_image_metrics(image_bytes: bytes) -> dict[str, float]:
    from PIL import Image, ImageStat

    with Image.open(io.BytesIO(image_bytes)) as opened:
        grayscale = opened.convert("L")
        grayscale.thumbnail((512, 512))
        histogram = grayscale.histogram()
        total = max(1, sum(histogram))
        nonwhite = sum(histogram[:245])
        mean = float(ImageStat.Stat(grayscale).mean[0])
        stddev = float(ImageStat.Stat(grayscale).stddev[0])
    return {
        "mean_luminance": round(mean, 6),
        "luminance_stddev": round(stddev, 6),
        "nonwhite_ratio": round(nonwhite / total, 6),
    }


def is_effectively_blank(image_bytes: bytes) -> tuple[bool, dict[str, float]]:
    metrics = blank_image_metrics(image_bytes)
    blank = (
        metrics["mean_luminance"] >= 250.0
        and metrics["luminance_stddev"] <= 3.0
        and metrics["nonwhite_ratio"] <= 0.002
    )
    return blank, metrics


def dense_text_metrics(image_bytes: bytes) -> dict[str, float | bool]:
    """Measure text-like page density without relying on an OCR installation."""

    from PIL import Image

    with Image.open(io.BytesIO(image_bytes)) as opened:
        grayscale = opened.convert("L")
        grayscale.thumbnail((512, 512))
        width, height = grayscale.size
        pixels = list(grayscale.getdata())
    if width < 2 or height < 2:
        return {
            "ink_ratio": 0.0,
            "active_row_ratio": 0.0,
            "horizontal_transition_ratio": 0.0,
            "dense_text_candidate": False,
        }
    ink = [value < 235 for value in pixels]
    ink_ratio = sum(ink) / len(ink)
    active_rows = 0
    transitions = 0
    for row in range(height):
        values = ink[row * width:(row + 1) * width]
        if sum(values) / width >= 0.012:
            active_rows += 1
        transitions += sum(left != right for left, right in zip(values, values[1:]))
    active_row_ratio = active_rows / height
    transition_ratio = transitions / (height * (width - 1))
    dense = (
        ink_ratio >= 0.018
        and active_row_ratio >= 0.16
        and transition_ratio >= 0.025
    )
    return {
        "ink_ratio": round(ink_ratio, 6),
        "active_row_ratio": round(active_row_ratio, 6),
        "horizontal_transition_ratio": round(transition_ratio, 6),
        "dense_text_candidate": dense,
    }
