#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared Document IR, provenance, failure, and chunk models."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from constants import BLOCK_STATUSES, BLOCK_TYPES, CONTENT_ORIGINS


@dataclass(slots=True)
class Location:
    page: int | None = None
    bbox: list[float] | None = None
    dom_path: str | None = None
    xml_path: str | None = None
    element_index: int | None = None
    row_start: int | None = None
    row_end: int | None = None
    time_start: float | None = None
    time_end: float | None = None
    asset_id: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value is not None}


@dataclass(slots=True)
class AttemptRecord:
    attempt: int
    backend: str
    strategy: str
    status: str
    parameters: dict[str, Any] = field(default_factory=dict)
    quality: dict[str, Any] = field(default_factory=dict)
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value not in (None, {}, [])}


@dataclass(slots=True)
class Block:
    block_id: str
    type: str
    text: str
    location: Location = field(default_factory=Location)
    heading_path: list[str] = field(default_factory=list)
    content_origin: str = "native_text"
    required: bool = True
    critical: bool = False
    status: str = "success"
    verbatim: bool = True
    raw_text: str | None = None
    transformation_summary: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    attempts: list[AttemptRecord] = field(default_factory=list)

    def validate(self) -> None:
        if self.type not in BLOCK_TYPES:
            raise ValueError(f"unsupported_block_type:{self.type}")
        if self.content_origin not in CONTENT_ORIGINS:
            raise ValueError(f"unsupported_content_origin:{self.content_origin}")
        if self.status not in BLOCK_STATUSES:
            raise ValueError(f"unsupported_block_status:{self.status}")
        if self.content_origin in {"llm_visual_summary", "llm_visual_text"} and self.verbatim:
            raise ValueError(f"{self.content_origin}_must_not_be_verbatim")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        data = asdict(self)
        data["location"] = self.location.to_dict()
        data["attempts"] = [attempt.to_dict() for attempt in self.attempts]
        return {key: value for key, value in data.items() if value not in (None, [], {})}


@dataclass(slots=True)
class Provenance:
    source_id: str
    user_specified_name: str
    original_upload_name: str
    runtime_path: str
    extension: str
    requested_media_type: str
    runtime_media_type: str
    magic_bytes: str
    sha256: str
    actual_adapter: str
    original_binary_processed: bool
    derived_snapshot: bool
    input_fidelity: str
    derivation_chain: list[dict[str, Any]] = field(default_factory=list)
    source_dimensions: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class FailureItem:
    source_id: str
    source_file: str
    block_id: str | None
    failure_stage: str
    failure_reason: str
    attempts: int
    required: bool
    critical: bool
    location: dict[str, Any] = field(default_factory=dict)
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {key: value for key, value in asdict(self).items() if value not in (None, {}, [])}


@dataclass(slots=True)
class DocumentIR:
    source_id: str
    title: str
    provenance: Provenance
    blocks: list[Block]
    metadata: dict[str, Any] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def successful_blocks(self) -> list[Block]:
        return [block for block in self.blocks if block.status == "success"]

    def verified_chunk_blocks(self, allow_partial: bool = False) -> list[Block]:
        blocks = [block for block in self.blocks if block.status == "success" and block.type != "placeholder"]
        if allow_partial:
            return blocks
        return blocks


@dataclass(slots=True)
class Chunk:
    chunk_id: str
    source_id: str
    title: str
    heading_path: list[str]
    section_titles: list[str]
    source_block_ids: list[str]
    overlap_block_ids: list[str]
    overlap_text: str
    overlap_token_count: int
    token_estimate: int
    locators: list[dict[str, Any]]
    source_hash: str
    normalized_document_hash: str
    content_status: str
    text: str
    markdown_body: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class SourceItem:
    path: Path
    display_name: str
    original_upload_name: str
    requested_media_type: str | None = None
    derivation_chain: list[dict[str, Any]] = field(default_factory=list)
    collection_id: str | None = None
    collection_member_path: str | None = None
    collection_virtual_base_path: str | None = None
    canonical_member_path: str | None = None
