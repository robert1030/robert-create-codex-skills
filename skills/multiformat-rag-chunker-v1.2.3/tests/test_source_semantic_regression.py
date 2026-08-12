from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from ocr import _content_consistency, _obvious_ocr_garbage
from source_semantics import audit_source_semantics, observed_semantic_units
from validate_collection import validate_collection_output
from helpers import only_source_dir, run_cli


CHEATSHEET = """<?xml version="1.0" encoding="UTF-8"?>
<compositeCheatsheet name="Follow these steps to become an iTest Rock Star">
  <taskGroup name="iTest Skills: Follow each of these cheat sheets in order">
    <task name="1. Create a robust session profile for connecting to a device"><intro>Introduction</intro></task>
    <task name="2. Capture and document a manual test"><intro>Introduction</intro></task>
    <task name="3. Create an automated test case from captured sessions"><intro>Introduction</intro></task>
    <task name="4. Find the session or file that you are looking for"><intro>Introduction</intro></task>
    <task name="5. Restore the iTest layout to its original state"><intro>Introduction</intro></task>
    <task name="6. Run a test case and review the resulting report"><intro>Introduction</intro></task>
    <task name="7. Troubleshoot a test case that hangs during execution"><intro>Introduction</intro></task>
    <task name="8. Check for a string in a response"><intro>Introduction</intro></task>
    <task name="9. Compare a field to an expected value"><intro>Introduction</intro></task>
    <task name="10. Add a loop to a test case"><intro>Introduction</intro></task>
    <task name="11. Add a parameter into a command"><intro>Introduction</intro></task>
  </taskGroup>
</compositeCheatsheet>
"""


NONSTANDARD_HTML = """<html><body>
<h1>Command reference</h1>
<ul>
  <p><b>[info status]</b> Returns Pass, Fail, or Indeterminate.</p>
  <b>file uriToPath</b> <em>URI</em><br>Returns the full operating system path for the specified URI.
</ul>
<table><caption>Yes: Parameter is defined in command line; No: Parameter is not defined.</caption>
<tr><th>Option</th><th>Available</th></tr><tr><td>--example</td><td>Yes</td></tr></table>
</body></html>
"""


UNCLOSED_PARAGRAPH_LIST_HTML = """<html><body><ul>
<p><b>[info homeDir]</b> Returns the home directory.
<p><b>[info hostIp]</b> Returns the host IP address.</p>
</body></html>"""


class SourceSemanticRegressionTests(unittest.TestCase):
    def test_cheatsheet_titles_and_steps_are_rendered_in_source_order(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "getting_started_with_itest.xml"
            source.write_text(CHEATSHEET, encoding="utf-8")
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            normalized = (source_dir / "normalized-document.md").read_text(encoding="utf-8")
            self.assertIn("Follow these steps to become an iTest Rock Star", normalized)
            steps = [f"{index}." for index in range(1, 12)]
            positions = [normalized.index(step) for step in steps]
            self.assertEqual(positions, sorted(positions))
            report = json.loads((source_dir / "processing-report.json").read_text(encoding="utf-8"))
            audit = report["source_metadata"]["source_semantic_audit"]
            self.assertEqual(audit["expected_total"], 13)
            self.assertEqual(audit["verified_total"], 13)
            self.assertEqual(audit["critical_coverage_ratio"], 1.0)

    def test_nonstandard_list_content_and_caption_are_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "commands.html"
            source.write_text(NONSTANDARD_HTML, encoding="utf-8")
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            normalized = (source_dir / "normalized-document.md").read_text(encoding="utf-8")
            self.assertIn("[info status] Returns Pass, Fail, or Indeterminate.", normalized)
            self.assertIn("file uriToPath", normalized)
            self.assertIn("Returns the full operating system path for the specified URI.", normalized)
            self.assertIn("Yes: Parameter is defined in command line; No: Parameter is not defined.", normalized)
            records = [json.loads(line) for line in (source_dir / "document-ir.jsonl").read_text(encoding="utf-8").splitlines() if line]
            table = next(record for record in records if record["type"] == "table")
            self.assertEqual(table["metadata"]["caption"], "Yes: Parameter is defined in command line; No: Parameter is not defined.")
            audit = json.loads((source_dir / "processing-report.json").read_text(encoding="utf-8"))["source_metadata"]["source_semantic_audit"]
            self.assertEqual(audit["status"], "passed")
            self.assertEqual(audit["by_kind"]["html_nonstandard_list_content"]["verified"], 4)
            self.assertEqual(audit["by_kind"]["table_caption"]["verified"], 1)

    def test_raw_semantic_audit_rejects_the_previous_xml_drop(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            source = Path(temp_name) / "First.xml"
            source.write_text("""<cheatsheet title="Mapping a response"><item title="Create a response map"><description>Introduction</description></item></cheatsheet>""", encoding="utf-8")
            audit = audit_source_semantics(source, observed_semantic_units([], "Introduction"))
            self.assertEqual(audit["status"], "failed")
            self.assertEqual(audit["critical_expected_total"], 2)
            self.assertEqual(audit["critical_verified_total"], 0)

    def test_unclosed_html_paragraphs_are_audited_as_distinct_list_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source = temp / "info.html"
            source.write_text(UNCLOSED_PARAGRAPH_LIST_HTML, encoding="utf-8")
            code, summary = run_cli(source, temp / "output")
            self.assertEqual(code, 0, summary)
            source_dir = only_source_dir(temp / "output")
            audit = json.loads((source_dir / "processing-report.json").read_text(encoding="utf-8"))["source_metadata"]["source_semantic_audit"]
            self.assertEqual(audit["status"], "passed")
            self.assertEqual(audit["by_kind"]["html_nonstandard_list_content"], {"expected": 2, "verified": 2})

    def test_collection_validator_recomputes_raw_semantic_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            source_root = temp / "source"
            source_root.mkdir()
            (source_root / "guide.xml").write_text(CHEATSHEET, encoding="utf-8")
            output = temp / "output"
            code, summary = run_cli(source_root, output)
            self.assertEqual(code, 0, summary)
            source_dir = Path(summary["sources"][0]["output_dir"])
            (source_dir / "normalized-document.md").write_text("Introduction\n", encoding="utf-8")
            (source_dir / "document-ir.jsonl").write_text("", encoding="utf-8")
            validation_code, validation = validate_collection_output(source_root, output)
            self.assertEqual(validation_code, 1, validation)
            reasons = {error.get("reason") for error in validation["errors"]}
            self.assertIn("source_semantic_content_missing", reasons)

    def test_ocr_garbage_requires_multiple_signals_not_confidence_alone(self) -> None:
        garbage = _content_consistency('“" _Geeatons])\netme,')
        self.assertTrue(_obvious_ocr_garbage(garbage, 8.67))
        plain_text = _content_consistency("info status")
        self.assertFalse(_obvious_ocr_garbage(plain_text, 8.67))


if __name__ == "__main__":
    unittest.main()
