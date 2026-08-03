from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from helpers import FIXTURES, ROOT, load_json, load_jsonl, only_source_dir, run_cli

QR_PAYLOAD = "https://youtu.be/y0ziAlaqOH4"
EPISODE_TITLE = "威林每周英語新聞 EP.388 (2025-09-22)"
EXPECTED_SECTION_TITLES = [
    EPISODE_TITLE,
    "[得演算法得天下?] TikTok變成美國版? 帶你看懂美中的社群角力",
    "影片單字",
    "英文段落",
]


def assert_tiktok_fixture(testcase: unittest.TestCase, source_dir: Path, expected_media_type: str) -> None:
    normalized = (source_dir / "normalized-document.md").read_text(encoding="utf-8")
    report = load_json(source_dir / "processing-report.json")
    manifest = load_json(source_dir / "manifest.json")
    ir = load_jsonl(source_dir / "document-ir.jsonl")
    chunks = load_jsonl(source_dir / "chunks.jsonl")

    testcase.assertTrue(manifest["provenance"]["original_binary_processed"])
    testcase.assertEqual(manifest["provenance"]["runtime_media_type"], expected_media_type)
    testcase.assertEqual(manifest["provenance"]["source_dimensions"]["page_count"], 2)
    testcase.assertIn("EP.388", normalized)
    testcase.assertIn("2025-09-22", normalized)
    testcase.assertIn(QR_PAYLOAD, normalized)
    testcase.assertNotRegex(normalized, r"(?mi)^\s*(?:PAGE|PAG\s*E)\s*\d+\s*$")
    testcase.assertNotIn("fen 英文", normalized)
    testcase.assertNotIn("~ 閱讀", normalized)

    table_records = [record for record in ir if record.get("type") == "table" and record.get("status") == "success"]
    testcase.assertTrue(table_records)
    table = next(record for record in table_records if record.get("metadata", {}).get("data_row_count") == 25)
    testcase.assertEqual(table["metadata"]["logical_column_count"], 4)
    rows = table["metadata"]["rows"]
    testcase.assertEqual(len(rows), 25)
    testcase.assertEqual([int(row[0]) for row in rows], list(range(1, 26)))
    testcase.assertEqual(rows[0][2], "/ˈstɪk.ɪŋ pɔɪnt/")
    testcase.assertEqual(rows[2][2], "/nɪˌɡoʊ.ʃiˈeɪ.ʃən/")
    testcase.assertEqual(rows[3][2], "/ˈæl.ɡə.rɪ.ðəm/")
    testcase.assertEqual(rows[4][3], "n. 內容；滿足 / adj. 滿足的")
    testcase.assertEqual(rows[18][3], "n. 威脅；危害 / v. 威脅")
    testcase.assertEqual(rows[20][3], "adj. 最初的；開始的 / n. 首字母")
    testcase.assertEqual(rows[21][3], "n. 禁令 / v. 禁止")
    testcase.assertIn("激勵", rows[23][3])

    ordered_lists = [record for record in ir if record.get("type") == "list" and record.get("metadata", {}).get("ordered")]
    testcase.assertTrue(ordered_lists)
    items = max((record["metadata"]["items"] for record in ordered_lists), key=len)
    testcase.assertEqual(len(items), 4)
    testcase.assertTrue(items[0].startswith("A sticking point in negotiations"))
    testcase.assertTrue(items[3].endswith("presidential campaign."))

    pre = report["chunk_pre_validation"]
    post = report["chunk_post_validation"]
    testcase.assertEqual(report["final_status"], "success")
    testcase.assertEqual(pre["source_unit_accounting_ratio"], 1.0)
    testcase.assertGreaterEqual(pre["required_content_coverage_ratio"], 0.95)
    testcase.assertEqual(pre["critical_content_coverage_ratio"], 1.0)
    testcase.assertEqual(post["chunk_block_mapping_ratio"], 1.0)
    testcase.assertEqual(post["omitted_verified_blocks"], [])
    testcase.assertEqual(post["unexpected_chunk_content_count"], 0)
    testcase.assertEqual(post["atomic_unit_violation_count"], 0)
    testcase.assertEqual(post["orphan_heading_context_count"], 0)
    testcase.assertEqual(post["reading_order_violation_count"], 0)
    testcase.assertEqual(post["source_order_metadata_violation_count"], 0)
    testcase.assertEqual(post["visual_heading_relation_violation_count"], 0)
    testcase.assertEqual(post["document_title_mismatch_count"], 0)
    testcase.assertEqual(len(chunks), 1)
    testcase.assertEqual(chunks[0]["heading_path"], [EPISODE_TITLE])
    testcase.assertEqual(chunks[0]["section_titles"], EXPECTED_SECTION_TITLES)

    source_metadata = report["source_metadata"]
    testcase.assertEqual(source_metadata["layout_semantics_status"], "reliable")
    testcase.assertEqual(source_metadata["document_title_semantics_status"], "reliable")
    testcase.assertLess(normalized.index(EXPECTED_SECTION_TITLES[1]), normalized.index(QR_PAYLOAD))
    testcase.assertLess(normalized.index(QR_PAYLOAD), normalized.index("影片單字"))
    testcase.assertLess(normalized.index("影片單字"), normalized.index("英文段落"))

    article = next(record for record in ir if record.get("text") == EXPECTED_SECTION_TITLES[1] and record.get("status") == "success")
    qr = next(record for record in ir if record.get("content_origin") == "qr_decoder" and record.get("status") == "success")
    vocabulary = next(record for record in ir if record.get("text") == "影片單字" and record.get("status") == "success")
    testcase.assertEqual(qr["metadata"]["associated_heading_block_id"], article["block_id"])
    testcase.assertEqual(qr["heading_path"], article["heading_path"])
    testcase.assertLess(article["metadata"]["source_order"], qr["metadata"]["source_order"])
    testcase.assertLess(qr["metadata"]["source_order"], vocabulary["metadata"]["source_order"])

    synthetic_heading = next(record for record in ir if record.get("type") == "heading" and record.get("text") == "英文段落")
    testcase.assertEqual(synthetic_heading["content_origin"], "derived_normalization")
    testcase.assertFalse(synthetic_heading["verbatim"])
    testcase.assertTrue(synthetic_heading["metadata"]["derived"])
    testcase.assertEqual(synthetic_heading["metadata"]["derivation_type"], "synthetic_section_heading")


