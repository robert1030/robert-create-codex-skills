#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Archive processing is intentionally centralized in intake.py.

This module exists to make the adapter boundary explicit. It does not parse content
or chunk documents. Nested ZIP expansion, path traversal protection, and SHA-256
source deduplication are implemented by intake.collect_sources.
"""

from __future__ import annotations


def handled_by_intake() -> bool:
    return True
