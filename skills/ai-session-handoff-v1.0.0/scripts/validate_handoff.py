#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交接文件驗證器：驗結構與可驗證的紀律，任一不過退出碼 1。

檢查項（規格見 references/output-contract.md，常數見 scripts/handoff_contract.py）：
  1. 九節凍結標題齊全且順序正確（標題文字一字不差）。
  2. 凍結雜湊未被動過。
  3. 無空節（不適用的節寫「本節無內容。」，不得刪節）。
  4. 無殘留佔位符（TODO／FIXME／待填／〈…〉樣板角括號）。
  5. 第〇節（啟動指令）三條機器閘門：
     a. 內文去除空白後不得超過 200 字元。
     b. 至少三個編號條目（圓圈數字或行首阿拉伯數字）。
     c. 第一個編號條目須同時含錨詞「讀」與「再回應」。
  6. 狀態標記合法：全大寫方括號詞彙必須屬於契約定義的五級狀態或遮蔽標記。
  7. 第七節每條決議都帶狀態標記（防止把推論寫成已確認事實）。
  8. 第八節含「脈絡涵蓋」聲明（誠實交代可見範圍）。
  9. 第三節的 artifact 引用行帶狀態標記（防止虛構檔案與未驗證宣稱）。
 10. 全文無明文秘密（掃描含程式碼區塊）。

涵蓋誠實聲明：本驗證器驗得了結構與紀律形式，驗不了內容是否忠於對話。
「祈使語氣」與「事實是否真的成立」屬人工留意項，不在機器閘門內。

用法：
  python scripts/validate_handoff.py <handoff.md>
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import handoff_contract as contract  # noqa: E402
import redaction  # noqa: E402
from check_encoding import DecodeFailure, read_text  # noqa: E402

PLACEHOLDERS = re.compile(r"TODO|FIXME|待填|〈[^〉]*〉")
BRACKET_TOKEN = re.compile(r"\[[A-Z][A-Z0-9_]{2,}\]")
NUMBER_MARK = re.compile(r"[①-⑳]|^[ \t]*\d+[.、\)]", re.M)
BULLET = re.compile(r"^\s*(?:[-*+]|\d+[.、\)])\s+")
ARTIFACT = re.compile(r"https?://\S+|`[^`\n]*[\\/][^`\n]*`|`[^`\n]+\.[A-Za-z0-9]{1,6}`")


def _strip_fences(text):
    """以等行數空白置換 fenced code，讓行號維持正確。"""
    return re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)


def _sections(lines):
    """回傳 [(lineno, title, body_lines)]，body 不含下一節標題。"""
    found = []
    for i, line in enumerate(lines):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            found.append((i, m.group(1)))
    out = []
    for idx, (lineno, title) in enumerate(found):
        end = found[idx + 1][0] if idx + 1 < len(found) else len(lines)
        out.append((lineno, title, lines[lineno + 1:end]))
    return out


def _body_text(body_lines):
    return "\n".join(l for l in body_lines if not l.strip().startswith("#"))


