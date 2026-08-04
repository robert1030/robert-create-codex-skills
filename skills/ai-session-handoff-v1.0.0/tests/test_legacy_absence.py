#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""舊版殘留掃描與套件級驗證。

本檔不直接寫出舊名稱字串，改由 scripts/validate_skill.py 以組合方式建構，
避免測試檔自身觸發掃描。
"""
import os
import re
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import ROOT, check, read_package_file, summary  # noqa: E402

import handoff_contract as contract  # noqa: E402
import validate_skill  # noqa: E402

print("== 套件級驗證 ==")
errors = validate_skill.check_package(ROOT)
if not check("套件驗證無錯誤", errors == []):
    for item in errors:
        print("      {0}".format(item))

print("== 舊版殘留掃描 ==")
findings = validate_skill.scan_legacy(ROOT)
if not check("runtime 套件無舊名稱與舊版本殘留", findings == []):
    for item in findings:
        print("      {0}".format(item))

sandbox = tempfile.mkdtemp(prefix="legacy-probe-")
try:
    planted = os.path.join(sandbox, "planted.md")
    with open(planted, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("這份文件提到 {0} 這個舊名稱。\n".format(validate_skill.LEGACY_STRINGS[0]))
    check("掃描器抓得到植入的舊名稱", validate_skill.scan_legacy(sandbox) != [])

    with open(planted, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("這份文件提到舊版本 v1{0}2 的歷史。\n".format("."))
    check("掃描器抓得到植入的舊版本字串", validate_skill.scan_legacy(sandbox) != [])

    with open(planted, "w", encoding="utf-8", newline="\n") as handle:
        handle.write("版本 1.0.0 與數值 1.2 公升不該被誤判。\n")
    check("一般數值不被誤判", validate_skill.scan_legacy(sandbox) == [])
finally:
    shutil.rmtree(sandbox, ignore_errors=True)

print("== 名稱與版本一致 ==")
skill = read_package_file("SKILL.md")
metadata = read_package_file("agents/openai.yaml")
frozen = read_package_file("FROZEN.md")
readme = read_package_file("README.md")

check("SKILL.md 名稱為新名稱", "name: {0}".format(contract.SKILL_NAME) in skill)
check("SKILL.md 版本戳記為 v{0}".format(contract.VERSION), "v" + contract.VERSION in skill)
check("metadata 預設提示引用新名稱", "$" + contract.SKILL_NAME in metadata)
check("metadata 版本正確", 'version: "{0}"'.format(contract.VERSION) in metadata)
check("README 標題為新名稱", contract.SKILL_NAME in readme)
check("FROZEN.md 含新版本條目", "v" + contract.VERSION in frozen)

versions = set(re.findall(r"v\d+\.\d+(?:\.\d+)?", frozen))
check("FROZEN.md 只有一個版本條目（無舊帳）", versions == {"v" + contract.VERSION})
check("FROZEN.md 無 migration 或 release notes 段落",
      all(word not in frozen for word in ("migration", "遷移", "release notes", "升級流程")))
check("FROZEN.md 保留另開新版規則", "另開新版" in frozen)

print("== 無升級機制殘留 ==")
files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".git")]
    files.extend(os.path.join(dirpath, f) for f in filenames)
check("套件內無 migration 檔案",
      not any(re.search(r"migrat|upgrade|changelog|release[-_]note", os.path.basename(f), re.I)
              for f in files))

sys.exit(summary("test_legacy_absence"))
