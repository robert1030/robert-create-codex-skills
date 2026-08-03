from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from helpers import FIXTURES, load_json, load_jsonl, only_source_dir, run_cli


def _has_tesseract_languages() -> bool:
    executable = shutil.which("tesseract")
    if not executable:
        return False
    completed = subprocess.run(
        [executable, "--list-langs"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        timeout=30,
    )
    return completed.returncode == 0 and {"chi_tra", "chi_sim", "eng"}.issubset(set(completed.stdout.split()))


class SmallFormatIntegrationTests(unittest.TestCase):
    def test_markdown_html_xml_csv_and_qr_are_isolated(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "inputs"
            source.mkdir()
            for name in ("sample.md", "sample.html", "sample.xml", "sample.csv", "qr.png"):
                shutil.copy2(FIXTURES / name, source / name)
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            self.assertEqual(summary["status"], "success")
            self.assertEqual(summary["source_count"], 5)
            output_dirs = [path for path in (temp / "output").iterdir() if path.is_dir()]
            self.assertEqual(len(output_dirs), 5)
            for output_dir in output_dirs:
                report = load_json(output_dir / "processing-report.json")
                self.assertEqual(report["final_status"], "success")
                self.assertEqual(report["chunk_post_validation"]["chunk_block_mapping_ratio"], 1.0)
                self.assertTrue((output_dir / "normalized-document.md").read_text(encoding="utf-8").strip())
            qr_dir = next(path for path in output_dirs if path.name.startswith("qr.png"))
            self.assertIn("https://example.test/rag-fixture", (qr_dir / "normalized-document.md").read_text(encoding="utf-8"))

    def test_scanned_pdf_uses_ocr_and_preserves_text(self) -> None:
        if not _has_tesseract_languages():
            self.skipTest("optional_tool_lane_requires_tesseract_languages")
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "scanned.pdf", temp / "output", "--forensic")
            self.assertIn(code, (0, 2), summary)
            source_dir = only_source_dir(temp / "output")
            normalized = (source_dir / "normalized-document.md").read_text(encoding="utf-8")
            ir = load_jsonl(source_dir / "document-ir.jsonl")
            self.assertIn("SCANNED OCR FIXTURE 2026", normalized)
            self.assertTrue(any(record.get("content_origin") == "ocr" for record in ir))
            forensic = source_dir / "forensic"
            self.assertTrue((forensic / "source-assets" / "scanned.pdf").is_file())
            self.assertTrue((forensic / "rendered-pages" / "page-001.png").is_file())
            self.assertTrue(any((forensic / "preprocessed").glob("*.png")))
            self.assertTrue(any((forensic / "ocr-candidates").glob("*.txt")))
            self.assertTrue((forensic / "debug-report.json").is_file())

    def test_no_audio_video_never_claims_success(self) -> None:
        if not shutil.which("ffprobe"):
            self.skipTest("optional_tool_lane_requires_ffprobe")
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            code, summary = run_cli(FIXTURES / "no-audio.mp4", temp / "output")
            self.assertIn(code, (1, 2), summary)
            self.assertIn(summary["status"], {"fatal_error", "partial_success"})
            source_dir = only_source_dir(temp / "output")
            failed = load_jsonl(source_dir / "failed-items.jsonl")
            self.assertTrue(any("no_audio_stream" in item.get("failure_reason", "") for item in failed))


if __name__ == "__main__":
    unittest.main()
