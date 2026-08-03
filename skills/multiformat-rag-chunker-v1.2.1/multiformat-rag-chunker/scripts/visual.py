#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Visual classification and dedicated QR or barcode decoding."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class VisualInspection:
    visual_class: str
    qr_payloads: list[str] = field(default_factory=list)
    barcode_payloads: list[str] = field(default_factory=list)
    width: int | None = None
    height: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


def load_image(source: Path | bytes):
    from PIL import Image
    import io

    if isinstance(source, bytes):
        image = Image.open(io.BytesIO(source))
    else:
        image = Image.open(source)
    return image.convert("RGB")


def decode_qr(image) -> list[str]:
    import cv2
    import numpy as np

    array = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    detector = cv2.QRCodeDetector()
    payloads: list[str] = []
    try:
        ok, decoded, _points, _straight = detector.detectAndDecodeMulti(array)
        if ok:
            payloads.extend(value for value in decoded if value)
    except Exception:
        pass
    if not payloads:
        try:
            value, _points, _straight = detector.detectAndDecode(array)
            if value:
                payloads.append(value)
        except Exception:
            pass
    return list(dict.fromkeys(payloads))


def decode_barcode_details(image) -> list[dict[str, str]]:
    """Return decoder-confirmed barcode payloads and their actual symbology."""

    try:
        from pyzbar.pyzbar import decode  # type: ignore
    except Exception:
        decode = None
    payloads: list[dict[str, str]] = []
    if decode is not None:
        try:
            for item in decode(image):
                value = item.data.decode("utf-8", errors="replace").strip()
                if value:
                    payloads.append({
                        "payload": value,
                        "symbology": str(item.type or "UNKNOWN"),
                        "decoder": "pyzbar",
                    })
        except Exception:
            payloads = []
    if not payloads:
        try:
            import cv2
            import numpy as np

            array = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            detector = cv2.barcode_BarcodeDetector()
            detected, values, symbologies, _points = detector.detectAndDecodeWithType(array)
            if detected:
                for value, symbology in zip(values, symbologies):
                    payload = str(value).strip()
                    if payload:
                        payloads.append({
                            "payload": payload,
                            "symbology": str(symbology or "UNKNOWN"),
                            "decoder": "opencv_barcode_detector",
                        })
        except Exception:
            pass
    unique: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for payload in payloads:
        key = (payload["payload"], payload["symbology"], payload["decoder"])
        if key not in seen:
            seen.add(key)
            unique.append(payload)
    return unique


def decode_barcodes(image) -> list[str]:
    """Return barcode payloads for compatibility with existing callers."""

    return [item["payload"] for item in decode_barcode_details(image)]


def screen_capture_evidence(image) -> dict[str, Any]:
    """Return deterministic layout evidence without reading image text.

    A screen capture commonly contains sustained horizontal separators, menus, or
    table boundaries. Some wide command, tree, and result panes instead contain
    separated short text-like controls with no sustained horizontal divider. This
    remains a conservative routing signal: it only suppresses OCR for either the
    original divider pattern or a dense, low-ink interface pattern. It is not a
    claim that the image text has been read.
    """

    import cv2
    import numpy as np

    array = np.array(image)
    gray = cv2.cvtColor(array, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 60, 160)
    horizontal_kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (max(8, gray.shape[1] // 18), 1)
    )
    horizontal_edges = cv2.morphologyEx(edges, cv2.MORPH_OPEN, horizontal_kernel)
    edge_density = float(np.mean(edges > 0))
    horizontal_edge_density = float(np.mean(horizontal_edges > 0))
    dark_pixel_ratio = float(np.mean(gray < 200))
    width, height = image.size
    divider_pattern = edge_density >= 0.03 and horizontal_edge_density >= 0.02
    interface_geometry = (
        edge_density >= 0.05
        and 0.05 <= dark_pixel_ratio <= 0.20
        and (horizontal_edge_density >= 0.005 or width / max(height, 1) >= 4.0)
    )
    return {
        "classifier": "deterministic_layout_edges_v2",
        "edge_density": round(edge_density, 6),
        "horizontal_edge_density": round(horizontal_edge_density, 6),
        "dark_pixel_ratio": round(dark_pixel_ratio, 6),
        "screen_capture": divider_pattern or interface_geometry,
        "text_block": dark_pixel_ratio >= 0.01 and edge_density <= 0.025,
    }


def classify_visual(image, *, page_fraction: float | None = None, name_hint: str = "") -> VisualInspection:
    width, height = image.size
    qr_payloads = decode_qr(image)
    barcode_details = decode_barcode_details(image)
    barcode_payloads = [item["payload"] for item in barcode_details]
    layout_evidence = screen_capture_evidence(image)
    hint = name_hint.lower()
    if qr_payloads:
        visual_class = "qr_code"
    elif page_fraction is not None and page_fraction >= 0.75:
        visual_class = "full_page_scan"
    elif layout_evidence["screen_capture"]:
        visual_class = "screen_capture"
    elif barcode_payloads:
        visual_class = "barcode"
    elif "logo" in hint or (max(width, height) <= 420 and width / max(height, 1) > 1.4):
        visual_class = "logo"
    elif width <= 96 and height <= 96:
        visual_class = "icon"
    elif layout_evidence["text_block"]:
        visual_class = "text_block"
    elif width >= 320 and height >= 220:
        visual_class = "photo"
    else:
        visual_class = "unknown"
    return VisualInspection(
        visual_class=visual_class,
        qr_payloads=qr_payloads,
        barcode_payloads=barcode_payloads,
        width=width,
        height=height,
        metadata={"layout_evidence": layout_evidence, "barcode_details": barcode_details},
    )
