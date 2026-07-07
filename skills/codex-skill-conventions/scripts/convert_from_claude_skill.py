#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把一支遵守 Joan／GPT Skill 房規的 Claude-era 或 GPT-era skill，轉換成 Codex skill 骨架。

用法：
    python scripts/convert_from_claude_skill.py <來源 skill 目錄> <輸出目錄>

做的事（只動外殼，不碰房規知識本身，見 SKILL.md「轉換器」一節的五步驟）：
  步驟一　結構補件：複製 SKILL.md／scripts／references／assets 到輸出目錄
          （這三個資源夾在 Claude 版與 Codex 版定義完全相同，不用重整）。
  步驟二　frontmatter 對齊：檢查 name 命名規則、description 一千零二十四字
          上限、以及本治理契約不接受的多餘欄位。
  步驟三　語意與用語轉換：掃描內文，列出疑似「來源平台專屬指涉」的行號與
          原句，供人工改寫（不自動代寫，避免語意失真，呼應房規五、七）。
  步驟四　環境相依重寫提示：偵測到寫死的 --break-system-packages 就提醒
          改用本 skill 的 scripts/bootstrap.py 環境偵測範式。
  步驟五　產生 agents/openai.yaml 草稿：display_name／short_description／
          default_prompt 都先給預設值，並標記待人工確認的項目。

