#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""回歸測試：session-handoff。執行：python3 tests/test_handoff.py
純文字型 skill，無重相依，全部測試皆可離線跑。"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(ROOT, "scripts"))

PASS = 0
FAIL = 0


def check(name, cond):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  [PASS] {name}")
    else:
        FAIL += 1
        print(f"  [FAIL] {name}")


import check_handoff  # noqa: E402

# 1) 凍結契約守門
try:
    check_handoff.assert_frozen()
    check("凍結雜湊守門（未被動過）", True)
except RuntimeError:
    check("凍結雜湊守門（未被動過）", False)

check("九節數量", len(check_handoff.HEADINGS) == 9)
check("第〇節標題凍結值", check_handoff.HEADINGS[0] == "〇、啟動指令（給下一個 session）")
check("第八節標題凍結值", check_handoff.HEADINGS[-1] == "八、未決事項與風險")

# 2) 建一份完整合格樣本（第〇節須過三條閘門：字數、編號、首條錨詞）
BOOT_OK = "你是接手本工作的新 session。請依序執行：①完整讀完本文件再回應；②載入第四節紀律；③嚴守第五第六節契約；④從第一節下一步接手。"
GOOD = "# Session 交接摘要｜測試｜2026-07-15\n\n" + "".join(
    f"## {h}\n\n{BOOT_OK if h == check_handoff.HEADINGS[0] else '本節有實質內容。'}\n\n"
    for h in check_handoff.HEADINGS
)


def run_check(content):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(content)
        path = f.name
    try:
        return check_handoff.check(path)
    finally:
        os.unlink(path)


check("完整樣本通過", run_check(GOOD) == [])

# 3) 缺節擋
bad = GOOD.replace("## 五、邊界與禁區\n\n本節有實質內容。\n\n", "")
check("缺節被擋", any("缺少章節" in e for e in run_check(bad)))

# 4) 順序錯擋
lines = GOOD
swapped = lines.replace("## 一、任務身分卡", "##TMP").replace(
    "## 二、核心脈絡", "## 一、任務身分卡").replace("##TMP", "## 二、核心脈絡")
check("順序錯被擋", run_check(swapped) != [])

# 5) 空節擋
empty = GOOD.replace("## 二、核心脈絡\n\n本節有實質內容。", "## 二、核心脈絡\n")
check("空節被擋", any("空節" in e for e in run_check(empty)))

# 6) 佔位符擋（TODO 與樣板角括號）
todo = GOOD.replace("本節有實質內容。", "TODO 之後補", 1)
check("TODO 佔位符被擋", any("佔位符" in e for e in run_check(todo)))
ph = GOOD.replace("本節有實質內容。", "〈一句話主題〉", 1)
check("樣板角括號被擋", any("佔位符" in e for e in run_check(ph)))

# 7) fenced code 內的 TODO 不誤殺
fenced = GOOD + "\n```python\n# TODO: code 裡的不算\n```\n"
check("程式碼區塊內 TODO 放行", run_check(fenced) == [])

# 8) validate_punct：乾淨過、髒的擋、破折號擋、連字號放行
VP = os.path.join(ROOT, "scripts", "validate_punct.py")


def run_vp(content):
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
        f.write(content)
        path = f.name
    try:
        return subprocess.run([sys.executable, VP, path], capture_output=True).returncode
    finally:
        os.unlink(path)


check("標點驗證：全形乾淨過", run_vp("這是一句全形標點，沒有問題。\n") == 0)
check("標點驗證：半形夾中文擋", run_vp("這是半形,錯誤示範\n") != 0)
check("標點驗證：破折號擋", run_vp("這裡有破折號——不行\n") != 0)
check("標點驗證：半形連字號放行", run_vp("UTF-8 與 2023-2024 都合法\n") == 0)

