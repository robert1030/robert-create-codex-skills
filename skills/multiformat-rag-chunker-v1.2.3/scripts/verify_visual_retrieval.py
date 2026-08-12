#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run deterministic retrieval smoke checks for reviewed visual summaries."""

from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA = "multiformat-rag-chunker.visual-retrieval-smoke.v1"
_TOKEN = re.compile(r"[a-z0-9]+")
_STOP_WORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "by", "do", "for", "from", "how",
    "i", "in", "including", "is", "it", "its", "of", "on", "or", "run", "shown", "that",
    "the", "to", "use", "where", "which", "with", "without",
})


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _tokens(value: str) -> Counter[str]:
    return Counter(token for token in _TOKEN.findall(value.lower()) if token not in _STOP_WORDS)


def _bm25_score(
    query_tokens: Counter[str],
    document_tokens: Counter[str],
    document_frequency: Counter[str],
    document_count: int,
    average_length: float,
) -> float:
    """Return a deterministic lexical rank that discounts corpus-wide terms."""
    score = 0.0
    document_length = sum(document_tokens.values())
    for term in query_tokens:
        frequency = document_tokens.get(term, 0)
        if not frequency:
            continue
        inverse_frequency = math.log(
            (document_count - document_frequency[term] + 0.5) / (document_frequency[term] + 0.5) + 1.0
        )
        normalizer = frequency + 1.2 * (1.0 - 0.75 + 0.75 * document_length / average_length)
        score += inverse_frequency * (frequency * 2.2) / normalizer
    return score


def load_spec(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or payload.get("schema") != SCHEMA:
        raise ValueError("visual_retrieval_smoke_schema_invalid")
    queries = payload.get("queries")
    if not isinstance(queries, list) or not queries:
        raise ValueError("visual_retrieval_smoke_queries_required")
    seen: set[str] = set()
    for query in queries:
        if not isinstance(query, dict):
            raise ValueError("visual_retrieval_smoke_query_invalid")
        identifier = str(query.get("id") or "")
        text = str(query.get("query") or "")
        reference = str(query.get("expected_reference") or "")
        top_k = query.get("top_k", 5)
        if not identifier or identifier in seen or not _tokens(text) or not reference or not isinstance(top_k, int) or top_k < 1:
            raise ValueError("visual_retrieval_smoke_query_invalid")
        seen.add(identifier)
    return queries


def validate_retrieval(output_root: Path, queries: list[dict[str, Any]]) -> tuple[list[str], list[dict[str, Any]]]:
    reviewed_blocks: dict[str, str] = {}
    chunks: list[dict[str, Any]] = []
    for ir_path in output_root.rglob("document-ir.jsonl"):
        for block in _read_jsonl(ir_path):
            metadata = block.get("metadata", {})
            evidence = metadata.get("visual_summary_evidence", {})
            if (
                block.get("type") == "image"
                and block.get("content_origin") == "llm_visual_summary"
                and block.get("verbatim") is False
                and evidence.get("review_method") == "native_visual_nonverbatim"
            ):
                reviewed_blocks[str(block["block_id"])] = str(metadata.get("reference") or "")
        chunks_path = ir_path.with_name("chunks.jsonl")
        if chunks_path.is_file():
            chunks.extend(_read_jsonl(chunks_path))

    errors: list[str] = []
    results: list[dict[str, Any]] = []
    chunk_tokens = [_tokens(str(chunk.get("text") or "")) for chunk in chunks]
    document_frequency: Counter[str] = Counter()
    for tokens in chunk_tokens:
        document_frequency.update(tokens.keys())
    average_length = max(1.0, sum(sum(tokens.values()) for tokens in chunk_tokens) / max(1, len(chunk_tokens)))
    for query in queries:
        expected_reference = str(query["expected_reference"])
        expected_ids = {
            block_id for block_id, reference in reviewed_blocks.items()
            if reference == expected_reference
        }
        if not expected_ids:
            errors.append(f"reviewed_reference_missing:{query['id']}:{expected_reference}")
            continue
        query_tokens = _tokens(str(query["query"]))
        ranked = sorted(
            zip(chunks, chunk_tokens),
            key=lambda item: (
                -_bm25_score(query_tokens, item[1], document_frequency, len(chunks), average_length),
                str(item[0].get("chunk_id") or ""),
            ),
        )
        top = [chunk for chunk, _ in ranked[:int(query.get("top_k", 5))]]
        returned = any(expected_ids & set(chunk.get("source_block_ids") or []) for chunk in top)
        results.append({
            "id": query["id"],
            "expected_reference": expected_reference,
            "returned": returned,
            "top_chunk_ids": [str(chunk.get("chunk_id") or "") for chunk in top],
        })
        if not returned:
            errors.append(f"expected_visual_summary_not_retrieved:{query['id']}:{expected_reference}")
    return errors, results


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify retrieval of reviewed visual summaries.")
    parser.add_argument("output", type=Path)
    parser.add_argument("--spec", type=Path, required=True)
    args = parser.parse_args()
    try:
        queries = load_spec(args.spec)
        errors, results = validate_retrieval(args.output, queries)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"passed": False, "errors": [str(exc)]}, ensure_ascii=False, indent=2))
        return 1
    print(json.dumps({"passed": not errors, "errors": errors, "results": results}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
