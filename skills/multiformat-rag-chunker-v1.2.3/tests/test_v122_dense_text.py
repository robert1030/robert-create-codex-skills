from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from helpers import load_json, load_jsonl, only_source_dir, run_cli
from prepare_visual_review import prepare_pdf_review
from validate_against_source import validate_against_source
from validate_dense_retrieval import load_spec, validate_dense_retrieval
from visual_semantics import load_visual_semantics


def _create_dense_scan(path: Path) -> None:
    import fitz

    raster_source = fitz.open()
    raster_page = raster_source.new_page(width=600, height=800)
    rows = [
        "1. abandon /əˈbændən/ v. 放棄；He abandoned the broken car.",
        "2. vivid /ˈvɪvɪd/ adj. 生動的；She gave a vivid description.",
        "3. fragile /ˈfrædʒaɪl/ adj. 易碎的；This glass is fragile.",
    ]
    raster_page.insert_text((42, 55), "SCANNED MULTILINGUAL VOCABULARY", fontsize=16, fontname="china-s")
    for repeat in range(7):
        for index, row in enumerate(rows):
            raster_page.insert_text(
                (45, 100 + repeat * 90 + index * 26),
                row,
                fontsize=10,
                fontname="china-s",
            )
    pixels = raster_page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    image_bytes = pixels.tobytes("png")
    raster_source.close()

    document = fitz.open()
    page = document.new_page(width=600, height=800)
    page.insert_image(page.rect, stream=image_bytes)
    document.new_page(width=600, height=800)
    document.set_metadata({"title": "Dense Multilingual Vocabulary Fixture"})
    document.save(path)
    document.close()


def _units() -> list[dict]:
    return [
        {
            "unit_id": "p001-u001",
            "unit_type": "lexical_entry",
            "reading_order": 1,
            "text": "abandon /əˈbændən/ v. 放棄；He abandoned the broken car.",
            "fields": {
                "headword": "abandon",
                "ipa": "/əˈbændən/",
                "part_of_speech": "v.",
                "definition_zh": "放棄",
                "example_en": "He abandoned the broken car.",
            },
            "uncertain_spans": [],
        },
        {
            "unit_id": "p001-u002",
            "unit_type": "lexical_entry",
            "reading_order": 2,
            "text": "vivid /ˈvɪvɪd/ adj. 生動的；She gave a vivid description.",
            "fields": {
                "headword": "vivid",
                "ipa": "/ˈvɪvɪd/",
                "part_of_speech": "adj.",
                "definition_zh": "生動的",
                "example_en": "She gave a vivid description.",
            },
            "uncertain_spans": [],
        },
        {
            "unit_id": "p001-u003",
            "unit_type": "lexical_entry",
            "reading_order": 3,
            "text": "fragile /ˈfrædʒaɪl/ adj. 易碎的；This glass is fragile.",
            "fields": {
                "headword": "fragile",
                "ipa": "/ˈfrædʒaɪl/",
                "part_of_speech": "adj.",
                "definition_zh": "易碎的",
                "example_en": "This glass is fragile.",
            },
            "uncertain_spans": [],
        },
    ]


