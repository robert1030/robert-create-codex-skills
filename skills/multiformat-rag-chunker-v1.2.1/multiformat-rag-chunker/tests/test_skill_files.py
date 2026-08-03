from __future__ import annotations

import subprocess
import sys
import unittest
from unittest import mock
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class SkillFileTests(unittest.TestCase):
    def test_skill_frontmatter_and_line_budget(self) -> None:
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertLessEqual(len(text.splitlines()), 500)
        self.assertNotIn("TODO", text)
        self.assertTrue(text.startswith("---\n"))
        _start, frontmatter, _body = text.split("---", 2)
        data = yaml.safe_load(frontmatter)
        self.assertEqual(set(data), {"name", "description"})
        self.assertEqual(data["name"], "multiformat-rag-chunker")
        self.assertEqual(data["name"], data["name"].lower())
        self.assertEqual(data["description"], data["description"].lower())

    def test_release_version_and_freeze_contract(self) -> None:
        import importlib.util

        spec = importlib.util.spec_from_file_location("skill_constants", ROOT / "scripts" / "constants.py")
        self.assertIsNotNone(spec)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        self.assertEqual(module.SKILL_VERSION, "1.2.1")
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        frozen_text = (ROOT / "FROZEN.md").read_text(encoding="utf-8")
        self.assertIn("> **v1.2.1｜2026-07-30**", skill_text)
        self.assertIn("> **v1.2.1-dev-r4｜2026-07-29**", skill_text)
        self.assertIn("> **v1.2.1-dev-r3｜2026-07-29**", skill_text)
        self.assertIn("> **v1.2.1-dev-r2｜2026-07-29**", skill_text)
        self.assertIn("> **v1.2.1-dev-r1｜2026-07-28**", skill_text)
        self.assertIn("## v1.1.1 正式凍結契約", frozen_text)
        self.assertIn("## v1.1.2-dev-r3 開發契約", frozen_text)
        self.assertIn("## v1.1.2 正式凍結契約", frozen_text)
        self.assertIn("至少另開 v1.1.3 開發版", frozen_text)
        self.assertIn("## v1.2.0-dev-r1 collection 開發契約", frozen_text)
        self.assertIn("## v1.2.0-dev-r2 collection 接入契約", frozen_text)
        self.assertIn("## v1.2.0-dev-r3 補件與異質回歸契約", frozen_text)
        self.assertIn("## v1.2.0-dev-r4 原包內部關聯復原契約", frozen_text)
        self.assertIn("## v1.2.0 正式凍結契約", frozen_text)
        self.assertIn("至少另開 v1.2.1 開發版", frozen_text)
        self.assertIn("## v1.2.1-dev-r1 來源語意完整度修補契約", frozen_text)
        self.assertIn("## v1.2.1-dev-r2 LLM-first、runtime-aware 多格式處理契約", frozen_text)
        self.assertIn("## v1.2.1-dev-r3 獨立 XML 關聯 occurrence 對帳契約", frozen_text)
        self.assertIn("## v1.2.1-dev-r4 圖片語意與 decoder provenance 契約", frozen_text)
        self.assertIn("## v1.2.1 正式凍結契約", frozen_text)
        self.assertIn("至少另開 v1.2.2 開發版", frozen_text)
        self.assertIn("needs_capability", frozen_text)

    def test_runtime_contract_is_platform_adaptive(self) -> None:
        dependencies = (ROOT / "references" / "dependencies.md").read_text(encoding="utf-8")
        workflow = (ROOT / "references" / "workflow.md").read_text(encoding="utf-8")
        output_schema = (ROOT / "references" / "output-schema.md").read_text(encoding="utf-8")
        agent_config = yaml.safe_load((ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8"))
        self.assertIn("權限、隔離性、持久性與可回復性", dependencies)
        self.assertNotIn("Codex、Claude Code", dependencies)
        self.assertIn("needs_capability", workflow)
        self.assertIn("needs_source", output_schema)
        self.assertIn("$multiformat-rag-chunker", agent_config["interface"]["default_prompt"])

    def test_required_files_exist(self) -> None:
        expected = [
            "SKILL.md",
            "FROZEN.md",
            "agents/openai.yaml",
            "scripts/rag_chunker.py",
            "scripts/models.py",
            "scripts/intake.py",
            "scripts/normalize.py",
            "scripts/markdown_builder.py",
            "scripts/coverage.py",
            "scripts/chunker.py",
            "scripts/output.py",
            "scripts/validate.py",
            "scripts/collection.py",
            "scripts/relationship_resolver.py",
            "scripts/supplement_manifest.py",
            "scripts/validate_collection.py",
            "scripts/source_semantics.py",
            "scripts/visual_semantics.py",
            "scripts/verify_visual_retrieval.py",
            "references/workflow.md",
            "references/adapter-contract.md",
            "references/document-ir.md",
            "references/normalized-markdown.md",
            "references/output-schema.md",
            "references/quality-gates.md",
            "references/image-semantics-gate.md",
            "references/failure-policy.md",
            "references/dependencies.md",
            "references/test-coverage.md",
            "references/collection-contract.md",
            "references/supplement-contract.md",
            "references/r3-regression-plan.md",
            "references/r4-internal-resolution-contract.md",
            "tests/test_reading_order_validation.py",
            "tests/test_docx_title_semantics.py",
            "tests/test_semantic_downgrade.py",
            "tests/test_validator_contract.py",
            "tests/test_collection_contract.py",
            "tests/test_collection_integration.py",
            "tests/test_source_semantic_regression.py",
            "tests/test_supplement_contract.py",
            "tests/test_internal_relationship_resolution.py",
            "tests/test_image_semantic_contract.py",
            "tests/fixtures/2025-09-TikTok變成美國版.doc",
            "tests/fixtures/barcode-ean13.png",
            "legacy/README.md",
        ]
        for relative in expected:
            self.assertTrue((ROOT / relative).is_file(), relative)


    def test_bootstrap_includes_opencv_and_uses_platform_aware_pip_flags(self) -> None:
        import importlib.util

        spec = importlib.util.spec_from_file_location("skill_bootstrap", ROOT / "scripts" / "bootstrap.py")
        self.assertIsNotNone(spec)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        self.assertEqual(module.CORE_PYTHON.get("cv2"), "opencv-python-headless")

        captured: list[list[str]] = []
        with mock.patch.object(module, "_externally_managed_python", return_value=False), mock.patch.object(
            module.subprocess, "run", side_effect=lambda command, check: captured.append(command)
        ):
            module._pip_install(["opencv-python-headless"])
        self.assertEqual(captured[0][:4], [sys.executable, "-m", "pip", "install"])
        self.assertNotIn("--break-system-packages", captured[0])

        captured.clear()
        with mock.patch.object(module, "_externally_managed_python", return_value=True), mock.patch.object(
            module.subprocess, "run", side_effect=lambda command, check: captured.append(command)
        ):
            module._pip_install(["opencv-python-headless"])
        self.assertIn("--break-system-packages", captured[0])

    def test_punctuation_validator_passes_all_skill_markdown(self) -> None:
        files = [ROOT / "SKILL.md", ROOT / "FROZEN.md", *sorted((ROOT / "references").glob("*.md")), ROOT / "legacy/README.md"]
        for path in files:
            completed = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "validate_punct.py"), str(path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            self.assertEqual(completed.returncode, 0, f"{path}: {completed.stdout} {completed.stderr}")


if __name__ == "__main__":
    unittest.main()
