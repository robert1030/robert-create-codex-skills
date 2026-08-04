#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Public constants for multiformat-rag-chunker v1.2.1."""

from __future__ import annotations

SKILL_VERSION = "1.2.1"
SUPPORTED_EXTENSIONS = frozenset({
    ".pdf", ".docx", ".doc", ".html", ".htm", ".xml", ".csv",
    ".md", ".markdown", ".mp4", ".jpg", ".jpeg", ".png", ".heif",
    ".heic", ".zip",
})
DIRECT_SOURCE_EXTENSIONS = SUPPORTED_EXTENSIONS - {".zip"}
IMAGE_EXTENSIONS = frozenset({".jpg", ".jpeg", ".png", ".heif", ".heic"})

TARGET_MIN_TOKENS = 1000
TARGET_MAX_TOKENS = 1400
OVERLAP_MIN_TOKENS = 80
OVERLAP_MAX_TOKENS = 120
DEFAULT_OVERLAP_TOKENS = 100
MAX_RETRIES = 3
FORENSIC_MAX_RETRIES = 5
OCR_LANGUAGES = "chi_tra+chi_sim+eng"
REQUIRED_COVERAGE_THRESHOLD = 0.95

EXIT_SUCCESS = 0
EXIT_FATAL = 1
EXIT_PARTIAL_SUCCESS = 2

NORMALIZED_MD = "normalized-document.md"
DOCUMENT_IR_JSONL = "document-ir.jsonl"
CHUNKS_DIR = "chunks"
CHUNKS_JSONL = "chunks.jsonl"
FAILED_JSONL = "failed-items.jsonl"
REPORT_JSON = "processing-report.json"
MANIFEST_JSON = "manifest.json"

BLOCK_TYPES = frozenset({
    "heading", "paragraph", "list", "table", "image", "code",
    "transcript", "placeholder",
})
CONTENT_ORIGINS = frozenset({
    "native_text", "native_table", "ocr", "qr_decoder", "transcript",
    "llm_visual_summary", "derived_normalization", "placeholder",
})
BLOCK_STATUSES = frozenset({"success", "skipped", "low_quality", "failed"})
VISUAL_CLASSES = frozenset({
    "decorative", "logo", "icon", "qr_code", "barcode", "photo",
    "text_block", "table_image", "infographic", "screen_capture",
    "full_page_scan", "unknown",
})

FROZEN_CONTRACT_KEYS = (
    "SUPPORTED_EXTENSIONS",
    "TARGET_MIN_TOKENS",
    "TARGET_MAX_TOKENS",
    "DEFAULT_OVERLAP_TOKENS",
    "MAX_RETRIES",
    "OCR_LANGUAGES",
    "EXIT_SUCCESS",
    "EXIT_FATAL",
    "EXIT_PARTIAL_SUCCESS",
)