class PdfDocxRegressionTests(unittest.TestCase):
    def test_pdf_binary_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.pdf", temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            assert_tiktok_fixture(self, source_dir, "application/pdf")
            manifest = load_json(source_dir / "manifest.json")
            self.assertEqual(
                manifest["provenance"]["sha256"],
                "b1159e2d372200cccc6e61d24411f828d82f072e1df720d22aae0b49c2c8cd82",
            )

            chunks_path = source_dir / "chunks.jsonl"
            records = load_jsonl(chunks_path)
            records[0]["heading_path"] = [EPISODE_TITLE, "英文段落"]
            chunks_path.write_text(
                "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
                encoding="utf-8",
            )
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
            result = json.loads(completed.stdout)
            reasons = {error.get("reason") for error in result.get("errors", [])}
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("chunk_heading_path_mismatch", reasons)

    def test_doc_binary_fixture(self) -> None:
        if not (shutil.which("libreoffice") or shutil.which("soffice")):
            self.skipTest("optional_tool_lane_requires_libreoffice")
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.doc", temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            assert_tiktok_fixture(self, source_dir, "application/msword")
            report = load_json(source_dir / "processing-report.json")
            manifest = load_json(source_dir / "manifest.json")
            self.assertEqual(report["source_metadata"]["adapter"], "doc_adapter")
            self.assertEqual(report["source_metadata"]["fallback"], "libreoffice_doc_to_docx")
            self.assertTrue(any(step.get("operation") == "libreoffice_doc_to_docx" for step in manifest["provenance"]["derivation_chain"]))

    def test_missing_opencv_downgrades_visual_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            blocker = temp / "no-cv2"
            blocker.mkdir()
            (blocker / "cv2.py").write_text(
                'raise ModuleNotFoundError("No module named \'cv2\'")\n',
                encoding="utf-8",
            )
            for fixture_name in ("2025-09-TikTok變成美國版.pdf", "2025-09-TikTok變成美國版.docx"):
                with self.subTest(fixture=fixture_name):
                    output = temp / f"output-{Path(fixture_name).suffix[1:]}"
                    env = os.environ.copy()
                    existing = env.get("PYTHONPATH", "")
                    env["PYTHONPATH"] = os.pathsep.join(
                        value for value in (str(blocker), str(ROOT / "scripts"), existing) if value
                    )
                    completed = subprocess.run(
                        [
                            sys.executable,
                            str(ROOT / "scripts" / "rag_chunker.py"),
                            str(FIXTURES / fixture_name),
                            "-o",
                            str(output),
                            "--require-original-binary",
                            "--json",
                        ],
                        cwd=ROOT,
                        env=env,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True,
                        encoding="utf-8",
                        errors="replace",
                        check=False,
                        timeout=180,
                    )
                    self.assertEqual(completed.returncode, 2, completed.stdout + completed.stderr)
                    summary = json.loads(completed.stdout)
                    source = summary["sources"][0]
                    self.assertEqual(source["status"], "partial_success")
                    self.assertEqual(source["chunk_count"], 0)
                    self.assertEqual(source["coverage"]["visual"]["coverage_ratio"], 0.0)
                    source_dir = only_source_dir(output)
                    failures = load_jsonl(source_dir / "failed-items.jsonl")
                    self.assertEqual(len(failures), 3)
                    self.assertTrue(all(item["required"] for item in failures))


    def test_output_validator_rejects_swapped_docx_block_order(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.docx", temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            chunks_path = source_dir / "chunks.jsonl"
            records = load_jsonl(chunks_path)
            source_block_ids = records[0]["source_block_ids"]
            self.assertGreaterEqual(len(source_block_ids), 3)
            source_block_ids[1], source_block_ids[2] = source_block_ids[2], source_block_ids[1]
            chunks_path.write_text(
                "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
                encoding="utf-8",
            )
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
            result = json.loads(completed.stdout)
            reasons = {error.get("reason") for error in result.get("errors", [])}
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("chunk_reading_order_mismatch", reasons)

    def test_output_validator_rejects_swapped_pdf_block_order(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.pdf", temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            chunks_path = source_dir / "chunks.jsonl"
            records = load_jsonl(chunks_path)
            source_block_ids = records[0]["source_block_ids"]
            self.assertGreaterEqual(len(source_block_ids), 3)
            source_block_ids[1], source_block_ids[2] = source_block_ids[2], source_block_ids[1]
            chunks_path.write_text(
                "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
                encoding="utf-8",
            )
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
            result = json.loads(completed.stdout)
            reasons = {error.get("reason") for error in result.get("errors", [])}
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("chunk_reading_order_mismatch", reasons)

    def test_output_validator_rejects_wrong_pdf_visual_heading(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.pdf", temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            ir_path = source_dir / "document-ir.jsonl"
            records = load_jsonl(ir_path)
            vocabulary = next(record for record in records if record.get("text") == "影片單字")
            qr = next(record for record in records if record.get("content_origin") == "qr_decoder")
            qr["metadata"]["associated_heading_block_id"] = vocabulary["block_id"]
            qr["metadata"]["associated_heading_path"] = vocabulary["heading_path"]
            qr["heading_path"] = vocabulary["heading_path"]
            ir_path.write_text(
                "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
                encoding="utf-8",
            )
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
            result = json.loads(completed.stdout)
            reasons = {error.get("reason") for error in result.get("errors", [])}
            self.assertNotEqual(completed.returncode, 0)
            self.assertIn("visual_heading_relation_mismatch", reasons)

    def test_docx_binary_fixture_with_drawingml(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "2025-09-TikTok變成美國版.docx", temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            assert_tiktok_fixture(
                self,
                source_dir,
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
            report = load_json(source_dir / "processing-report.json")
            manifest = load_json(source_dir / "manifest.json")
            self.assertEqual(report["source_metadata"]["fallback"], "drawingml_shape_parser")
            self.assertIn("docx_drawingml_rendering_caution", report["warnings"])
            self.assertTrue(any(step.get("operation") == "ooxml_drawingml_extraction" for step in manifest["provenance"]["derivation_chain"]))

if __name__ == "__main__":
    unittest.main()
