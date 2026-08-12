from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from coverage import evaluate_source_coverage
from models import Block, DocumentIR, Location, Provenance
from prepare_visual_review import prepare_pdf_review
from utils import sha256_file
from validate import validate_source_output
from validate_against_source import validate_against_source

from helpers import load_json, load_jsonl, only_source_dir, run_cli


def _provenance() -> Provenance:
    return Provenance(
        source_id="source-001",
        user_specified_name="scan.pdf",
        original_upload_name="scan.pdf",
        runtime_path="/tmp/scan.pdf",
        extension=".pdf",
        requested_media_type="application/pdf",
        runtime_media_type="application/pdf",
        magic_bytes="25504446",
        sha256="a" * 64,
        actual_adapter="pdf_adapter",
        original_binary_processed=True,
        derived_snapshot=False,
        input_fidelity="original_binary",
    )


def _create_scanned_pdf(path: Path) -> None:
    import fitz

    image_path = path.with_suffix(".png")
    image = Image.new("RGB", (800, 1100), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle((40, 40, 760, 1060), outline="black", width=4)
    draw.text((80, 100), "SCANNED VOCABULARY PAGE", fill="black")
    for index in range(12):
        y = 180 + index * 65
        draw.text((90, y), f"{index + 1}. word{index + 1}  definition {index + 1}", fill="black")
        draw.line((80, y + 32, 720, y + 32), fill="gray", width=2)
    image.save(image_path)

    document = fitz.open()
    page = document.new_page(width=400, height=550)
    page.insert_image(page.rect, filename=str(image_path))
    document.new_page(width=400, height=550)
    document.set_metadata({"title": "Scanned Vocabulary Fixture", "author": "Test"})
    document.save(path)
    document.close()


def _refresh_manifest_hash(source_dir: Path, relative: str) -> None:
    manifest_path = source_dir / "manifest.json"
    manifest = load_json(manifest_path)
    manifest["output_file_hashes"][relative] = sha256_file(source_dir / relative)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )


