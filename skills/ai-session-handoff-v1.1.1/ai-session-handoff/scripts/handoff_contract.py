#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ai-session-handoff 的凍結契約與共用常數：本檔是唯一真實來源。

SKILL.md、references/output-contract.md、schemas/handoff.schema.json 三處的
章節清單與狀態標記，皆由 scripts/validate_skill.py 比對本檔，任一漂移即失敗。
要改章節結構一律另開新版（major），不就地修改本檔。
"""
import hashlib
import json

SKILL_NAME = "ai-session-handoff"
VERSION = "1.1.1"

# 九節交接骨架：標題文字與順序為 v1.0.0 凍結契約。
HEADINGS = [
    "〇、啟動指令（給下一個 session）",
    "一、任務身分卡",
    "二、核心脈絡",
    "三、工作流現況",
    "四、工作紀律與規範",
    "五、邊界與禁區",
    "六、凍結契約與關鍵閘門",
    "七、已確認的對話決議",
    "八、未決事項與風險",
]

# 對 HEADINGS 做 json.dumps(ensure_ascii=False) 後取 sha256 前 16 碼。
EXPECTED_DIGEST = "7f29cd5d626067c2"

# 第〇節（啟動指令）三條機器閘門的門檻。
BOOT_MAX_CHARS = 200
BOOT_MIN_ITEMS = 3
BOOT_ANCHORS = ("讀", "再回應")

# 事實分級狀態標記：平台中立 ASCII 標記，可被機器驗證。
STATUS_TAGS = (
    "[CONFIRMED]",
    "[INFERRED]",
    "[UNVERIFIED]",
    "[BLOCKED]",
    "[SUPERSEDED]",
)

# 遮蔽標記；[REDACTED] 與 <REDACTED> 語意等價，本套件一律採前者以免被當成 HTML 標籤。
REDACTION_MARK = "[REDACTED]"

# 除狀態標記外，交接文件中合法的全大寫方括號詞彙。
ALLOWED_BRACKET_TOKENS = tuple(STATUS_TAGS) + (REDACTION_MARK,)

# 不適用章節的固定寫法：寫這一句，不得刪節。
EMPTY_SECTION_TEXT = "本節無內容。"

# 第八節必須聲明的可見範圍欄位。
COVERAGE_MARKER = "脈絡涵蓋"

# 需要逐條標示狀態的章節索引（對應 HEADINGS）。
DECISION_SECTION_INDEX = 7          # 七、已確認的對話決議
COVERAGE_SECTION_INDEX = 8          # 八、未決事項與風險
ARTIFACT_SECTION_INDEXES = (3,)     # 三、工作流現況：檔案、URL、commit 等引用集中於此

# 套件必要檔案（相對於套件根目錄）。
REQUIRED_FILES = (
    "SKILL.md",
    "README.md",
    "LICENSE",
    "FROZEN.md",
    "agents/openai.yaml",
    "references/output-contract.md",
    "references/platform-capabilities.md",
    "references/encoding-policy.md",
    "references/redaction-policy.md",
    "references/examples.md",
    "schemas/handoff.schema.json",
    "scripts/_console.py",
    "scripts/handoff_contract.py",
    "scripts/validate_handoff.py",
    "scripts/validate_skill.py",
    "scripts/check_encoding.py",
    "scripts/detect_capabilities.py",
    "scripts/redaction.py",
    "scripts/validate_punct.py",
    "tests/run_all.py",
)


def frozen_digest(headings=None):
    """回傳章節清單的凍結雜湊（sha256 前 16 碼）。"""
    blob = json.dumps(list(headings if headings is not None else HEADINGS),
                      sort_keys=False, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def assert_frozen():
    """章節清單被動過就拋錯：凍結項要改一律另開新版（major）。"""
    got = frozen_digest()
    if got != EXPECTED_DIGEST:
        raise RuntimeError(
            "凍結契約被動到（雜湊 {0} 不等於定版 {1}）。"
            "要改章節結構請另開新版（major），不動凍結項。".format(got, EXPECTED_DIGEST)
        )
