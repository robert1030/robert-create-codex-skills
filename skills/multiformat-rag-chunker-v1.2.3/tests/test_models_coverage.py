from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from coverage import evaluate_source_coverage
from models import Block, DocumentIR, Location, Provenance
from normalize import normalize_block, normalize_document_blocks
from output import failure_records
from utils import common_heading_path


def provenance(*, snapshot: bool = False) -> Provenance:
    return Provenance(
        source_id="source-001",
        user_specified_name="example.pdf",
        original_upload_name="example.pdf",
        runtime_path="/tmp/example.pdf",
        extension=".pdf",
        requested_media_type="application/pdf",
        runtime_media_type="text/markdown" if snapshot else "application/pdf",
        magic_bytes="25504446",
        sha256="a" * 64,
        actual_adapter="pdf_adapter",
        original_binary_processed=not snapshot,
        derived_snapshot=snapshot,
        input_fidelity="derived_snapshot" if snapshot else "original_binary",
    )


class CoverageGateTests(unittest.TestCase):
    def test_validated_dense_visual_text_is_not_demoted_as_repeated_header(self) -> None:
        blocks = [
            Block(
                f"source-001-block-{page:03d}",
                "heading",
                "Chapter 1 Shared page heading",
                Location(page=page),
                content_origin="llm_visual_text",
                required=True,
                status="success",
                verbatim=False,
                metadata={
                    "dense_text_required": True,
                    "visual_text_unit_id": f"p{page:03d}-u001",
                },
            )
            for page in (1, 2)
        ]

        normalized = normalize_document_blocks(blocks)

        self.assertTrue(all(block.required for block in normalized))
        self.assertTrue(all(block.status == "success" for block in normalized))
        self.assertTrue(all("skip_reason" not in block.metadata for block in normalized))

    def test_validated_dense_visual_text_same_page_duplicates_remain_distinct_units(self) -> None:
        blocks = [
            Block(
                f"source-001-block-{index:03d}",
                "paragraph",
                "Repeated but independently validated dense text",
                Location(page=1),
                content_origin="llm_visual_text",
                required=True,
                status="success",
                verbatim=False,
                metadata={
                    "dense_text_required": True,
                    "visual_text_unit_id": f"p001-u{index:03d}",
                },
            )
            for index in (1, 2)
        ]

        normalized = normalize_document_blocks(blocks)

        self.assertTrue(all(block.required for block in normalized))
        self.assertTrue(all(block.status == "success" for block in normalized))

    def test_native_text_repeated_headers_are_still_removed(self) -> None:
        blocks = [
            Block(
                f"source-001-block-{page:03d}",
                "heading",
                "Repeated native page heading",
                Location(page=page),
            )
            for page in (1, 2)
        ]

        normalized = normalize_document_blocks(blocks)

        self.assertTrue(all(not block.required for block in normalized))
        self.assertTrue(all(block.status == "skipped" for block in normalized))
        self.assertTrue(all(block.metadata.get("skip_reason") == "repeated_header" for block in normalized))

    def test_common_heading_path_uses_longest_shared_prefix(self) -> None:
        paths = [
            ["Document", "Vocabulary"],
            ["Document", "English paragraphs"],
            ["Document"],
        ]
        self.assertEqual(common_heading_path(paths, ["Fallback"]), ["Document"])
        self.assertEqual(common_heading_path([], ["Fallback"]), ["Fallback"])

    def test_table_definition_whitespace_is_normalized_without_touching_ipa_or_url(self) -> None:
        block = Block(
            "source-001-block-001",
            "table",
            "",
            metadata={
                "header": ["編號", "單字", "IPA", "詞性與中文定義"],
                "rows": [
                    ["1", "content", "/ˈkɑn.tɛnt/ (n)", "n. 內容；滿足   /  adj. 滿足的"],
                    ["2", "link", "", "https://example.com/a/b"],
                ],
            },
        )
        normalized = normalize_block(block)
        self.assertEqual(normalized.metadata["rows"][0][2], "/ˈkɑn.tɛnt/ (n)")
        self.assertEqual(normalized.metadata["rows"][0][3], "n. 內容；滿足 / adj. 滿足的")
        self.assertEqual(normalized.metadata["rows"][1][3], "https://example.com/a/b")
        self.assertIn("table_general_text_whitespace_normalized", normalized.transformation_summary)

    def test_removed_page_footer_is_auditable_but_not_required_content(self) -> None:
        block = Block(
            "source-001-block-001",
            "paragraph",
            "page\u00a0301",
            Location(page=301),
            ["Title"],
            required=True,
            metadata={"collection_occurrence": {"source_member": "topics/example.htm", "source_order": 1}},
        )
        normalized = normalize_block(block)
        self.assertEqual(normalized.raw_text, "page\u00a0301")
        self.assertEqual(normalized.text, "")
        self.assertFalse(normalized.required)
        self.assertEqual(normalized.status, "skipped")
        self.assertEqual(normalized.metadata["skip_reason"], "normalization_only_noise")
        self.assertIn("page_footer_removed", normalized.transformation_summary)

    def test_zero_over_zero_is_not_applicable(self) -> None:
        blocks = [
            Block("source-001-block-001", "heading", "Title", Location(page=1), ["Title"], critical=True),
            Block("source-001-block-002", "paragraph", "Body text.", Location(page=1), ["Title"]),
        ]
        document = DocumentIR("source-001", "Title", provenance(), blocks)
        metrics = evaluate_source_coverage(document, "# Title\n\nBody text.\n")
        self.assertIsNone(metrics["visual"]["coverage_ratio"])
        self.assertEqual(metrics["visual"]["metric_status"], "not_applicable")
        self.assertEqual(metrics["content_completeness_status"], "success")

    def test_critical_failure_is_fatal(self) -> None:
        blocks = [
            Block("source-001-block-001", "heading", "Title", Location(page=1), ["Title"], critical=True),
            Block(
                "source-001-block-002",
                "table",
                "",
                Location(page=1),
                ["Title"],
                content_origin="placeholder",
                required=True,
                critical=True,
                status="failed",
                verbatim=False,
                metadata={"reason": "table_unreadable"},
            ),
        ]
        document = DocumentIR("source-001", "Title", provenance(), blocks)
        markdown = "# Title\n\n> [內容擷取未完成]\n>\n> - 單元：source-001-block-002\n"
        metrics = evaluate_source_coverage(document, markdown)
        self.assertEqual(metrics["content_completeness_status"], "fatal_error")
        self.assertIn("critical_content_incomplete", metrics["fatal_reasons"])


    def test_unresolved_required_visual_is_partial(self) -> None:
        blocks = [
            Block("source-001-block-001", "heading", "Title", Location(page=1), ["Title"], required=True, critical=True),
            Block("source-001-block-002", "paragraph", "Body text.", Location(page=1), ["Title"], required=True),
            Block(
                "source-001-block-003",
                "image",
                "",
                Location(page=1, asset_id="image-001"),
                ["Title"],
                content_origin="placeholder",
                required=True,
                critical=False,
                status="failed",
                verbatim=False,
                metadata={"visual_class": "unknown", "error": "No module named 'cv2'"},
            ),
        ]
        document = DocumentIR("source-001", "Title", provenance(), blocks)
        markdown = "# Title\n\nBody text.\n\n> [內容擷取未完成]\n>\n> - 單元：source-001-block-003\n"
        metrics = evaluate_source_coverage(document, markdown)
        self.assertEqual(metrics["content_completeness_status"], "partial_success")
        self.assertEqual(metrics["visual"]["coverage_ratio"], 0.0)
        self.assertIn("required_content_coverage_below_0.95", metrics["partial_reasons"])
        self.assertIn("needs_capability", metrics["partial_reasons"])

    def test_missing_runtime_capability_is_recorded_without_new_status(self) -> None:
        blocks = [
            Block(
                "source-001-block-001",
                "placeholder",
                "",
                Location(),
                ["Title"],
                content_origin="placeholder",
                required=True,
                critical=True,
                status="failed",
                verbatim=False,
                metadata={"reason": "libreoffice_not_available_for_doc_conversion"},
            ),
        ]
        document = DocumentIR("source-001", "Title", provenance(), blocks)
        metrics = evaluate_source_coverage(document, "> [內容擷取未完成]\n")
        self.assertEqual(metrics["content_completeness_status"], "fatal_error")
        self.assertIn("needs_capability", metrics["fatal_reasons"])
        failure = failure_records(document)[0]
        self.assertEqual(failure.failure_reason, "needs_capability")
        self.assertEqual(
            failure.details["next_action"],
            "agent_evaluate_safe_capability_fulfillment_or_equivalent",
        )
        self.assertEqual(
            failure.details["observed_failure_reason"],
            "libreoffice_not_available_for_doc_conversion",
        )

    def test_snapshot_is_partial_or_fatal_when_required(self) -> None:
        blocks = [
            Block("source-001-block-001", "heading", "Title", Location(), ["Title"], critical=True),
            Block("source-001-block-002", "paragraph", "Body text.", Location(), ["Title"]),
        ]
        document = DocumentIR("source-001", "Title", provenance(snapshot=True), blocks)
        partial = evaluate_source_coverage(document, "# Title\n\nBody text.\n")
        fatal = evaluate_source_coverage(document, "# Title\n\nBody text.\n", require_original_binary=True)
        self.assertEqual(partial["content_completeness_status"], "partial_success")
        self.assertEqual(fatal["content_completeness_status"], "fatal_error")


if __name__ == "__main__":
    unittest.main()
