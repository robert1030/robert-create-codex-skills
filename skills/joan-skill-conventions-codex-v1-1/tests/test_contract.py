#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Contract regression tests for joan-skill-conventions-codex-v1-1."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")

PASS = 0
FAIL = 0

def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"[PASS] {name}")
    else:
        FAIL += 1
        print(f"[FAIL] {name}")

check("frontmatter name is versioned", "name: joan-skill-conventions-codex-v1-1" in skill)
check("description forces validator and regression tests", "必須同步設計、建立或更新驗證器與回歸測試" in skill)
check("trigger includes create inspect upgrade refactor", all(x in skill for x in ["新開", "檢視", "升級", "重構"]))
check("mandatory flow exists", "驗證測試強制流程" in skill)
check("minimum tests section exists", "tests/test_*.py 最低覆蓋範圍" in skill)
check("validation script exists in scripts", (ROOT / "scripts" / "validate_punct.py").exists())
check("frozen contract exists", (ROOT / "FROZEN.md").exists())
check("agents metadata exists", (ROOT / "agents" / "openai.yaml").exists())
check("no unicode em or en dash in SKILL.md", not re.search("[\u2013\u2014]", skill))

print(f"Result: {PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
