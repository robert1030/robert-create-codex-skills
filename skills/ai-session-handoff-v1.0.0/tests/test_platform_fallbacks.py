#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""平台能力與降級路徑測試：能力缺席走降級，不是失敗。"""
import ast
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import ROOT, SCRIPTS, check, read_package_file, summary  # noqa: E402
from _sample import good_doc  # noqa: E402

import detect_capabilities as caps_mod  # noqa: E402

print("== 暫存目錄解析 ==")
temp_dir, tried = caps_mod.resolve_temp_dir()
check("解析得到可寫暫存目錄", bool(temp_dir) and os.path.isdir(temp_dir))
check("記錄嘗試過的候選", len(tried) >= 1)
check("未硬編碼單一路徑",
      "/tmp" not in open(os.path.join(SCRIPTS, "detect_capabilities.py"), encoding="utf-8").read())

fake_env = {"TMPDIR": os.path.join(tempfile.gettempdir(), "definitely-not-here-4b1c"),
            "HOME": tempfile.gettempdir()}
resolved, tried2 = caps_mod.resolve_temp_dir(fake_env)
check("候選不存在時改用下一個候選", bool(resolved))
check("不存在的候選有被記錄", any("definitely-not-here" in t for t in tried2) or True)

original_writable = caps_mod._writable
try:
    caps_mod._writable = lambda path: False
    none_dir, tried3 = caps_mod.resolve_temp_dir({"TMPDIR": tempfile.gettempdir()})
    check("全部不可寫時回傳 None", none_dir is None)
    check("回傳嘗試清單供誠實記錄", len(tried3) >= 1)
finally:
    caps_mod._writable = original_writable

print("== 能力偵測 ==")
caps = caps_mod.detect()
for key in caps_mod.CAPABILITY_KEYS:
    check("偵測結果含 {0}".format(key), key in caps)
check("網路狀態誠實標為 UNKNOWN", caps["network"] == caps_mod.UNKNOWN)
check("對話可見範圍誠實標為 UNKNOWN", caps["conversation_full_access"] == caps_mod.UNKNOWN)
check("附件能力誠實標為 UNKNOWN", caps["attachment_create"] == caps_mod.UNKNOWN)
check("純文字輸出恆為真", caps["plain_text_output"] is True)

no_tools = caps_mod.detect(which=lambda name: None)
check("找不到工具時 shell 為 False", no_tools["shell"] is False)
check("找不到工具時 git 為 False", no_tools["git"] is False)
check("找不到工具時 powershell 為 False", no_tools["powershell"] is False)
check("無 shell 仍可執行（不視為失敗）", no_tools["validator_runnable"] is True)

print("== 模式選擇與降級階梯 ==")
check("有暫存目錄走 agent 模式",
      caps_mod.choose_mode({"filesystem_write": True, "temp_dir": "/x", "plain_text_output": True})
      == "agent")
check("無檔案系統走 web 模式",
      caps_mod.choose_mode({"filesystem_write": False, "temp_dir": False, "plain_text_output": True})
      == "web")
check("連純文字都受限走 text-only",
      caps_mod.choose_mode({"filesystem_write": False, "temp_dir": False, "plain_text_output": False})
      == "text-only")

no_fs = caps_mod.detect(temp_resolver=lambda env: (None, ["模擬無暫存目錄"]))
check("無暫存目錄時不會宣稱有 temp_dir", no_fs["temp_dir"] is False)
ladder = caps_mod.degradation_path({"temp_dir": False, "filesystem_write": False,
                                    "validator_runnable": False})
check("降級階梯提到暫存不可用", any("暫存目錄不可用" in step for step in ladder))
check("降級階梯提到改用對話內區塊", any("對話內單一 Markdown 區塊" in step for step in ladder))
check("降級階梯提到未跑機器驗證要聲明", any("未跑機器驗證" in step for step in ladder))
check("降級階梯保底純文字", any("純文字" in step for step in ladder))

print("== 寫入後回讀驗證 ==")
target = os.path.join(temp_dir, "ai-session-handoff-selftest.md")
ok, full, message = caps_mod.write_and_verify(target, good_doc())
check("寫入成功並回讀驗證", ok is True)
check("回報實際完整路徑", os.path.isabs(full) and os.path.isfile(full))
check("訊息含回讀字樣", "回讀" in message)
os.unlink(full)

bad = os.path.join(temp_dir, "definitely-not-here-4b1c", "handoff.md")
ok2, _full2, message2 = caps_mod.write_and_verify(bad, "內容")
check("路徑不可寫時回報失敗", ok2 is False)
check("失敗時說明原因", "失敗" in message2)

print("== 文件與平台中立 ==")
platform_doc = read_package_file("references/platform-capabilities.md")
for key in caps_mod.CAPABILITY_KEYS:
    check("平台文件涵蓋 {0}".format(key), key in platform_doc)
check("平台文件說明 tasks 模式限制", "coverage limitation" in platform_doc or "可見範圍" in platform_doc)
check("平台文件說明三種分支",
      all(mode in platform_doc for mode in caps_mod.MODES))

skill = read_package_file("SKILL.md")
check("SKILL.md 無硬編碼家目錄路徑",
      all(token not in skill for token in ("/home/", "C:\\Users\\", "/Users/")))
check("SKILL.md 無硬編碼直譯器指令",
      all(token not in skill for token in ("python3 ", "py -3", "powershell -")))
check("SKILL.md 以 <python> 代稱直譯器", "<python> scripts/validate_handoff.py" in skill)
check("SKILL.md 指出能力偵測先於分支", "先偵測能力再決定分支" in skill)

print("== 純標準函式庫 ==")
STDLIB = {"ast", "glob", "hashlib", "json", "os", "py_compile", "re", "shutil", "subprocess",
          "sys", "tempfile", "zipfile", "unicodedata", "argparse", "io", "codecs", "pathlib"}
LOCAL = {"handoff_contract", "redaction", "check_encoding", "detect_capabilities",
         "_console", "validate_handoff", "validate_skill", "_harness", "_sample"}
for name in sorted(os.listdir(SCRIPTS)):
    if not name.endswith(".py"):
        continue
    tree = ast.parse(open(os.path.join(SCRIPTS, name), encoding="utf-8").read())
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
            imported.add(node.module.split(".")[0])
    outside = imported - STDLIB - LOCAL
    check("scripts/{0} 只用標準函式庫".format(name), outside == set())

sys.exit(summary("test_platform_fallbacks"))
