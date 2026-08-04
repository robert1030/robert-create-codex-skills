#!/usr/bin/env python3
"""獨立驗證 iTest Help skill 的結構、來源身份與資料鏈。

支援三個佈署 profile：

- `full`：含原樣 `knowledge/rag/`，走完整 provenance 鏈驗證。
- `runtime`：不含 `knowledge/rag/`，改以凍結雜湊比對 index 與 Chat Web 知識檔。
- `chatweb`：`runtime` 再去掉 `chat-web-knowledge.md`，另驗 claude.ai 上傳限制。

不指定 `--profile` 時依目錄內容自動判定，維持 v1.0.0 的 `validate_itest_help.py <root>` 呼叫方式。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


BASE_REQUIRED_FILES = (
    "SKILL.md", "README.md", "FROZEN.md", "manifest.json",
    "core/role-and-scope.md", "core/query-policy.md", "core/retrieval-policy.md",
    "core/source-policy.md", "core/version-policy.md", "core/external-research-policy.md",
    "core/response-format.md", "core/uncertainty-policy.md",
    "knowledge/source-manifest.json", "knowledge/provenance-map.json", "knowledge/version-matrix.json",
    "knowledge/validation-report.md", "knowledge/retrieval-index.jsonl",
    "knowledge/retrieval-index-manifest.json",
    "tests/retrieval-tests.jsonl", "tests/answer-tests.jsonl", "tests/citation-tests.jsonl",
    "tests/version-conflict-tests.jsonl", "tests/external-fallback-tests.jsonl",
    "tests/retrieval-discipline-tests.jsonl",
    "adapters/chat-web/instructions.md", "adapters/chat-web/knowledge-configuration.md",
    "adapters/chat-web/conversation-starters.md", "adapters/chat-web/claude-ai-skill.md",
    "adapters/chat-web/chatgpt-skill.md",
    "adapters/agent/instructions.md", "adapters/agent/claude-code.md",
    "adapters/agent/tool-contracts.md", "adapters/agent/retrieval-interface.md",
    "adapters/agent/web-search-interface.md", "adapters/agent/error-handling.md",
    "adapters/README.md", "docs/platform-matrix.md",
    "scripts/search_itest_help.py", "scripts/inspect_chunk.py", "scripts/run_regression_tests.py",
    "scripts/validate_deploy_targets.py",
)
CHAT_WEB_KNOWLEDGE = "knowledge/chat-web-knowledge.md"
REQUIRED_FILES = BASE_REQUIRED_FILES + (CHAT_WEB_KNOWLEDGE,)
PROFILES = ("full", "runtime", "chatweb")
FROZEN_INDEX_RECORD_COUNT = 1522
FROZEN_RAG_FILE_COUNT = 9329
CHATWEB_MAX_FILES = 200
METRIC_EXPECTATIONS = {
    "critical_occurrence_coverage_ratio": 1.0,
    "existing_target_resolution_ratio": 1.0,
    "member_accounting_ratio": 1.0,
    "relationship_occurrence_accounting_ratio": 1.0,
    "semantic_order_inversion_count": 0,
    "source_semantic_coverage_ratio": 1.0,
    "source_semantic_critical_coverage_ratio": 1.0,
    "unreported_relationship_failure_count": 0,
}


def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest().upper()


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def force_utf8_stdout() -> None:
    """Windows 主控台預設字碼頁可能是 CP950，強制 UTF-8 輸出以免 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def detect_profile(root: Path) -> str:
    """依目錄實際內容判定 profile，讓舊的 `validate_itest_help.py <root>` 呼叫方式維持有效。"""
    if (root / "knowledge" / "rag").is_dir():
        return "full"
    if (root / CHAT_WEB_KNOWLEDGE).is_file():
        return "runtime"
    return "chatweb"


