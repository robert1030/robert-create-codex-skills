#!/usr/bin/env python3
"""執行 iTest Help skill 的檢索、引用與政策回歸案例。"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def force_utf8_stdout() -> None:
    """Windows 主控台預設字碼頁可能是 CP950，強制 UTF-8 輸出以免 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def load_jsonl(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def run_json(command: list[str], root: Path) -> dict:
    completed = subprocess.run(command, cwd=root, capture_output=True, text=True, encoding="utf-8")
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(command)}\n{completed.stderr}\n{completed.stdout}")
    return json.loads(completed.stdout)


def main() -> int:
    force_utf8_stdout()
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
    tests_root = root / "tests"
    failures: list[str] = []
    passed = 0
    search = root / "scripts" / "search_itest_help.py"
    inspect = root / "scripts" / "inspect_chunk.py"
    for case in load_jsonl(tests_root / "retrieval-tests.jsonl"):
        try:
            response = run_json([sys.executable, str(search), case["query"], "--limit", "8"], root)
            if response["status"] != "ok" or not response["results"]:
                raise AssertionError("retrieval returned no usable result")
            evidence = "\n".join(
                " ".join([result["source_file"], result["title"], " ".join(result["heading_path"]), result["text"]])
                for result in response["results"]
            ).casefold()
            missing = [term for term in case["required_terms"] if term.casefold() not in evidence]
            if missing:
                raise AssertionError("missing terms: " + ", ".join(missing))
            if any(not result["chunk_id"] or not result["source_file"] for result in response["results"]):
                raise AssertionError("result omits citation fields")
            passed += 1
        except Exception as error:
            failures.append(f"{case['id']}: {error}")

    response_format = (root / "core" / "response-format.md").read_text(encoding="utf-8")
    for case in load_jsonl(tests_root / "answer-tests.jsonl"):
        missing = [section for section in case["required_sections"] if section not in response_format]
        if missing:
            failures.append(f"{case['id']}: response format omits " + ", ".join(missing))
        else:
            passed += 1

    for case in load_jsonl(tests_root / "citation-tests.jsonl"):
        try:
            response = run_json([sys.executable, str(inspect), case["chunk_id"]], root)
            record = response.get("record", {})
            if response["status"] != "ok" or record.get("source_file") != case["source_file"]:
                raise AssertionError("Chunk ID did not resolve to the expected source")
            for field in case["required_fields"]:
                if not record.get(field):
                    raise AssertionError(f"missing citation field: {field}")
            passed += 1
        except Exception as error:
            failures.append(f"{case['id']}: {error}")

    version_policy = (root / "core" / "version-policy.md").read_text(encoding="utf-8")
    for case in load_jsonl(tests_root / "version-conflict-tests.jsonl"):
        if case["required_policy_text"] not in version_policy:
            failures.append(f"{case['id']}: version policy omits required handling")
        else:
            passed += 1

    external_policy = (root / "core" / "external-research-policy.md").read_text(encoding="utf-8")
    error_policy = (root / "adapters" / "agent" / "error-handling.md").read_text(encoding="utf-8")
    for case in load_jsonl(tests_root / "external-fallback-tests.jsonl"):
        target = external_policy if case["policy_file"] == "external" else error_policy
        if case["required_policy_text"] not in target:
            failures.append(f"{case['id']}: fallback policy omits required handling")
        else:
            passed += 1

    discipline_targets = {
        "retrieval": root / "core" / "retrieval-policy.md",
        "agent": root / "adapters" / "agent" / "instructions.md",
        "chatweb": root / "adapters" / "chat-web" / "instructions.md",
    }
    for case in load_jsonl(tests_root / "retrieval-discipline-tests.jsonl"):
        target = discipline_targets[case["policy_file"]].read_text(encoding="utf-8")
        if case["required_policy_text"] not in target:
            failures.append(f"{case['id']}: retrieval discipline omits required handling")
        else:
            passed += 1

    if failures:
        for failure in failures:
            print("FAIL: " + failure)
        return 1
    print(f"Regression tests: PASS ({passed} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
