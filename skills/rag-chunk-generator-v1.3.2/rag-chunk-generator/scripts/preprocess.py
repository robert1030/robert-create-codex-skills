"""
preprocess.py — 文字前處理層（v1.1 新增）

抽出「切片前的文字清洗」成獨立一層，引擎（chunk_*.py）只管切，不管洗。
三件事：
  1. 部首字修復：PDF 字型子集常把常用字存成康熙部首（U+2F00～U+2FDF）
     或 CJK 部首補充（U+2E80～U+2EFF）碼位，例如「⾏⼯⼈⻑」。這些字
     長得一樣但碼位不同，會讓 embedding 與關鍵字檢索通通對不上。
     只針對部首區做字元級 NFKC，全形標點原封不動（不可整段 NFKC，
     那會把「，：（）？」通通打成半形，違反全形標點鐵則）。
  2. 破折號統一：依房規三，破折號一律不留，統一改全形冒號。
  3. 頁眉頁尾濾除：版權列、頁碼列不進切片正文。

跨學科通用：不綁任何特定講義，footer 樣式以樣式庫（FOOTER_PATTERNS）
表達，要擴充就往清單加，不動引擎。
"""
import re
import unicodedata

# 部首補充區（U+2E80～U+2EFF）NFKC 不會處理，手動對照常見字
RADICAL_SUPPLEMENT_MAP = {
    "\u2ed1": "\u9577",  # CJK RADICAL LONG ONE → 長
    "\u2ed2": "\u9577",  # CJK RADICAL LONG TWO → 長
    "\u2eba": "\u4eba",  # CJK RADICAL C-SIMPLIFIED PERSON → 人
    "\u2ebf": "\u8279",  # CJK RADICAL GRASS ONE → 艹
    "\u2ee2": "\u9580",  # CJK RADICAL C-SIMPLIFIED GATE → 門
    "\u2ee4": "\u98a8",  # CJK RADICAL C-SIMPLIFIED WIND → 風
    "\u2ee8": "\u9ce5",  # CJK RADICAL C-SIMPLIFIED BIRD → 鳥
}

# 頁眉頁尾樣式庫（擴充往這裡加，不動引擎）
FOOTER_PATTERNS = [
    r"^©\s*\d{4}.*(版權所有|All Rights Reserved)",
    r"^第\s*[0-9一二三四五六七八九十]+\s*章\s*[·・.]\s*\d+$",
    r"^\s*[-–]?\s*\d{1,3}\s*[-–]?\s*$",
    r"^Page\s+\d+(\s*/\s*\d+)?$",
]
_FOOTER_RE = re.compile("|".join(FOOTER_PATTERNS))

# 標題樣式庫：章層級與節層級
CHAPTER_PATTERNS = [
    r"^第\s*[0-9一二三四五六七八九十]+\s*章\s*$",
    r"^第\s*[0-9一二三四五六七八九十]+\s*章[｜|：:]",
    r"^Chapter\s+\d+\s*$",
]
SECTION_PATTERNS = [
    r"^第[一二三四五六七八九十]+節[｜|：:]",
    r"^(本章重點整理|本章自我檢核|本章總結)",
    r"^(練習[一二三四五六七八九十]|課堂練習|Case Study|Chapter Goal)",
    r"^(術語速查|附錄|Appendix)",
    r"^(SME AOS Insight|SME AOS 管理觀念)",
    r"^Step\s*\d+[：:]",
]
_CHAPTER_RE = re.compile("|".join(CHAPTER_PATTERNS))
_SECTION_RE = re.compile("|".join(SECTION_PATTERNS))

# 行首裝飾符號（emoji、箭頭、勾選記號）
_DECOR_RE = re.compile(r"^[\U0001F300-\U0001FAFF\u2190-\u27BF\u2B00-\u2BFF\uFE0F\s]+")


def normalize_text(text: str) -> str:
    """部首字修復 ＋ 破折號統一。全形標點不動。"""
    out = []
    for ch in text:
        cp = ord(ch)
        if 0x2F00 <= cp <= 0x2FDF or 0xF900 <= cp <= 0xFAFF:
            nf = unicodedata.normalize("NFKC", ch)
            out.append(nf if len(nf) == 1 else ch)
        elif ch in RADICAL_SUPPLEMENT_MAP:
            out.append(RADICAL_SUPPLEMENT_MAP[ch])
        else:
            out.append(ch)
    s = "".join(out)
    s = s.replace("\u2014\u2014", "\uff1a").replace("\u2014", "\uff1a").replace("\u2013", "\uff0d")
    return s


def is_footer(line: str) -> bool:
    """判斷是否為頁眉頁尾雜訊行。"""
    return bool(_FOOTER_RE.match(line.strip()))


def heading_kind(line: str) -> tuple[str | None, str]:
    """回傳（'chapter' / 'section' / None, 去掉裝飾符號的標題文字）。"""
    s = _DECOR_RE.sub("", line).strip()
    if not s:
        return None, ""
    if _CHAPTER_RE.match(s):
        return "chapter", s
    if _SECTION_RE.match(s):
        return "section", s
    return None, ""


def compose_heading(chapter: str | None, section: str | None) -> str | None:
    """把章與節組成 section_title，例如「第 7 章｜第一節｜AI 不會一開始就做到 100 分」。"""
    parts = [p for p in (chapter, section) if p]
    return "｜".join(parts) if parts else None
