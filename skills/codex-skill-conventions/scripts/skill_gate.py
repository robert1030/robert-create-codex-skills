#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In-skill delivery gate for codex-skill-conventions.

Checks：
1. Required structure and frontmatter.
2. `agents/openai.yaml` metadata.
3. Chinese punctuation hygiene.
4. GPT v1.6.1 and Joan v1.2 contract terms.
5. Regression tests through pytest or direct execution.

Usage：
    python scripts/skill_gate.py <skill-root>
    python scripts/skill_gate.py <skill-root> --test-runner pytest
    python scripts/skill_gate.py <skill-root> --test-runner direct
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import re
import subprocess
import sys
from pathlib import Path

TEXT_SUFFIXES = {".md", ".txt", ".html", ".yaml", ".yml", ".py"}
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache"}

REQUIRED_IN_SKILL = [
    "v1.6.1-codex",
    "gpt-skill-conventions v1.6.1",
    "Codex-Desktop（Windows）",
    "codex-cli（Windows）",
    "codex-cli（Linux）",
    "No-abstraction default",
    "Interactive recommendation flow",
    "CLI prompt format",
    "請輸入 A、B、C，或直接輸入你的需求。",
    "Acceptance prompt template",
    "Page truncation",
    "Overflow greater than 2px",
    "constructivist `check_pages.py`",
    "Math correctness",
    "SymPy",
    "Mismatch is a hard block",
    "constructivist `check_math.py`",
    "cornell `verify_math.py`",
    "KaTeX rendering",
    "no leftover placeholder tokens",
    "no unrendered `$$` or `\\(`",
    "no `katex-error`",
    "`check_katex.py`",
    "Domain correctness",
    "validate before rendering",
    "cornell `verify_structures.py`",
    "tests/test_*.py",
    "intercept `_pip` or `subprocess`",
    "Engine-change gate",
    "Layout measurement",
    "less than one card",
    "kmap `measure_bands.py`",
    "scripts/validate_punct.py",
    "scripts/skill_gate.py <skill-root> [--test-runner auto|pytest|direct]",
    "tests/test_skill_contract.py",
]

REQUIRED_IN_FROZEN = [
    "v1.6.1-codex",
    "No-abstraction rule",
    "Page truncation gate",
    "Math correctness gate",
    "KaTeX gate",
    "Domain gate",
    "Bootstrap gate",
    "Layout measurement gate",
    "Regression test contract",
    "Skill gate runner",
    "Contract tests",
    "CLI interaction",
    "Traceability",
]

REQUIRED_IN_TRACE = [
    "Page truncation",
    "Math correctness",
    "KaTeX rendering",
    "Domain correctness",
    "Regression self-tests",
    "Bootstrap tests",
    "Layout measurement",
    "Non-equivalent or Platform-Converted Items",
]


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    print("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)


def fail(message: str) -> int:
    print(f"[FAIL] {message}")
    return 1


def _read_frontmatter(skill_md: Path) -> tuple[str | None, str]:
    text = skill_md.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return None, text
    return m.group(1), text


def _frontmatter_keys(raw: str) -> list[str]:
    keys = []
    for line in raw.splitlines():
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):", line)
        if m:
            keys.append(m.group(1))
    return keys


def _yaml_string_value(raw: str, key: str) -> str:
    m = re.search(rf"^\s*{re.escape(key)}:\s*(.*?)\s*$", raw, re.M)
    if not m:
        return ""
    value = m.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return value


def check_structure(root: Path) -> int:
    required = [
        "SKILL.md",
        "agents/openai.yaml",
        "scripts/bootstrap.py",
        "scripts/convert_from_claude_skill.py",
        "scripts/skill_gate.py",
        "scripts/sync_validator.py",
        "scripts/validate_punct.py",
        "tests/test_validate_punct.py",
        "tests/test_skill_contract.py",
        "references/acceptance-checklists.md",
        "references/canonical-snippets.md",
        "references/maintenance-protocol.md",
        "references/migration-notes.md",
        "references/migration-traceability.md",
        "FROZEN.md",
        "LESSONS.md",
    ]
    missing = [p for p in required if not (root / p).exists()]
    if missing:
        return fail("缺少必要檔案：" + ", ".join(missing))

    fm, skill_text = _read_frontmatter(root / "SKILL.md")
    if fm is None:
        return fail("SKILL.md frontmatter 格式錯誤")
    keys = _frontmatter_keys(fm)
    if set(keys) != {"name", "description"} or len(keys) != 2:
        return fail("SKILL.md frontmatter 只能包含 name 與 description")
    if "name: codex-skill-conventions" not in fm:
        return fail("SKILL.md name 必須是 codex-skill-conventions")
    desc = _yaml_string_value(fm, "description")
    if len(desc) > 1024:
        return fail(f"SKILL.md description 超過 1024 字：{len(desc)}")
    if "[TODO" in skill_text or "TODO:" in skill_text:
        return fail("SKILL.md 仍含 TODO")
    print("[PASS] 結構檢查")
    return 0


