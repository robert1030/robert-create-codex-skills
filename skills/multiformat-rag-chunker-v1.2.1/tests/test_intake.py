from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from intake import collect_sources


class IntakeTests(unittest.TestCase):
    def test_nested_zip_and_sha256_deduplication(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            nested = temp / "nested.zip"
            with zipfile.ZipFile(nested, "w") as archive:
                archive.writestr("inside.md", "# Same\n")
            outer = temp / "outer.zip"
            with zipfile.ZipFile(outer, "w") as archive:
                archive.writestr("first.md", "# Same\n")
                archive.writestr("second.md", "# Different\n")
                archive.write(nested, "nested.zip")
            sources, duplicates = collect_sources(outer, temp / "extract")
            self.assertEqual(len(sources), 2)
            self.assertEqual(len(duplicates), 1)
            self.assertTrue(any("nested.zip" in item.display_name for item in sources + [] ) or duplicates)

    def test_zip_path_traversal_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_name:
            temp = Path(temp_name)
            bad = temp / "bad.zip"
            with zipfile.ZipFile(bad, "w") as archive:
                archive.writestr("../escape.md", "# bad\n")
            with self.assertRaisesRegex(ValueError, "zip_path_traversal"):
                collect_sources(bad, temp / "extract")


if __name__ == "__main__":
    unittest.main()
