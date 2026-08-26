#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""人話化候選清單過濾器：套用保護清單第一層九項規則，命中即剔除。

設計原理：speak-human-tw 的人話化改寫是文字層面的自由動作，
ai-session-handoff 的九節骨架卻依賴精確字串與結構被機器驗證
（見 scripts/validate_handoff.py、scripts/handoff_contract.py）。
本腳本在「第一輪清單生成」之前先跑，把注定會撞上結構閘門的候選項
自動剔除，不留給使用者去勾選一個必然導致驗證失敗的選項。

只做過濾，不做改寫；不引入外部套件；退出碼恆為 0（過濾本身不是失敗）。

用法：
  <python> scripts/humanize_filter.py <candidates.json>
  candidates.json 格式：
    [{"location": "...", "original": "...", "reason": "...", "suggestion": "..."}, ...]
  輸出：
    {"kept": [...], "removed": [{"item": {...}, "hit_rule": "..."}]}
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import handoff_contract as contract  # noqa: E402

# --- 保護清單第一層九項，逐項對應 handoff_contract.py 的凍結常數 ---

# 下一行的正規表達式含半形句點與半形右括號，是字元類別語法本身，用來比對候選
# 清單裡真實出現的半形阿拉伯數字編號記號，與 validate_handoff.py 既有的
# NUMBER_MARK 同一套模式。這是程式碼字面量，不是中文散文裡的標點，改成全形
# 會讓比對邏輯失效；純 .py 原始碼不在 validate_punct.py 的圍欄跳過範圍內，
# 這是既有已知落差（validate_handoff.py 本身也有同樣情況），非本次新增問題。
NUMBER_MARK = re.compile(r"[①-⑳]|(?:^|\n)[ \t]*\d+[.、\)]")


def _hits_heading(text):
    """規則一：九節標題文字（含順序在內，逐字比對）。"""
    for heading in contract.HEADINGS:
        if heading in text:
            return "九節標題文字「{0}」不可被人話化改寫".format(heading)
    return None


def _hits_status_tag(text):
    """規則二：狀態標記字面（五級事實標記＋遮蔽標記）。"""
    for tag in contract.ALLOWED_BRACKET_TOKENS:
        if tag in text:
            return "狀態標記「{0}」不可被移除或改寫成同義詞".format(tag)
    return None


def _hits_empty_section(text):
    """規則三：「本節無內容。」固定句。"""
    if contract.EMPTY_SECTION_TEXT in text:
        return "固定句「{0}」不可被改寫成其他說法".format(contract.EMPTY_SECTION_TEXT)
    return None


def _hits_coverage_marker(text):
    """規則四：「脈絡涵蓋」四字（第八節必填欄位字串）。"""
    if contract.COVERAGE_MARKER in text:
        return "欄位名稱「{0}」為驗證器逐字比對依據，不可改寫".format(contract.COVERAGE_MARKER)
    return None


def _hits_boot_anchors(text):
    """規則五：第〇節錨詞，「讀」與「再回應」同時出現時視為命中。"""
    if all(anchor in text for anchor in contract.BOOT_ANCHORS):
        return "同時含錨詞「{0}」與「{1}」，屬第〇節首條判定依據，不可改寫".format(
            *contract.BOOT_ANCHORS)
    return None


def _hits_boot_length_or_count(item, section_hint):
    """規則六：第〇節編號條目數量與字數上限。

    「候選項自己開頭帶編號符號」不等於「套用後整節條數不足」，單純換掉某一條
    的措辭、保留編號位置，並不會讓整節少於下限。真正該剔除的只有兩種情況：
    （ａ）建議改法本身把編號符號拿掉（去編號動作，會讓條數判定失準）；
    （ｂ）建議改法字數已超過整節二百字上限。
    這裡改吃整個候選項 dict，才能分別檢查 original 是否帶編號、suggestion 是否仍帶編號。
    """
    if not (section_hint and contract.HEADINGS[0] in section_hint):
        return None

    original = str(item.get("original", ""))
    suggestion = str(item.get("suggestion", ""))

    original_has_mark = bool(NUMBER_MARK.search(original))
    suggestion_has_mark = bool(NUMBER_MARK.search(suggestion))
    if original_has_mark and not suggestion_has_mark:
        return "建議改法拿掉了原句的編號符號，位於第〇節，該節要求至少 {0} 條編號，去編號動作會讓條數判定失準".format(
            contract.BOOT_MIN_ITEMS)

    n = len(re.sub(r"\s", "", suggestion)) if suggestion else len(re.sub(r"\s", "", original))
    if n > contract.BOOT_MAX_CHARS:
        return "候選項的建議改法長度已達 {0} 字，位於第〇節（{1} 字上限），拉長敘述會違反上限".format(
            n, contract.BOOT_MAX_CHARS)
    return None