def check_frozen_hashes(root: Path, profile: str, failures: list[str]) -> list[dict]:
    """不含 `knowledge/rag/` 時，改以凍結雜湊確認 index 與 Chat Web 知識檔未被竄改。"""
    manifest_path = root / "knowledge" / "retrieval-index-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    index_path = root / "knowledge" / "retrieval-index.jsonl"
    require(
        digest(index_path) == manifest["index_sha256"].upper(),
        "Retrieval index SHA-256 does not match the frozen manifest",
        failures,
    )
    require(
        manifest["record_count"] == FROZEN_INDEX_RECORD_COUNT,
        f"Index manifest record_count is not {FROZEN_INDEX_RECORD_COUNT}",
        failures,
    )
    index_records = load_jsonl(index_path)
    require(
        len(index_records) == FROZEN_INDEX_RECORD_COUNT,
        f"Retrieval index does not hold {FROZEN_INDEX_RECORD_COUNT} records",
        failures,
    )
    index_ids = [record["chunk_id"] for record in index_records]
    require(len(index_ids) == len(set(index_ids)), "Duplicate Chunk ID in retrieval index", failures)
    if profile == "runtime":
        chat_path = root / CHAT_WEB_KNOWLEDGE
        require(
            digest(chat_path) == manifest["chat_web_sha256"].upper(),
            "Chat Web knowledge SHA-256 does not match the frozen manifest",
            failures,
        )
        chat_text = chat_path.read_text(encoding="utf-8")
        require(
            chat_text.count("## Chunk ID: ") == len(index_records),
            "Chat Web knowledge count does not match index",
            failures,
        )
    return index_records


def check_chatweb_limits(root: Path, failures: list[str]) -> None:
    """claude.ai Skills 上傳的硬性限制，超過就別浪費你一次上傳。"""
    files = [path for path in root.rglob("*") if path.is_file()]
    require(
        len(files) <= CHATWEB_MAX_FILES,
        f"Chat Web skill package holds {len(files)} files, over the {CHATWEB_MAX_FILES} file cap",
        failures,
    )
    require(
        not (root / CHAT_WEB_KNOWLEDGE).is_file(),
        "Chat Web skill package must not ship chat-web-knowledge.md, it retrieves through the index",
        failures,
    )
    frontmatter = (root / "SKILL.md").read_text(encoding="utf-8").split("---", 2)
    require(len(frontmatter) >= 3, "SKILL.md has no closed YAML frontmatter", failures)
    if len(frontmatter) >= 3:
        keys = re.findall(r"^([A-Za-z_-]+):", frontmatter[1], flags=re.MULTILINE)
        require(
            set(keys) == {"name", "description"},
            f"Chat Web SKILL.md frontmatter must hold only name and description, found {sorted(set(keys))}",
            failures,
        )


