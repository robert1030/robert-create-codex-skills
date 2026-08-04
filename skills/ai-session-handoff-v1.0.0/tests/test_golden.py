#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Golden fixtures：五組情境的交接文件必須通過驗證並滿足語意期望。

不做整份文字的脆弱比對，而是驗結構、必要語意、狀態正確性與禁止內容。
"""
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import FIXTURES, ROOT, SCRIPTS, check, summary, temp_file  # noqa: E402

import handoff_contract as contract  # noqa: E402
import redaction  # noqa: E402
import validate_handoff  # noqa: E402

VP = os.path.join(SCRIPTS, "validate_punct.py")
SCENARIOS = ["dev", "research", "writing", "troubleshooting", "sensitive"]


def run_punct(path):
    env = dict(os.environ)
    env["PYTHONUTF8"] = "1"
    return subprocess.run([sys.executable, VP, path], capture_output=True, env=env).returncode


check("五組情境齊備", all(os.path.isdir(os.path.join(FIXTURES, s)) for s in SCENARIOS))

for scenario in SCENARIOS:
    base = os.path.join(FIXTURES, scenario)
    print("== fixture：{0} ==".format(scenario))

    conv_path = os.path.join(base, "conversation.md")
    hand_path = os.path.join(base, "handoff.md")
    exp_path = os.path.join(base, "expectations.json")
    if not check("{0}：三份素材齊備".format(scenario),
                 all(os.path.isfile(p) for p in (conv_path, hand_path, exp_path))):
        continue

    with open(exp_path, encoding="utf-8") as handle:
        expect = json.load(handle)
    with open(hand_path, encoding="utf-8") as handle:
        doc = handle.read()
    with open(conv_path, encoding="utf-8") as handle:
        conversation = handle.read()

    check("{0}：輸入對話非空".format(scenario), len(conversation.strip()) > 100)

    errors, _warnings = validate_handoff.check(hand_path)
    if not check("{0}：交接文件通過結構驗證".format(scenario), errors == []):
        for item in errors:
            print("      {0}".format(item))
    check("{0}：交接文件通過標點驗證".format(scenario), run_punct(hand_path) == 0)

    missing = [p for p in expect["must_include"] if not re.search(p, doc)]
    if not check("{0}：必要事實齊備".format(scenario), missing == []):
        print("      缺少：{0}".format(missing))

    leaked = [p for p in expect["must_not_include"] if re.search(p, doc)]
    if not check("{0}：禁止內容未出現".format(scenario), leaked == []):
        print("      出現：{0}".format(leaked))

    check("{0}：下一步可執行".format(scenario), bool(re.search(expect["expected_next_step"], doc)))

    absent = [a for a in expect["artifact_references"] if a not in doc]
    if not check("{0}：artifact 引用齊備".format(scenario), absent == []):
        print("      缺少：{0}".format(absent))

    secrets = [p for p in expect["forbidden_values"] if re.search(p, doc)]
    if not check("{0}：無明文秘密".format(scenario), secrets == []):
        print("      洩漏樣式：{0}".format(secrets))
    check("{0}：遮蔽標記數量足夠".format(scenario),
          doc.count(contract.REDACTION_MARK) >= expect["min_redaction_marks"])
    check("{0}：遮蔽掃描乾淨".format(scenario), redaction.scan(doc) == [])

    tags_used = {t for t in contract.STATUS_TAGS if t in doc}
    check("{0}：至少使用三種狀態標記".format(scenario), len(tags_used) >= 3)
    check("{0}：第八節含脈絡涵蓋".format(scenario), contract.COVERAGE_MARKER in doc)

print("== references/examples.md 的範例 ==")
examples_path = os.path.join(ROOT, "references", "examples.md")
with open(examples_path, encoding="utf-8") as handle:
    examples = handle.read()
block = re.search(r"```markdown\n(.*?)\n```", examples, flags=re.DOTALL)
if check("範例區塊存在", block is not None):
    sample_path = temp_file(block.group(1) + "\n")
    try:
        errors, _warnings = validate_handoff.check(sample_path)
        if not check("範例通過結構驗證", errors == []):
            for item in errors:
                print("      {0}".format(item))
        check("範例通過標點驗證", run_punct(sample_path) == 0)
        check("範例九節齊備", all(h in block.group(1) for h in contract.HEADINGS))
    finally:
        os.unlink(sample_path)

sys.exit(summary("test_golden"))
