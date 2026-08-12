#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate exact dense-text anchors, lexical retrieval, and page citations."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA = "multiformat-rag-chunker.dense-retrieval-golden.v1"
_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_WORD = re.compile(r"[a-z0-9]+|[\u3400-\u9fff]", re.IGNORECASE)


def _read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"json_object_required:{path.name}")
    return value


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _tokens(value: str) -> Counter[str]:
    base = [token.lower() for token in _WORD.findall(value)]
    han = [token for token in base if "\u3400" <= token <= "\u9fff"]
    bigrams = [left + right for left, right in zip(han, han[1:])]
    return Counter(base + bigrams)


def _bm25(
    query: Counter[str],
    document: Counter[str],
    frequency: Counter[str],
    document_count: int,
    average_length: float,
) -> float:
    score = 0.0
    length = sum(document.values())
    for term in query:
        count = document.get(term, 0)
        if not count:
            continue
        inverse = math.log((document_count - frequency[term] + 0.5) / (frequency[term] + 0.5) + 1.0)
        score += inverse * (count * 2.2) / (count + 1.2 * (0.25 + 0.75 * length / average_length))
    return score


def load_spec(path: Path) -> dict[str, Any]:
    payload = _read_json(path)
    if payload.get("schema") != SCHEMA:
        raise ValueError("dense_retrieval_golden_schema_invalid")
    for field in ("input_sha256", "extraction_manifest_sha256"):
        if not _SHA256.fullmatch(str(payload.get(field) or "").lower()):
            raise ValueError(f"dense_retrieval_{field}_invalid")
    queries = payload.get("queries")
    if not isinstance(queries, list) or not queries:
        raise ValueError("dense_retrieval_queries_required")
    seen: set[str] = set()
    for query in queries:
        if not isinstance(query, dict):
            raise ValueError("dense_retrieval_query_invalid")
        identifier = str(query.get("id") or "")
        query_type = str(query.get("query_type") or "")
        top_k = query.get("top_k")
        if (
            not identifier or identifier in seen
            or query_type not in {"headword", "definition", "example", "content"}
            or not _tokens(str(query.get("query") or ""))
            or not str(query.get("expected_unit_id") or "")
            or not str(query.get("expected_reference") or "")
            or not isinstance(query.get("expected_page"), int)
            or not str(query.get("expected_anchor") or "")
            or not isinstance(top_k, int) or top_k < 1
        ):
            raise ValueError("dense_retrieval_query_invalid")
        required_k = 1 if query_type == "headword" else 3
        if top_k != required_k:
            raise ValueError("dense_retrieval_query_top_k_contract_invalid")
        seen.add(identifier)
    return payload


def _source_dirs(output: Path) -> list[Path]:
    if (output / "document-ir.jsonl").is_file():
        return [output]
    return sorted(path.parent for path in output.rglob("document-ir.jsonl"))


