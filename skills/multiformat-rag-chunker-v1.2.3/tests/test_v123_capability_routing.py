from __future__ import annotations

import ast
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from adapters.base import AdapterContext
from models import Provenance
from ocr import ocr_image
from utils import sha256_file
from validate import validate_source_output
from visual_semantics import CapabilityEvidence, load_capability_evidence

from helpers import FIXTURES, load_json, load_jsonl, only_source_dir, run_cli


def _create_scanned_pdf(path: Path) -> None:
    import fitz

    image_path = path.with_suffix(".png")
    image = Image.new("RGB", (800, 1100), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((40, 40, 760, 1060), outline="black", width=4)
    draw.text((80, 100), "NATIVE MULTIMODAL ROUTING FIXTURE", fill="black")
    for index in range(10):
        draw.text((90, 180 + index * 70), f"{index + 1}. capability routing row", fill="black")
    image.save(image_path)
    document = fitz.open()
    page = document.new_page(width=400, height=550)
    page.insert_image(page.rect, filename=str(image_path))
    document.set_metadata({"title": "Capability Routing Fixture"})
    document.save(path)
    document.close()


def _write_capability(path: Path, status: str, *, attempted: bool = False) -> None:
    failure_reason = None if status == "available" else f"test_{status}"
    payload = {
        "schema": "multiformat-rag-chunker.capability-evidence.v1",
        "native_llm_multimodal": {
            "status": status,
            "evidence": [f"test_runtime_reports_{status}"],
            "llm_visual_attempted": attempted,
            "failure_reason": failure_reason,
        },
    }
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")


def _refresh_manifest_hash(source_dir: Path, relative: str) -> None:
    manifest_path = source_dir / "manifest.json"
    manifest = load_json(manifest_path)
    manifest["output_file_hashes"][relative] = sha256_file(source_dir / relative)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


def _provenance(source: Path) -> Provenance:
    return Provenance(
        source_id="capability-fixture",
        user_specified_name=source.name,
        original_upload_name=source.name,
        runtime_path=str(source),
        extension=source.suffix,
        requested_media_type="image/png",
        runtime_media_type="image/png",
        magic_bytes="89504e47",
        sha256=sha256_file(source),
        actual_adapter="image_adapter",
        original_binary_processed=True,
        derived_snapshot=False,
        input_fidelity="original_binary",
    )


class V123CapabilityRoutingTests(unittest.TestCase):
    def test_native_text_pdf_stays_on_structured_parser_without_visual_or_ocr_route(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            output = Path(temp_name) / "output"
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.pdf", output)
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(output)
            report = load_json(source_dir / "processing-report.json")
            self.assertEqual(report["source_metadata"]["adapter"], "pdf_adapter")
            self.assertEqual(report["source_metadata"]["capability_routing"]["routing_events"], [])
            self.assertEqual(report["ocr_fallback_statistics"]["total_backend_attempts"], 0)

    def test_standalone_image_hash_bound_review_precedes_ocr(self) -> None:
        source = FIXTURES / "ocr-text.png"
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            review = temp / "review.json"
            review.write_text(json.dumps({
                "schema": "multiformat-rag-chunker.visual-semantics.v1",
                "input_sha256": sha256_file(source),
                "reviews": [{
                    "reference": source.name,
                    "source_asset_sha256": sha256_file(source),
                    "review_method": "native_visual_nonverbatim",
                    "summary": "A hash-bound native visual review of the standalone text image.",
                }],
            }), encoding="utf-8")
            code, summary = run_cli(source, temp / "output", "--visual-semantics", str(review))
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            records = load_jsonl(source_dir / "document-ir.jsonl")
            block = next(item for item in records if item.get("content_origin") == "llm_visual_summary")
            self.assertEqual(block["metadata"]["capability_route"]["selected_lane"], "native_llm_multimodal")
            self.assertFalse(block["metadata"]["capability_route"]["ocr_admitted"])
            self.assertNotIn("attempts", block)

    def test_available_native_multimodal_blocks_ocr_and_records_zero_attempts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            capability = temp / "capability.json"
            _create_scanned_pdf(source)
            _write_capability(capability, "available")

            code, summary = run_cli(
                source,
                temp / "output",
                "--capability-evidence",
                str(capability),
            )
            self.assertEqual(code, 1, summary)
            source_dir = only_source_dir(temp / "output")
            report = load_json(source_dir / "processing-report.json")
            routing = report["source_metadata"]["capability_routing"]
            event = next(item for item in routing["routing_events"] if item["visual_class"] == "full_page_scan")
            self.assertEqual(event["native_llm_multimodal_status"], "available")
            self.assertEqual(event["selected_lane"], "native_llm_multimodal")
            self.assertFalse(event["ocr_admitted"])
            scan = next(
                item for item in load_jsonl(source_dir / "document-ir.jsonl")
                if item.get("metadata", {}).get("visual_class") == "full_page_scan" and item.get("required")
            )
            self.assertEqual(scan["metadata"]["reason"], "native_visual_review_required")
            self.assertNotIn("attempts", scan)
            self.assertNotEqual(scan["metadata"]["reason"], "ocr_backend_not_available")

    def test_unknown_capability_is_not_reinterpreted_as_unavailable(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            _create_scanned_pdf(source)
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 1, summary)
            source_dir = only_source_dir(temp / "output")
            report = load_json(source_dir / "processing-report.json")
            event = next(
                item for item in report["source_metadata"]["capability_routing"]["routing_events"]
                if item["visual_class"] == "full_page_scan"
            )
            self.assertEqual(event["native_llm_multimodal_status"], "unknown")
            self.assertEqual(event["selected_lane"], "capability_evidence_required")
            self.assertFalse(event["ocr_admitted"])

    def test_validator_rejects_available_capability_with_ocr_admission_tamper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            capability = temp / "capability.json"
            _create_scanned_pdf(source)
            _write_capability(capability, "available")
            _code, _summary = run_cli(source, temp / "output", "--capability-evidence", str(capability))
            source_dir = only_source_dir(temp / "output")
            report_path = source_dir / "processing-report.json"
            report = load_json(report_path)
            event = report["source_metadata"]["capability_routing"]["routing_events"][0]
            event["ocr_admitted"] = True
            event["selected_lane"] = "ocr_fallback"
            event["ocr_admission_reason"] = "native_multimodal_unavailable"
            report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            _refresh_manifest_hash(source_dir, "processing-report.json")
            code, result = validate_source_output(source_dir)
            self.assertEqual(code, 1)
            self.assertIn("capability_priority_violation", {item.get("reason") for item in result["errors"]})

    def test_validator_rejects_ocr_evidence_without_a_capability_route(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            _create_scanned_pdf(source)
            _code, _summary = run_cli(source, temp / "output")
            source_dir = only_source_dir(temp / "output")
            ir_path = source_dir / "document-ir.jsonl"
            records = load_jsonl(ir_path)
            scan = next(
                item for item in records
                if item.get("metadata", {}).get("visual_class") == "full_page_scan" and item.get("required")
            )
            scan["content_origin"] = "ocr"
            scan["text"] = "tampered OCR text"
            scan["status"] = "success"
            scan["attempts"] = [{"attempt": 1, "backend": "tesseract", "strategy": "attempt_1", "status": "success"}]
            scan["metadata"].pop("capability_route", None)
            ir_path.write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in records), encoding="utf-8")
            _refresh_manifest_hash(source_dir, "document-ir.jsonl")
            code, result = validate_source_output(source_dir)
            self.assertEqual(code, 1)
            self.assertIn("visual_block_capability_route_missing", {item.get("reason") for item in result["errors"]})

    def test_validator_rejects_faked_unavailable_event_not_bound_to_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            capability = temp / "capability.json"
            _create_scanned_pdf(source)
            _write_capability(capability, "available")
            _code, _summary = run_cli(source, temp / "output", "--capability-evidence", str(capability))
            source_dir = only_source_dir(temp / "output")
            report_path = source_dir / "processing-report.json"
            report = load_json(report_path)
            event = report["source_metadata"]["capability_routing"]["routing_events"][0]
            event["native_llm_multimodal_status"] = "unavailable"
            event["native_llm_multimodal_evidence"] = ["forged_unavailable"]
            event["selected_lane"] = "ocr_fallback"
            event["ocr_admitted"] = True
            event["ocr_admission_reason"] = "native_multimodal_unavailable"
            report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
            _refresh_manifest_hash(source_dir, "processing-report.json")
            code, result = validate_source_output(source_dir)
            self.assertEqual(code, 1)
            self.assertIn(
                "ocr_admission_not_bound_to_capability_manifest",
                {item.get("reason") for item in result["errors"]},
            )

    def test_validator_rejects_tesseract_only_failure_when_native_is_available(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            capability = temp / "capability.json"
            _create_scanned_pdf(source)
            _write_capability(capability, "available")
            _code, _summary = run_cli(source, temp / "output", "--capability-evidence", str(capability))
            source_dir = only_source_dir(temp / "output")
            ir_path = source_dir / "document-ir.jsonl"
            records = load_jsonl(ir_path)
            scan = next(
                item for item in records
                if item.get("metadata", {}).get("visual_class") == "full_page_scan" and item.get("required")
            )
            scan["metadata"]["reason"] = "ocr_backend_not_available"
            scan["metadata"]["ocr_quality"] = {"reasons": ["ocr_backend_not_available"]}
            ir_path.write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in records), encoding="utf-8")
            _refresh_manifest_hash(source_dir, "document-ir.jsonl")
            code, result = validate_source_output(source_dir)
            self.assertEqual(code, 1)
            self.assertIn("capability_priority_violation", {item.get("reason") for item in result["errors"]})

    def test_fallback_statuses_are_admitted_only_with_machine_readable_evidence(self) -> None:
        source = FIXTURES / "ocr-text.png"
        for status, attempted in (("unavailable", False), ("denied", False), ("unsupported", False), ("failed", True)):
            with self.subTest(status=status), tempfile.TemporaryDirectory() as temp_name:
                context = AdapterContext(
                    _provenance(source),
                    Path(temp_name),
                    "eng",
                    capability_evidence=CapabilityEvidence(
                        status=status,
                        evidence=(f"test_{status}",),
                        llm_visual_attempted=attempted,
                        failure_reason=f"test_{status}",
                    ),
                )
                route, admission = context.visual_route(
                    source.name,
                    sha256_file(source),
                    review_present=False,
                    visual_class="text_block",
                )
                self.assertTrue(route["ocr_admitted"])
                with mock.patch("ocr._ocr_once", return_value=("fallback text", 99.0, {"token_count": 2, "line_count": 1})) as backend:
                    result = ocr_image(source, admission=admission, max_attempts=1)
                self.assertEqual(result.status, "success")
                self.assertEqual(backend.call_count, 1)

    def test_failed_capability_requires_prior_llm_attempt_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            path = Path(temp_name) / "capability.json"
            _write_capability(path, "failed", attempted=False)
            with self.assertRaisesRegex(ValueError, "native_multimodal_failed_attempt_evidence_required"):
                load_capability_evidence(path)
            _write_capability(path, "failed", attempted=True)
            evidence = load_capability_evidence(path)
            self.assertEqual(evidence.status, "failed")
            self.assertTrue(evidence.llm_visual_attempted)

    def test_every_adapter_ocr_call_has_an_explicit_admission(self) -> None:
        calls = []
        for path in sorted((ROOT / "scripts" / "adapters").glob("*_adapter.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "ocr_image":
                    calls.append((path.name, node.lineno, {item.arg for item in node.keywords}))
        self.assertGreaterEqual(len(calls), 7)
        self.assertEqual([], [(name, line) for name, line, keywords in calls if "admission" not in keywords])


if __name__ == "__main__":
    unittest.main()