def check_agents_metadata(root: Path) -> int:
    raw = (root / "agents" / "openai.yaml").read_text(encoding="utf-8")
    display = _yaml_string_value(raw, "display_name")
    short = _yaml_string_value(raw, "short_description")
    prompt = _yaml_string_value(raw, "default_prompt")
    if display != "Codex Skill Conventions":
        return fail("agents/openai.yaml display_name 不正確")
    if not (10 <= len(short) <= 64):
        return fail(f"agents/openai.yaml short_description 長度需為 10 到 64 字，目前 {len(short)}")
    if "$codex-skill-conventions" not in prompt:
        return fail("agents/openai.yaml default_prompt 必須包含 $codex-skill-conventions")
    if not re.search(r"allow_implicit_invocation:\s*true", raw):
        return fail("agents/openai.yaml 必須設定 allow_implicit_invocation: true")
    print("[PASS] agents metadata 檢查")
    return 0


def iter_text_files(root: Path):
    for current, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = Path(current) / name
            if path.suffix.lower() in TEXT_SUFFIXES:
                yield path


def check_punctuation(root: Path) -> int:
    validator = root / "scripts" / "validate_punct.py"
    spec = importlib.util.spec_from_file_location("validate_punct", validator)
    if spec is None or spec.loader is None:
        return fail("無法載入 scripts/validate_punct.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    failures = []
    for path in iter_text_files(root):
        rel = path.relative_to(root)
        if str(rel).startswith("tests"):
            continue
        print(f"$ {sys.executable} {validator} {path}")
        if module.check(str(path)) != 0:
            failures.append(rel)
    if failures:
        print("[FAIL] 標點驗證失敗")
        for rel in failures:
            print(f"--- {rel}")
        return 1
    print("[PASS] 標點驗證")
    return 0


def _missing_items(text: str, required: list[str], source_name: str) -> list[str]:
    return [f"{source_name} missing：{needle}" for needle in required if needle not in text]


def check_contract_terms(root: Path) -> int:
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    frozen = (root / "FROZEN.md").read_text(encoding="utf-8")
    trace = (root / "references" / "migration-traceability.md").read_text(encoding="utf-8")
    missing = []
    missing.extend(_missing_items(skill, REQUIRED_IN_SKILL, "SKILL.md"))
    missing.extend(_missing_items(frozen, REQUIRED_IN_FROZEN, "FROZEN.md"))
    missing.extend(_missing_items(trace, REQUIRED_IN_TRACE, "migration-traceability.md"))
    if missing:
        print("[FAIL] contract term check failed")
        for item in missing:
            print("  " + item)
        return 1
    print("[PASS] contract term 檢查")
    return 0


def check_tests_direct(root: Path) -> int:
    tests = sorted((root / "tests").glob("test_*.py"))
    if not tests:
        return fail("缺少 tests/test_*.py 回歸測試")
    failed = []
    for test in tests:
        r = run([sys.executable, str(test)], root)
        print(r.stdout)
        if r.stderr:
            print(r.stderr)
        if r.returncode != 0:
            failed.append(test.name)
    if failed:
        return fail("直接執行回歸測試失敗：" + ", ".join(failed))
    print("[PASS] 直接執行回歸測試")
    return 0


def check_tests_pytest(root: Path) -> int:
    r = run([sys.executable, "-m", "pytest", "tests", "-q"], root)
    print(r.stdout)
    if r.stderr:
        print(r.stderr)
    if r.returncode != 0:
        return fail("pytest 回歸測試失敗")
    print("[PASS] pytest 回歸測試")
    return 0


def check_tests(root: Path, runner: str) -> int:
    if runner == "direct":
        return check_tests_direct(root)
    if runner == "pytest":
        return check_tests_pytest(root)

    probe = run([sys.executable, "-m", "pytest", "--version"], root)
    if probe.returncode == 0:
        print("[INFO] auto test runner：pytest")
        return check_tests_pytest(root)
    print("[INFO] auto test runner：direct，pytest 不可用")
    return check_tests_direct(root)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the codex-skill-conventions delivery gate.")
    parser.add_argument("root", nargs="?", default=".", help="Skill root directory.")
    parser.add_argument("--test-runner", choices=["auto", "pytest", "direct"], default="auto")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    if not root.is_dir():
        return fail(f"不是目錄：{root}")

    rc = 0
    rc |= check_structure(root)
    rc |= check_agents_metadata(root)
    rc |= check_contract_terms(root)
    rc |= check_tests(root, args.test_runner)
    rc |= check_punctuation(root)
    if rc == 0:
        print("結果：in-skill gate 通過。")
    else:
        print("結果：in-skill gate 失敗。")
    return 0 if rc == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
