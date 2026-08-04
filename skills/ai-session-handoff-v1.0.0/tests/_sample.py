#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生合格交接文件樣本，供多支測試共用（避免各自複製一份樣本）。"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "scripts"))

import handoff_contract as contract  # noqa: E402

BOOT_OK = ("你是接手本工作的新 session。請依序執行：①完整讀完本文件再回應；"
           "②載入第四節列出的紀律；③嚴守第六節凍結項；④從第一節的下一步接手。")

BODIES = {
    0: BOOT_OK,
    3: ("- 已完成：驗證器 `scripts/validate_handoff.py`｜結構閘門｜實測退出碼 0 [CONFIRMED]\n"
        "- 被阻塞：雲端流程 `ci/pipeline.yaml`｜缺執行權限 [BLOCKED]"),
    7: ("- 以退出碼為唯一閘門｜原因：人工檢查會漏｜影響：全部交付路徑｜可重新討論：否 [CONFIRMED]\n"
        "- 標記採 ASCII 方括號｜原因：便於機器比對｜影響：模板｜可重新討論：是 [INFERRED]"),
    8: ("- 待使用者決定：是否接進提交前掛鉤 [UNVERIFIED]\n"
        "- 脈絡涵蓋：本對話全程可見，來源時間 2026-08-04。"),
}

DEFAULT_BODY = "本節有實質內容。"


def good_doc(overrides=None):
    """回傳一份通過全部結構閘門的樣本；overrides 以節索引覆寫內容。"""
    overrides = overrides or {}
    parts = ["# Session 交接摘要｜測試樣本｜2026-08-04\n"]
    for index, heading in enumerate(contract.HEADINGS):
        body = overrides.get(index, BODIES.get(index, DEFAULT_BODY))
        parts.append("## {0}\n\n{1}\n".format(heading, body))
    return "\n".join(parts)
