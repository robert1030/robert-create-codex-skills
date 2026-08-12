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
        self.assertEqual(module.SKILL_VERSION, "1.2.3")
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        frozen_text = (ROOT / "FROZEN.md").read_text(encoding="utf-8")
        migration_text = (ROOT / "references" / "migration-report.md").read_text(encoding="utf-8")
        self.assertIn("> **v1.2.3｜2026-08-12**", skill_text)
        self.assertEqual(skill_text.count("\n> **v"), 1)
        self.assertLessEqual(skill_text.splitlines().index("## 目的") + 1, 12)
        for historical_stamp in (
            "> **v1.2.3-dev-r3｜2026-08-11**",
            "> **v1.2.3-dev-r2｜2026-08-10**",
            "> **v1.2.3-dev-r1｜2026-08-10**",
            "> **v1.2.2｜2026-08-09**",
            "> **v1.2.1｜2026-07-30**",
        ):
            self.assertNotIn(historical_stamp, skill_text)
        self.assertIn("## 目錄", migration_text)
        self.assertIn("## v1.2.3-dev-r3 範本非產品規則修補", migration_text)
        self.assertIn("## v1.2.3 正式凍結", migration_text)
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
        self.assertIn("## v1.2.2-dev-r1 PDF 原生視覺與防繞過開發契約", frozen_text)
        self.assertIn("## v1.2.2-dev-r2 Dense-text 與 Recall 開發契約", frozen_text)
        self.assertIn("## v1.2.2 前次發布候選保留紀錄", frozen_text)
        self.assertIn("## v1.2.2-dev-r3 統一多格式語意修補契約", frozen_text)
        self.assertIn("## v1.2.2 正式凍結契約", frozen_text)
        self.assertIn("至少另開 v1.2.3 開發版", frozen_text)
        self.assertIn("## v1.2.3-dev-r1 capability routing 開發契約", frozen_text)
        self.assertIn("## v1.2.3-dev-r2 切片策略與未洩題驗證契約", frozen_text)
        self.assertIn("## v1.2.3-dev-r3 範本非產品規則與通用解析契約", frozen_text)
        self.assertIn("## v1.2.3 正式凍結契約", frozen_text)
        self.assertIn("`SKILL_VERSION` 固定為 `1.2.3`", frozen_text)
        self.assertIn("至少另開 v1.2.4 開發版", frozen_text)
        self.assertIn("不得因 v1.2.3 曾被錯誤宣稱正式發布而跳到 v1.2.4", frozen_text)
        self.assertIn("needs_capability", frozen_text)

        self.assertIn("## 切片策略對焦", skill_text)
        self.assertIn("每份來源的替代 min／max Token", skill_text)
        self.assertIn("Validation SubAgent 必須由原檔重新建立判準", skill_text)
        default_prompt = yaml.safe_load((ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8"))["interface"]["default_prompt"]
        self.assertIn("assess each source's hierarchy", default_prompt)
        self.assertIn("source-specific min/max tokens", default_prompt)
        self.assertNotIn("15000英語單字", skill_text)
        self.assertNotIn("TikTok變成美國版", skill_text)
        self.assertNotIn("15000英語單字", default_prompt)
        self.assertNotIn("TikTok變成美國版", default_prompt)

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

    def test_representative_fixture_content_is_not_runtime_policy(self) -> None:
        runtime_text = "\n".join(
            path.read_text(encoding="utf-8")
            for path in sorted((ROOT / "scripts").rglob("*.py"))
        )
        for leaked_fixture_detail in (
            "TikTok",
            "社群角力",
            "影片單字",
            "本篇講解",
            "WEI LIN ENGLISH",
            "WEILINENGLISH",
        ):
            self.assertNotIn(leaked_fixture_detail, runtime_text)
        self.assertNotRegex(runtime_text, r"data_row_count[^\n]{0,30}==\s*25")
        self.assertNotRegex(runtime_text, r"range\(1,\s*26\)")

    def test_multiformat_scope_is_primary_and_pdf_lanes_are_conditional(self) -> None:
        skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        _start, frontmatter, _body = skill_text.split("---", 2)
        description = yaml.safe_load(frontmatter)["description"]
        agent_config = yaml.safe_load((ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8"))
        prompt = agent_config["interface"]["default_prompt"]

        for token in (
            "pdf", "docx", "doc", "html", "htm", "xml", "csv", "markdown",
            "mp4", "jpg", "jpeg", "png", "heif", "heic", "zip", "nested zip", "directory",
        ):
            self.assertIn(token, description)
        self.assertIn("all supported source formats are first-class routes", description)
        self.assertIn("pdf visual and dense-text handling are conditional format-specific lanes", description)
        self.assertIn("## 統一多格式優先原則", skill_text)
        self.assertIn("不得因最新修補、示例或驗收檔使用 PDF，就把 Skill 解讀成 PDF 優先或 PDF 專用", skill_text)
        self.assertIn("### 全格式標準路徑", skill_text)
        self.assertIn("### PDF 條件式視覺與 dense-text 路徑", skill_text)
        self.assertIn("every supplied source", prompt)
        self.assertIn("as first-class routes", prompt)
        self.assertIn("Apply format-specific lanes only when their conditions match", prompt)
        self.assertIn("never infer the whole skill's scope from a recent patch or test fixture", prompt)

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
            "scripts/visual_review.py",
            "scripts/prepare_visual_review.py",
            "scripts/validate_against_source.py",
            "scripts/verify_visual_retrieval.py",
            "scripts/validate_dense_retrieval.py",
            "references/workflow.md",
            "references/adapter-contract.md",
            "references/document-ir.md",
            "references/normalized-markdown.md",
            "references/output-schema.md",
            "references/quality-gates.md",
            "references/image-semantics-gate.md",
            "references/dense-text-contract.md",
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
            "tests/test_v122_visual_review.py",
            "tests/test_v122_dense_text.py",
            "tests/test_v123_capability_routing.py",
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
