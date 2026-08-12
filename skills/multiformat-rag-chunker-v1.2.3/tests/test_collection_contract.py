from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection import (
    ECLIPSE_HELP_COLLECTION,
    LINKED_MARKUP_COLLECTION,
    CollectionMember,
    build_collection_inventory,
    select_collection_profile,
)
from relationship_resolver import resolve_relationship
from validate_collection import validate_collection_metrics


class CollectionContractTests(unittest.TestCase):
    def test_generic_linked_markup_does_not_assume_a_fixture_profile(self) -> None:
        profile = select_collection_profile(("docs/start.html", "meta/catalog.xml"))
        self.assertEqual(profile.name, LINKED_MARKUP_COLLECTION)
        self.assertFalse(profile.requires_control_documents)

    def test_specialised_profile_requires_controls_and_signature(self) -> None:
        members = ("toc.xml", "contexts.xml", "index.xml", "topics/start.htm")
        without_signature = select_collection_profile(members)
        self.assertEqual(without_signature.name, LINKED_MARKUP_COLLECTION)
        with_signature = select_collection_profile(members, markers={"eclipse_help_signature": True})
        self.assertEqual(with_signature.name, ECLIPSE_HELP_COLLECTION)

    def test_inventory_preserves_alias_virtual_base_paths(self) -> None:
        inventory = build_collection_inventory(
            "fixture",
            (
                CollectionMember("a/topic.htm", "same", "a"),
                CollectionMember("b/topic.htm", "same", "b", canonical_member="a/topic.htm"),
            ),
        )
        self.assertEqual(inventory.alias_count, 1)
        self.assertEqual(inventory.members[1].virtual_base_path, "b")

    def test_relationship_resolver_preserves_help_and_htm_fallback(self) -> None:
        available = {"topics/command.htm", "images/example.png"}
        help_result = resolve_relationship(
            "popups/command.html",
            "help::/vendor.bundle/topics/command.html#details",
            available,
        )
        self.assertEqual(help_result.status, "resolved")
        self.assertEqual(help_result.target_member, "topics/command.htm")
        self.assertEqual(help_result.fragment, "details")
        image_result = resolve_relationship("popups/command.html", "../images/example.png", available)
        self.assertEqual(image_result.status, "resolved")
        self.assertEqual(image_result.target_member, "images/example.png")

    def test_source_missing_and_external_references_remain_explicit(self) -> None:
        available = {"topics/command.htm"}
        missing = resolve_relationship("topics/command.htm", "missing.htm", available)
        external = resolve_relationship("topics/command.htm", "https://example.test/help", available)
        external_help = resolve_relationship(
            "topics/command.htm",
            "help::/other.docs.bundle/topics/not-in-this-archive.htm",
            available,
        )
        bare_email = resolve_relationship("topics/command.htm", "help@example.test", available)
        self.assertEqual(missing.status, "source_missing_target")
        self.assertEqual(external.status, "external")
        self.assertEqual(external_help.status, "external")
        self.assertEqual(external_help.strategy, "help_external_bundle")
        self.assertEqual(bare_email.status, "external")

    def test_collection_gate_rejects_missing_metrics_and_hidden_failures(self) -> None:
        missing = validate_collection_metrics({"member_accounting_ratio": 1.0})
        self.assertFalse(missing.passed)
        failed = validate_collection_metrics({
            "member_accounting_ratio": 1.0,
            "critical_occurrence_coverage_ratio": 1.0,
            "source_semantic_coverage_ratio": 1.0,
            "source_semantic_critical_coverage_ratio": 1.0,
            "semantic_order_inversion_count": 0,
            "relationship_occurrence_accounting_ratio": 1.0,
            "existing_target_resolution_ratio": 1.0,
            "unreported_relationship_failure_count": 1,
        })
        self.assertFalse(failed.passed)
        passed = validate_collection_metrics({
            "member_accounting_ratio": 1.0,
            "critical_occurrence_coverage_ratio": 1.0,
            "source_semantic_coverage_ratio": 1.0,
            "source_semantic_critical_coverage_ratio": 1.0,
            "semantic_order_inversion_count": 0,
            "relationship_occurrence_accounting_ratio": 1.0,
            "existing_target_resolution_ratio": 1.0,
            "unreported_relationship_failure_count": 0,
        })
        self.assertTrue(passed.passed)


if __name__ == "__main__":
    unittest.main()
