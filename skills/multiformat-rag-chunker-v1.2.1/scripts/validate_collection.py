#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent collection validation and collection hard-gate enforcement."""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
import json
import tempfile
from pathlib import Path
from typing import Any, Mapping

from constants import EXIT_FATAL, EXIT_PARTIAL_SUCCESS, EXIT_SUCCESS
from intake import collect_collection_sources
from source_semantics import audit_source_semantics, observed_semantic_units


@dataclass(frozen=True)
class CollectionGateResult:
    """Report hard-gate failures without silently normalising missing evidence."""

    passed: bool
    violations: tuple[str, ...]


REQUIRED_COLLECTION_METRICS = frozenset({
    "member_accounting_ratio",
    "critical_occurrence_coverage_ratio",
    "source_semantic_coverage_ratio",
    "source_semantic_critical_coverage_ratio",
    "semantic_order_inversion_count",
    "relationship_occurrence_accounting_ratio",
    "existing_target_resolution_ratio",
    "unreported_relationship_failure_count",
})


def validate_collection_metrics(metrics: Mapping[str, float | int | None]) -> CollectionGateResult:
    """Apply the collection contract without accepting missing metric defaults."""

    missing = sorted(key for key in REQUIRED_COLLECTION_METRICS if key not in metrics or metrics[key] is None)
    violations = [f"missing_metric:{key}" for key in missing]
    if missing:
        return CollectionGateResult(False, tuple(violations))

    required_one = (
        "member_accounting_ratio",
        "critical_occurrence_coverage_ratio",
        "source_semantic_coverage_ratio",
        "source_semantic_critical_coverage_ratio",
        "relationship_occurrence_accounting_ratio",
        "existing_target_resolution_ratio",
    )
    for key in required_one:
        if float(metrics[key]) != 1.0:
            violations.append(f"ratio_not_one:{key}")
    for key in ("semantic_order_inversion_count", "unreported_relationship_failure_count"):
        if int(metrics[key]) != 0:
            violations.append(f"nonzero_metric:{key}")
    return CollectionGateResult(not violations, tuple(violations))


def _relationship_key(record: Mapping[str, object]) -> tuple[str, str, str, str | None, str, str, str]:
    return (
        str(record.get("source_member") or ""),
        str(record.get("raw_reference") or ""),
        str(record.get("relationship_type") or ""),
        str(record.get("target_member")) if record.get("target_member") is not None else None,
        str(record.get("fragment") or ""),
        str(record.get("status") or ""),
        str(record.get("strategy") or ""),
    )


def _raw_xml_relationships(path: Path, member_path: str, runtime) -> list[dict[str, object]]:
    from xml.etree import ElementTree

    attributes = {"href", "src", "data", "target", "link", "url", "uri", "topic", "context", "file"}
    records: list[dict[str, object]] = []
    root = ElementTree.parse(path).getroot()
    for element in root.iter():
        tag = str(element.tag).split("}")[-1].lower()
        for attribute, raw_value in element.attrib.items():
            name = str(attribute).split("}")[-1].lower()
            value = str(raw_value).strip()
            if name not in attributes or not value:
                continue
            if name in {"target", "context"} and not any(token in value for token in ("/", ".", ":", "#")):
                records.append({
                    "source_member": member_path,
                    "raw_reference": value,
                    "relationship_type": f"xml_{tag}_{name}",
                    "target_member": None,
                    "fragment": "",
                    "status": "non_file_identifier",
                    "strategy": "attribute_identifier",
                })
                continue
            semantic_hint = str(element.attrib.get("title") or element.attrib.get("label") or "").strip()
            resolution = runtime.resolve_relationship(member_path, value, semantic_hint=semantic_hint)
            records.append({
                "source_member": resolution.source_member,
                "raw_reference": resolution.raw_reference,
                "relationship_type": f"xml_{tag}_{name}",
                "target_member": resolution.target_member,
                "fragment": resolution.fragment,
                "status": resolution.status,
                "strategy": resolution.strategy,
                "evidence": resolution.evidence,
            })
        if tag == "param" and str(element.attrib.get("name") or "").strip().lower() == "path":
            value = str(element.attrib.get("value") or "").strip()
            if value:
                resolution = runtime.resolve_relationship(member_path, value)
                records.append({
                    "source_member": resolution.source_member,
                    "raw_reference": resolution.raw_reference,
                    "relationship_type": "xml_param_value",
                    "target_member": resolution.target_member,
                    "fragment": resolution.fragment,
                    "status": resolution.status,
                    "strategy": resolution.strategy,
                    "evidence": resolution.evidence,
                })
    return records


