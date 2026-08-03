#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Common chunker that reads only normalized Markdown plus verified Document IR."""

from __future__ import annotations

from collections import Counter
from typing import Any

from models import Block, Chunk, DocumentIR
from utils import common_heading_path, estimate_tokens, sha256_text

ATOMIC_TYPES = {"table", "list", "code", "image"}


def _overlap_blocks(previous: list[Block], token_limit: int) -> list[Block]:
    selected: list[Block] = []
    total = 0
    for block in reversed(previous):
        if block.type in ATOMIC_TYPES or block.type == "heading":
            continue
        tokens = estimate_tokens(block.text)
        if selected and total + tokens > token_limit:
            break
        selected.append(block)
        total += tokens
        if total >= token_limit:
            break
    return list(reversed(selected))


def create_chunks(
    document: DocumentIR,
    normalized_markdown: str,
    block_markdown: dict[str, str],
    *,
    min_tokens: int,
    max_tokens: int,
    overlap_tokens: int,
    content_status: str,
) -> list[Chunk]:
    eligible = [
        block for block in document.blocks
        if block.status == "success" and block.type != "placeholder" and block.block_id in block_markdown
    ]
    if not eligible:
        return []
    groups: list[list[Block]] = []
    current: list[Block] = []
    current_tokens = 0
    for block in eligible:
        markdown = block_markdown[block.block_id]
        tokens = estimate_tokens(markdown)
        starts_major_heading = block.type == "heading" and int(block.metadata.get("level", 6)) <= 2
        # A reviewed visual summary is deliberately non-verbatim.  Keep it in an
        # independently retrievable chunk so a long surrounding table or page
        # cannot suppress the source-backed visual concept at query time.
        is_visual_retrieval_unit = (
            block.type == "image"
            and block.content_origin == "llm_visual_summary"
            and block.verbatim is False
        )
        if current and starts_major_heading and current_tokens >= min_tokens:
            groups.append(current)
            current = []
            current_tokens = 0
        if current and is_visual_retrieval_unit:
            groups.append(current)
            current = []
            current_tokens = 0
        if current and current_tokens + tokens > max_tokens and current_tokens >= min_tokens:
            groups.append(current)
            current = []
            current_tokens = 0
        current.append(block)
        current_tokens += tokens
        if is_visual_retrieval_unit:
            groups.append(current)
            current = []
            current_tokens = 0
    if current:
        groups.append(current)

    chunks: list[Chunk] = []
    normalized_hash = sha256_text(normalized_markdown)
    previous_group: list[Block] = []
    fallback_heading = [document.title]
    for index, group in enumerate(groups, start=1):
        overlap = _overlap_blocks(previous_group, overlap_tokens) if previous_group else []
        overlap_text = "\n\n".join(block_markdown[block.block_id] for block in overlap)
        body_parts = [block_markdown[block.block_id] for block in group]
        body = "\n\n".join(body_parts)
        if overlap_text:
            body = "> [前文重疊]\n>\n" + "\n".join(f"> {line}" for line in overlap_text.splitlines()) + "\n\n" + body
        heading_path = common_heading_path((block.heading_path for block in group), fallback_heading)
        section_titles = [block.text for block in group if block.type == "heading"]
        locators = [block.location.to_dict() for block in group if block.location.to_dict()]
        chunks.append(Chunk(
            chunk_id=f"{document.source_id}-chunk-{index:04d}",
            source_id=document.source_id,
            title=document.title,
            heading_path=heading_path,
            section_titles=section_titles,
            source_block_ids=[block.block_id for block in group],
            overlap_block_ids=[block.block_id for block in overlap],
            overlap_text=overlap_text,
            overlap_token_count=estimate_tokens(overlap_text),
            token_estimate=estimate_tokens(body),
            locators=locators,
            source_hash=document.provenance.sha256,
            normalized_document_hash=normalized_hash,
            content_status=content_status,
            text=body,
            markdown_body=body,
        ))
        previous_group = group
    return chunks


def _ordered_verified_blocks(document: DocumentIR) -> tuple[list[Block], int]:
    eligible = [
        block for block in document.blocks
        if block.status == "success" and block.type != "placeholder"
    ]
    source_orders = [block.metadata.get("source_order") for block in eligible]
    layout_required = document.metadata.get("layout_semantics_status") == "reliable"
    if not any(value is not None for value in source_orders) and not layout_required:
        return eligible, 0
    violations = sum(value is None or not isinstance(value, int) for value in source_orders)
    valid_orders = [value for value in source_orders if isinstance(value, int)]
    violations += len(valid_orders) - len(set(valid_orders))
    violations += sum(
        current >= following
        for current, following in zip(valid_orders, valid_orders[1:])
    )
    ordered = sorted(
        eligible,
        key=lambda block: (
            block.metadata.get("source_order") if isinstance(block.metadata.get("source_order"), int) else 10**12,
            document.blocks.index(block),
        ),
    )
    return ordered, violations


def _sequence_mismatch_count(expected: list[str], actual: list[str]) -> int:
    shared = min(len(expected), len(actual))
    return sum(expected[index] != actual[index] for index in range(shared)) + abs(len(expected) - len(actual))


