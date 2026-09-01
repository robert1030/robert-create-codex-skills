#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
check_output_contract.py — challenge-claim v0.2.1 輸出契約驗證器。

驗的是「本次要交付的那一份論點挑戰分析」，不是寫死的範例。

對應 joan-skill-conventions 房規二「閘門要有牙齒」三問：
  一、獨立來源重算：不採信產出自報的「我有做」，直接掃描交付檔案本身，
      逐節切出內容重新判斷實質性、判定詞、證據標記與違規字樣。
  二、fail-closed：檔案不存在、內容為空、七元件缺任一、或元件有標題卻無實質內容，
      一律紅燈，不靜默放行。
  三、驗當前產出：讀的是使用者傳入的這份檔案，不讀套件內的任何樣本。

刻意涵蓋的假閘門反例：上一代同類驗證器只比對七個標題是否存在，
一份「七標題齊全、內容全是略與無」的空殼產出會被判為通過。
本驗證器的 C2 實質內容檢查專門擋這種產出，對應 tests 內的 hollow shell 案例。

用法：
    python3 check_output_contract.py <產出檔.md>
    python3 check_output_contract.py <任意路徑> --self-test

退出碼：0 全通過；1 任一檢查未過或必要輸入缺席；2 用法錯誤。
"""
import io
import contextlib
import os
import re
import sys
import tempfile

# ---------------------------------------------------------------------------
# 輸出契約：七元件，順序固定，正本定義在 SKILL.md 的「輸出契約」一節。
# ---------------------------------------------------------------------------
REQUIRED_SECTIONS = [
    ("核心主張", r"核心主張"),
    ("論證結構", r"論證結構"),
    ("前提與證據檢查", r"前提[與及]證據"),
    ("反方壓力測試", r"反方壓力測試"),
    ("偏誤與缺口", r"偏誤[與及]缺口"),
    ("校準結論", r"校準結論"),
    ("驗證計畫", r"驗證計畫"),
]

VALID_VERDICTS = ["部分支持", "無法判定", "不支持", "支持"]

# 實質內容門檻：扣掉佔位字樣後，每個元件至少要有這麼多個非空白字元。
MIN_SECTION_CHARS = 20
PLACEHOLDER_LINE = re.compile(r"^[\s\-*>]*(略|無|N/A|n/a|待補|待補充|TBD|tbd|——|\.\.\.)[\s。，]*$")

# 反向檢查：三條鐵則對應的違規字樣。
VAGUE_ATTACK_PATTERNS = [
    r"看起來就是有問題",
    r"整體邏輯很?薄弱",
    r"邏輯很?薄弱，?建議重寫",
    r"建議(全部)?重寫",
    r"寫得很爛",
    r"感覺(整體)?不對",
]

FABRICATION_PATTERNS = [
    r"證據不足.{0,30}(推測應為|合理估計|估計約|應該是|大致可判斷為)",
    r"原文未提供.{0,20}(推測|估計)(應)?為",
]

SEVERITY_ONLY_PATTERNS = [
    r"雖然?查?無明確反例.{0,20}(仍|但)(保留|列入|寫入)",
    r"雖然?沒有(明確)?反例.{0,20}(仍|但)(保留|列入|寫入)",
    r"因為?(影響|事關)重大.{0,20}(仍|故|因此)(保留|列入)",
]

# 來源可追溯性：出現這些概括宣稱時，同一行必須帶可定位標記或明確標示未核實。
UNSOURCED_CLAIM_PATTERNS = [
    r"有研究指出",
    r"據研究",
    r"研究顯示",
    r"文獻顯示",
    r"根據統計",
    r"眾所周知",
    r"一般認為",
]
TRACEABLE_MARKERS = [
    r"S-\d+", r"未核實", r"arXiv", r"https?://", r"依據類型", r"使用者提供",
]


# ---------------------------------------------------------------------------
# 切節
# ---------------------------------------------------------------------------
def split_sections(text):
    """把 markdown 依標題切成 [(標題文字, 內容), ...]，順序保留。"""
    lines = text.splitlines()
    sections = []
    current_title = None
    buf = []
    for line in lines:
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*\S)\s*$", line)
        if m:
            if current_title is not None:
                sections.append((current_title, "\n".join(buf)))
            current_title = m.group(1)
            buf = []
        else:
            buf.append(line)
    if current_title is not None:
        sections.append((current_title, "\n".join(buf)))
    return sections


def find_section(sections, pattern):
    for title, body in sections:
        if re.search(pattern, title):
            return title, body
    return None, None


def substantive_length(body):
    """扣掉佔位行、清單符號與空白後的實質字元數。"""
    kept = []
    for line in body.splitlines():
        if not line.strip():
            continue
        if PLACEHOLDER_LINE.match(line):
            continue
        kept.append(line)
    joined = "".join(kept)
    joined = re.sub(r"[\s\-*>#|`]", "", joined)
    return len(joined)


def paragraphs(body):
    """以空行切塊，回傳非空區塊。"""
    return [p for p in re.split(r"\n\s*\n", body) if p.strip()]


def item_lines(body):
    """條目行：X1 這類編號、或數字編號、或以 - 開頭的清單行。"""
    out = []
    for line in body.splitlines():
        if re.match(r"^\s*(X\d+|IP\d+|E\d+|C\d+|P\d+|R\d+|\d+[.、)]|[-*]\s)", line.strip()):
            out.append(line.strip())
    return out


# ---------------------------------------------------------------------------
# 各項檢查
# ---------------------------------------------------------------------------
def check_sections_present_and_ordered(sections, errors):
    """C1：七元件齊全且順序正確。"""
    found_index = []
    for label, pattern in REQUIRED_SECTIONS:
        idx = None
        for i, (title, _) in enumerate(sections):
            if re.search(pattern, title):
                idx = i
                break
        if idx is None:
            errors.append(f"C1 缺少必要元件：{label}")
        else:
            found_index.append((label, idx))
    if len(found_index) == len(REQUIRED_SECTIONS):
        order = [i for _, i in found_index]
        if order != sorted(order):
            got = [lab for lab, _ in sorted(found_index, key=lambda x: x[1])]
            errors.append(f"C1 元件順序錯誤，實際順序為：{got}")


def check_sections_substantive(sections, errors):
    """C2：每個元件都要有實質內容，擋七標題齊全但內容空殼的產出。"""
    for label, pattern in REQUIRED_SECTIONS:
        title, body = find_section(sections, pattern)
        if title is None:
            continue
        n = substantive_length(body)
        if n < MIN_SECTION_CHARS:
            errors.append(
                f"C2 元件「{label}」只有標題沒有實質內容（實質字元數 {n}，門檻 {MIN_SECTION_CHARS}）"
            )


def check_verdict(sections, errors):
    """C3：校準結論必須有唯一且合法的判定詞，並附信心與限制條件。"""
    title, body = find_section(sections, r"校準結論")
    if title is None:
        return
    verdict_lines = [ln for ln in body.splitlines() if re.search(r"判定[：:]", ln)]
    if not verdict_lines:
        errors.append("C3 校準結論缺少「判定：」欄位")
    elif len(verdict_lines) > 1:
        errors.append(f"C3 校準結論出現 {len(verdict_lines)} 個判定欄位，應恰為一個")
    else:
        line = verdict_lines[0]
        tail = re.split(r"判定[：:]", line, maxsplit=1)[1].strip()
        matched = None
        for v in VALID_VERDICTS:
            if tail.startswith(v):
                matched = v
                break
        if matched is None:
            errors.append(
                f"C3 判定詞不合法：「{tail[:12]}」，僅允許 支持、部分支持、無法判定、不支持"
            )
    if not re.search(r"信心", body):
        errors.append("C3 校準結論缺少信心程度")
    if not re.search(r"限制條件|適用範圍|不宜外推", body):
        errors.append("C3 校準結論缺少限制條件")


def check_confirmed_has_signal(sections, errors):
    """C4：每個 confirmed 判定所在的段落必須附可觀察訊號。"""
    for title, body in sections:
        for para in paragraphs(body):
            if re.search(r"\bconfirmed\b", para) and "可觀察訊號" not in para:
                snippet = para.strip().replace("\n", " ")[:34]
                errors.append(f"C4 confirmed 判定未附可觀察訊號：{snippet}…")


def check_counterexamples(sections, errors):
    """C5：反方壓力測試至少一條反例，且每條都要說明對原論證的影響。"""
    title, body = find_section(sections, r"反方壓力測試")
    if title is None:
        return
    items = item_lines(body)
    if not items:
        errors.append("C5 反方壓力測試沒有任何可辨識的反例條目")
        return
    for line in items:
        if "影響" not in line:
            errors.append(f"C5 反例未說明對原論證的影響：{line[:34]}…")


def scan_patterns(text, patterns, code, label, errors):
    for pat in patterns:
        for m in re.finditer(pat, text):
            snippet = text[max(0, m.start() - 6):m.start() + 30].strip().replace("\n", " ")
            errors.append(f"{code} {label}：…{snippet}…")


def check_untraceable_sources(text, errors):
    """C9：概括的研究宣稱必須帶可定位標記，或明確標示未核實。"""
    for line in text.splitlines():
        for pat in UNSOURCED_CLAIM_PATTERNS:
            if re.search(pat, line):
                if not any(re.search(mk, line) for mk in TRACEABLE_MARKERS):
                    errors.append(f"C9 來源不可追溯的概括宣稱：{line.strip()[:34]}…")
                break


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------
def run(path: str) -> int:
    if not os.path.isfile(path):
        print(f"❌ 找不到檔案：{path}（fail-closed，不視為通過）")
        return 1

    try:
        with open(path, encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print(f"❌ 檔案無法讀取：{exc}（fail-closed，不視為通過）")
        return 1

    if not text.strip():
        print("❌ 檔案為空（fail-closed，不視為通過）")
        return 1

    sections = split_sections(text)
    errors = []

    check_sections_present_and_ordered(sections, errors)
    check_sections_substantive(sections, errors)
    check_verdict(sections, errors)
    check_confirmed_has_signal(sections, errors)
    check_counterexamples(sections, errors)
    scan_patterns(text, VAGUE_ATTACK_PATTERNS, "C6", "空泛挑錯，違反鐵則一", errors)
    scan_patterns(text, FABRICATION_PATTERNS, "C7", "自行補上缺失證據，違反鐵則二", errors)
    scan_patterns(text, SEVERITY_ONLY_PATTERNS, "C8", "無明確反例仍因嚴重而保留", errors)
    check_untraceable_sources(text, errors)

    if errors:
        print(f"❌ 輸出契約驗證未通過，共 {len(errors)} 項：")
        for e in errors:
            print("   " + e)
        return 1

    print("✅ 輸出契約驗證通過：七元件齊全且順序正確、內容具實質、判定詞合法、"
          "confirmed 皆附可觀察訊號、反例皆說明影響、未偵測到鐵則違規字樣。")
    return 0


# ---------------------------------------------------------------------------
# 內建負向自檢：餵故意錯的產出，驗證器必須紅燈。
# ---------------------------------------------------------------------------
_GOOD = """## 核心主張
C1：導入遠距辦公可提升留任率，應全公司推行。主張類型為因果加規範建議。

