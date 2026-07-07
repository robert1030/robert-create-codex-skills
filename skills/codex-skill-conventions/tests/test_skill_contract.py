#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contract tests for GPT v1.6.1 fidelity in codex-skill-conventions.

These tests are pytest-compatible and directly executable with：

    python tests/test_skill_contract.py
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "SKILL.md").read_text(encoding="utf-8")
FROZEN = (ROOT / "FROZEN.md").read_text(encoding="utf-8")
TRACE = (ROOT / "references" / "migration-traceability.md").read_text(encoding="utf-8")
ACCEPT = (ROOT / "references" / "acceptance-checklists.md").read_text(encoding="utf-8")

REQUIRED_IN_SKILL = [
    "v1.6.1-codex",
    "gpt-skill-conventions v1.6.1",
    "No-abstraction default",
    "Codex-Desktop（Windows）",
    "codex-cli（Windows）",
    "codex-cli（Linux）",
    "CLI prompt format",
    "請輸入 A、B、C，或直接輸入你的需求。",
    "Interactive recommendation flow",
    "Acceptance prompt template",
    "Page truncation",
    "Overflow greater than 2px",
    "constructivist `check_pages.py`",
    "Math correctness",
    "SymPy",
    "Mismatch is a hard block",
    "Answer correctness must never rely on eyesight",
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
    "tests/test_skill_contract.py",
]

REQUIRED_IN_FROZEN = [
    "No-abstraction rule",
    "Page truncation gate",
    "constructivist `check_pages.py`",
    "Math correctness gate",
    "constructivist `check_math.py`",
    "cornell `verify_math.py`",
    "KaTeX gate",
    "`check_katex.py`",
    "Domain gate",
    "cornell `verify_structures.py`",
    "Bootstrap gate",
    "Layout measurement gate",
    "kmap `measure_bands.py`",
    "Regression test contract",
    "Skill gate runner",
    "Contract tests",
    "CLI interaction",
    "Traceability",
]

REQUIRED_IN_TRACE = [
    "Page truncation",
    "`check_pages.py`",
    "Math correctness",
    "`check_math.py`",
    "`verify_math.py`",
    "KaTeX rendering",
    "`check_katex.py`",
    "Domain correctness",
    "`verify_structures.py`",
    "Regression self-tests",
    "Bootstrap tests",
    "Layout measurement",
    "`measure_bands.py`",
    "Non-equivalent or Platform-Converted Items",
]

REQUIRED_IN_ACCEPTANCE = [
    "v1.6.1 named gate acceptance",
    "`check_pages.py`",
    "`check_math.py`",
    "`verify_math.py`",
    "`check_katex.py`",
    "`verify_structures.py`",
    "`measure_bands.py`",
    "CLI option input",
]


def missing_items(text: str, required: list[str], source_name: str) -> list[str]:
    return [f"{source_name} missing：{needle}" for needle in required if needle not in text]


def test_skill_contains_full_gpt_v161_contract_terms():
    missing = missing_items(SKILL, REQUIRED_IN_SKILL, "SKILL.md")
    assert not missing, "\n".join(missing)


def test_frozen_contains_non_abstraction_contract():
    missing = missing_items(FROZEN, REQUIRED_IN_FROZEN, "FROZEN.md")
    assert not missing, "\n".join(missing)


def test_traceability_contains_required_rule_units():
    missing = missing_items(TRACE, REQUIRED_IN_TRACE, "migration-traceability.md")
    assert not missing, "\n".join(missing)


def test_acceptance_checklist_contains_named_gates_and_cli_ui():
    missing = missing_items(ACCEPT, REQUIRED_IN_ACCEPTANCE, "acceptance-checklists.md")
    assert not missing, "\n".join(missing)


def _run_direct() -> int:
    tests = [
        test_skill_contains_full_gpt_v161_contract_terms,
        test_frozen_contains_non_abstraction_contract,
        test_traceability_contains_required_rule_units,
        test_acceptance_checklist_contains_named_gates_and_cli_ui,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print(f"[PASS] {test.__name__}")
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f"[FAIL] {test.__name__}: {exc}")
    print(f"結果：{len(tests) - len(failures)} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(_run_direct())
