#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Invocation 與流程契約測試。

誠實聲明：真正的觸發行為由宿主模型決定，無法在本機以程式驗證。
本檔驗的是可靜態檢查的必要條件（description 是否涵蓋各個 branch、
是否堆疊同義詞、是否寫出不該觸發的界線、流程是否每步都有完成條件）。
實際觸發驗證屬人工測試，結果記錄在發行目錄的 04 驗證報告。
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import check, read_package_file, summary  # noqa: E402

import handoff_contract as contract  # noqa: E402

skill = read_package_file("SKILL.md")
front = re.match(r"^---\n(.*?)\n---\n", skill, flags=re.DOTALL)
frontmatter = front.group(1) if front else ""
desc_match = re.search(r'description:\s*"(.*)"\s*$', frontmatter, flags=re.DOTALL)
description = desc_match.group(1) if desc_match else ""

print("== description 契約 ==")
check("frontmatter 有 name", "name: {0}".format(contract.SKILL_NAME) in frontmatter)
check("有 description（model-invoked）", len(description) > 0)
check("未設 disable-model-invocation", "disable-model-invocation" not in frontmatter)
check("leading word 前置", description.lower().startswith("handoff"))
check("description 長度受控（{0} 字）".format(len(description)), len(description) <= 400)

BRANCHES = {
    "session 交接": ("session 交接", "handoff"),
    "context 快滿換新對話": ("context 快滿",),
    "換另一個 agent 或平台接手": ("另一個 agent",),
    "保存工作狀態供延續": ("保存下來", "延續"),
}
for branch, keywords in BRANCHES.items():
    check("涵蓋 branch：{0}".format(branch), any(k in description for k in keywords))

check("寫出不該觸發的界線", "不適用" in description)
for word, limit in (("交接", 2), ("handoff", 2), ("摘要", 2)):
    occurrences = description.count(word)
    check("無同義詞堆疊：{0} 出現 {1} 次".format(word, occurrences), occurrences <= limit)

print("== 呼叫參數 ==")
step1 = skill.split("## Step 2")[0]
for label in ("下一個 session 的用途", "下一步焦點", "目標 agent 或平台",
              "輸出路徑", "詳細程度", "交接範圍"):
    check("Step 1 決策表含：{0}".format(label), label in step1)
check("缺參數不中斷流程", "缺參數採安全預設" in step1)
check("多主題混雜才停下問一題", "多主題混雜" in step1)

print("== 流程完成條件 ==")
steps = re.findall(r"^## Step (\d)：(.+)$", skill, flags=re.M)
check("六個步驟齊備", [s[0] for s in steps] == ["1", "2", "3", "4", "5", "6"])
# v1.1.0：允許 Step N.5 這類子步驟（例如 Step 5.5）額外存在完成條件，
# 只要主線六個 Step 各自仍有一次即可；子步驟數量不設上限，因為子步驟
# 本身是否該有完成條件屬於流程設計判斷，不該被計數規則反過來限制設計。
main_step_markers = re.findall(r"^## Step \d：", skill, flags=re.M)
substep_markers = re.findall(r"^## Step \d\.\d：", skill, flags=re.M)
completion_count = skill.count("**完成條件**")
check("每步都有完成條件",
      completion_count == len(main_step_markers) + len(substep_markers))
check("Step 2 建立 evidence map", "evidence map" in skill)
check("Step 3 採引用而非複製", "引用 artifact，不要複製 artifact" in skill)
check("Step 5 列出五級狀態標記", all(tag in skill for tag in contract.STATUS_TAGS))
check("Step 6 依能力輸出三種分支",
      all(mode in skill for mode in ("agent 模式", "web 模式", "tasks 模式")))
check("驗證非 0 不得請示放行", "不得請示放行" in skill)
check("交付後問滿意度", "是否滿意" in skill)

print("== 硬規則與邊界 ==")
check("不虛構 artifact", "不虛構 artifact" in skill)
check("不替使用者做新決定", "不替使用者做新決定" in skill)
check("不跨對話", "只交接當前對話" in skill)
check("凍結項另開新版", "另開 major 版本" in skill)
check("誠實聲明：沒跑過或沒通過的測試不得寫成完成",
      "沒跑過的命令" in skill and "沒通過的測試" in skill)
check("條件式參考有明確讀取時機", skill.count("| 何時讀 | 讀什麼 |") == 1)

print("== 參考檔位置與載入降級 ==")
check("明講 pointer 基準為 skill 根目錄", "本 skill 的根目錄" in skill)
check("排除當前工作目錄與專案目錄的誤解",
      "不是當前工作目錄" in skill and "使用者的專案目錄" in skill)
check("寫出讀不到參考檔時的降級行為", "讀不到" in skill and "降級，不是中止理由" in skill)
check("降級後結構不變", "結構與讀得到時完全相同" in skill)
check("要求產出的路徑可被下一個 agent 解析",
      "skill 名稱 ＋ 檔案名" in skill and "不留沒有基準的相對路徑" in skill)

# Web Chat 只載入 SKILL.md 的情境：本檔必須自足到能產出通過驗證的九節文件。
print("== SKILL.md 自足性（只載入本檔也能產出）==")
for element, probe in [
    ("九節標題", all(h in skill for h in contract.HEADINGS)),
    ("第〇節三條閘門門檻", "200 字" in skill and "三個編號條目" in skill
     and all(a in skill for a in contract.BOOT_ANCHORS)),
    ("五級狀態標記", all(tag in skill for tag in contract.STATUS_TAGS)),
    ("遮蔽標記", contract.REDACTION_MARK in skill),
    ("不適用章節寫法", contract.EMPTY_SECTION_TEXT in skill),
    ("第八節脈絡涵蓋欄", contract.COVERAGE_MARKER in skill),
    ("web 模式交付形式", "fenced code block" in skill and "四個反引號" in skill),
    ("artifact 引用紀律", "引用 artifact，不要複製 artifact" in skill),
]:
    check("自足性：{0}".format(element), probe)
for ref in ("references/output-contract.md", "references/platform-capabilities.md",
            "references/encoding-policy.md", "references/redaction-policy.md",
            "references/examples.md", "schemas/handoff.schema.json"):
    check("指向 {0}".format(ref), "`{0}`".format(ref) in skill)

sys.exit(summary("test_invocation"))