class V122VisualReviewTests(unittest.TestCase):
    def test_qr_payload_cannot_mask_unresolved_primary_content(self) -> None:
        blocks = [
            Block("source-001-block-001", "heading", "Title", Location(page=1), ["Title"], critical=True),
            Block(
                "source-001-block-002",
                "image",
                "QR Code payload：https://example.test",
                Location(page=1, asset_id="qr-001"),
                ["Title"],
                content_origin="qr_decoder",
                required=True,
                critical=True,
                metadata={"content_role": "machine_payload"},
            ),
            Block(
                "source-001-block-003",
                "image",
                "",
                Location(page=1, asset_id="scan-001"),
                ["Title"],
                content_origin="placeholder",
                required=True,
                status="failed",
                verbatim=False,
                metadata={"content_role": "primary", "reason": "native_visual_review_required"},
            ),
        ]
        document = DocumentIR("source-001", "Title", _provenance(), blocks)
        markdown = "# Title\n\nQR Code payload：https://example.test\n\n> [內容擷取未完成]\n"
        metrics = evaluate_source_coverage(document, markdown)
        self.assertEqual(metrics["content_completeness_status"], "fatal_error")
        self.assertIn("no_effective_main_content", metrics["fatal_reasons"])
        self.assertEqual(metrics["primary_content"]["verified_primary_count"], 0)
        self.assertEqual(metrics["primary_content"]["unresolved_primary_count"], 1)

    def test_hash_bound_pdf_page_review_produces_complete_chunks_and_skips_blank_page(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            _create_scanned_pdf(source)
            review_work = temp / "review-work"
            request = prepare_pdf_review(source, review_work)
            self.assertEqual([item["page"] for item in request["items"]], [1])
            self.assertEqual(
                [item["page"] for item in request["skipped_pages"] if item["reason"] == "blank_page"],
                [2],
            )
            response = {
                "schema": "multiformat-rag-chunker.visual-semantics.v1",
                "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "reviews": [
                    {
                        "reference": item["reference"],
                        "source_asset_sha256": item["source_asset_sha256"],
                        "review_method": "native_visual_nonverbatim",
                        "summary": "本頁為掃描單字教材，包含編號單字與對應定義的條列內容。",
                    }
                    for item in request["items"]
                ],
            }
            response_path = temp / "visual-review-response.json"
            response_path.write_text(
                json.dumps(response, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            code, summary = run_cli(
                source,
                temp / "output",
                "--visual-semantics",
                str(response_path),
                "--require-original-binary",
            )
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            records = load_jsonl(source_dir / "document-ir.jsonl")
            visual = next(record for record in records if record.get("content_origin") == "llm_visual_summary")
            self.assertEqual(visual["metadata"]["visual_class"], "full_page_scan")
            self.assertFalse(visual["verbatim"])
            self.assertNotIn("attempts", visual)
            blank = next(record for record in records if record.get("metadata", {}).get("skip_reason") == "blank_page")
            self.assertFalse(blank["required"])
            self.assertEqual(blank["status"], "skipped")
            report = load_json(source_dir / "processing-report.json")
            self.assertEqual(report["source_metadata"]["title_source"], "pdf_metadata")
            self.assertEqual(report["source_metadata"]["document_title_semantics_status"], "reliable")
            self.assertEqual(report["final_status"], "success")
            source_code, source_result = validate_against_source(source, source_dir, require_complete=True)
            self.assertEqual(source_code, 0, source_result)
            self.assertEqual(source_result["required_scan_pages"], [1])
            self.assertEqual(source_result["blank_pages"], [2])

    def test_pdf_validator_rejects_missing_asset_hash_even_after_manifest_rehash(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            _create_scanned_pdf(source)
            request = prepare_pdf_review(source, temp / "review-work")
            response = {
                "schema": "multiformat-rag-chunker.visual-semantics.v1",
                "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "reviews": [{
                    "reference": request["items"][0]["reference"],
                    "source_asset_sha256": request["items"][0]["source_asset_sha256"],
                    "review_method": "native_visual_nonverbatim",
                    "summary": "本頁為掃描教材，包含編號、單字與定義等主要內容。",
                }],
            }
            response_path = temp / "response.json"
            response_path.write_text(json.dumps(response, ensure_ascii=False), encoding="utf-8")
            code, summary = run_cli(source, temp / "output", "--visual-semantics", str(response_path))
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            ir_path = source_dir / "document-ir.jsonl"
            records = load_jsonl(ir_path)
            image_record = next(record for record in records if record.get("type") == "image")
            image_record["metadata"].pop("asset_sha256", None)
            ir_path.write_text(
                "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
                encoding="utf-8",
                newline="\n",
            )
            _refresh_manifest_hash(source_dir, "document-ir.jsonl")
            validate_code, result = validate_source_output(source_dir)
            self.assertEqual(validate_code, 1, result)
            self.assertTrue(any(error.get("reason") == "image_metadata_field_missing" for error in result["errors"]))

    def test_validator_rejects_partial_flag_without_authorization_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "scan.pdf"
            _create_scanned_pdf(source)
            request = prepare_pdf_review(source, temp / "review-work")
            response_path = temp / "response.json"
            response_path.write_text(json.dumps({
                "schema": "multiformat-rag-chunker.visual-semantics.v1",
                "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "reviews": [{
                    "reference": request["items"][0]["reference"],
                    "source_asset_sha256": request["items"][0]["source_asset_sha256"],
                    "review_method": "native_visual_nonverbatim",
                    "summary": "本頁為掃描教材，包含編號、單字與定義等主要內容。",
                }],
            }, ensure_ascii=False), encoding="utf-8")
            code, summary = run_cli(source, temp / "output", "--visual-semantics", str(response_path))
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            report_path = source_dir / "processing-report.json"
            report = load_json(report_path)
            report["parameters"]["allow_partial_chunks"] = True
            report["parameters"]["partial_authorization"] = None
            report_path.write_text(
                json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
                newline="\n",
            )
            _refresh_manifest_hash(source_dir, "processing-report.json")
            validate_code, result = validate_source_output(source_dir)
            self.assertEqual(validate_code, 1, result)
            self.assertTrue(any(
                error.get("reason") == "partial_chunks_without_explicit_user_authorization"
                for error in result["errors"]
            ))


if __name__ == "__main__":
    unittest.main()
