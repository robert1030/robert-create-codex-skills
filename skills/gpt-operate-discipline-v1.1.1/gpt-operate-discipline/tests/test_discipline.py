#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gpt-operate-discipline 回歸測試。

守七道門：
  1）validate_punct 對 SKILL.md 綠燈。
  2）v1.0 凍結內容：八節全文與五題題目、路由雜湊不變。
  3）無交接殘留詞。
  4）單一事實來源：九項觸發條件只由 description 定義，自測段不複製清單。
  5）v1.1 執行契約：來源品質、引用對應、證據降級與通用計算驗證齊全。
  6）跨領域驗收案例存在且涵蓋所有正式觸發類型。
  7）ChatGPT Web 與 Codex metadata 同時存在。

改動 Skill 後必跑，全 PASS 才可封裝。
用法：python tests/test_discipline.py
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
ACCEPTANCE = ROOT / "tests" / "acceptance_cases.md"
OPENAI_YAML = ROOT / "agents" / "openai.yaml"

SECTION_TITLES = [
    "一、讀出請求真正在問什麼",
    "二、把難題拆成可獨立驗證的片段",
    "三、判斷風險住在哪裡",
    "四、用重新推導取代「聽起來對」",
    "五、分開已知與猜測，並且說出口",
    "六、交付前先攻擊自己的結論",
    "七、先答案、再推理、最後講風險",
    "八、看起來像能力、其實不是的錯誤",
]

SELFTEST_ROUTES = ["回第一節", "回第四節", "回第五節", "回第六節", "回第七節"]
TRIGGER_TERMS = ["數字", "法條", "程式", "開發", "科學", "科技", "電腦", "研究", "決策"]
FORBIDDEN_WORDS = ["前任", "接替", "交接", "手冊"]

EIGHT_BLOCK_SHA256 = "201a5e8fa1ab00a83bcd02b17f72aa9a8550a16b3cdfe093b9ea1c3b4ebf8a09"
SELFTEST_QUESTIONS_SHA256 = "0cffaa8228e79980c3c8fc51410a4e51b2d68eb2695a6eabe48a9db54a9fa792"

CONTRACT_PHRASES = [
    "## 最高優先執行補強（v1.1）",
    "本節不另建觸發清單",
    "第一方、官方或原始來源",
    "不得單獨支撐高風險的確定結論",
    "引用來源必須直接支持引用旁的主張",
    "依第五節降級為推論或猜測",
    "所有會影響結論的計算性主張",
    "不限金額",
    "比例、日期、時間、單位轉換、容量、效能、統計與公式結果",
]

ACCEPTANCE_MARKERS = [
    "A01 | 法條",
    "A02 | 數字",
    "A03 | 程式",
    "A04 | 開發／科技／電腦",
    "A05 | 科學／研究",
    "A06 | 決策",
    "A07 | 已知失敗回歸",
    "A08 | 引用對應",
]

FAILED = []


def check(name, condition, detail=""):
    if condition:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        FAILED.append(name)


def sha256_text(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def extract_eight_block(text):
    start = text.index("## 一、讀出請求真正在問什麼")
    end = text.index("\n---\n\n## 出手前的五題自測")
    return text[start:end]


def extract_selftest_questions(text):
    match = re.search(
        r"1\. 我回答的是.*?\n"
        r"2\. 最關鍵的.*?\n"
        r"3\. 回覆裡的.*?\n"
        r"4\. 我有沒有.*?\n"
        r"5\. 如果對方.*?（否→回第七節）",
        text,
        re.DOTALL,
    )
    return match.group(0) if match else ""


def main():
    text = SKILL.read_text(encoding="utf-8")

    print("[1] validate_punct 閘門")
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_punct.py"), str(SKILL)],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    check("validate_punct 退出碼 0", result.returncode == 0, result.stdout.strip()[:200])

    print("[2] v1.0 凍結契約")
    for title in SECTION_TITLES:
        check(f"章節存在：{title[:12]}", title in text)
    check("八節標題數量恰為 8", sum(1 for title in SECTION_TITLES if title in text) == 8)
    eight_block = extract_eight_block(text)
    check(
        "八節全文雜湊未變",
        sha256_text(eight_block) == EIGHT_BLOCK_SHA256,
        sha256_text(eight_block),
    )
    questions = extract_selftest_questions(text)
    check("五題自測恰為 5 題", len(re.findall(r"（否→回第[一四五六七]節）", questions)) == 5)
    check(
        "五題題目與路由雜湊未變",
        sha256_text(questions) == SELFTEST_QUESTIONS_SHA256,
        sha256_text(questions),
    )
    for route in SELFTEST_ROUTES:
        check(f"自測路由存在：{route}", route in questions)

    print("[3] 交接殘留清潔度")
    for word in FORBIDDEN_WORDS:
        hits = [line_no for line_no, line in enumerate(text.splitlines(), 1) if word in line]
        check(f"無殘留詞「{word}」", not hits, f"出現於行 {hits}")

    print("[4] 單一事實來源一致性")
    frontmatter = re.search(r'^description:\s*"(.*?)"\s*$', text, re.MULTILINE)
    check("frontmatter description 可解析", frontmatter is not None)
    if frontmatter:
        description = frontmatter.group(1)
        for term in TRIGGER_TERMS:
            check(f"description 含觸發詞「{term}」", term in description)
    scope = re.search(
        r"\*\*適用範圍（單一事實來源）：\*\*(.*?)(?:\n\n|$)",
        text,
        re.DOTALL,
    )
    check("自測適用段存在", scope is not None)
    if scope:
        scope_text = scope.group(1)
        check("適用段引用 frontmatter description", "frontmatter `description`" in scope_text)
        check("適用段明示不維護第二份清單", "本段不維護第二份觸發清單" in scope_text)
        duplicated = "數字、法條、程式、開發、科學、科技、電腦、研究、決策"
        check("適用段未複製九項觸發清單", duplicated not in scope_text)

    print("[5] v1.1 執行契約")
    check("v1.1 版本戳記存在", "**v1.1｜2026-07-10**" in text)
    for phrase in CONTRACT_PHRASES:
        check(f"契約存在：{phrase[:16]}", phrase in text)

    print("[6] 跨領域驗收案例")
    check("acceptance_cases.md 存在", ACCEPTANCE.exists())
    if ACCEPTANCE.exists():
        acceptance_text = ACCEPTANCE.read_text(encoding="utf-8")
        for marker in ACCEPTANCE_MARKERS:
            check(f"驗收案例存在：{marker}", marker in acceptance_text)
        check("已知失敗案例禁止百科作唯一依據", "百科不得作為唯一法規依據" in acceptance_text)
        check("計算案例不限金額", "金額以外的計算" in acceptance_text)

    print("[7] ChatGPT Web 與 Codex metadata")
    check("agents/openai.yaml 存在", OPENAI_YAML.exists())
    if OPENAI_YAML.exists():
        metadata_text = OPENAI_YAML.read_text(encoding="utf-8")
        for marker in [
            "icon:",
            "accent_color:",
            "brand_color:",
            "default_prompt:",
            "$gpt-operate-discipline",
            "allow_implicit_invocation: true",
        ]:
            check(f"metadata 存在：{marker}", marker in metadata_text)

    print()
    if FAILED:
        print(f"❌ {len(FAILED)} 項未過：{FAILED}")
        return 1
    print("✅ 全部通過，v1.0 凍結契約與 v1.1 執行補強均完好。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