def _write_sidecars(temp: Path, source: Path) -> tuple[dict, Path, Path]:
    request = prepare_pdf_review(source, temp / "review-work", profile="dense_text")
    item = request["items"][0]
    extraction = {
        "schema": "multiformat-rag-chunker.visual-semantics.v2",
        "input_sha256": request["input_sha256"],
        "reviews": [{
            "reference": item["reference"],
            "source_asset_sha256": item["source_asset_sha256"],
            "review_method": "native_visual_nonverbatim",
            "review_mode": "dense_text",
            "required_review_mode": "dense_text",
            "density_metrics": item["density_metrics"],
            "text_units": _units(),
        }],
    }
    extraction_path = temp / "REVIEW.json"
    extraction_path.write_text(
        json.dumps(extraction, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    extraction_sha = hashlib.sha256(extraction_path.read_bytes()).hexdigest()
    validation = {
        "schema": "multiformat-rag-chunker.visual-text-validation.v1",
        "input_sha256": request["input_sha256"],
        "extraction_manifest_sha256": extraction_sha,
        "validations": [{
            "reference": item["reference"],
            "source_asset_sha256": item["source_asset_sha256"],
            "validation_method": "independent_native_visual",
            "status": "passed",
            "checked_unit_ids": [unit["unit_id"] for unit in _units()],
            "missing_units": [],
            "unexpected_units": [],
            "mismatched_units": [],
            "reading_order_status": "passed",
            "mode_appropriate": True,
        }],
    }
    validation_path = temp / "VALIDATION.json"
    validation_path.write_text(
        json.dumps(validation, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return request, extraction_path, validation_path


class DenseTextContractTests(unittest.TestCase):
    def test_dense_text_requires_independent_validation_and_produces_searchable_units(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "dense.pdf"
            _create_dense_scan(source)
            request, extraction, validation = _write_sidecars(temp, source)
            with self.assertRaisesRegex(ValueError, "visual_text_independent_validation_required"):
                load_visual_semantics(extraction, source)

            code, summary = run_cli(
                source,
                temp / "output",
                "--visual-semantics", str(extraction),
                "--visual-text-validation", str(validation),
                "--require-original-binary",
                "--min-tokens", "1",
                "--max-tokens", "20",
                "--overlap-tokens", "0",
            )
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            records = load_jsonl(source_dir / "document-ir.jsonl")
            dense = [record for record in records if record.get("content_origin") == "llm_visual_text"]
            self.assertEqual([record["metadata"]["visual_text_unit_id"] for record in dense], [
                "p001-u001", "p001-u002", "p001-u003",
            ])
            self.assertTrue(all(record["verbatim"] is False for record in dense))
            chunks = load_jsonl(source_dir / "chunks.jsonl")
            self.assertGreaterEqual(len(chunks), 3)
            report = load_json(source_dir / "processing-report.json")
            self.assertEqual(report["chunk_pre_validation"]["dense_text"]["coverage_ratio"], 1.0)
            source_code, source_result = validate_against_source(source, source_dir, require_complete=True)
            self.assertEqual(source_code, 0, source_result)
            self.assertEqual(source_result["verified_dense_text_pages"], [1])

            golden = {
                "schema": "multiformat-rag-chunker.dense-retrieval-golden.v1",
                "input_sha256": request["input_sha256"],
                "extraction_manifest_sha256": hashlib.sha256(extraction.read_bytes()).hexdigest(),
                "queries": [
                    {
                        "id": "headword-abandon", "query_type": "headword", "query": "abandon",
                        "expected_unit_id": "p001-u001", "expected_reference": "pages/page-001.png",
                        "expected_page": 1, "expected_anchor": "abandon /əˈbændən/", "top_k": 1,
                    },
                    {
                        "id": "definition-vivid", "query_type": "definition", "query": "生動的",
                        "expected_unit_id": "p001-u002", "expected_reference": "pages/page-001.png",
                        "expected_page": 1, "expected_anchor": "生動的", "top_k": 3,
                    },
                    {
                        "id": "example-fragile", "query_type": "example", "query": "glass fragile",
                        "expected_unit_id": "p001-u003", "expected_reference": "pages/page-001.png",
                        "expected_page": 1, "expected_anchor": "This glass is fragile.", "top_k": 3,
                    },
                ],
            }
            golden_path = temp / "GOLDEN.json"
            golden_path.write_text(json.dumps(golden, ensure_ascii=False), encoding="utf-8")
            retrieval = validate_dense_retrieval(source_dir, load_spec(golden_path))
            self.assertTrue(retrieval["passed"], retrieval)
            self.assertEqual(retrieval["metrics"]["headword_recall_at_1"], 1.0)
            self.assertEqual(retrieval["metrics"]["definition_recall_at_3"], 1.0)
            self.assertEqual(retrieval["metrics"]["example_recall_at_3"], 1.0)

    def test_dense_page_summary_cannot_satisfy_dense_requirement(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "dense.pdf"
            _create_dense_scan(source)
            request = prepare_pdf_review(source, temp / "review", profile="dense_text")
            item = request["items"][0]
            extraction = temp / "summary.json"
            extraction.write_text(json.dumps({
                "schema": "multiformat-rag-chunker.visual-semantics.v2",
                "input_sha256": request["input_sha256"],
                "reviews": [{
                    "reference": item["reference"],
                    "source_asset_sha256": item["source_asset_sha256"],
                    "review_method": "native_visual_nonverbatim",
                    "review_mode": "semantic_summary",
                    "required_review_mode": "dense_text",
                    "density_metrics": item["density_metrics"],
                    "summary": "This is only a high-level summary and cannot replace the page text.",
                }],
            }), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "visual_semantics_required_review_mode_mismatch"):
                load_visual_semantics(extraction, source)

    def test_dense_sidecar_tampering_is_rejected(self) -> None:
        mutations = {
            "extraction_hash": ("visual_text_validation_extraction_sha256_mismatch", "validation", lambda value: value.update({"extraction_manifest_sha256": "0" * 64})),
            "checked_units": ("visual_text_validation_checked_units_mismatch", "validation", lambda value: value["validations"][0].update({"checked_unit_ids": ["p001-u001"]})),
            "missing_unit": ("visual_text_validation_missing_units_not_empty", "validation", lambda value: value["validations"][0].update({"missing_units": ["p001-u004"]})),
            "mode": ("visual_text_validation_mode_inappropriate", "validation", lambda value: value["validations"][0].update({"mode_appropriate": False})),
            "uncertainty": ("visual_text_unit_uncertainty_unresolved", "extraction", lambda value: value["reviews"][0]["text_units"][0].update({"uncertain_spans": ["IPA"]})),
            "order": ("visual_text_unit_reading_order_not_contiguous", "extraction", lambda value: value["reviews"][0]["text_units"][2].update({"reading_order": 8})),
        }
        for name, (message, target, mutate) in mutations.items():
            with self.subTest(name=name), tempfile.TemporaryDirectory() as temp_name:
                temp = Path(temp_name)
                source = temp / "dense.pdf"
                _create_dense_scan(source)
                _request, extraction_path, validation_path = _write_sidecars(temp, source)
                extraction = json.loads(extraction_path.read_text(encoding="utf-8"))
                validation = json.loads(validation_path.read_text(encoding="utf-8"))
                mutate(extraction if target == "extraction" else validation)
                if target == "extraction":
                    extraction_path.write_text(json.dumps(extraction, ensure_ascii=False), encoding="utf-8")
                    validation["extraction_manifest_sha256"] = hashlib.sha256(extraction_path.read_bytes()).hexdigest()
                validation_path.write_text(json.dumps(validation, ensure_ascii=False), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, message):
                    load_visual_semantics(extraction_path, source, validation_path)

    def test_visual_text_asset_binding_uses_exact_rendered_page(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "dense.pdf"
            _create_dense_scan(source)
            _request, extraction, validation = _write_sidecars(temp, source)
            payload = json.loads(extraction.read_text(encoding="utf-8"))
            payload["reviews"][0]["source_asset_sha256"] = "f" * 64
            extraction.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
            validation_payload = json.loads(validation.read_text(encoding="utf-8"))
            validation_payload["extraction_manifest_sha256"] = hashlib.sha256(extraction.read_bytes()).hexdigest()
            validation_payload["validations"][0]["source_asset_sha256"] = "f" * 64
            validation.write_text(json.dumps(validation_payload, ensure_ascii=False), encoding="utf-8")
            semantics = load_visual_semantics(extraction, source, validation)
            exact_asset = prepare_pdf_review(source, temp / "second-review", profile="dense_text")["items"][0]
            self.assertIsNone(semantics.lookup(exact_asset["reference"], exact_asset["source_asset_sha256"]))


if __name__ == "__main__":
    unittest.main()