輸出一份轉換報告；不自動覆蓋任何需要判斷的內容，人工確認後才算轉換完成。
"""
import re
import shutil
import sys
from pathlib import Path

MAX_NAME_LEN = 64
MAX_DESC_LEN = 1024
NAME_RE = re.compile(r"^[a-z0-9-]+$")
ALLOWED_FRONTMATTER_KEYS = {"name", "description"}

# 疑似來源平台專屬指涉的樣式，只偵測、不代寫。
CLAUDE_SPECIFIC_PATTERNS = [
    r"另一個\s*Claude",
    r"讓\s*Claude\s*知道",
    r"Claude\s*實例",
    r"claude\.ai",
    r"Claude\s*Code",
    r"Claude\s*讀到",
    r"ChatGPT\s*Web",
    r"gpt-skill-conventions",
    r"/mnt/skills",
]


def read_frontmatter(skill_md: Path):
    """回傳三元組：frontmatter dict 或 None、frontmatter 原始文字、內文。"""
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, None, text
    try:
        import yaml
        fm = yaml.safe_load(m.group(1)) or {}
    except Exception:
        fm = None
    return fm, m.group(1), m.group(2)


def scan_claude_specific(body: str):
    hits = []
    for lineno, line in enumerate(body.splitlines(), 1):
        for pat in CLAUDE_SPECIFIC_PATTERNS:
            if re.search(pat, line):
                hits.append((lineno, line.strip()))
                break
    return hits


def guess_display_name(name: str) -> str:
    return " ".join(w.capitalize() for w in name.split("-"))


def guess_short_description(description: str) -> str:
    """從長描述截一句當草稿，強制落在二十五至六十四字。"""
    first_sentence = re.split(r"[。！？]", description.strip())[0]
    short = first_sentence.strip()
    if len(short) > 64:
        short = short[:64].rstrip()
    if len(short) < 25:
        short = (short + "，套用房規並驗證交付")[:64]
    return short


def build_openai_yaml(name: str, description: str) -> str:
    display_name = guess_display_name(name)
    short = guess_short_description(description) if description else f"{display_name} 相關工作流"
    default_prompt = f"使用 ${name} 檢查這支 skill 是否符合房規"

    def q(v: str) -> str:
        return '"' + v.replace("\\", "\\\\").replace('"', '\\"') + '"'

    lines = [
        "interface:",
        f"  display_name: {q(display_name)}",
        f"  short_description: {q(short)}  # TODO 人工確認二十五至六十四字、用詞是否精準",
        f"  default_prompt: {q(default_prompt)}  # TODO 依實際用途調整",
        "",
        "policy:",
        "  allow_implicit_invocation: true",
    ]
    return "\n".join(lines) + "\n"


def validate_frontmatter(fm):
    problems = []
    if fm is None:
        return ["frontmatter 是空的或 YAML 格式錯誤，無法解析"]
    name = fm.get("name", "") or ""
    desc = fm.get("description", "") or ""
    if not name:
        problems.append("缺少 name 欄位")
    elif not NAME_RE.match(name):
        problems.append(f"name「{name}」不符合小寫字母／數字／連字號規則")
    elif name.startswith("-") or name.endswith("-") or "--" in name:
        problems.append(f"name「{name}」不可開頭結尾連字號或連續連字號")
    elif len(name) > MAX_NAME_LEN:
        problems.append(f"name 超過 {MAX_NAME_LEN} 字（目前 {len(name)} 字）")
    if not desc:
        problems.append("缺少 description 欄位")
    elif len(desc) > MAX_DESC_LEN:
        problems.append(f"description 超過 {MAX_DESC_LEN} 字（目前 {len(desc)} 字），會被 quick_validate.py 擋下")
    extra = set(fm.keys()) - ALLOWED_FRONTMATTER_KEYS
    if extra:
        problems.append(f"frontmatter 含本治理契約不接受的欄位：{', '.join(sorted(extra))}（標準交付只保留 name 與 description；其餘欄位需人工裁決）")
    return problems


def convert(src: Path, dst: Path) -> int:
    if not src.exists() or not src.is_dir():
        print(f"[錯誤] 來源目錄不存在：{src}")
        return 1
    skill_md = src / "SKILL.md"
    if not skill_md.exists():
        print(f"[錯誤] 來源目錄找不到 SKILL.md：{src}")
        return 1
    if dst.exists():
        print(f"[錯誤] 輸出目錄已存在，避免覆蓋既有內容：{dst}")
        return 1

    shutil.copytree(src, dst)
    print(f"[OK] 步驟一　已複製骨架到 {dst}")

    fm, _fm_text, body = read_frontmatter(dst / "SKILL.md")
    problems = validate_frontmatter(fm)
    print("\n[步驟二　frontmatter 對齊]")
    if problems:
        for p in problems:
            print(f"  [問題] {p}")
    else:
        print("  frontmatter 格式正常。")

    hits = scan_claude_specific(body)
    print("\n[步驟三　語意與用語轉換]")
    if hits:
        print(f"  疑似來源平台專屬用語（{len(hits)} 處，需人工改寫，不自動代寫）：")
        for lineno, line in hits:
            print(f"    L{lineno}: {line}")
    else:
        print("  沒有掃到明顯的 Claude 專屬用語。")

    print("\n[步驟四　環境相依重寫提示]")
    if "--break-system-packages" in body:
        print("  偵測到寫死的 --break-system-packages，建議改用 scripts/bootstrap.py 的環境偵測版 ensure 函式。")
    else:
        print("  沒有偵測到寫死的安裝旗標。")

    name = (fm or {}).get("name") or dst.name
    description = (fm or {}).get("description") or ""
    yaml_content = build_openai_yaml(name, description)
    agents_dir = dst / "agents"
    agents_dir.mkdir(exist_ok=True)
    (agents_dir / "openai.yaml").write_text(yaml_content, encoding="utf-8")
    print("\n[步驟五　產生 agents/openai.yaml 草稿]")
    print("  已產生，display_name／short_description／default_prompt 待人工確認。")

    print("\n=== 轉換報告完畢 ===")
    print("下一步：改寫上列疑似 Claude 用語、確認 agents/openai.yaml 字數與用詞，")
    print("再跑 Codex 自帶的 python scripts/quick_validate.py 做最終格式驗收（房規二）。")

    return 0 if not problems else 1


def main():
    if len(sys.argv) != 3:
        print("用法：python scripts/convert_from_claude_skill.py <來源 skill 目錄> <輸出目錄>")
        sys.exit(2)
    sys.exit(convert(Path(sys.argv[1]), Path(sys.argv[2])))


if __name__ == "__main__":
    main()