def validate_dense_retrieval(output: Path, spec: dict[str, Any]) -> dict[str, Any]:
    expected_source_sha = str(spec["input_sha256"]).lower()
    expected_extraction_sha = str(spec["extraction_manifest_sha256"]).lower()
    blocks: dict[str, dict[str, Any]] = {}
    units: dict[str, dict[str, Any]] = {}
    chunks: list[dict[str, Any]] = []
    errors: list[str] = []
    for source_dir in _source_dirs(output):
        manifest = _read_json(source_dir / "manifest.json")
        if str(manifest.get("provenance", {}).get("sha256") or "").lower() != expected_source_sha:
            continue
        for block in _read_jsonl(source_dir / "document-ir.jsonl"):
            if block.get("content_origin") != "llm_visual_text":
                continue
            metadata = block.get("metadata", {})
            evidence = metadata.get("visual_text_evidence", {})
            if str(evidence.get("review_manifest_sha256") or "").lower() != expected_extraction_sha:
                errors.append(f"extraction_manifest_sha256_mismatch:{block.get('block_id')}")
            unit_id = str(metadata.get("visual_text_unit_id") or "")
            if unit_id in units:
                errors.append(f"duplicate_visual_text_unit:{unit_id}")
            units[unit_id] = block
            blocks[str(block.get("block_id") or "")] = block
        chunks.extend(_read_jsonl(source_dir / "chunks.jsonl"))
    if not units:
        errors.append("no_dense_text_units_for_bound_source")

    tokenized = [_tokens(str(chunk.get("text") or "")) for chunk in chunks]
    frequency: Counter[str] = Counter()
    for tokens in tokenized:
        frequency.update(tokens.keys())
    average_length = max(1.0, sum(sum(tokens.values()) for tokens in tokenized) / max(1, len(tokenized)))
    results: list[dict[str, Any]] = []
    passed_by_type: Counter[str] = Counter()
    total_by_type: Counter[str] = Counter()
    anchor_passed = 0
    citation_passed = 0
    for query in spec["queries"]:
        query_id = str(query["id"])
        query_type = str(query["query_type"])
        unit_id = str(query["expected_unit_id"])
        expected_reference = str(query["expected_reference"])
        expected_page = int(query["expected_page"])
        expected_anchor = str(query["expected_anchor"])
        block = units.get(unit_id)
        anchor_ok = bool(block) and expected_anchor in str(block.get("text") or "")
        reference_ok = bool(block) and str(block.get("metadata", {}).get("reference") or "") == expected_reference
        page_ok = bool(block) and block.get("location", {}).get("page") == expected_page
        ranked = sorted(
            zip(chunks, tokenized),
            key=lambda item: (
                -_bm25(_tokens(str(query["query"])), item[1], frequency, max(1, len(chunks)), average_length),
                str(item[0].get("chunk_id") or ""),
            ),
        )
        top = [chunk for chunk, _tokens_value in ranked[:int(query["top_k"])]]
        expected_block_id = str(block.get("block_id") or "") if block else ""
        retrieved = any(expected_block_id in (chunk.get("source_block_ids") or []) for chunk in top)
        chunk_anchor_ok = any(
            expected_block_id in (chunk.get("source_block_ids") or [])
            and expected_anchor in str(chunk.get("text") or "")
            for chunk in chunks
        )
        citation_ok = reference_ok and page_ok and any(
            expected_block_id in (chunk.get("source_block_ids") or [])
            and any(locator.get("page") == expected_page for locator in chunk.get("locators", []))
            for chunk in top
        )
        passed = anchor_ok and chunk_anchor_ok and retrieved and citation_ok
        total_by_type[query_type] += 1
        passed_by_type[query_type] += int(passed)
        anchor_passed += int(anchor_ok and chunk_anchor_ok)
        citation_passed += int(citation_ok)
        if not passed:
            errors.append(f"dense_retrieval_query_failed:{query_id}")
        results.append({
            "id": query_id,
            "query_type": query_type,
            "expected_unit_id": unit_id,
            "anchor_preserved": anchor_ok and chunk_anchor_ok,
            "retrieved": retrieved,
            "citation_accurate": citation_ok,
            "top_chunk_ids": [str(chunk.get("chunk_id") or "") for chunk in top],
            "passed": passed,
        })

    query_total = len(spec["queries"])
    metrics = {
        "critical_anchor_preservation_ratio": round(anchor_passed / query_total, 6),
        "headword_recall_at_1": round(passed_by_type["headword"] / total_by_type["headword"], 6)
        if total_by_type["headword"] else None,
        "definition_recall_at_3": round(passed_by_type["definition"] / total_by_type["definition"], 6)
        if total_by_type["definition"] else None,
        "example_recall_at_3": round(passed_by_type["example"] / total_by_type["example"], 6)
        if total_by_type["example"] else None,
        "citation_page_accuracy": round(citation_passed / query_total, 6),
        "query_total": query_total,
        "query_passed": sum(passed_by_type.values()),
    }
    required = [
        metrics["critical_anchor_preservation_ratio"],
        metrics["headword_recall_at_1"],
        metrics["definition_recall_at_3"],
        metrics["example_recall_at_3"],
        metrics["citation_page_accuracy"],
    ]
    passed = not errors and all(value in {None, 1.0} for value in required)
    return {"passed": passed, "errors": errors, "metrics": metrics, "results": results}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate dense visual text retrieval and citation gates.")
    parser.add_argument("output", type=Path)
    parser.add_argument("--golden", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = validate_dense_retrieval(args.output, load_spec(args.golden))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        result = {"passed": False, "errors": [str(exc)], "metrics": {}, "results": []}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