def _raw_html_relationships(path: Path, member_path: str, runtime) -> list[dict[str, object]]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(path.read_bytes(), "html.parser")
    records: list[dict[str, object]] = []
    for tag in soup.find_all(True):
        for attribute in ("href", "src", "data"):
            value = tag.get(attribute)
            if not isinstance(value, str) or not value.strip():
                continue
            semantic_hint = str(tag.get("title") or "").strip()
            resolution = runtime.resolve_relationship(member_path, value, semantic_hint=semantic_hint)
            records.append({
                "source_member": resolution.source_member,
                "raw_reference": resolution.raw_reference,
                "relationship_type": f"html_{tag.name}_{attribute}",
                "target_member": resolution.target_member,
                "fragment": resolution.fragment,
                "status": resolution.status,
                "strategy": resolution.strategy,
                "evidence": resolution.evidence,
            })
    return records


def _independent_source_relationships(runtime) -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    """Reparse raw source with separate parser choices from the adapters."""

    relationships: list[dict[str, object]] = []
    parse_errors: list[dict[str, object]] = []
    for member in runtime.inventory.members:
        category = runtime.member_categories.get(member.relative_path)
        if category not in {"content", "control"}:
            continue
        path = runtime.path_for(member.relative_path)
        if path is None:
            parse_errors.append({"member": member.relative_path, "reason": "catalog_member_path_missing"})
            continue
        extension = path.suffix.lower()
        try:
            if extension in {".html", ".htm"}:
                relationships.extend(_raw_html_relationships(path, member.relative_path, runtime))
            elif extension == ".xml":
                relationships.extend(_raw_xml_relationships(path, member.relative_path, runtime))
        except Exception as exc:
            parse_errors.append({"member": member.relative_path, "reason": f"raw_relationship_parse_failed:{type(exc).__name__}"})
    return relationships, parse_errors


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _output_collection_records(report: Mapping[str, Any], output_root: Path) -> tuple[list[dict[str, object]], list[dict[str, Any]], list[dict[str, Any]]]:
    relationships = [record for record in report.get("control_relationships", []) if isinstance(record, dict)]
    source_reports: list[dict[str, Any]] = []
    ir_records: list[dict[str, Any]] = []
    for member in report.get("members", []):
        if member.get("category") != "content":
            continue
        source_id = member.get("source_id")
        if not isinstance(source_id, str) or not source_id:
            continue
        source_dir = output_root / source_id
        source_report = json.loads((source_dir / "processing-report.json").read_text(encoding="utf-8"))
        source_reports.append(source_report)
        relationships.extend(
            record for record in source_report.get("source_metadata", {}).get("relationships", [])
            if isinstance(record, dict)
        )
        ir_records.extend(_read_jsonl(source_dir / "document-ir.jsonl"))
    return relationships, source_reports, ir_records


def _semantic_summary(audits: list[dict[str, Any]]) -> dict[str, int]:
    return {
        "expected_total": sum(int(audit.get("expected_total") or 0) for audit in audits),
        "verified_total": sum(int(audit.get("verified_total") or 0) for audit in audits),
        "critical_expected_total": sum(int(audit.get("critical_expected_total") or 0) for audit in audits),
        "critical_verified_total": sum(int(audit.get("critical_verified_total") or 0) for audit in audits),
    }


