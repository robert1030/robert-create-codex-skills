#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""套件驗證器：交付前的總閘門，任一不過退出碼 1。

檢查項：
  1. skill 名稱與版本正確且三處一致（SKILL.md、FROZEN.md、agents metadata）。
  2. frontmatter 與 agents metadata 欄位齊全。
  3. 必要檔案齊備。
  4. SKILL.md 的 context pointer 指向確實存在的檔案。
  5. schema 為合法 JSON，且章節與狀態標記與契約模組一致。
  6. references/output-contract.md 的九節與狀態標記與契約模組一致。
  7. SKILL.md 無明顯重複行（duplication）。
  8. 無舊名稱與舊版本殘留（掃描字串以組合方式建構，避免本檔自身誤觸）。
  9. 全套件為 UTF-8 without BOM ＋ LF（刻意測試用的 fixture 目錄除外）。
 10. 所有 scripts 可被 Python 編譯。
 11. SKILL.md 不使用只存在於單一 shell 的無條件命令，也不寫死家目錄路徑。
 12. platform-capabilities.md 對每一項偵測能力都寫出降級行為（能力缺席不是失敗）。
 13. 加 --zip 時，檢查封裝內容可在 Windows 與 Linux 正確解壓且無舊字串。

用法：
  python scripts/validate_skill.py [套件根目錄] [--zip <package.zip>]