def _hits_decision_status_line(text, section_hint):
    """規則七：第七節（已確認的對話決議）逐條決議需要狀態標記，同規則二覆蓋，
    此處額外標記出處以利使用者理解為何被擋。"""
    if section_hint and contract.HEADINGS[contract.DECISION_SECTION_INDEX] in section_hint:
        for tag in contract.STATUS_TAGS:
            if tag in text:
                return "第七節決議行帶有狀態標記「{0}」，標記本身與其緊鄰的限定語不可被稀釋".format(tag)
    return None


def _hits_artifact_status_line(text, section_hint):
    """規則八：第三節 artifact 引用行需要狀態標記。"""
    idx = contract.ARTIFACT_SECTION_INDEXES[0]
    if section_hint and contract.HEADINGS[idx] in section_hint:
        for tag in contract.STATUS_TAGS:
            if tag in text:
                return "第三節 artifact 引用行帶有狀態標記「{0}」，防止虛構或未驗證宣稱被潤稿掉".format(tag)
    return None


def _hits_redaction_rewrite(text):
    """規則九：[REDACTED] 不可被改寫成委婉同義詞（例如「已隱藏」「已省略」）。"""
    if contract.REDACTION_MARK in text:
        return "遮蔽標記「{0}」不可被改寫成委婉說法，會被判定為非法方括號標記".format(
            contract.REDACTION_MARK)
    return None


RULES = (
    _hits_heading,
    _hits_status_tag,
    _hits_empty_section,
    _hits_coverage_marker,
    _hits_boot_anchors,
    _hits_redaction_rewrite,
)

# 需要 section_hint 的規則在 filter_candidates() 內直接呼叫；
# _hits_boot_length_or_count 的參數依序為 item、section_hint，與另外兩個
# 依序為 text、section_hint 不同，不放進同一個可迭代 tuple 裡統一呼叫，避免誤用。


def filter_candidates(candidates):
    """回傳 kept 與 removed 兩個清單。removed 為 [{"item": ..., "hit_rule": ...}]。

    規則一（九節標題）只比對 original／suggestion 內文，不比對 location：
    location 欄位本身就是「候選項屬於哪一節」的合法標記，必然含九節標題之一，
    若把 location 併入比對文字，規則一會對每一筆都誤判命中，等於全數剔除、
    過濾器形同虛設（房規二所稱「閘門要有牙齒」的反例：規則過寬導致自我循環）。
    section_hint 仍取自 location，供 SECTION_AWARE_RULES 判斷候選項所屬章節。
    """
    kept = []
    removed = []
    for item in candidates:
        content_text = " ".join(str(item.get(k, "")) for k in ("original", "suggestion"))
        section_hint = str(item.get("location", ""))

        hit = None
        for rule in RULES:
            hit = rule(content_text)
            if hit:
                break
        if not hit:
            hit = _hits_boot_length_or_count(item, section_hint)
        if not hit:
            for rule in (_hits_decision_status_line, _hits_artifact_status_line):
                hit = rule(content_text, section_hint)
                if hit:
                    break

        if hit:
            removed.append({"item": item, "hit_rule": hit})
        else:
            kept.append(item)
    return kept, removed


def main(argv):
    from _console import configure_console
    configure_console()
    if len(argv) != 1:
        print("用法：python scripts/humanize_filter.py <candidates.json>")
        return 2
    path = argv[0]
    try:
        with open(path, "r", encoding="utf-8") as f:
            candidates = json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        print("[FAIL] 無法讀取或解析候選清單：{0}".format(exc))
        return 1

    kept, removed = filter_candidates(candidates)
    result = {"kept": kept, "removed": removed}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print("")
    print("[OK] 過濾完成：保留 {0} 項可勾選候選、剔除 {1} 項命中保護清單。".format(
        len(kept), len(removed)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