def _visual_heading_relation_violations(document: DocumentIR) -> list[dict[str, Any]]:
    if document.metadata.get("layout_semantics_status") != "reliable":
        return []
    ordered = sorted(
        document.blocks,
        key=lambda block: (
            block.metadata.get("source_order") if isinstance(block.metadata.get("source_order"), int) else 10**12,
            document.blocks.index(block),
        ),
    )
    nearest_heading: Block | None = None
    violations: list[dict[str, Any]] = []
    for block in ordered:
        if block.status != "success":
            continue
        if block.type == "heading":
            nearest_heading = block
            continue
        if block.type != "image":
            continue
        associated = block.metadata.get("associated_heading_block_id")
        expected = nearest_heading.block_id if nearest_heading else None
        if not associated or associated != expected:
            violations.append({
                "block_id": block.block_id,
                "reason": "associated_heading_not_nearest_preceding_heading",
                "expected": expected,
                "actual": associated,
            })
            continue
        expected_path = nearest_heading.heading_path if nearest_heading else []
        if block.heading_path != expected_path:
            violations.append({
                "block_id": block.block_id,
                "reason": "visual_heading_path_mismatch",
                "expected": expected_path,
                "actual": block.heading_path,
            })
        associated_path = block.metadata.get("associated_heading_path")
        if associated_path != expected_path:
            violations.append({
                "block_id": block.block_id,
                "reason": "associated_heading_path_mismatch",
                "expected": expected_path,
                "actual": associated_path,
            })
        association_method = block.metadata.get("association_method")
        if not isinstance(association_method, str) or not association_method.strip():
            violations.append({
                "block_id": block.block_id,
                "reason": "association_method_missing",
            })
    return violations


def _document_title_violations(document: DocumentIR) -> list[dict[str, Any]]:
    if document.metadata.get("document_title_semantics_status") != "reliable":
        return []
    title_blocks = [
        block for block in document.blocks
        if block.status == "success"
        and block.type == "heading"
        and block.metadata.get("semantic_role") == "document_title"
    ]
    violations: list[dict[str, Any]] = []
    if len(title_blocks) != 1:
        violations.append({"reason": "document_title_block_count", "expected": 1, "actual": len(title_blocks)})
        return violations
    title_block = title_blocks[0]
    if title_block.text != document.title:
        violations.append({
            "block_id": title_block.block_id,
            "reason": "document_title_text_mismatch",
            "expected": document.title,
            "actual": title_block.text,
        })
    if int(title_block.metadata.get("level", 0)) != 1:
        violations.append({"block_id": title_block.block_id, "reason": "document_title_level_not_one"})
    if title_block.heading_path != [document.title]:
        violations.append({
            "block_id": title_block.block_id,
            "reason": "document_title_heading_path_mismatch",
            "expected": [document.title],
            "actual": title_block.heading_path,
        })
    return violations


def validate_chunk_mapping(document: DocumentIR, chunks: list[Chunk], normalized_markdown: str) -> dict[str, Any]:
    eligible, source_order_metadata_violations = _ordered_verified_blocks(document)
    expected_ids = [block.block_id for block in eligible]
    eligible_ids = set(expected_ids)
    mapped_ids = [block_id for chunk in chunks for block_id in chunk.source_block_ids]
    counts = Counter(mapped_ids)
    mapped_unique = set(mapped_ids)
    omitted = sorted(eligible_ids - mapped_unique)
    unexpected = sorted(mapped_unique - eligible_ids)
    duplicates = sorted(block_id for block_id, count in counts.items() if count != 1)
    failed_ids = {
        block.block_id for block in document.blocks if block.status in {"failed", "low_quality"}
    }
    failed_mapped = sorted(failed_ids & mapped_unique)
    atomic_violations = len(duplicates) + len(failed_mapped)
    block_by_id = {block.block_id: block for block in document.blocks}
    heading_context_violations = 0
    for chunk in chunks:
        mapped_blocks = [block_by_id[block_id] for block_id in chunk.source_block_ids if block_id in block_by_id]
        expected_heading = common_heading_path(
            (block.heading_path for block in mapped_blocks),
            [document.title] if document.title else [],
        )
        if chunk.heading_path != expected_heading:
            heading_context_violations += 1
    ratio = round(len(mapped_unique & eligible_ids) / len(eligible_ids), 6) if eligible_ids else None
    unexpected_content_count = len(unexpected)
    normalized_hash = sha256_text(normalized_markdown)
    unexpected_content_count += sum(chunk.normalized_document_hash != normalized_hash for chunk in chunks)
    reading_order_violation_count = _sequence_mismatch_count(expected_ids, mapped_ids)
    visual_relation_violations = _visual_heading_relation_violations(document)
    title_violations = _document_title_violations(document)
    status = "passed"
    if (
        ratio != 1.0
        or omitted
        or unexpected_content_count
        or atomic_violations
        or heading_context_violations
        or reading_order_violation_count
        or source_order_metadata_violations
        or visual_relation_violations
        or title_violations
    ):
        status = "failed"
    result = {
        "normalized_block_total": len(eligible_ids),
        "chunk_mapped_block_total": len(mapped_unique & eligible_ids),
        "chunk_block_mapping_ratio": ratio,
        "omitted_verified_blocks": omitted,
        "unexpected_chunk_content_count": unexpected_content_count,
        "unexpected_block_ids": unexpected,
        "duplicate_source_block_ids": duplicates,
        "failed_blocks_in_chunks": failed_mapped,
        "atomic_unit_violation_count": atomic_violations,
        "orphan_heading_context_count": heading_context_violations,
        "reading_order_violation_count": reading_order_violation_count,
        "source_order_metadata_violation_count": source_order_metadata_violations,
        "visual_heading_relation_violation_count": len(visual_relation_violations),
        "document_title_mismatch_count": len(title_violations),
        "chunk_validation_status": status,
    }
    if reading_order_violation_count:
        result["expected_source_block_order"] = expected_ids
        result["actual_source_block_order"] = mapped_ids
    if visual_relation_violations:
        result["visual_heading_relation_violations"] = visual_relation_violations
    if title_violations:
        result["document_title_violations"] = title_violations
    return result
