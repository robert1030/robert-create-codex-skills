#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Adapter context and deterministic block-id allocation."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from models import Block, DocumentIR, Location, Provenance


@dataclass(slots=True)
class AdapterContext:
    provenance: Provenance
    work_dir: Path
    ocr_languages: str
    forensic: bool = False
    collection_runtime: Any | None = None
    collection_member_path: str | None = None
    visual_semantics: Any | None = None
    _counter: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    def next_block_id(self) -> str:
        self._counter += 1
        return f"{self.provenance.source_id}-block-{self._counter:04d}"

    def block(
        self,
        block_type: str,
        text: str,
        *,
        location: Location | None = None,
        heading_path: list[str] | None = None,
        content_origin: str = "native_text",
        required: bool = True,
        critical: bool = False,
        status: str = "success",
        verbatim: bool = True,
        raw_text: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> Block:
        return Block(
            block_id=self.next_block_id(),
            type=block_type,
            text=text,
            location=location or Location(),
            heading_path=list(heading_path or []),
            content_origin=content_origin,
            required=required,
            critical=critical,
            status=status,
            verbatim=verbatim,
            raw_text=raw_text,
            metadata=dict(metadata or {}),
        )


def empty_document(context: AdapterContext, title: str) -> DocumentIR:
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=[],
        metadata=dict(context.metadata),
    )
