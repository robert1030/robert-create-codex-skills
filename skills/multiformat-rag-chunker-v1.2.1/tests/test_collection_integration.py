from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_collection import validate_collection_output
from helpers import run_cli


class CollectionIntegrationTests(unittest.TestCase):
    def _write(self, root: Path, relative: str, content: str) -> None:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def test_generic_collection_preserves_aliases_bare_text_and_relationships(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            self._write(root, "docs/start.html", """<html><head><title>Start</title></head><body><h1>Start</h1>Unwrapped introduction text.<br><a href=\"details.htm#section\">Details</a><span>&nbsp;</span></body></html>""")
            details = """<html><body><h1>Details</h1><p id=\"section\">Verified details.</p></body></html>"""
            self._write(root, "docs/details.htm", details)
            self._write(root, "docs/alias.htm", details)
            self._write(root, "meta/catalog.xml", """<guide><title>Catalog</title><description>Linked document catalog.</description><entry target=\"../docs/details.htm#section\">Details record.</entry></guide>""")

            code, summary = run_cli(root, output)
            self.assertEqual(code, 0, summary)
            self.assertEqual(summary["source_count"], 4)
            self.assertEqual(summary["duplicate_source_count"], 1)
            self.assertEqual(summary["collections"][0]["profile"], "linked_markup_collection")
            report_path = Path(summary["collections"][0]["report"])
            report = json.loads(report_path.read_text(encoding="utf-8"))
            self.assertTrue(report["gate"]["passed"])
            self.assertEqual(report["metrics"]["relationship_occurrence_accounting_ratio"], 1.0)
            start_result = next(result for result in summary["sources"] if result["collection_member_path"] == "docs/start.html")
            normalized = (Path(start_result["output_dir"]) / "normalized-document.md").read_text(encoding="utf-8")
            self.assertIn("Unwrapped introduction text.", normalized)
            validation_code, validation = validate_collection_output(root, output)
            self.assertEqual(validation_code, 0, validation)

    def test_verified_eclipse_profile_uses_control_hierarchy_without_merging_documents(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            self._write(root, "toc.xml", """<?xml version=\"1.0\"?><!DOCTYPE toc><?NLS TYPE=\"org.eclipse.help.toc\"?><toc xmlns=\"urn:Eclipse-TOC-Schema\"><topic label=\"Guide\"><topic label=\"Topic\" href=\"topics/topic.htm#main\"/></topic></toc>""")
            self._write(root, "contexts.xml", """<contexts><context href=\"topics/topic.htm#main\"/></contexts>""")
            self._write(root, "index.xml", """<index><entry href=\"topics/topic.htm#main\">Topic index</entry></index>""")
            self._write(root, "topics/topic.htm", """<html><body><h1>Topic</h1><p id=\"main\">Topic body.</p></body></html>""")
            self._write(root, "topics/picture.png", "not-an-independent-source")

            code, summary = run_cli(root, output)
            self.assertEqual(code, 0, summary)
            self.assertEqual(summary["source_count"], 1)
            collection = summary["collections"][0]
            self.assertEqual(collection["profile"], "eclipse_help_collection")
            report = json.loads(Path(collection["report"]).read_text(encoding="utf-8"))
            picture = next(member for member in report["members"] if member["relative_path"] == "topics/picture.png")
            self.assertEqual(picture["category"], "resource")
            source_dir = Path(summary["sources"][0]["output_dir"])
            ir = [json.loads(line) for line in (source_dir / "document-ir.jsonl").read_text(encoding="utf-8").splitlines() if line]
            self.assertEqual(ir[0]["heading_path"], ["Guide", "Topic"])
            validation_code, validation = validate_collection_output(root, output)
            self.assertEqual(validation_code, 0, validation)

    def test_declared_missing_target_is_partial_not_silent(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            self._write(root, "start.html", """<html><body><h1>Start</h1><p>Known content.</p><a href=\"missing.htm\">Missing</a></body></html>""")
            code, summary = run_cli(root, output)
            self.assertEqual(code, 2, summary)
            report = json.loads(Path(summary["collections"][0]["report"]).read_text(encoding="utf-8"))
            self.assertEqual(report["relationship_summary"]["source_missing_target"], 1)
            self.assertEqual(report["status"], "partial_success")
            validation_code, validation = validate_collection_output(root, output)
            self.assertEqual(validation_code, 2, validation)

    def test_internal_relationship_evidence_is_recomputed_by_validator(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            alias = """<html><body><h1>Alias source</h1><a href=\"../assets/item.bin\">Asset</a></body></html>"""
            self._write(root, "popups/alias.html", alias)
            self._write(root, "topics/popups/alias.html", alias)
            self._write(root, "assets/item.bin", "original package resource")
            self._write(root, "docs/reference.htm", """<html><body><h1>Reference</h1><a href=\"obsolete.htm#section\" title=\"Current topic\">Current topic</a></body></html>""")
            self._write(root, "docs/current.htm", """<html><head><title>Current topic</title></head><body><h1>Current topic</h1><a name=\"section\">Verified content.</a></body></html>""")

            code, summary = run_cli(root, output)
            self.assertEqual(code, 0, summary)
            relationships = []
            for source in summary["sources"]:
                source_report = json.loads((Path(source["output_dir"]) / "processing-report.json").read_text(encoding="utf-8"))
                relationships.extend(source_report["source_metadata"].get("relationships", []))
            strategies = {record["strategy"] for record in relationships}
            self.assertIn("equivalent_source_alias", strategies)
            self.assertIn("semantic_fragment_title", strategies)
            evidence = [record.get("evidence", {}) for record in relationships]
            self.assertIn("identical_source_member", {item.get("evidence_kind") for item in evidence})
            self.assertIn("unique_fragment_and_title", {item.get("evidence_kind") for item in evidence})

            validation_code, validation = validate_collection_output(root, output)
            self.assertEqual(validation_code, 0, validation)

    def test_xml_param_path_relationship_is_independently_recomputed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            self._write(root, "docs/target.htm", """<html><body><h1>Target</h1><p>Verified target content.</p></body></html>""")
            self._write(root, "guides/guide.xml", """<guide><title>Guide</title><description>XML relationship coverage.</description><entry target="../docs/target.htm">Standard target relationship.</entry><param name="path" value="../docs/target.htm"/><param name="mode" value="../docs/must-not-be-a-relationship.htm"/></guide>""")

            code, summary = run_cli(root, output)
            self.assertEqual(code, 0, summary)
            guide_result = next(result for result in summary["sources"] if result["collection_member_path"] == "guides/guide.xml")
            guide_report = json.loads((Path(guide_result["output_dir"]) / "processing-report.json").read_text(encoding="utf-8"))
            relationships = guide_report["source_metadata"]["relationships"]
            self.assertEqual(
                [(record["relationship_type"], record["raw_reference"]) for record in relationships],
                [
                    ("xml_entry_target", "../docs/target.htm"),
                    ("xml_param_value", "../docs/target.htm"),
                ],
            )

            validation_code, validation = validate_collection_output(root, output)
            self.assertEqual(validation_code, 0, validation)

    def test_collection_xml_resources_are_structurally_classified_without_path_rules(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            self._write(root, "content/guide.xml", """<guide><!-- authored note --><title>Guide</title><description>Human-readable collection guidance.</description></guide>""")
            self._write(root, "content/plain.xml", """<records><value>Readable non-critical collection status.</value></records>""")
            self._write(root, "support/mapping.xml", """<mapping><entry key=\"alpha\" value=\"beta\" /></mapping>""")
            self._write(root, "support/locale-data.xml", """<Locales><StopWords>a about after all also am an and another any are as at be</StopWords></Locales>""")

            code, summary = run_cli(root, output)
            self.assertEqual(code, 0, summary)
            self.assertEqual(summary["source_count"], 2)
            report = json.loads(Path(summary["collections"][0]["report"]).read_text(encoding="utf-8"))
            mapping = next(member for member in report["members"] if member["relative_path"] == "support/mapping.xml")
            self.assertEqual(mapping["category"], "resource")
            locales = next(member for member in report["members"] if member["relative_path"] == "support/locale-data.xml")
            self.assertEqual(locales["category"], "resource")
            plain = next(result for result in summary["sources"] if result["collection_member_path"] == "content/plain.xml")
            plain_report = json.loads((Path(plain["output_dir"]) / "processing-report.json").read_text(encoding="utf-8"))
            self.assertEqual(plain_report["chunk_pre_validation"]["critical_metric_status"], "not_applicable")
            self.assertEqual(plain_report["final_status"], "success")

    def test_collection_member_source_ids_remain_distinct_after_display_slug_truncation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name) / "source"
            output = Path(temp_name) / "output"
            long_parent = "/".join(["shared-long-member-path"] * 12)
            self._write(root, f"{long_parent}/reports_filenames_document.xml", """<guide><title>First</title><description>First authored document.</description></guide>""")
            self._write(root, f"{long_parent}/reports_images_document.xml", """<guide><title>Second</title><description>Second authored document.</description></guide>""")

            code, summary = run_cli(root, output)
            self.assertEqual(code, 0, summary)
            self.assertEqual(summary["source_count"], 2)
            source_ids = {result["source_id"] for result in summary["sources"]}
            output_dirs = {result["output_dir"] for result in summary["sources"]}
            self.assertEqual(len(source_ids), 2)
            self.assertEqual(len(output_dirs), 2)


if __name__ == "__main__":
    unittest.main()