## 論證結構
E1 離職率下降　→　R1 遠距改善留任　→　IP1 其他條件未變動　→　C1 應全面推行。

## 前提與證據檢查
IP1 隱含前提：同期間沒有其他人事政策變動，狀態為未驗證，重要性高。
E1 證據等級 E1，限制為單一組織單一年度，無對照組。依據類型：使用者提供資訊。

## 反方壓力測試
X1 邊界反例：同業在相同期間離職率普遍下降。影響：削弱把降幅歸因於制度的推論。

## 偏誤與缺口
問題一：事後歸因，判定 confirmed。可觀察訊號：原文以時點先後作為因果依據，未處理同期變因。

## 校準結論
判定：部分支持
信心：中低
限制條件：僅適用於原始資料涵蓋的單一組織與單一年度。

## 驗證計畫
1. 取得同業同期離職率作為基準情境。
2. 取得同期薪酬政策異動紀錄，區分兩個變因。
"""

_HOLLOW = """## 核心主張
略

## 論證結構
略

## 前提與證據檢查
無

## 反方壓力測試
略

## 偏誤與缺口
無

## 校準結論
判定：部分支持

## 驗證計畫
略
"""


def self_test() -> int:
    cases = [
        ("完整合格產出", _GOOD, True),
        ("七標題齊全但內容空殼", _HOLLOW, False),
        ("缺少驗證計畫元件", _GOOD.split("## 驗證計畫")[0], False),
        ("判定詞不合法", _GOOD.replace("判定：部分支持", "判定：大致同意"), False),
        ("confirmed 缺可觀察訊號",
         _GOOD.replace("可觀察訊號：原文以時點先後作為因果依據，未處理同期變因。", "就是事後歸因。"),
         False),
        ("反例未說明影響",
         _GOOD.replace("影響：削弱把降幅歸因於制度的推論。", "值得注意。"), False),
        ("自行補上缺失證據",
         _GOOD.replace("E1 證據等級 E1，限制為單一組織單一年度，無對照組。依據類型：使用者提供資訊。",
                       "E1 證據不足，推測應為樣本數過少所致。"), False),
        ("來源不可追溯",
         _GOOD.replace("X1 邊界反例：同業在相同期間離職率普遍下降。",
                       "X1 邊界反例：有研究指出同業離職率普遍下降。"), False),
        ("空檔案", "   \n", False),
    ]

    passed = failed = 0
    with tempfile.TemporaryDirectory() as tmp:
        for name, content, expect_pass in cases:
            fp = os.path.join(tmp, "case.md")
            with open(fp, "w", encoding="utf-8") as f:
                f.write(content)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                code = run(fp)
            got_pass = (code == 0)
            ok = (got_pass == expect_pass)
            print(f"[{'PASS' if ok else 'FAIL'}] {name}："
                  f"預期{'通過' if expect_pass else '紅燈'}，"
                  f"實際{'通過' if got_pass else '紅燈'}")
            if ok:
                passed += 1
            else:
                failed += 1
                print(buf.getvalue())

    print(f"\n負向自檢總結：{passed} 通過 / {failed} 失敗（共 {len(cases)} 案例）")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 check_output_contract.py <產出檔.md>")
        print("      python3 check_output_contract.py <任意路徑> --self-test")
        sys.exit(2)
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    sys.exit(run(sys.argv[1]))