def _independent_source_semantic_audits(runtime, report: Mapping[str, Any], output_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, object]]]:
    """Reparse source semantics independently from the adapter and persisted audit."""

    audits: list[dict[str, Any]] = []
    errors: list[dict[str, object]] = []
    for member in report.get("members", []):
        if not isinstance(member, Mapping) or member.get("category") != "content":
            continue
        source_id = member.get("source_id")
        member_path = str(member.get("relative_path") or "")
        raw_path = runtime.path_for(member_path)
        if not isinstance(source_id, str) or raw_path is None:
            errors.append({"reason": "source_semantic_audit_input_missing", "member": member_path})
            continue
        source_dir = output_root / source_id
        try:
            normalized = (source_dir / "normalized-document.md").read_text(encoding="utf-8")
            records = _read_jsonl(source_dir / "document-ir.jsonl")
            audit = audit_source_semantics(raw_path, observed_semantic_units(records, normalized))
            audits.append({"member": member_path, **audit})
        except Exception as exc:
            errors.append({"reason": f"source_semantic_audit_failed:{type(exc).__name__}", "member": member_path})
    return audits, errors


def _recompute_metrics(report: Mapping[str, Any], relationships: list[dict[str, object]], source_reports: list[dict[str, Any]], ir_records: list[dict[str, Any]], expected_relationships: list[dict[str, object]], semantic_audits: list[dict[str, Any]]) -> tuple[dict[str, float | int], list[dict[str, object]]]:
    members = [member for member in report.get("members", []) if isinstance(member, dict)]
    member_ratio = sum(bool(member.get("accounted")) for member in members) / len(members) if members else 0.0
    required_total = sum(int(source.get("chunk_pre_validation", {}).get("required_unit_total") or 0) for source in source_reports)
    required_verified = sum(int(source.get("chunk_pre_validation", {}).get("required_unit_verified") or 0) for source in source_reports)
    semantic = _semantic_summary(semantic_audits)
    orders_by_source: dict[str, list[int]] = {}
    order_violations = 0
    for record in ir_records:
        metadata = record.get("metadata", {})
        occurrence = metadata.get("collection_occurrence")
        member_path = occurrence.get("source_member") if isinstance(occurrence, dict) else None
        value = metadata.get("source_order")
        if not isinstance(member_path, str) or not isinstance(value, int):
            order_violations += 1
            continue
        orders_by_source.setdefault(member_path, []).append(value)
    for values in orders_by_source.values():
        order_violations += sum(current >= following for current, following in zip(values, values[1:]))
        order_violations += len(values) - len(set(values))
    expected_counter = Counter(_relationship_key(record) for record in expected_relationships)
    actual_counter = Counter(_relationship_key(record) for record in relationships)
    missing_relationships: list[dict[str, object]] = []
    for key, count in (expected_counter - actual_counter).items():
        missing_relationships.append({"relationship": key, "count": count})
    locally_expected = [record for record in expected_relationships if record.get("status") == "resolved"]
    resolved_existing = len(locally_expected)
    unreported = len(missing_relationships) + sum(
        record.get("status") not in {"resolved", "source_missing_target", "external", "non_file_identifier"}
        for record in relationships
    )
    metrics: dict[str, float | int] = {
        "member_accounting_ratio": round(member_ratio, 6),
        "critical_occurrence_coverage_ratio": round(required_verified / required_total, 6) if required_total else 1.0,
        "source_semantic_coverage_ratio": round(semantic["verified_total"] / semantic["expected_total"], 6) if semantic["expected_total"] else 1.0,
        "source_semantic_critical_coverage_ratio": round(semantic["critical_verified_total"] / semantic["critical_expected_total"], 6) if semantic["critical_expected_total"] else 1.0,
        "semantic_order_inversion_count": order_violations,
        "relationship_occurrence_accounting_ratio": round(len(relationships) / len(expected_relationships), 6) if expected_relationships else 1.0,
        "existing_target_resolution_ratio": round(resolved_existing / len(locally_expected), 6) if locally_expected else 1.0,
        "unreported_relationship_failure_count": unreported,
    }
    return metrics, missing_relationships