"""
import json
import os
import py_compile
import re
import shutil
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import handoff_contract as contract  # noqa: E402
import detect_capabilities  # noqa: E402
from check_encoding import DecodeFailure, check_tree, read_text  # noqa: E402

# 舊名稱與舊版本以組合方式建構，本檔文字中不出現完整字串。
_LEGACY_PREFIX = "gpt"
LEGACY_STRINGS = (
    _LEGACY_PREFIX + "-session-handoff",
    _LEGACY_PREFIX.upper() + " Session Handoff",
)
LEGACY_PATTERNS = (
    re.compile(r"\bv1\." + "2" + r"\b"),
    re.compile(_LEGACY_PREFIX + r"[-_]session[-_]handoff", re.I),
)

REQUIRED_METADATA_KEYS = (
    "display_name:",
    "short_description:",
    "icon:",
    "accent_color:",
    "brand_color:",
    "default_prompt:",
    "version:",
    "argument_hint:",
    "allow_implicit_invocation:",
)

SINGLE_SHELL_COMMANDS = ("python3 ", "py -3", "powershell -", "Get-Content ", "#!/bin/bash")
HARDCODED_PATHS = ("/home/", "C:\\Users\\", "/Users/", "%USERPROFILE%\\")


def _read(root, rel):
    return read_text(os.path.join(root, rel), allow_bom=True)[0]


def _frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"')
    return data


def check_package(root):
    errors = []

    # 1) 必要檔案
    for rel in contract.REQUIRED_FILES:
        if not os.path.isfile(os.path.join(root, rel)):
            errors.append("缺少必要檔案：{0}".format(rel))
    if errors:
        return errors

    skill = _read(root, "SKILL.md")
    frozen = _read(root, "FROZEN.md")
    metadata = _read(root, "agents/openai.yaml")
    output_contract = _read(root, "references/output-contract.md")
    platform_doc = _read(root, "references/platform-capabilities.md")

    # 2) 名稱與版本
    fm = _frontmatter(skill)
    if fm.get("name") != contract.SKILL_NAME:
        errors.append("SKILL.md frontmatter 名稱應為 {0}，實得 {1}".format(
            contract.SKILL_NAME, fm.get("name")))
    if not fm.get("description"):
        errors.append("SKILL.md frontmatter 缺 description（model-invoked 必要欄位）")
    stamp = re.search(r"v(\d+\.\d+\.\d+)", skill)
    if not stamp or stamp.group(1) != contract.VERSION:
        errors.append("SKILL.md 版本戳記應為 v{0}".format(contract.VERSION))
    if "v" + contract.VERSION not in frozen:
        errors.append("FROZEN.md 缺 v{0} 凍結條目".format(contract.VERSION))
    if 'version: "{0}"'.format(contract.VERSION) not in metadata:
        errors.append('agents/openai.yaml 應含 version: "{0}"'.format(contract.VERSION))
    if "$" + contract.SKILL_NAME not in metadata:
        errors.append("agents/openai.yaml 的 default_prompt 應引用 ${0}".format(contract.SKILL_NAME))

    # 3) metadata 欄位齊全
    for key in REQUIRED_METADATA_KEYS:
        if key not in metadata:
            errors.append("agents/openai.yaml 缺欄位：{0}".format(key))

    # 4) context pointer 指向存在的檔案
    for match in re.finditer(r"`((?:references|scripts|schemas|tests)/[A-Za-z0-9_./-]+)`", skill):
        rel = match.group(1)
        if not os.path.exists(os.path.join(root, rel)):
            errors.append("SKILL.md 的 pointer 指向不存在的檔案：{0}".format(rel))

    # 5) schema 合法且與契約一致
    schema_path = os.path.join(root, "schemas/handoff.schema.json")
    try:
        with open(schema_path, encoding="utf-8") as handle:
            schema = json.load(handle)
    except (ValueError, OSError) as exc:
        schema = None
        errors.append("schemas/handoff.schema.json 非合法 JSON：{0}".format(exc))
    if schema is not None:
        sections = schema.get("properties", {}).get("sections", {})
        enum = sections.get("items", {}).get("properties", {}).get("heading", {}).get("enum")
        if enum != contract.HEADINGS:
            errors.append("schema 的章節 enum 與契約模組不一致")
        status_enum = schema.get("$defs", {}).get("status", {}).get("enum")
        if status_enum != list(contract.STATUS_TAGS):
            errors.append("schema 的狀態標記 enum 與契約模組不一致")
        if schema.get("title", "").find(contract.SKILL_NAME) < 0:
            errors.append("schema title 應含 skill 名稱")

    # 6) output-contract 的九節與狀態標記
    for heading in contract.HEADINGS:
        if output_contract.count("## " + heading) != 1:
            errors.append("references/output-contract.md 的章節「{0}」應恰好出現一次".format(heading))
    positions = [output_contract.find("## " + h) for h in contract.HEADINGS]
    if positions != sorted(positions):
        errors.append("references/output-contract.md 的章節順序與凍結順序不符")
    for tag in contract.STATUS_TAGS:
        if tag not in output_contract:
            errors.append("references/output-contract.md 未定義狀態標記 {0}".format(tag))
    declared = set(re.findall(r"\[[A-Z][A-Z0-9_]{2,}\]", output_contract))
    unexpected = declared - set(contract.ALLOWED_BRACKET_TOKENS)
    if unexpected:
        errors.append("references/output-contract.md 出現契約外的標記：{0}".format(sorted(unexpected)))

    # 7) SKILL.md 重複行
    seen = {}
    for lineno, line in enumerate(skill.splitlines(), 1):
        norm = line.strip()
        if len(norm) < 24 or norm.startswith(("|", ">", "#", "-", "`")):
            continue
        if norm in seen:
            errors.append("SKILL.md 重複行（L{0} 與 L{1}）：{2}".format(seen[norm], lineno, norm[:40]))
        seen[norm] = lineno

    # 8) 舊名稱與舊版本殘留
    errors.extend(scan_legacy(root))

    # 9) 編碼
    problems, _checked = check_tree(root)
    errors.extend(problems)

    # 10) scripts 可編譯
    scripts_dir = os.path.join(root, "scripts")
    cache_dir = tempfile.mkdtemp(prefix="ai-session-handoff-pyc-")
    try:
        for name in sorted(os.listdir(scripts_dir)):
            if name.endswith(".py"):
                try:
                    py_compile.compile(os.path.join(scripts_dir, name), doraise=True,
                                       cfile=os.path.join(cache_dir, name + "c"))
                except py_compile.PyCompileError as exc:
                    errors.append("scripts/{0} 無法編譯：{1}".format(name, exc))
    finally:
        shutil.rmtree(cache_dir, ignore_errors=True)

    # 11) 單一 shell 命令與硬編碼路徑
    for token in SINGLE_SHELL_COMMANDS:
        if token in skill:
            errors.append("SKILL.md 出現只服務單一 shell 的無條件命令：{0}".format(token.strip()))
    for token in HARDCODED_PATHS:
        if token in skill:
            errors.append("SKILL.md 出現硬編碼路徑：{0}".format(token))

    # 12) 每項能力都有降級說明
    for key in detect_capabilities.CAPABILITY_KEYS:
        if key not in platform_doc:
            errors.append("references/platform-capabilities.md 未涵蓋能力：{0}".format(key))

    return errors


def scan_legacy(root):
    """掃描套件內所有文字檔的舊名稱與舊版本字串。"""
    findings = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".git")]
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            rel = os.path.relpath(path, root).replace("\\", "/")
            if not (name.endswith((".md", ".py", ".json", ".yaml", ".yml", ".txt"))
                    or name == "LICENSE"):
                continue
            try:
                text, _ = read_text(path, allow_bom=True)
            except DecodeFailure:
                continue
            for literal in LEGACY_STRINGS:
                if literal in text:
                    findings.append("{0} 殘留舊字串：{1}".format(rel, literal))
            for pattern in LEGACY_PATTERNS:
                m = pattern.search(text)
                if m:
                    findings.append("{0} 殘留舊版本或舊名稱樣式：{1}".format(rel, m.group(0)))
    return findings


def check_zip(zip_path):
    """檢查封裝可在 Windows 與 Linux 正確解壓，且不含舊字串。"""
    errors = []
    with zipfile.ZipFile(zip_path) as archive:
        bad = archive.testzip()
        if bad:
            errors.append("ZIP 內容毀損：{0}".format(bad))
        for info in archive.infolist():
            name = info.filename
            try:
                name.encode("ascii")
            except UnicodeEncodeError:
                errors.append("ZIP entry 名稱含非 ASCII 字元，跨平台解壓有風險：{0}".format(name))
            if "\\" in name:
                errors.append("ZIP entry 使用反斜線分隔，Linux 解壓會產生怪檔名：{0}".format(name))
            if name.startswith("/") or ".." in name.split("/"):
                errors.append("ZIP entry 為絕對路徑或含上層參照：{0}".format(name))
            if name.endswith("/"):
                continue
            if "tests/fixtures/encoding/" in name:
                continue  # 刻意帶 BOM／CP950／不可解碼位元組的測試素材
            data = archive.read(name)
            if data.startswith(b"\xef\xbb\xbf"):
                errors.append("ZIP 內檔案含 BOM：{0}".format(name))
            if name.endswith((".md", ".py", ".json", ".yaml", ".yml", ".txt")) or \
                    name.endswith("LICENSE"):
                try:
                    text = data.decode("utf-8")
                except UnicodeDecodeError as exc:
                    errors.append("ZIP 內檔案非 UTF-8：{0}（byte {1}）".format(name, exc.start))
                    continue
                for literal in LEGACY_STRINGS:
                    if literal in text:
                        errors.append("ZIP 內 {0} 殘留舊字串：{1}".format(name, literal))
                for pattern in LEGACY_PATTERNS:
                    m = pattern.search(text)
                    if m:
                        errors.append("ZIP 內 {0} 殘留舊版本樣式：{1}".format(name, m.group(0)))
    return errors


def main(argv):
    from _console import configure_console
    configure_console()
    args = [a for a in argv if not a.startswith("--")]
    root = args[0] if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    contract.assert_frozen()
    errors = check_package(root)
    if "--zip" in argv:
        idx = argv.index("--zip")
        if idx + 1 >= len(argv):
            print("用法：python scripts/validate_skill.py [root] [--zip <package.zip>]")
            return 2
        errors.extend(check_zip(argv[idx + 1]))
    if errors:
        print("[FAIL] 套件驗證未過（{0} 項）：".format(len(errors)))
        for item in errors:
            print("  - {0}".format(item))
        return 1
    print("[OK] 套件驗證通過：名稱 {0}、版本 {1}、必要檔案齊備、契約一致、無舊版殘留。".format(
        contract.SKILL_NAME, contract.VERSION))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
