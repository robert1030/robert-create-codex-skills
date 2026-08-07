#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""結構與凍結契約回歸測試。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import ROOT, check, read_package_file, summary, temp_file  # noqa: E402
from _sample import BOOT_OK, good_doc  # noqa: E402

import handoff_contract as contract  # noqa: E402
import validate_handoff  # noqa: E402


def errors_for(content):
    path = temp_file(content)
    try:
        errs, _warn = validate_handoff.check(path)
        return errs
    finally:
        os.unlink(path)


print("== 凍結契約 ==")
try:
    contract.assert_frozen()
    check("凍結雜湊守門（未被動過）", True)
except RuntimeError:
    check("凍結雜湊守門（未被動過）", False)
check("九節數量", len(contract.HEADINGS) == 9)
check("第〇節標題凍結值", contract.HEADINGS[0] == "〇、啟動指令（給下一個 session）")
check("第八節標題凍結值", contract.HEADINGS[-1] == "八、未決事項與風險")
check("凍結雜湊值", contract.frozen_digest() == contract.EXPECTED_DIGEST)
check("改動章節清單會被雜湊擋下",
      contract.frozen_digest(contract.HEADINGS[:-1]) != contract.EXPECTED_DIGEST)

print("== 基本結構 ==")
GOOD = good_doc()
check("完整樣本通過", errors_for(GOOD) == [])
check("缺節被擋", any("缺少章節" in e for e in errors_for(
    GOOD.replace("## 五、邊界與禁區\n\n本節有實質內容。\n", ""))))
swapped = GOOD.replace("## 一、任務身分卡", "##TMP").replace(
    "## 二、核心脈絡", "## 一、任務身分卡").replace("##TMP", "## 二、核心脈絡")
check("順序錯被擋", errors_for(swapped) != [])
check("空節被擋", any("空節" in e for e in errors_for(
    GOOD.replace("## 二、核心脈絡\n\n本節有實質內容。", "## 二、核心脈絡\n"))))
check("本節無內容放行", errors_for(
    GOOD.replace("## 二、核心脈絡\n\n本節有實質內容。",
                 "## 二、核心脈絡\n\n" + contract.EMPTY_SECTION_TEXT)) == [])
check("多出非凍結章節被擋",
      any("多出非凍結章節" in e for e in errors_for(GOOD + "\n## 九、額外章節\n\n多出來的。\n")))

print("== 佔位符 ==")
check("TODO 佔位符被擋", any("佔位符" in e for e in errors_for(
    GOOD.replace("本節有實質內容。", "TODO 之後補", 1))))
check("樣板角括號被擋", any("佔位符" in e for e in errors_for(
    GOOD.replace("本節有實質內容。", "〈一句話主題〉", 1))))
check("程式碼區塊內 TODO 放行",
      errors_for(GOOD + "\n```python\n# TODO: code 裡的不算\n```\n") == [])

print("== 第〇節三條閘門 ==")
long_boot = BOOT_OK[:-1] + "多餘冗長說明" * 30 + "。"
check("超過 200 字被擋", any("過長" in e for e in errors_for(good_doc({0: long_boot}))))
check("合規長度放行", errors_for(GOOD) == [])
check("無編號被擋", any("編號條目不足" in e for e in errors_for(
    good_doc({0: "先讀完本文件再回應，然後載入紀律，嚴守契約，從下一步接手。"}))))
check("僅兩條編號被擋", any("編號條目不足" in e for e in errors_for(
    good_doc({0: "①先讀完本文件再回應；②載入紀律後接手。"}))))
check("首條缺錨詞被擋", any("缺錨詞" in e for e in errors_for(
    good_doc({0: "①載入第四節紀律；②讀完本文件再回應；③嚴守契約；④接手。"}))))
check("首條錨詞不齊被擋", any("缺錨詞" in e for e in errors_for(
    good_doc({0: "①先讀完本文件；②再回應使用者；③嚴守契約；④接手。"}))))
check("阿拉伯數字編號放行", errors_for(good_doc({
    0: "1. 先讀完本文件再回應\n2. 載入第四節紀律\n3. 嚴守契約並從下一步接手"})) == [])

print("== 狀態標記 ==")
check("狀態標記為平台中立 ASCII",
      all(tag.isascii() and tag.isupper() for tag in
          (t.strip("[]") for t in contract.STATUS_TAGS)))
check("五級狀態齊備", set(contract.STATUS_TAGS) == {
    "[CONFIRMED]", "[INFERRED]", "[UNVERIFIED]", "[BLOCKED]", "[SUPERSEDED]"})
check("非法狀態標記被擋", any("非法狀態標記" in e for e in errors_for(
    good_doc({2: "這條標成 [APPROVED] 是非法的。"}))))
check("遮蔽標記合法", errors_for(good_doc({2: "憑證值以 [REDACTED] 表示。"})) == [])

print("== 逐節必填 ==")
check("第七節缺狀態標記被擋", any("第七節決議缺狀態標記" in e for e in errors_for(
    good_doc({7: "- 以退出碼為唯一閘門｜原因：人工檢查會漏"}))))
check("第七節本節無內容放行",
      errors_for(good_doc({7: contract.EMPTY_SECTION_TEXT})) == [])
check("第八節缺脈絡涵蓋被擋", any("脈絡涵蓋" in e for e in errors_for(
    good_doc({8: "- 待使用者決定：是否接進掛鉤 [UNVERIFIED]"}))))
check("第三節 artifact 缺狀態被擋", any("artifact 引用缺狀態標記" in e for e in errors_for(
    good_doc({3: "- 已完成：驗證器 `scripts/validate_handoff.py`｜結構閘門"}))))
check("第三節 URL 缺狀態被擋", any("artifact 引用缺狀態標記" in e for e in errors_for(
    good_doc({3: "- 已完成：規格見 https://example.com/spec"}))))
check("第三節 artifact 帶狀態放行", errors_for(good_doc({
    3: "- 已完成：規格見 https://example.com/spec｜已審閱 [CONFIRMED]"})) == [])

print("== 契約單一真實來源 ==")
skill = read_package_file("SKILL.md")
oc = read_package_file("references/output-contract.md")
check("SKILL.md 列出全部九節", all(h in skill for h in contract.HEADINGS))
check("output-contract 每節恰好一次",
      all(oc.count("## " + h) == 1 for h in contract.HEADINGS))
check("output-contract 定義全部狀態標記", all(t in oc for t in contract.STATUS_TAGS))
check("涵蓋誠實聲明存在", "祈使語氣" in oc and "人工留意項" in oc)
check("驗證器 docstring 含涵蓋聲明",
      "祈使語氣" in (validate_handoff.__doc__ or ""))
check("schema 與契約一致（由套件驗證器把關）",
      os.path.isfile(os.path.join(ROOT, "schemas", "handoff.schema.json")))

sys.exit(summary("test_structure"))
