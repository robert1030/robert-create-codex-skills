from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_visual_retrieval import validate_retrieval


class VisualRetrievalSmokeTests(unittest.TestCase):
    def test_nonverbatim_visual_summary_is_retrieved_by_matching_query(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            source = Path(temp_name) / "source"
            source.mkdir()
            (source / "document-ir.jsonl").write_text(
                '{"block_id":"image-001","type":"image","content_origin":"llm_visual_summary","verbatim":false,"metadata":{"reference":"images/view.png","visual_summary_evidence":{"review_method":"native_visual_nonverbatim"}}}\n',
                encoding="utf-8",
            )
            (source / "chunks.jsonl").write_text(
                '{"chunk_id":"chunk-001","text":"Window Show View pop-out menu selects an available iTest view.","source_block_ids":["image-001"]}\n',
                encoding="utf-8",
            )
            errors, results = validate_retrieval(Path(temp_name), [{
                "id": "show-view",
                "query": "Show View menu available iTest view",
                "expected_reference": "images/view.png",
                "top_k": 1,
            }])
            self.assertEqual(errors, [])
            self.assertTrue(results[0]["returned"])


if __name__ == "__main__":
    unittest.main()