def main() -> int:
    force_utf8_stdout()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=None, help="skill 根目錄，省略時取本腳本的上層目錄")
    parser.add_argument("--profile", choices=PROFILES, default=None, help="省略時依目錄內容自動判定")
    args = parser.parse_args()
    root = Path(args.root if args.root else Path(__file__).resolve().parents[1]).resolve()
    profile = args.profile or detect_profile(root)
    print(f"Profile: {profile}")
    failures: list[str] = []
    required = REQUIRED_FILES if profile in ("full", "runtime") else BASE_REQUIRED_FILES
    for relative in required:
        require((root / relative).is_file(), f"Missing required file: {relative}", failures)
    if profile == "full":
        require((root / "knowledge" / "rag").is_dir(), "Full profile requires knowledge/rag/", failures)
    if failures:
        for failure in failures:
            print("FAIL: " + failure)
        return 1

    skill_text = (root / "SKILL.md").read_text(encoding="utf-8")
    require(skill_text.startswith("---\nname: itest-help\n"), "SKILL.md frontmatter or name is invalid", failures)
    require("PowerShell Test Step" in skill_text, "SKILL.md lacks PowerShell Test Step scope", failures)
    require("【知識庫來源】" in skill_text, "SKILL.md lacks citation contract", failures)
    package = json.loads((root / "manifest.json").read_text(encoding="utf-8"))
    source_manifest = json.loads((root / "knowledge" / "source-manifest.json").read_text(encoding="utf-8"))
    version_matrix = json.loads((root / "knowledge" / "version-matrix.json").read_text(encoding="utf-8"))
    require(package["name"] == root.name == "itest-help", "Package directory and manifest name diverge", failures)
    require(package["product"] == source_manifest["product"] == "iTest Help", "Product name diverges", failures)
    require(package["product_version"] == source_manifest["product_version"] == "26.2.0", "Product version diverges", failures)
    require(version_matrix["knowledge_base_version"] == "26.2.0", "Version matrix is not 26.2.0", failures)

    raw_chunks: dict[str, dict] = {}
    index_records: list[dict] = []
    if profile != "full":
        index_records = check_frozen_hashes(root, profile, failures)
    if profile == "chatweb":
        check_chatweb_limits(root, failures)
    if profile == "full":
        rag_root = root / "knowledge" / "rag" / "v1.2.1-full-visual-semantics-20260730"
        report_paths = list(rag_root.glob("collection-report-*.json"))
        require(len(report_paths) == 1, "Expected exactly one extracted collection report", failures)
        require(sum(1 for path in (root / "knowledge" / "rag").rglob("*") if path.is_file()) == FROZEN_RAG_FILE_COUNT, f"Extracted RAG file count is not {FROZEN_RAG_FILE_COUNT}", failures)
        if report_paths:
            report_path = report_paths[0]
            report = json.loads(report_path.read_text(encoding="utf-8"))
            require(digest(report_path) == source_manifest["rag"]["collection_report_sha256"], "Collection report SHA-256 mismatch", failures)
            require(report["collection_id"] == source_manifest["rag"]["collection_id"], "Collection ID mismatch", failures)
            require(report["display_name"] == "itest-help_26.2.0.zip", "Collection product archive name mismatch", failures)
            require(report["skill_version"] == "1.2.1", "RAG version mismatch", failures)
            require(report["gate"]["passed"] is True and not report["gate"]["violations"], "Collection gate did not pass", failures)
            require(report["status"] == "partial_success" and report["exit_code"] == 2, "Known collection status was altered", failures)
            require(report["relationship_summary"]["source_missing_target"] == 1, "Known missing target count was altered", failures)
            for key, expected in METRIC_EXPECTATIONS.items():
                require(report["metrics"].get(key) == expected, f"Collection metric mismatch: {key}", failures)

            for metadata_path in rag_root.rglob("chunks.jsonl"):
                for record in load_jsonl(metadata_path):
                    identifier = record["chunk_id"]
                    require(identifier not in raw_chunks, f"Duplicate raw Chunk ID: {identifier}", failures)
                    raw_chunks[identifier] = record
            index_records = load_jsonl(root / "knowledge" / "retrieval-index.jsonl")
            index_ids = [record["chunk_id"] for record in index_records]
            require(len(index_ids) == len(set(index_ids)), "Duplicate Chunk ID in retrieval index", failures)
            require(len(index_records) == len(raw_chunks), "Index count does not match raw Chunk count", failures)
            member_by_source = {member["source_id"]: member for member in report["members"] if member.get("source_id")}
            for index in index_records:
                raw = raw_chunks.get(index["chunk_id"])
                require(raw is not None, f"Index references unknown Chunk ID: {index['chunk_id']}", failures)
                if raw is not None:
                    require(index["content_sha256"] == raw["content_sha256"], f"Content hash mismatch: {index['chunk_id']}", failures)
                    require(index["source_sha256"] == raw["source_hash"], f"Source hash mismatch: {index['chunk_id']}", failures)
                    member = member_by_source.get(raw["source_id"])
                    require(member is not None and index["source_file"] == member["relative_path"], f"Source file mismatch: {index['chunk_id']}", failures)
            chat_text = (root / CHAT_WEB_KNOWLEDGE).read_text(encoding="utf-8")
            require(chat_text.count("## Chunk ID: ") == len(index_records), "Chat Web knowledge count does not match index", failures)
            for index in (index_records[0], index_records[len(index_records) // 2], index_records[-1]):
                require(index["chunk_id"] in chat_text, f"Chat Web knowledge omits Chunk ID: {index['chunk_id']}", failures)

    known_chunk_ids = set(raw_chunks) if raw_chunks else {record["chunk_id"] for record in index_records}
    source_files = {record["source_file"] for record in index_records}
    for test_name in ("retrieval-tests.jsonl", "answer-tests.jsonl", "citation-tests.jsonl", "version-conflict-tests.jsonl", "external-fallback-tests.jsonl", "retrieval-discipline-tests.jsonl"):
        records = load_jsonl(root / "tests" / test_name)
        require(bool(records), f"No cases in {test_name}", failures)
        require(len({record["id"] for record in records}) == len(records), f"Duplicate test ID in {test_name}", failures)
    for citation in load_jsonl(root / "tests" / "citation-tests.jsonl"):
        require(citation["chunk_id"] in known_chunk_ids, f"Citation test has unknown Chunk ID: {citation['chunk_id']}", failures)
        require(citation["source_file"] in source_files, f"Citation test has unknown source file: {citation['source_file']}", failures)

    report_text = (root / "knowledge" / "validation-report.md").read_text(encoding="utf-8")
    require("partial_success" in report_text and "source_missing_target" in report_text, "Validation report hides the known limitation", failures)
    if failures:
        for failure in failures:
            print("FAIL: " + failure)
        return 1
    print("Validation: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