def check(path):
    """回傳 (errors, warnings)。errors 非空即不得交付。"""
    # allow_bom=False：BOM 與 CRLF 都會回報，交接文件視為警告而非失敗。
    text, enc_issues = read_text(path, allow_bom=False)
    warnings = ["{0}：{1}".format(os.path.basename(path), i) for i in enc_issues]

    stripped = _strip_fences(text)
    lines = stripped.splitlines()
    sections = _sections(lines)
    titles = [t for _, t, _ in sections]
    errors = []

    # 1) 標題齊全且順序正確
    if titles != contract.HEADINGS:
        missing = [h for h in contract.HEADINGS if h not in titles]
        extra = [t for t in titles if t not in contract.HEADINGS]
        if missing:
            errors.append("缺少章節：{0}".format(missing))
        if extra:
            errors.append("多出非凍結章節：{0}".format(extra))
        if not missing and not extra:
            errors.append("章節順序與凍結順序不符")

    # 2) 空節
    for lineno, title, body in sections:
        real = [l for l in body if l.strip() and not l.strip().startswith("#")]
        if not real:
            errors.append("空節：「{0}」（無內容請寫「{1}」）".format(title, contract.EMPTY_SECTION_TEXT))

    # 3) 第〇節三條閘門
    if sections and sections[0][1] == contract.HEADINGS[0]:
        body0 = _body_text(sections[0][2])
        n = len(re.sub(r"\s", "", body0))
        if n > contract.BOOT_MAX_CHARS:
            errors.append("第〇節啟動指令過長（{0} 字大於 {1} 字上限）：請濃縮為編號祈使句".format(
                n, contract.BOOT_MAX_CHARS))
        marks = list(NUMBER_MARK.finditer(body0))
        if len(marks) < contract.BOOT_MIN_ITEMS:
            errors.append("第〇節編號條目不足（{0} 條少於 {1} 條下限）：請改為逐條編號".format(
                len(marks), contract.BOOT_MIN_ITEMS))
        else:
            first_item = body0[marks[0].end():marks[1].start()]
            if not all(anchor in first_item for anchor in contract.BOOT_ANCHORS):
                errors.append("第〇節首條缺錨詞：第一個編號條目須同時含「{0}」與「{1}」".format(
                    *contract.BOOT_ANCHORS))

    # 4) 佔位符
    for lineno, line in enumerate(lines, 1):
        m = PLACEHOLDERS.search(line)
        if m:
            errors.append("L{0} 殘留佔位符「{1}」：{2}".format(lineno, m.group(0), line.strip()[:40]))

    # 5) 狀態標記合法
    for lineno, line in enumerate(lines, 1):
        for m in BRACKET_TOKEN.finditer(line):
            if m.group(0) not in contract.ALLOWED_BRACKET_TOKENS:
                errors.append("L{0} 非法狀態標記「{1}」：合法值為 {2}".format(
                    lineno, m.group(0), " ".join(contract.ALLOWED_BRACKET_TOKENS)))

    by_index = {contract.HEADINGS.index(t): (ln, b)
                for ln, t, b in sections if t in contract.HEADINGS}

    # 6) 第七節：每條決議都要有狀態標記
    entry = by_index.get(contract.DECISION_SECTION_INDEX)
    if entry:
        start_line, body = entry
        if contract.EMPTY_SECTION_TEXT not in _body_text(body):
            for offset, line in enumerate(body, start_line + 2):
                if BULLET.match(line) and not line.startswith(("  ", "\t")):
                    if not any(tag in line for tag in contract.STATUS_TAGS):
                        errors.append("L{0} 第七節決議缺狀態標記：{1}".format(offset, line.strip()[:40]))

    # 7) 第八節：脈絡涵蓋聲明
    entry = by_index.get(contract.COVERAGE_SECTION_INDEX)
    if entry and contract.COVERAGE_MARKER not in _body_text(entry[1]):
        errors.append("第八節缺「{0}」聲明：須誠實交代本次可見的對話範圍".format(contract.COVERAGE_MARKER))

    # 8) 第三節：artifact 引用行需帶狀態標記
    for index in contract.ARTIFACT_SECTION_INDEXES:
        entry = by_index.get(index)
        if not entry:
            continue
        start_line, body = entry
        for offset, line in enumerate(body, start_line + 2):
            if ARTIFACT.search(line) and BULLET.match(line):
                if not any(tag in line for tag in contract.STATUS_TAGS):
                    errors.append("L{0} artifact 引用缺狀態標記（存在與否須誠實標示）：{1}".format(
                        offset, line.strip()[:40]))

    # 9) 明文秘密（掃原文，不略過程式碼區塊）
    for lineno, name, desc, snippet in redaction.scan(text):
        errors.append("L{0} 明文秘密 {1}（{2}）：請改為 {3} 並改寫成安全取得方式：{4}".format(
            lineno, name, desc, contract.REDACTION_MARK, snippet))

    return errors, warnings


def main(argv):
    from _console import configure_console
    configure_console()
    if len(argv) != 1:
        print("用法：python scripts/validate_handoff.py <handoff.md>")
        return 2
    contract.assert_frozen()
    try:
        errors, warnings = check(argv[0])
    except DecodeFailure as exc:
        print("[FAIL] {0}".format(exc))
        return 1
    for warning in warnings:
        print("[WARN] {0}".format(warning))
    if errors:
        print("[FAIL] 交接文件驗證未過（{0} 項）：".format(len(errors)))
        for item in errors:
            print("  - {0}".format(item))
        return 1
    print("[OK] 交接文件驗證通過：九節齊全、狀態標記合法、無佔位符、無明文秘密。")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
