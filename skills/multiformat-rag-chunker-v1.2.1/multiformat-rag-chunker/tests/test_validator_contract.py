from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Callable

from helpers import FIXTURES, ROOT, load_json, load_jsonl, only_source_dir, run_cli


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )


def refresh_manifest_hash(source_dir: Path, relative_path: str) -> None:
    manifest_path = source_dir / "manifest.json"
    manifest = load_json(manifest_path)
    manifest["output_file_hashes"][relative_path] = sha256_file(source_dir / relative_path)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def validate(source_dir: Path) -> tuple[int, dict]:
    completed = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_output.py"), str(source_dir), "--json"],
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        timeout=60,
    )
    return completed.returncode, json.loads(completed.stdout)


class ValidatorContractTests(unittest.TestCase):
    def test_reliable_layout_contract_cannot_be_bypassed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.pdf", temp / "output")
            self.assertEqual(code, 0, summary)
            original = only_source_dir(temp / "output")

            cases: list[tuple[str, str, Callable[[Path], None]]] = []

            def remove_source_order(source_dir: Path) -> None:
                path = source_dir / "document-ir.jsonl"
                records = load_jsonl(path)
                for record in records:
                    record.get("metadata", {}).pop("source_order", None)
                write_jsonl(path, records)
                refresh_manifest_hash(source_dir, "document-ir.jsonl")

            cases.append(("missing_source_order", "source_order_metadata_invalid", remove_source_order))

            def remove_visual_metadata(source_dir: Path) -> None:
                path = source_dir / "document-ir.jsonl"
                records = load_jsonl(path)
                for record in records:
                    if record.get("type") == "image" and record.get("status") == "success":
                        record.get("metadata", {}).pop("associated_heading_path", None)
                        record.get("metadata", {}).pop("association_method", None)
                write_jsonl(path, records)
                refresh_manifest_hash(source_dir, "document-ir.jsonl")

            cases.append(("missing_visual_metadata", "associated_heading_path_mismatch", remove_visual_metadata))

            def remove_semantics_status(source_dir: Path) -> None:
                path = source_dir / "processing-report.json"
                report = load_json(path)
                report["source_metadata"].pop("layout_semantics_status", None)
                report["source_metadata"].pop("document_title_semantics_status", None)
                path.write_text(
                    json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                refresh_manifest_hash(source_dir, "processing-report.json")

            cases.append(("missing_semantics_status", "success_without_reliable_layout_semantics", remove_semantics_status))

            def remove_post_metrics(source_dir: Path) -> None:
                path = source_dir / "processing-report.json"
                report = load_json(path)
                for name in (
                    "reading_order_violation_count",
                    "source_order_metadata_violation_count",
                    "visual_heading_relation_violation_count",
                    "document_title_mismatch_count",
                ):
                    report["chunk_post_validation"].pop(name, None)
                path.write_text(
                    json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                    encoding="utf-8",
                )
                refresh_manifest_hash(source_dir, "processing-report.json")

            cases.append(("missing_post_metrics", "chunk_post_validation_metric_missing", remove_post_metrics))

            for case_name, expected_reason, mutate in cases:
                with self.subTest(case=case_name):
                    case_dir = temp / case_name
                    shutil.copytree(original, case_dir)
                    mutate(case_dir)
                    validation_code, result = validate(case_dir)
                    reasons = {error.get("reason") for error in result.get("errors", [])}
                    self.assertNotEqual(validation_code, 0, result)
                    self.assertIn(expected_reason, reasons)


if __name__ == "__main__":
    unittest.main()
