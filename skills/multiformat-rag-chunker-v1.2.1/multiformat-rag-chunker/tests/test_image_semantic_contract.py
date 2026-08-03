from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from helpers import FIXTURES, load_jsonl, only_source_dir, run_cli
from adapters.base import AdapterContext
from adapters.image_adapter import parse as parse_image
from models import AttemptRecord, Provenance
from ocr import OCRResult, ocr_image
from output import failure_records
from visual import classify_visual, load_image
from visual_semantics import load_visual_semantics


def _image_block(records: list[dict]) -> dict:
    return next(record for record in records if record["type"] == "image")


class ImageSemanticContractTests(unittest.TestCase):
    def test_hash_bound_visual_review_enters_chunks_as_nonverbatim_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            image_path = temp / "structured-ui.png"
            image = Image.new("RGB", (560, 340), "#edf0f3")
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, 559, 38), fill="#365f91")
            draw.rectangle((20, 60, 540, 315), outline="#6e7a87", width=2)
            for y in range(88, 310, 28):
                draw.line((22, y, 538, y), fill="#6e7a87", width=2)
            image.save(image_path)
            source = temp / "screen.html"
            source.write_text(
                "<html><body><h1>Screen</h1><img src=\"structured-ui.png\"></body></html>",
                encoding="utf-8",
            )
            review = temp / "visual-semantics.json"
            review.write_text(json.dumps({
                "schema": "multiformat-rag-chunker.visual-semantics.v1",
                "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "reviews": [{
                    "reference": "structured-ui.png",
                    "source_asset_sha256": hashlib.sha256(image_path.read_bytes()).hexdigest(),
                    "review_method": "native_visual_nonverbatim",
                    "summary": "A non-verbatim summary of a structured application configuration screen.",
                }],
            }), encoding="utf-8")

            code, summary = run_cli(source, temp / "output", "--visual-semantics", str(review))
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            block = _image_block(load_jsonl(source_dir / "document-ir.jsonl"))
            chunks = load_jsonl(source_dir / "chunks.jsonl")
            self.assertEqual(block["content_origin"], "llm_visual_summary")
            self.assertTrue(block["required"])
            self.assertFalse(block["verbatim"])
            self.assertEqual(block["metadata"]["visual_summary_evidence"]["review_method"], "native_visual_nonverbatim")
            self.assertNotIn("attempts", block)
            self.assertTrue(any(block["block_id"] in chunk["source_block_ids"] for chunk in chunks))
            self.assertTrue(any(chunk["source_block_ids"] == [block["block_id"]] for chunk in chunks))

    def test_visual_review_rejects_a_manifest_for_a_different_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "screen.html"
            source.write_text("<html><body>Screen</body></html>", encoding="utf-8")
            review = temp / "visual-semantics.json"
            review.write_text(json.dumps({
                "schema": "multiformat-rag-chunker.visual-semantics.v1",
                "input_sha256": "0" * 64,
                "reviews": [{
                    "reference": "structured-ui.png",
                    "source_asset_sha256": "1" * 64,
                    "review_method": "native_visual_nonverbatim",
                    "summary": "A non-verbatim summary of a structured application configuration screen.",
                }],
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "visual_semantics_input_sha256_mismatch"):
                load_visual_semantics(review, source)

    def test_unreviewed_parent_relative_image_reference_is_ignored(self) -> None:
        self.assertIsNone(load_visual_semantics(None, FIXTURES / "sample.html").lookup(
            "../images/unreviewed.png",
            "0" * 64,
        ))

    def test_wide_dense_interface_without_divider_is_screen_capture(self) -> None:
        image = Image.new("RGB", (960, 160), "#f4f6f8")
        draw = ImageDraw.Draw(image)
        for column in range(4):
            base_x = 18 + column * 230
            for row in range(6):
                y = 20 + row * 21
                for glyph in range(8):
                    x = base_x + glyph * 24
                    draw.rectangle((x, y, x + 15, y + 7), fill="#34495e")

        inspection = classify_visual(image)
        self.assertEqual(inspection.visual_class, "screen_capture")
        self.assertEqual(
            inspection.metadata["layout_evidence"]["classifier"],
            "deterministic_layout_edges_v2",
        )
        self.assertFalse(inspection.metadata["layout_evidence"]["text_block"])

    def test_structured_screen_capture_skips_ocr_without_machine_payload(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "structured-ui.png"
            image = Image.new("RGB", (560, 340), "#edf0f3")
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, 559, 38), fill="#365f91")
            draw.rectangle((20, 60, 540, 315), outline="#6e7a87", width=2)
            for y in range(88, 310, 28):
                draw.line((22, y, 538, y), fill="#6e7a87", width=2)
            for x in (150, 330, 450):
                draw.line((x, 62, x, 314), fill="#9ba6b1", width=2)
            image.save(source)

            self.assertEqual(classify_visual(load_image(source)).visual_class, "screen_capture")
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 1, summary)
            self.assertEqual(summary["status"], "fatal_error")
            source_dir = only_source_dir(temp / "output")
            block = _image_block(load_jsonl(source_dir / "document-ir.jsonl"))
            self.assertEqual(block["status"], "skipped")
            self.assertFalse(block["required"])
            self.assertFalse(block["critical"])
            self.assertFalse(block["verbatim"])
            self.assertEqual(block["content_origin"], "derived_normalization")
            self.assertEqual(block["metadata"]["skip_reason"], "no_verified_machine_payload")
            self.assertEqual(block["metadata"]["machine_payloads"], [])
            self.assertNotIn("attempts", block)

    def test_qr_payload_has_decoder_provenance_and_never_routes_to_ocr(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "qr.png"
            shutil.copy2(FIXTURES / "qr.png", source)
            source_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            block = _image_block(load_jsonl(source_dir / "document-ir.jsonl"))
            self.assertEqual(block["content_origin"], "qr_decoder")
            self.assertTrue(block["required"])
            self.assertTrue(block["critical"])
            self.assertTrue(block["verbatim"])
            self.assertEqual(
                block["metadata"]["machine_payloads"],
                [{
                    "kind": "qr",
                    "symbology": "QR_CODE",
                    "payload": "https://example.test/rag-fixture",
                    "source_asset_sha256": source_sha256,
                }],
            )
            self.assertEqual(block["metadata"]["decoder_evidence"]["backend"], "opencv_qrcode_detector")
            self.assertNotIn("attempts", block)

    def test_barcode_payload_has_symbology_and_never_routes_to_ocr(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "barcode-ean13.png"
            shutil.copy2(FIXTURES / "barcode-ean13.png", source)
            source_sha256 = hashlib.sha256(source.read_bytes()).hexdigest()
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            block = _image_block(load_jsonl(source_dir / "document-ir.jsonl"))
            self.assertEqual(block["content_origin"], "qr_decoder")
            self.assertEqual(
                block["metadata"]["machine_payloads"],
                [{
                    "kind": "barcode",
                    "symbology": "EAN_13",
                    "payload": "5901234123457",
                    "source_asset_sha256": source_sha256,
                }],
            )
            self.assertEqual(block["metadata"]["decoder_evidence"]["backend"], ["opencv_barcode_detector"])
            self.assertNotIn("attempts", block)

    def test_text_block_uses_accepted_ocr_result(self) -> None:
        source = FIXTURES / "ocr-text.png"
        provenance = Provenance(
            source_id="ocr-text-fixture",
            user_specified_name=source.name,
            original_upload_name=source.name,
            runtime_path=str(source),
            extension=".png",
            requested_media_type="image/png",
            runtime_media_type="image/png",
            magic_bytes="89504e47",
            sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
            actual_adapter="image_adapter",
            original_binary_processed=True,
            derived_snapshot=False,
            input_fidelity="original_binary",
        )
        result = OCRResult(
            text="SCANNED OCR FIXTURE 2026",
            status="success",
            attempts=[AttemptRecord(1, "tesseract", "attempt_1", "success")],
            confidence=99.0,
            quality={"reasons": []},
        )
        with tempfile.TemporaryDirectory() as temp_name, mock.patch(
            "adapters.image_adapter.ocr_image", return_value=result
        ) as mocked_ocr:
            document = parse_image(source, AdapterContext(provenance, Path(temp_name), "eng"))
        block = next(item for item in document.blocks if item.type == "image")
        self.assertEqual(block.metadata["visual_class"], "text_block")
        self.assertEqual(block.content_origin, "ocr")
        self.assertEqual(block.status, "success")
        self.assertEqual(block.metadata["ocr_semantic_status"], "accepted")
        self.assertEqual(block.text, "SCANNED OCR FIXTURE 2026")
        self.assertEqual(mocked_ocr.call_count, 1)

    def test_unavailable_ocr_backend_is_needs_capability_not_quality_failure(self) -> None:
        source = FIXTURES / "ocr-text.png"
        with mock.patch(
            "ocr._ocr_once",
            side_effect=RuntimeError("tesseract is not installed or it is not in your PATH"),
        ):
            result = ocr_image(source, max_attempts=1)

        self.assertEqual(result.status, "failed")
        self.assertEqual(result.quality["reasons"], ["ocr_backend_not_available"])
        self.assertEqual(len(result.attempts), 1)

        provenance = Provenance(
            source_id="ocr-backend-unavailable-fixture",
            user_specified_name=source.name,
            original_upload_name=source.name,
            runtime_path=str(source),
            extension=".png",
            requested_media_type="image/png",
            runtime_media_type="image/png",
            magic_bytes="89504e47",
            sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
            actual_adapter="image_adapter",
            original_binary_processed=True,
            derived_snapshot=False,
            input_fidelity="original_binary",
        )
        with tempfile.TemporaryDirectory() as temp_name, mock.patch(
            "adapters.image_adapter.ocr_image", return_value=result
        ):
            document = parse_image(source, AdapterContext(provenance, Path(temp_name), "eng"))

        block = _image_block([item.to_dict() for item in document.blocks])
        self.assertEqual(block["metadata"]["ocr_semantic_status"], "not_run")
        self.assertEqual(block["metadata"]["reason"], "ocr_backend_not_available")
        failure = failure_records(document)[0]
        self.assertEqual(failure.failure_reason, "needs_capability")
        self.assertEqual(
            failure.details["next_action"],
            "agent_evaluate_safe_capability_fulfillment_or_equivalent",
        )

    def test_html_screen_capture_is_not_ocrd_or_admitted_to_chunks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            image_path = temp / "structured-ui.png"
            image = Image.new("RGB", (560, 340), "#edf0f3")
            draw = ImageDraw.Draw(image)
            draw.rectangle((0, 0, 559, 38), fill="#365f91")
            draw.rectangle((20, 60, 540, 315), outline="#6e7a87", width=2)
            for y in range(88, 310, 28):
                draw.line((22, y, 538, y), fill="#6e7a87", width=2)
            for x in (150, 330, 450):
                draw.line((x, 62, x, 314), fill="#9ba6b1", width=2)
            image.save(image_path)
            source = temp / "screen.html"
            source.write_text(
                "<html><body><h1>Screen</h1><p>Source-backed body text.</p><img src=\"structured-ui.png\"></body></html>",
                encoding="utf-8",
            )

            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            block = _image_block(load_jsonl(source_dir / "document-ir.jsonl"))
            chunks = load_jsonl(source_dir / "chunks.jsonl")
            self.assertEqual(block["metadata"]["visual_class"], "screen_capture")
            self.assertEqual(block["content_origin"], "derived_normalization")
            self.assertEqual(block["status"], "skipped")
            self.assertFalse(block["required"])
            self.assertFalse(block["verbatim"])
            self.assertEqual(block["metadata"]["skip_reason"], "no_verified_machine_payload")
            self.assertNotIn("attempts", block)
            self.assertFalse(any(block["block_id"] in chunk["source_block_ids"] for chunk in chunks))

    def test_html_barcode_has_verified_decoder_payload(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            barcode = temp / "barcode-ean13.png"
            shutil.copy2(FIXTURES / "barcode-ean13.png", barcode)
            source = temp / "barcode.html"
            source.write_text(
                "<html><body><h1>Barcode</h1><img src=\"barcode-ean13.png\"></body></html>",
                encoding="utf-8",
            )

            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            block = _image_block(load_jsonl(source_dir / "document-ir.jsonl"))
            self.assertEqual(block["content_origin"], "qr_decoder")
            self.assertEqual(
                block["metadata"]["machine_payloads"],
                [{
                    "kind": "barcode",
                    "symbology": "EAN_13",
                    "payload": "5901234123457",
                    "source_asset_sha256": hashlib.sha256(barcode.read_bytes()).hexdigest(),
                }],
            )
            self.assertEqual(block["metadata"]["decoder_evidence"]["backend"], ["opencv_barcode_detector"])
            self.assertNotIn("attempts", block)


if __name__ == "__main__":
    unittest.main()
