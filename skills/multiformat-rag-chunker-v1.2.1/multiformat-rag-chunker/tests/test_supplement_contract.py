from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from supplement_manifest import MissingRelationship, expected_target_member, validate_supplement_manifest


BASE_SHA256 = "a" * 64
CONTENT_SHA256 = "b" * 64
ORIGIN_SHA256 = "c" * 64


def _edge(source_member: str, location: str) -> MissingRelationship:
    return MissingRelationship(
        source_member=source_member,
        raw_reference="missing.htm#section",
        relationship_type="html_a_href",
        fragment="section",
        location=location,
    )


def _manifest(edges: list[MissingRelationship], target_member: str = "docs/missing.htm") -> dict[str, object]:
    return {
        "schema_version": "1.0",
        "base": {"collection_sha256": BASE_SHA256},
        "members": [{
            "target_member": target_member,
            "category": "content",
            "content_sha256": CONTENT_SHA256,
            "origin": {"kind": "vendor_release", "artifact_sha256": ORIGIN_SHA256},
            "resolves": [edge.__dict__ for edge in edges],
        }],
    }


class SupplementContractTests(unittest.TestCase):
    def test_one_supplement_member_can_resolve_multiple_original_occurrences(self) -> None:
        first = _edge("docs/first.html", "html:/a[1]")
        second = _edge("docs/second.html", "html:/a[2]")
        result = validate_supplement_manifest(
            _manifest([first, second]),
            base_collection_sha256=BASE_SHA256,
            missing_relationships=[first, second],
        )
        self.assertTrue(result.passed, result.violations)
        self.assertTrue(result.fully_resolves_known_missing)
        self.assertEqual(len(result.resolved_relationships), 2)

    def test_partial_supplement_remains_explicitly_partial(self) -> None:
        first = _edge("docs/first.html", "html:/a[1]")
        second = _edge("docs/second.html", "html:/a[2]")
        result = validate_supplement_manifest(
            _manifest([first]),
            base_collection_sha256=BASE_SHA256,
            missing_relationships=[first, second],
        )
        self.assertTrue(result.passed, result.violations)
        self.assertFalse(result.fully_resolves_known_missing)
        self.assertEqual(result.unresolved_relationships, (second,))

    def test_supplement_rejects_unknown_or_mismatched_targets(self) -> None:
        edge = _edge("docs/first.html", "html:/a[1]")
        unknown = _edge("docs/unknown.html", "html:/a[9]")
        result = validate_supplement_manifest(
            _manifest([unknown]),
            base_collection_sha256=BASE_SHA256,
            missing_relationships=[edge],
        )
        self.assertFalse(result.passed)
        self.assertIn("member_0:edge_not_originally_missing", result.violations)
        mismatch = validate_supplement_manifest(
            _manifest([edge], target_member="other/missing.htm"),
            base_collection_sha256=BASE_SHA256,
            missing_relationships=[edge],
        )
        self.assertFalse(mismatch.passed)
        self.assertIn("member_0:target_member_mismatch", mismatch.violations)

    def test_supplement_rejects_wrong_base_or_bad_provenance_hash(self) -> None:
        edge = _edge("docs/first.html", "html:/a[1]")
        manifest = _manifest([edge])
        manifest["base"] = {"collection_sha256": "d" * 64}
        manifest["members"][0]["origin"]["artifact_sha256"] = "not-a-hash"  # type: ignore[index]
        result = validate_supplement_manifest(
            manifest,
            base_collection_sha256=BASE_SHA256,
            missing_relationships=[edge],
        )
        self.assertFalse(result.passed)
        self.assertIn("base_collection_sha256_mismatch", result.violations)
        self.assertIn("member_0:origin_artifact_sha256_invalid", result.violations)

    def test_target_member_is_derived_from_the_original_relative_reference(self) -> None:
        image = MissingRelationship(
            source_member="topics/popups/scriptget.html",
            raw_reference="../images/scriptget.jpg",
            relationship_type="html_img_src",
            fragment="",
            location="html:/img[1]",
        )
        self.assertEqual(expected_target_member(image), "topics/images/scriptget.jpg")


if __name__ == "__main__":
    unittest.main()
