#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
交接文件結構驗證器（session-handoff 專屬）。
驗四件事，任一不過退出碼 1：
  1) 九節凍結標題齊全且順序正確（標題文字一字不差）。
  2) 凍結雜湊未被動過（程式內 HEADINGS 對照 EXPECTED_DIGEST，防止有人改本檔的標題清單）。
  3) 無空節（每節標題下方至少要有一行非空白、非標題的內容）。
  4) 無殘留佔位符（TODO／FIXME／待填／〈…〉樣板角括號）。
  5) 第〇節（啟動指令）三條機器閘門：
     a. 內文去除空白後不得超過 200 字元（防冗長飄移）。
     b. 至少三個編號條目（①～⑳ 圓圈數字，或行首「1.」「1、」「1)」）。
     c. 第一個編號條目須同時含錨詞「讀」與「再回應」（防搶答飄移；
        錨定編號條目而非整節首句，開場定位句屬合法前導）。
     涵蓋誠實聲明：「祈使語氣」無法可靠機器判定，屬人工留意項，不在閘門內。
用法: python3 scripts/check_handoff.py <handoff.md>
"""
import hashlib
import json
import re
import sys

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

EXPECTED_DIGEST = "7f29cd5d626067c2"

PLACEHOLDERS = re.compile(r"TODO|FIXME|待填|〈[^〉]*〉")


def frozen_digest(headings):
    blob = json.dumps(list(headings), sort_keys=False, ensure_ascii=False)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:16]


def assert_frozen():
    got = frozen_digest(HEADINGS)
    if got != EXPECTED_DIGEST:
        raise RuntimeError(
            f"凍結契約被動到（雜湊 {got} ≠ 定版 {EXPECTED_DIGEST}）。"
            "要改章節結構請另開新版（major），不動凍結項。"
        )


def check(path):
    with open(path, encoding="utf-8") as f:
        raw = f.read()
    # 濾掉 fenced code（內容裡的程式碼不算章節內文判定與佔位符掃描）
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), raw, flags=re.DOTALL)
    lines = text.splitlines()

    errors = []

    # 1) 標題齊全且順序正確
    found = []
    for i, line in enumerate(lines):
        m = re.match(r"^##\s+(.+?)\s*$", line)
        if m:
            found.append((i, m.group(1)))
    titles = [t for _, t in found]
    if titles != HEADINGS:
        missing = [h for h in HEADINGS if h not in titles]
        extra = [t for t in titles if t not in HEADINGS]
        if missing:
            errors.append(f"缺少章節：{missing}")
        if extra:
            errors.append(f"多出非凍結章節：{extra}")
        if not missing and not extra:
            errors.append("章節順序與凍結順序不符")

    # 2) 空節檢查（每節標題到下一個 ## 之間至少一行實質內容）
    for idx, (lineno, title) in enumerate(found):
        end = found[idx + 1][0] if idx + 1 < len(found) else len(lines)
        body = [l for l in lines[lineno + 1:end] if l.strip() and not l.strip().startswith("#")]
        if not body:
            errors.append(f"空節：「{title}」（無內容請寫「本節無內容。」）")

    # 3) 第〇節三條閘門（a 字數、b 編號、c 首條錨詞）
    if found and found[0][1] == HEADINGS[0]:
        end0 = found[1][0] if len(found) > 1 else len(lines)
        body_lines = [l for l in lines[found[0][0] + 1:end0] if not l.strip().startswith("#")]
        body0 = "\n".join(body_lines)
        n = len(re.sub(r"\s", "", body0))
        if n > 200:
            errors.append(f"第〇節啟動指令過長（{n} 字 > 200 字上限）：請濃縮為編號祈使句")
        marks = list(re.finditer(r"[\u2460-\u2473]|^[ \t]*\d+[.、\)]", body0, re.M))
        if len(marks) < 3:
            errors.append(f"第〇節編號條目不足（{len(marks)} 條 < 3 條下限）：請改為逐條編號")
        else:
            first_item = body0[marks[0].end():marks[1].start()]
            if not ("讀" in first_item and "再回應" in first_item):
                errors.append("第〇節首條缺錨詞：第一個編號條目須同時含「讀」與「再回應」")

    # 4) 佔位符
    for lineno, line in enumerate(lines, 1):
        m = PLACEHOLDERS.search(line)
        if m:
            errors.append(f"L{lineno} 殘留佔位符「{m.group(0)}」：{line.strip()[:40]}")

    return errors


def main():
    if len(sys.argv) != 2:
        print("用法: python3 scripts/check_handoff.py <handoff.md>")
        return 2
    assert_frozen()
    errors = check(sys.argv[1])
    if errors:
        print(f"✗ 結構驗證未過（{len(errors)} 項）：")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("✓ 結構驗證通過：九節齊全、無空節、無佔位符。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
