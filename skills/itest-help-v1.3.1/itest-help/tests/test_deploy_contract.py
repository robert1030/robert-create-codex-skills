"""佈署契約與凍結值的回歸測試。改動任何腳本或 manifest 後必跑，全綠才算沒踩到既有契約。"""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_deploy_targets as deploy  # noqa: E402
import validate_itest_help as validate  # noqa: E402


FROZEN_RAG_SHA256 = "309BA7AACF41000C242FD0FBD1AF0B8B548F1EAB14A055284A3615DDE82BBC70"
FROZEN_INDEX_SHA256 = "7CF0F4ECD8A9E9943AB1E9467D9E2B0CCED68D8FA2C0A872BA3C4EAFC48832F0"
FROZEN_CHAT_WEB_SHA256 = "B0645A3856DFD9E3A319C2D97F61F3BFAEA1765E6CD0F561923C75E0E52BBB4E"
FROZEN_SOURCE_MEMBER_COUNT = 7004


def read_json(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


class FrozenContractTests(unittest.TestCase):
    """房規一：凍結值寫成斷言，有人改就紅燈。"""

    def test_rag_identity_is_unchanged(self) -> None:
        package = read_json("manifest.json")
        source = read_json("knowledge/source-manifest.json")
        self.assertEqual(package["knowledge_base"]["rag_archive_sha256"], FROZEN_RAG_SHA256)
        self.assertEqual(source["rag"]["archive_sha256"], FROZEN_RAG_SHA256)
        self.assertEqual(source["rag"]["version"], "1.2.1")
        self.assertEqual(source["product_version"], "26.2.0")

    def test_original_source_member_accounting_is_unchanged(self) -> None:
        source = read_json("knowledge/source-manifest.json")["original_source"]
        self.assertEqual(source["member_count"], FROZEN_SOURCE_MEMBER_COUNT)
        self.assertEqual(source["member_path_match_count"], FROZEN_SOURCE_MEMBER_COUNT)
        self.assertEqual(source["member_content_sha256_match_count"], FROZEN_SOURCE_MEMBER_COUNT)
        self.assertEqual(source["member_hash_mismatch_count"], 0)

    def test_known_limitation_is_still_disclosed(self) -> None:
        source = read_json("knowledge/source-manifest.json")["validation"]
        self.assertEqual(source["collection_status"], "partial_success")
        self.assertEqual(source["collection_exit_code"], 2)
        report = (ROOT / "knowledge" / "validation-report.md").read_text(encoding="utf-8")
        self.assertIn("partial_success", report)
        self.assertIn("source_missing_target", report)

    def test_index_hashes_match_the_shipped_files(self) -> None:
        manifest = read_json("knowledge/retrieval-index-manifest.json")
        self.assertEqual(manifest["index_sha256"], FROZEN_INDEX_SHA256)
        self.assertEqual(manifest["chat_web_sha256"], FROZEN_CHAT_WEB_SHA256)
        self.assertEqual(manifest["record_count"], validate.FROZEN_INDEX_RECORD_COUNT)
        self.assertEqual(validate.digest(ROOT / "knowledge" / "retrieval-index.jsonl"), FROZEN_INDEX_SHA256)
        chat_web = ROOT / "knowledge" / "chat-web-knowledge.md"
        if chat_web.is_file():
            self.assertEqual(validate.digest(chat_web), FROZEN_CHAT_WEB_SHA256)


class DeployTargetTests(unittest.TestCase):
    """房規二：佈署限制交給程式判斷，不靠肉眼。"""

    def test_skill_identity_passes_agent_skills_rules(self) -> None:
        failures: list[str] = []
        deploy.check_identity(ROOT, failures)
        self.assertEqual(failures, [])

    def test_no_file_exceeds_the_windows_path_limit(self) -> None:
        files = sorted(path for path in ROOT.rglob("*") if path.is_file())
        longest = max(
            deploy.WINDOWS_BASE_LENGTH + len(path.relative_to(ROOT.parent).as_posix().replace("/", "\\"))
            for path in files
        )
        self.assertLess(longest, deploy.WINDOWS_PATH_MAX)

    def test_chatweb_file_cap_leaves_headroom(self) -> None:
        files = [path for path in ROOT.rglob("*") if path.is_file() and "knowledge/rag/" not in path.as_posix()]
        chatweb_files = [path for path in files if path.name != "chat-web-knowledge.md"]
        self.assertLessEqual(len(chatweb_files), deploy.CHATWEB_MAX_FILES)

    def test_text_files_are_bom_free_utf8_with_lf(self) -> None:
        files = sorted(path for path in ROOT.rglob("*") if path.is_file())
        failures: list[str] = []
        deploy.check_encoding(ROOT, files, failures)
        self.assertEqual(failures, [])

    def test_scripts_import_standard_library_only(self) -> None:
        files = sorted(path for path in (ROOT / "scripts").rglob("*.py"))
        failures: list[str] = []
        deploy.check_dependencies(ROOT, files, failures)
        self.assertEqual(failures, [])


class ProfileTests(unittest.TestCase):
    def test_profile_detection_matches_the_shipped_layout(self) -> None:
        expected = "full" if (ROOT / "knowledge" / "rag").is_dir() else (
            "runtime" if (ROOT / "knowledge" / "chat-web-knowledge.md").is_file() else "chatweb"
        )
        self.assertEqual(validate.detect_profile(ROOT), expected)

    def test_skill_md_documents_a_cwd_independent_command(self) -> None:
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("${CLAUDE_SKILL_DIR}", skill)
        self.assertIn("python3", skill)

    def test_retrieval_discipline_survives_in_every_layer(self) -> None:
        """v1.2.0 修的是檢索層迴歸：中英雙查與多輪檢索的紀律不得再次被移除。"""
        policy = (ROOT / "core" / "retrieval-policy.md").read_text(encoding="utf-8")
        self.assertIn("知識庫全文為英文", policy)
        self.assertIn("一次查詢不足以作答", policy)
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("中文查詢詞對它無效", skill)
        for relative in ("adapters/agent/instructions.md", "adapters/chat-web/instructions.md"):
            text = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("英文技術詞", text, msg=f"{relative} lost the bilingual query rule")

    def test_snippets_surface_definitions_buried_deep_in_long_chunks(self) -> None:
        """v1.3.0 修的是截斷層迴歸：前綴截斷會讓 30k 字元的 chunk 只露出開頭概述。"""
        sys.path.insert(0, str(ROOT / "scripts"))
        import search_itest_help  # noqa: PLC0415

        records = search_itest_help.load_index(ROOT / "knowledge" / "retrieval-index.jsonl")
        target = next(r for r in records if "command_syntax.htm-8ad53b3df7d9" in r["chunk_id"])
        query = "local variable regexp string match if action true"
        self.assertGreater(len(target["text"]), 20000, "fixture chunk is no longer a long one")
        self.assertNotIn("Returns 1 if the expression matches", target["text"][:1200],
                         "the definition is no longer deep in the chunk, this test is moot")
        snippet = search_itest_help.snippets(target["text"], query)
        self.assertIn("Returns 1 if the expression matches", snippet)
        self.assertIn("java/util/regex/Pattern", snippet)
        self.assertLess(len(snippet), len(target["text"]) // 10, "snippet budget blew up")

    def test_itest_versus_native_tcl_rule_is_grounded_in_the_knowledge_base(self) -> None:
        """v1.3.1 修的是 iTest 直譯器與原生 Tcl 混淆。規則列出的每個不等價項都必須在知識庫有明文。"""
        sys.path.insert(0, str(ROOT / "scripts"))
        import search_itest_help  # noqa: PLC0415

        records = search_itest_help.load_index(ROOT / "knowledge" / "retrieval-index.jsonl")
        table = next(r for r in records if "command_syntax.htm-8ad53b3df7d9" in r["chunk_id"])["text"]
        for evidence in (
            "Some commands operate in the same way as their Tcl counterpart, some do not",
            "The command uses Java regexps to implement the command",
            "supports only * and ? glob pattern sequences and does not support",
            "The syntax differs from Tcl syntax",
            "The -command option is not supported",
        ):
            self.assertIn(evidence, table, msg=f"knowledge base no longer states: {evidence}")
        policy = (ROOT / "core" / "retrieval-policy.md").read_text(encoding="utf-8")
        for claim in ("Java", "string match", "array names", "lsort", "三個執行環境不可混用"):
            self.assertIn(claim, policy)

    def test_snippet_keeps_short_chunks_intact(self) -> None:
        sys.path.insert(0, str(ROOT / "scripts"))
        import search_itest_help  # noqa: PLC0415

        short = "a short chunk about regexp that fits well inside one budget"
        self.assertEqual(search_itest_help.snippets(short, "regexp"), short)

    def test_search_result_declares_full_length(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "search_itest_help.py"), "regexp command", "--limit", "3"],
            cwd=ROOT.parent, capture_output=True, text=True, encoding="utf-8", check=True,
        )
        for result in json.loads(completed.stdout)["results"]:
            self.assertIn("text_length", result)
            self.assertIn("text_truncated", result)
            self.assertEqual(result["text_truncated"], len(result["text"]) < result["text_length"])

    def test_search_default_limit_is_not_narrowed(self) -> None:
        """分數常擠在窄區間，預設 limit 調低會把切題來源擋在回傳範圍外。"""
        sys.path.insert(0, str(ROOT / "scripts"))
        import search_itest_help  # noqa: PLC0415

        parser_default = None
        source = (ROOT / "scripts" / "search_itest_help.py").read_text(encoding="utf-8")
        for line in source.splitlines():
            if '"--limit"' in line and "default=" in line:
                parser_default = int(line.split("default=")[1].split(")")[0].strip())
        self.assertIsNotNone(parser_default, "could not find the --limit default")
        self.assertGreaterEqual(parser_default, 10)
        self.assertTrue(hasattr(search_itest_help, "score"))

    def test_skill_md_warns_about_the_windows_python3_stub(self) -> None:
        """Windows 的 python3 是 Store 空殼，退出碼 49 且零輸出，指引寫錯會造成錯誤降級。"""
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("py -3", skill)
        self.assertIn("49", skill)
        matrix = (ROOT / "docs" / "platform-matrix.md").read_text(encoding="utf-8")
        self.assertIn("py -3", matrix)
        self.assertIn("WindowsApps", matrix)

    def test_frontmatter_holds_only_name_and_description(self) -> None:
        fields = deploy.parse_frontmatter((ROOT / "SKILL.md").read_text(encoding="utf-8"))
        self.assertEqual(set(fields), {"name", "description"})

    def test_search_runs_without_the_rag_directory(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "search_itest_help.py"), "Tcl Test Step", "--limit", "1"],
            cwd=ROOT.parent,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
        response = json.loads(completed.stdout)
        self.assertEqual(response["status"], "ok")
        self.assertTrue(response["results"][0]["chunk_id"])


if __name__ == "__main__":
    unittest.main()
