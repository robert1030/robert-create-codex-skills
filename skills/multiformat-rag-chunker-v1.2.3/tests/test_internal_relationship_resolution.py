from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from collection import build_collection_runtime
from constants import DIRECT_SOURCE_EXTENSIONS, IMAGE_EXTENSIONS
from relationship_resolver import resolve_relationship


class InternalRelationshipResolutionTests(unittest.TestCase):
    def _runtime(self, members: dict[str, bytes]):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name) / "source"
        rows = []
        canonical_by_hash: dict[str, str] = {}
        for relative, data in members.items():
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
            digest = hashlib.sha256(data).hexdigest()
            canonical = canonical_by_hash.get(digest)
            canonical_by_hash.setdefault(digest, relative)
            rows.append((relative, path, digest, canonical))
        return build_collection_runtime(
            "fixture",
            "fixture",
            root,
            rows,
            content_extensions=set(DIRECT_SOURCE_EXTENSIONS),
            image_extensions=set(IMAGE_EXTENSIONS),
        )

    def test_identical_source_alias_can_resolve_same_raw_reference(self) -> None:
        popup = b'<html><body><img src="../images/example.jpg"></body></html>'
        runtime = self._runtime({
            "popups/example.html": popup,
            "topics/popups/example.html": popup,
            "images/example.jpg": b"original-image-bytes",
        })
        result = runtime.resolve_relationship("topics/popups/example.html", "../images/example.jpg")
        self.assertEqual(result.status, "resolved")
        self.assertEqual(result.target_member, "images/example.jpg")
        self.assertEqual(result.strategy, "equivalent_source_alias")
        self.assertEqual(result.evidence["alias_member"], "popups/example.html")
        self.assertEqual(len(result.evidence["alias_sha256"]), 64)

    def test_unique_fragment_and_explicit_title_can_resolve_renamed_member(self) -> None:
        runtime = self._runtime({
            "docs/source.htm": b"<html><body>Source</body></html>",
            "docs/current.htm": b'<html><head><title>Current topic</title></head><body><a name="section">Body</a></body></html>',
        })
        result = runtime.resolve_relationship(
            "docs/source.htm",
            "obsolete.htm#section",
            semantic_hint="Current topic",
        )
        self.assertEqual(result.status, "resolved")
        self.assertEqual(result.target_member, "docs/current.htm")
        self.assertEqual(result.strategy, "semantic_fragment_title")
        self.assertEqual(result.evidence["target_title"], "Current topic")

    def test_semantic_reconciliation_rejects_ambiguous_targets(self) -> None:
        page = b'<html><head><title>Duplicate title</title></head><body><a id="section">Body</a></body></html>'
        runtime = self._runtime({
            "docs/source.htm": b"<html><body>Source</body></html>",
            "docs/first.htm": page,
            "docs/second.htm": page + b" ",
        })
        result = runtime.resolve_relationship(
            "docs/source.htm",
            "obsolete.htm#section",
            semantic_hint="Duplicate title",
        )
        self.assertEqual(result.status, "source_missing_target")

    def test_semantic_reconciliation_requires_an_explicit_source_hint(self) -> None:
        runtime = self._runtime({
            "docs/source.htm": b"<html><body>Source</body></html>",
            "docs/current.htm": b'<html><head><title>Current topic</title></head><body><a id="section">Body</a></body></html>',
        })
        result = runtime.resolve_relationship("docs/source.htm", "obsolete.htm#section")
        self.assertEqual(result.status, "source_missing_target")

    def test_strict_resolution_precedes_internal_reconciliation(self) -> None:
        runtime = self._runtime({
            "docs/source.htm": b"<html><body>Source</body></html>",
            "docs/existing.htm": b'<html><head><title>Existing</title></head><body><a id="section">Body</a></body></html>',
        })
        local = runtime.resolve_relationship("docs/source.htm", "existing.htm#section", semantic_hint="Existing")
        external = runtime.resolve_relationship("docs/source.htm", "https://example.test/obsolete.htm#section", semantic_hint="Existing")
        self.assertEqual(local.strategy, "relative_path")
        self.assertEqual(external.status, "external")

    def test_strict_primitive_does_not_apply_collection_reconciliation(self) -> None:
        result = resolve_relationship(
            "docs/source.htm",
            "obsolete.htm#section",
            {"docs/current.htm"},
        )
        self.assertEqual(result.status, "source_missing_target")


if __name__ == "__main__":
    unittest.main()
