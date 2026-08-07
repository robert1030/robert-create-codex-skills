from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def run_json(self, script: str, *arguments: str) -> dict:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / script), *arguments],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        return json.loads(completed.stdout)

    def test_frozen_identity(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        source = json.loads((ROOT / "knowledge" / "source-manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["name"], "itest-help")
        self.assertEqual(manifest["product_version"], "26.2.0")
        self.assertEqual(source["original_source"]["member_hash_mismatch_count"], 0)
        self.assertTrue(source["validation"]["collection_gate_passed"])

    def test_search_and_inspection_share_citation_fields(self) -> None:
        response = self.run_json("search_itest_help.py", "Tcl Test Step", "--limit", "1")
        self.assertEqual(response["status"], "ok")
        result = response["results"][0]
        detail = self.run_json("inspect_chunk.py", result["chunk_id"])
        self.assertEqual(detail["status"], "ok")
        for field in ("chunk_id", "source_file", "document_version", "source_sha256", "content_sha256"):
            self.assertEqual(result[field], detail["record"][field])

    def test_search_reports_no_results_without_invention(self) -> None:
        response = self.run_json("search_itest_help.py", "zqjxwpyv")
        self.assertEqual(response["status"], "no_results")
        self.assertEqual(response["results"], [])

    def test_bootstrap_is_explicitly_dependency_free(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "bootstrap.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        self.assertEqual(completed.returncode, 0)
        self.assertIn("不需要安裝額外相依套件", completed.stdout)


if __name__ == "__main__":
    unittest.main()
