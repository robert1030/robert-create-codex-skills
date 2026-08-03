from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from chunker import validate_chunk_mapping
from models import Block, Chunk, DocumentIR, Location, Provenance
from utils import sha256_text


def provenance() -> Provenance:
    return Provenance(
        source_id="source-001",
        user_specified_name="example.docx",
        original_upload_name="example.docx",
        runtime_path="/tmp/example.docx",
        extension=".docx",
        requested_media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        runtime_media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        magic_bytes="504b0304",
        sha256="a" * 64,
        actual_adapter="docx_adapter",
        original_binary_processed=True,
        derived_snapshot=False,
        input_fidelity="original_binary",
    )


def document() -> DocumentIR:
    title = Block(
        "source-001-block-001",
        "heading",
        "Document title",
        Location(page=1, element_index=1),
        ["Document title"],
        critical=True,
        metadata={
            "level": 1,
            "semantic_role": "document_title",
            "source_order": 1,
        },
    )
    paragraph = Block(
        "source-001-block-002",
        "paragraph",
        "Body text.",
        Location(page=1, element_index=2),
        ["Document title"],
        metadata={
            "source_order": 2,
            "associated_heading_block_id": title.block_id,
        },
    )
    image = Block(
        "source-001-block-003",
        "image",
        "QR Code payload：https://example.com",
        Location(page=1, element_index=3, asset_id="image-001"),
        ["Document title"],
        content_origin="qr_decoder",
        critical=True,
        metadata={
            "source_order": 3,
            "associated_heading_block_id": title.block_id,
            "associated_heading_path": ["Document title"],
            "association_method": "ooxml_container_order",
        },
    )
    return DocumentIR(
        "source-001",
        "Document title",
        provenance(),
        [title, paragraph, image],
        metadata={
            "adapter": "docx_adapter",
            "fallback": "native_ooxml",
            "document_title": "Document title",
            "layout_semantics_status": "reliable",
            "document_title_semantics_status": "reliable",
        },
    )


def chunk(source_block_ids: list[str], normalized_markdown: str) -> Chunk:
    return Chunk(
        chunk_id="source-001-chunk-001",
        source_id="source-001",
        title="Document title",
        heading_path=["Document title"],
        section_titles=["Document title"],
        source_block_ids=source_block_ids,
        overlap_block_ids=[],
        overlap_text="",
        overlap_token_count=0,
        token_estimate=10,
        locators=[{"page": 1}],
        source_hash="a" * 64,
        normalized_document_hash=sha256_text(normalized_markdown),
        content_status="success",
        text="Document title\nBody text.\nQR Code payload：https://example.com",
        markdown_body="# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n",
    )


class ReadingOrderValidationTests(unittest.TestCase):
    def test_exact_source_order_passes(self) -> None:
        doc = document()
        normalized = "# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n"
        result = validate_chunk_mapping(
            doc,
            [chunk([block.block_id for block in doc.blocks], normalized)],
            normalized,
        )
        self.assertEqual(result["chunk_validation_status"], "passed")
        self.assertEqual(result["reading_order_violation_count"], 0)
        self.assertEqual(result["visual_heading_relation_violation_count"], 0)
        self.assertEqual(result["document_title_mismatch_count"], 0)

    def test_swapped_source_block_ids_fail(self) -> None:
        doc = document()
        normalized = "# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n"
        result = validate_chunk_mapping(
            doc,
            [chunk([doc.blocks[0].block_id, doc.blocks[2].block_id, doc.blocks[1].block_id], normalized)],
            normalized,
        )
        self.assertEqual(result["chunk_validation_status"], "failed")
        self.assertGreater(result["reading_order_violation_count"], 0)
        self.assertEqual(
            result["expected_source_block_order"],
            [block.block_id for block in doc.blocks],
        )

    def test_all_source_order_metadata_missing_fails_when_layout_is_reliable(self) -> None:
        doc = document()
        for block in doc.blocks:
            block.metadata.pop("source_order", None)
        normalized = "# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n"
        result = validate_chunk_mapping(
            doc,
            [chunk([block.block_id for block in doc.blocks], normalized)],
            normalized,
        )
        self.assertEqual(result["chunk_validation_status"], "failed")
        self.assertEqual(result["source_order_metadata_violation_count"], len(doc.blocks))

    def test_visual_association_to_wrong_heading_fails(self) -> None:
        doc = document()
        doc.blocks[2].metadata["associated_heading_block_id"] = "source-001-block-999"
        normalized = "# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n"
        result = validate_chunk_mapping(
            doc,
            [chunk([block.block_id for block in doc.blocks], normalized)],
            normalized,
        )
        self.assertEqual(result["chunk_validation_status"], "failed")
        self.assertEqual(result["visual_heading_relation_violation_count"], 1)

    def test_visual_association_path_and_method_are_required(self) -> None:
        doc = document()
        doc.blocks[2].metadata.pop("associated_heading_path")
        doc.blocks[2].metadata.pop("association_method")
        normalized = "# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n"
        result = validate_chunk_mapping(
            doc,
            [chunk([block.block_id for block in doc.blocks], normalized)],
            normalized,
        )
        self.assertEqual(result["chunk_validation_status"], "failed")
        self.assertEqual(result["visual_heading_relation_violation_count"], 2)

    def test_missing_document_title_semantics_fail(self) -> None:
        doc = document()
        doc.blocks[0].metadata.pop("semantic_role")
        normalized = "# Document title\n\nBody text.\n\nQR Code payload：https://example.com\n"
        result = validate_chunk_mapping(
            doc,
            [chunk([block.block_id for block in doc.blocks], normalized)],
            normalized,
        )
        self.assertEqual(result["chunk_validation_status"], "failed")
        self.assertGreater(result["document_title_mismatch_count"], 0)


if __name__ == "__main__":
    unittest.main()