# 8.5) 第〇節閘門 a：200 字上限（維持編號與錨詞合規，只灌長度）
pad = "多餘冗長說明" * 30
long_boot = GOOD.replace(BOOT_OK, BOOT_OK[:-1] + pad + "。")
check("第〇節超過 200 字被擋", any("過長" in e for e in run_check(long_boot)))
check("第〇節合規長度放行", run_check(GOOD) == [])

# 8.51) 閘門 b：編號條目不足被擋
no_num = GOOD.replace(BOOT_OK, "先讀完本文件再回應，然後載入紀律，嚴守契約，從下一步接手。")
check("第〇節無編號被擋", any("編號條目不足" in e for e in run_check(no_num)))
two_num = GOOD.replace(BOOT_OK, "①先讀完本文件再回應；②載入紀律後接手。")
check("第〇節僅兩條編號被擋", any("編號條目不足" in e for e in run_check(two_num)))

# 8.52) 閘門 c：首條缺錨詞被擋
no_anchor = GOOD.replace(BOOT_OK, "①載入第四節紀律；②讀完本文件再回應；③嚴守契約；④接手。")
check("第〇節首條缺錨詞被擋", any("缺錨詞" in e for e in run_check(no_anchor)))
half_anchor = GOOD.replace(BOOT_OK, "①先讀完本文件；②再回應使用者；③嚴守契約；④接手。")
check("第〇節首條錨詞不齊被擋", any("缺錨詞" in e for e in run_check(half_anchor)))

# 8.53) 阿拉伯數字編號式也放行
arabic = GOOD.replace(BOOT_OK, "1. 先讀完本文件再回應\n2. 載入第四節紀律\n3. 嚴守契約並從下一步接手")
check("阿拉伯數字編號放行", run_check(arabic) == [])

# 8.55) 平台中立：SKILL.md 不得寫死平台路徑與直譯器指令
sk_body = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
check("SKILL.md 無寫死 /home/claude 路徑", "/home/claude" not in sk_body)
check("SKILL.md 驗證指令用 <python> 代稱", "<python> scripts/check_handoff.py" in sk_body)

# 8.6) 平台中立：出處分級標籤不得綁定單一模型名
tpl = open(os.path.join(ROOT, "references", "handoff-template.md"), encoding="utf-8").read()
check("模板使用平台中立標籤", "【AI 建議未確認】" in tpl and "【Claude" not in tpl)
sk = open(os.path.join(ROOT, "SKILL.md"), encoding="utf-8").read()
check("SKILL.md 使用平台中立標籤", "【AI 建議未確認】" in sk and "【Claude" not in sk)

# 8.7) ChatGPT Web 與 Codex 共用 metadata 契約
check("SKILL.md 名稱為 gpt-session-handoff", "name: gpt-session-handoff" in sk)
openai_yaml = os.path.join(ROOT, "agents", "openai.yaml")
metadata_exists = os.path.isfile(openai_yaml)
check("agents/openai.yaml 存在", metadata_exists)
metadata = open(openai_yaml, encoding="utf-8").read() if metadata_exists else ""
check(
    "ChatGPT Web metadata 齊全",
    all(key in metadata for key in ["display_name:", "short_description:", "icon:", "accent_color:"]),
)
check(
    "Codex metadata 齊全",
    all(key in metadata for key in ["brand_color:", "default_prompt:"]),
)
check("允許隱式觸發", "allow_implicit_invocation: true" in metadata)
check("預設提示引用正確 skill 名稱", "$gpt-session-handoff" in metadata)
check("Windows UTF-8 執行指引存在", '$env:PYTHONUTF8 = "1"' in sk)
check("Linux python3 流程保留", "python3" in sk)

# 9) 本包自身文件也守標點鐵則
for doc in ["SKILL.md", "FROZEN.md", os.path.join("references", "handoff-template.md")]:
    rc = subprocess.run([sys.executable, VP, os.path.join(ROOT, doc)], capture_output=True).returncode
    check(f"自身文件標點乾淨：{doc}", rc == 0)

print(f"\n結果：{PASS} passed, {FAIL} failed")
sys.exit(0 if FAIL == 0 else 1)