def validate_collection_output(input_path: Path, output_root: Path) -> tuple[int, dict[str, Any]]:
    """Independently validate collection membership, relation occurrences and gates."""

    errors: list[dict[str, object]] = []
    warnings: list[dict[str, object]] = []
    with tempfile.TemporaryDirectory(prefix="multiformat-rag-collection-validate-") as temp_name:
        sources, _aliases, runtimes = collect_collection_sources(input_path, Path(temp_name) / "intake")
        del sources
        if not runtimes:
            return EXIT_FATAL, {"status": "fatal_error", "errors": [{"reason": "input_is_not_collection"}], "warnings": warnings}
        summaries: list[dict[str, Any]] = []
        severity = 0
        for runtime in runtimes:
            report_path = output_root / f"collection-report-{runtime.collection_id}.json"
            if not report_path.is_file():
                errors.append({"reason": "collection_report_missing", "collection_id": runtime.collection_id})
                severity = max(severity, 2)
                continue
            report = json.loads(report_path.read_text(encoding="utf-8"))
            expected_members = {member.relative_path: member for member in runtime.inventory.members}
            actual_members = {
                str(member.get("relative_path")): member
                for member in report.get("members", [])
                if isinstance(member, dict)
            }
            if set(actual_members) != set(expected_members):
                errors.append({"reason": "member_catalog_mismatch", "collection_id": runtime.collection_id})
            for path, expected in expected_members.items():
                actual = actual_members.get(path, {})
                if actual.get("sha256") != expected.sha256 or actual.get("canonical_member") != expected.canonical_member:
                    errors.append({"reason": "member_identity_mismatch", "collection_id": runtime.collection_id, "member": path})
            raw_relationships, parse_errors = _independent_source_relationships(runtime)
            errors.extend({"collection_id": runtime.collection_id, **error} for error in parse_errors)
            try:
                output_relationships, source_reports, ir_records = _output_collection_records(report, output_root)
            except Exception as exc:
                errors.append({"reason": f"collection_output_read_failed:{type(exc).__name__}", "collection_id": runtime.collection_id})
                severity = max(severity, 2)
                continue
            semantic_audits, semantic_errors = _independent_source_semantic_audits(runtime, report, output_root)
            errors.extend({"collection_id": runtime.collection_id, **error} for error in semantic_errors)
            metrics, missing_relationships = _recompute_metrics(
                report,
                output_relationships,
                source_reports,
                ir_records,
                raw_relationships,
                semantic_audits,
            )
            if missing_relationships:
                errors.append({"reason": "relationship_occurrence_missing", "collection_id": runtime.collection_id, "details": missing_relationships})
            missing_semantic_units = [
                {"member": audit["member"], "missing": audit["missing"]}
                for audit in semantic_audits
                if audit.get("missing")
            ]
            if missing_semantic_units:
                errors.append({"reason": "source_semantic_content_missing", "collection_id": runtime.collection_id, "details": missing_semantic_units})
            reported_metrics = report.get("metrics", {})
            for name, value in metrics.items():
                if reported_metrics.get(name) != value:
                    errors.append({"reason": "collection_metric_mismatch", "collection_id": runtime.collection_id, "metric": name, "reported": reported_metrics.get(name), "measured": value})
            gate = validate_collection_metrics(metrics)
            if report.get("gate", {}).get("passed") != gate.passed:
                errors.append({"reason": "collection_gate_mismatch", "collection_id": runtime.collection_id})
            if report.get("source_semantic_audit") != _semantic_summary(semantic_audits):
                errors.append({"reason": "source_semantic_audit_mismatch", "collection_id": runtime.collection_id})
            collection_severity = 2 if not gate.passed else (1 if any(record.get("status") == "source_missing_target" for record in raw_relationships) else 0)
            severity = max(severity, collection_severity)
            summaries.append({
                "collection_id": runtime.collection_id,
                "profile": runtime.inventory.profile.name,
                "metrics": metrics,
                "gate": {"passed": gate.passed, "violations": list(gate.violations)},
            })
    if errors:
        return EXIT_FATAL, {"status": "fatal_error", "errors": errors, "warnings": warnings, "collections": summaries}
    if severity == 1:
        return EXIT_PARTIAL_SUCCESS, {"status": "partial_success", "errors": [], "warnings": warnings, "collections": summaries}
    return EXIT_SUCCESS, {"status": "success", "errors": [], "warnings": warnings, "collections": summaries}


def main() -> int:
    parser = argparse.ArgumentParser(description="Independently validate a multiformat RAG collection output.")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    code, result = validate_collection_output(args.input.resolve(), args.output.resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"status={result['status']} errors={len(result.get('errors', []))}")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
