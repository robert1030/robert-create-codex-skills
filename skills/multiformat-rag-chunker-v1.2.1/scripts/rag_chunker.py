#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CLI orchestrator: intake -> adapter -> Document IR -> normalized Markdown -> gates -> chunker -> output."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from adapters.base import AdapterContext
from adapters.registry import get_adapter
from chunker import create_chunks, validate_chunk_mapping
from collection import CollectionRuntime, attach_collection_context
from constants import (
    DEFAULT_OVERLAP_TOKENS,
    EXIT_FATAL,
    EXIT_PARTIAL_SUCCESS,
    EXIT_SUCCESS,
    MAX_RETRIES,
    OCR_LANGUAGES,
    SKILL_VERSION,
    TARGET_MAX_TOKENS,
    TARGET_MIN_TOKENS,
)
from coverage import evaluate_source_coverage
from intake import build_provenance, collect_collection_sources
from markdown_builder import build_normalized_markdown
from normalize import normalize_document_blocks
from output import write_json, write_source_output
from source_semantics import audit_source_semantics, observed_semantic_units
from validate import validate_source_output
from validate_collection import validate_collection_metrics
from visual_semantics import VisualSemantics, load_visual_semantics


def _prepare_output(path: Path, overwrite: bool) -> None:
    if path.exists() and any(path.iterdir()):
        if not overwrite:
            raise FileExistsError(f"output_not_empty:{path}")
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def _run_bootstrap(script_dir: Path) -> tuple[bool, str]:
    completed = subprocess.run(
        [sys.executable, str(script_dir / "bootstrap.py"), "--group", "all", "--log-file", str(script_dir / "bootstrap.log")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    return completed.returncode == 0, completed.stdout + completed.stderr


def _severity(status: str) -> int:
    if status == "fatal_error":
        return 2
    if status == "partial_success":
        return 1
    return 0


def _status_from_severity(value: int) -> tuple[str, int]:
    if value >= 2:
        return "fatal_error", EXIT_FATAL
    if value == 1:
        return "partial_success", EXIT_PARTIAL_SUCCESS
    return "success", EXIT_SUCCESS


def _empty_chunk_validation() -> dict[str, Any]:
    return {
        "normalized_block_total": 0,
        "chunk_mapped_block_total": 0,
        "chunk_block_mapping_ratio": None,
        "omitted_verified_blocks": [],
        "unexpected_chunk_content_count": 0,
        "atomic_unit_violation_count": 0,
        "orphan_heading_context_count": 0,
        "reading_order_violation_count": 0,
        "source_order_metadata_violation_count": 0,
        "visual_heading_relation_violation_count": 0,
        "document_title_mismatch_count": 0,
        "chunk_validation_status": "not_run",
    }


def process_source(
    item,
    output_root: Path,
    args: argparse.Namespace,
    temp_root: Path,
    collection_runtime: CollectionRuntime | None = None,
    visual_semantics: VisualSemantics | None = None,
) -> dict[str, Any]:
    adapter_name, adapter = get_adapter(item.path.suffix.lower())
    provenance = build_provenance(item, adapter_name)
    source_dir = output_root / provenance.source_id
    work_dir = temp_root / provenance.source_id
    work_dir.mkdir(parents=True, exist_ok=True)
    context = AdapterContext(
        provenance=provenance,
        work_dir=work_dir,
        ocr_languages=args.ocr_languages,
        forensic=args.forensic,
        collection_runtime=collection_runtime,
        collection_member_path=item.collection_member_path,
        visual_semantics=visual_semantics,
    )
    forensic_work_dir = None
    if args.forensic:
        forensic_work_dir = work_dir / "forensic"
        for name in ("source-assets", "rendered-pages", "crops", "preprocessed", "ocr-candidates", "overlays"):
            (forensic_work_dir / name).mkdir(parents=True, exist_ok=True)
        shutil.copy2(item.path, forensic_work_dir / "source-assets" / item.path.name)
    try:
        document = adapter(item.path, context)
    except Exception as exc:
        document = __import__("models").DocumentIR(
            source_id=provenance.source_id,
            title=item.path.stem,
            provenance=provenance,
            blocks=[context.block(
                "placeholder", "", content_origin="placeholder", required=True,
                critical=True, status="failed", verbatim=False,
                metadata={"reason": f"adapter_exception:{type(exc).__name__}:{exc}"},
            )],
            metadata={"adapter": adapter_name},
            errors=[f"adapter_exception:{type(exc).__name__}:{exc}"],
        )
    if collection_runtime is not None and item.collection_member_path:
        attach_collection_context(
            document,
            collection_runtime,
            item.collection_member_path,
            item.canonical_member_path,
        )
    document.blocks = normalize_document_blocks(document.blocks)
    normalized_markdown, block_markdown = build_normalized_markdown(document)
    source_semantic_audit = audit_source_semantics(
        item.path,
        observed_semantic_units(document.blocks, normalized_markdown),
    )
    document.metadata["source_semantic_audit"] = source_semantic_audit
    coverage = evaluate_source_coverage(
        document,
        normalized_markdown,
        require_original_binary=args.require_original_binary,
        source_semantic_audit=source_semantic_audit,
    )
    pre_status = coverage["content_completeness_status"]
    chunks = []
    chunk_validation = _empty_chunk_validation()
    final_status = pre_status
    if pre_status == "success" or (pre_status == "partial_success" and args.allow_partial_chunks):
        chunks = create_chunks(
            document,
            normalized_markdown,
            block_markdown,
            min_tokens=args.min_tokens,
            max_tokens=args.max_tokens,
            overlap_tokens=args.overlap_tokens,
            content_status=pre_status,
        )
        chunk_validation = validate_chunk_mapping(document, chunks, normalized_markdown)
        if chunk_validation["chunk_validation_status"] != "passed":
            final_status = "fatal_error"
            chunks = []
        elif pre_status == "partial_success":
            final_status = "partial_success"
    parameters = {
        "target_min_tokens": args.min_tokens,
        "target_max_tokens": args.max_tokens,
        "overlap_tokens": args.overlap_tokens,
        "ocr_languages": args.ocr_languages,
        "max_attempts": MAX_RETRIES,
        "allow_partial_chunks": args.allow_partial_chunks,
        "require_original_binary": args.require_original_binary,
        "forensic": args.forensic,
        "collection_id": item.collection_id,
        "collection_member_path": item.collection_member_path,
        "visual_semantics_review_count": visual_semantics.review_count if visual_semantics else 0,
    }
    write_source_output(
        source_dir,
        document,
        normalized_markdown,
        chunks,
        coverage,
        chunk_validation,
        final_status,
        parameters=parameters,
        forensic_dir=forensic_work_dir,
    )
    validation_code, validation = validate_source_output(source_dir)
    if validation_code == EXIT_FATAL and final_status != "fatal_error":
        final_status = "fatal_error"
        chunks = []
    write_source_output(
        source_dir,
        document,
        normalized_markdown,
        chunks,
        coverage,
        chunk_validation,
        final_status,
        parameters=parameters,
        validation_summary=validation,
        forensic_dir=forensic_work_dir,
    )
    validation_code, validation = validate_source_output(source_dir)
    return {
        "source_id": provenance.source_id,
        "source_file": item.display_name,
        "adapter": adapter_name,
        "status": final_status,
        "validation_code": validation_code,
        "validation": validation,
        "output_dir": str(source_dir),
        "chunk_count": len(chunks),
        "coverage": coverage,
        "collection_id": item.collection_id,
        "collection_member_path": item.collection_member_path,
    }


def _collection_source_records(runtime: CollectionRuntime, results: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Read persisted per-source metadata so the root report has no hidden state."""

    by_member = {
        str(result.get("collection_member_path")): result
        for result in results
        if result.get("collection_id") == runtime.collection_id and result.get("collection_member_path")
    }
    members: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = list(runtime.control_relationships)
    for member in runtime.inventory.members:
        category = runtime.member_categories.get(member.relative_path, "resource")
        record: dict[str, Any] = {
            "relative_path": member.relative_path,
            "sha256": member.sha256,
            "virtual_base_path": member.virtual_base_path,
            "canonical_member": member.canonical_member,
            "category": category,
        }
        result = by_member.get(member.relative_path)
        if category == "content":
            record["accounted"] = result is not None
            if result is not None:
                record["source_id"] = result.get("source_id")
                record["status"] = result.get("status")
                report_path = Path(str(result["output_dir"])) / "processing-report.json"
                report = json.loads(report_path.read_text(encoding="utf-8"))
                source_metadata = report.get("source_metadata", {})
                for relationship in source_metadata.get("relationships", []):
                    if isinstance(relationship, dict):
                        relationships.append(relationship)
        else:
            record["accounted"] = True
            record["status"] = "catalogued"
        members.append(record)
    return members, relationships


def _collection_metrics(runtime: CollectionRuntime, results: list[dict[str, Any]]) -> tuple[dict[str, float | int], list[dict[str, Any]], list[dict[str, Any]], dict[str, int]]:
    members, relationships = _collection_source_records(runtime, results)
    content_results = [
        result for result in results
        if result.get("collection_id") == runtime.collection_id and result.get("collection_member_path")
    ]
    member_ratio = (
        sum(bool(member.get("accounted")) for member in members) / len(members)
        if members else 0.0
    )
    required_total = 0
    required_verified = 0
    semantic_expected_total = 0
    semantic_verified_total = 0
    semantic_critical_expected_total = 0
    semantic_critical_verified_total = 0
    semantic_order_violations = 0
    for result in content_results:
        report_path = Path(str(result["output_dir"])) / "processing-report.json"
        report = json.loads(report_path.read_text(encoding="utf-8"))
        coverage = report.get("chunk_pre_validation", {})
        required_total += int(coverage.get("required_unit_total") or 0)
        required_verified += int(coverage.get("required_unit_verified") or 0)
        semantic_audit = report.get("source_metadata", {}).get("source_semantic_audit", {})
        semantic_expected_total += int(semantic_audit.get("expected_total") or 0)
        semantic_verified_total += int(semantic_audit.get("verified_total") or 0)
        semantic_critical_expected_total += int(semantic_audit.get("critical_expected_total") or 0)
        semantic_critical_verified_total += int(semantic_audit.get("critical_verified_total") or 0)
        ir_path = Path(str(result["output_dir"])) / "document-ir.jsonl"
        orders: list[int] = []
        for line in ir_path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            block = json.loads(line)
            occurrence = block.get("metadata", {}).get("collection_occurrence")
            if occurrence is None:
                semantic_order_violations += 1
                continue
            value = block.get("metadata", {}).get("source_order")
            if not isinstance(value, int):
                semantic_order_violations += 1
            else:
                orders.append(value)
        semantic_order_violations += sum(current >= following for current, following in zip(orders, orders[1:]))
        semantic_order_violations += len(orders) - len(set(orders))
    relationship_total = len(relationships)
    relationship_accounted = sum(
        isinstance(record.get("status"), str) and isinstance(record.get("strategy"), str)
        for record in relationships
    )
    locally_expected = [record for record in relationships if record.get("status") == "resolved"]
    resolved_existing = len(locally_expected)
    unreported = sum(
        record.get("status") not in {"resolved", "source_missing_target", "external", "non_file_identifier"}
        for record in relationships
    )
    metrics: dict[str, float | int] = {
        "member_accounting_ratio": round(member_ratio, 6),
        "critical_occurrence_coverage_ratio": round(required_verified / required_total, 6) if required_total else 1.0,
        "source_semantic_coverage_ratio": round(semantic_verified_total / semantic_expected_total, 6) if semantic_expected_total else 1.0,
        "source_semantic_critical_coverage_ratio": round(semantic_critical_verified_total / semantic_critical_expected_total, 6) if semantic_critical_expected_total else 1.0,
        "semantic_order_inversion_count": semantic_order_violations,
        "relationship_occurrence_accounting_ratio": round(relationship_accounted / relationship_total, 6) if relationship_total else 1.0,
        "existing_target_resolution_ratio": round(resolved_existing / len(locally_expected), 6) if locally_expected else 1.0,
        "unreported_relationship_failure_count": unreported,
    }
    semantic_summary = {
        "expected_total": semantic_expected_total,
        "verified_total": semantic_verified_total,
        "critical_expected_total": semantic_critical_expected_total,
        "critical_verified_total": semantic_critical_verified_total,
    }
    return metrics, members, relationships, semantic_summary


def _write_collection_reports(output_root: Path, runtimes: list[CollectionRuntime], results: list[dict[str, Any]]) -> list[dict[str, Any]]:
    summaries: list[dict[str, Any]] = []
    for runtime in runtimes:
        metrics, members, relationships, semantic_summary = _collection_metrics(runtime, results)
        gate = validate_collection_metrics(metrics)
        missing_target_count = sum(record.get("status") == "source_missing_target" for record in relationships)
        source_statuses = [
            str(result.get("status"))
            for result in results
            if result.get("collection_id") == runtime.collection_id
        ]
        severity = max((_severity(status) for status in source_statuses), default=0)
        if not gate.passed:
            severity = max(severity, 2)
        elif missing_target_count:
            severity = max(severity, 1)
        status, exit_code = _status_from_severity(severity)
        report = {
            "skill_version": SKILL_VERSION,
            "collection_id": runtime.collection_id,
            "display_name": runtime.display_name,
            "profile": {
                "name": runtime.inventory.profile.name,
                "reason": runtime.inventory.profile.reason,
                "requires_control_documents": runtime.inventory.profile.requires_control_documents,
            },
            "members": members,
            "toc_occurrences": list(runtime.toc_occurrences),
            "control_relationships": list(runtime.control_relationships),
            "relationship_summary": {
                "total": len(relationships),
                "resolved": sum(record.get("status") == "resolved" for record in relationships),
                "source_missing_target": missing_target_count,
                "external": sum(record.get("status") == "external" for record in relationships),
                "non_file_identifier": sum(record.get("status") == "non_file_identifier" for record in relationships),
            },
            "metrics": metrics,
            "source_semantic_audit": semantic_summary,
            "gate": {"passed": gate.passed, "violations": list(gate.violations)},
            "status": status,
            "exit_code": exit_code,
        }
        report_path = output_root / f"collection-report-{runtime.collection_id}.json"
        write_json(report_path, report)
        summaries.append({
            "collection_id": runtime.collection_id,
            "profile": runtime.inventory.profile.name,
            "status": status,
            "exit_code": exit_code,
            "report": str(report_path),
            "metrics": metrics,
        })
    return summaries


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert supported sources to validated normalized Markdown and RAG chunks.")
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--install-deps", action="store_true")
    parser.add_argument("--allow-partial-chunks", action="store_true")
    parser.add_argument("--require-original-binary", action="store_true")
    parser.add_argument("--requested-media-type")
    parser.add_argument("--forensic", action="store_true")
    parser.add_argument("--ocr-languages", default=OCR_LANGUAGES)
    parser.add_argument("--visual-semantics", type=Path)
    parser.add_argument("--min-tokens", type=int, default=TARGET_MIN_TOKENS)
    parser.add_argument("--max-tokens", type=int, default=TARGET_MAX_TOKENS)
    parser.add_argument("--overlap-tokens", type=int, default=DEFAULT_OVERLAP_TOKENS)
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.min_tokens <= 0 or args.max_tokens < args.min_tokens:
        parser.error("invalid_token_range")
    if not 0 <= args.overlap_tokens <= args.max_tokens:
        parser.error("invalid_overlap_tokens")
    try:
        visual_semantics = load_visual_semantics(args.visual_semantics, args.input)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_FATAL
    script_dir = Path(__file__).resolve().parent
    if args.install_deps:
        ok, log = _run_bootstrap(script_dir)
        print(log, file=sys.stderr)
        if not ok:
            print("dependency_bootstrap_failed", file=sys.stderr)
    output_root = args.output.resolve()
    try:
        _prepare_output(output_root, args.overwrite)
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return EXIT_FATAL
    with tempfile.TemporaryDirectory(prefix="multiformat-rag-") as temp_name:
        temp_root = Path(temp_name)
        try:
            sources, duplicates, runtimes = collect_collection_sources(args.input, temp_root / "intake", args.requested_media_type)
        except Exception as exc:
            print(f"intake_failed:{exc}", file=sys.stderr)
            return EXIT_FATAL
        if not sources:
            print("no_supported_sources", file=sys.stderr)
            return EXIT_FATAL
        runtime_by_id = {runtime.collection_id: runtime for runtime in runtimes}
        results = [
            process_source(
                item,
                output_root,
                args,
                temp_root / "work",
                runtime_by_id.get(item.collection_id),
                visual_semantics,
            )
            for item in sources
        ]
        collection_summaries = _write_collection_reports(output_root, runtimes, results)
    highest = max(
        [_severity(result["status"]) for result in results]
        + [_severity(summary["status"]) for summary in collection_summaries]
    )
    overall_status, exit_code = _status_from_severity(highest)
    summary = {
        "skill_version": SKILL_VERSION,
        "status": overall_status,
        "source_count": len(results),
        "duplicate_source_count": len(duplicates),
        "duplicates": duplicates,
        "sources": results,
        "collections": collection_summaries,
        "output": str(output_root),
    }
    if args.json_output:
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"status={overall_status} sources={len(results)} duplicates={len(duplicates)} output={output_root}")
        for result in results:
            print(f"{result['status']} {result['source_file']} -> {result['output_dir']} chunks={result['chunk_count']}")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
