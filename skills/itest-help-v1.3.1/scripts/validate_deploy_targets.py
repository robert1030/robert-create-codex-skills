#!/usr/bin/env python3
"""驗證 iTest Help skill 是否符合各佈署目標的硬性限制。

擋掉的是「上傳或安裝當下才會爆」的問題：skill 名稱與說明的長度規則、claude.ai 的檔案數上限、
Windows 路徑長度上限、編碼與換行、以及第三方相依。內容正確性由 validate_itest_help.py 負責。
"""

from __future__ import annotations

import argparse
import ast
import re
import sys
from pathlib import Path


PROFILES = ("full", "runtime", "chatweb")
NAME_PATTERN = re.compile(r"^[a-z0-9-]+$")
NAME_MAX = 64
NAME_RESERVED = ("anthropic", "claude")
DESCRIPTION_MAX = 1024
LISTING_MAX = 1536
CHATWEB_MAX_FILES = 200
WINDOWS_PATH_MAX = 260
# 模擬 Windows 個人 skill 安裝路徑 C:\Users\<username>\.claude\skills\，使用者名稱以 16 字元估算。
WINDOWS_BASE_LENGTH = len(r"C:\Users") + 1 + 16 + len(r"\.claude\skills") + 1
TEXT_SUFFIXES = {".md", ".py", ".json", ".jsonl", ".yaml", ".yml", ".txt"}
EXTRA_STDLIB = {"__future__"}
# knowledge/rag/ 是已驗證 RAG archive 的原樣解壓內容，換行與編碼屬凍結契約，不得為了通過檢查而改寫。
FROZEN_SUBTREE = "knowledge/rag/"


def force_utf8_stdout() -> None:
    """Windows 主控台預設字碼頁可能是 CP950，強制 UTF-8 輸出以免 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def parse_frontmatter(text: str) -> dict[str, str]:
    """只取本 skill 用到的純量欄位，不引入 YAML 相依。"""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def check_identity(root: Path, failures: list[str]) -> None:
    require(root.name == "itest-help", f"Skill directory name must be itest-help, found {root.name}", failures)
    fields = parse_frontmatter((root / "SKILL.md").read_text(encoding="utf-8"))
    require(bool(fields), "SKILL.md has no parsable YAML frontmatter", failures)
    name = fields.get("name", "")
    require(bool(name), "SKILL.md frontmatter has no name", failures)
    require(len(name) <= NAME_MAX, f"Skill name is longer than {NAME_MAX} characters", failures)
    require(bool(NAME_PATTERN.match(name)), f"Skill name must be lowercase letters, digits and hyphens: {name}", failures)
    for reserved in NAME_RESERVED:
        require(reserved not in name.lower(), f"Skill name must not contain the reserved word {reserved}", failures)
    description = fields.get("description", "")
    require(bool(description), "SKILL.md frontmatter has no description", failures)
    require(len(description) <= DESCRIPTION_MAX, f"Description is {len(description)} characters, over the {DESCRIPTION_MAX} cap", failures)
    require("<" not in description and ">" not in description, "Description must not contain XML tags", failures)
    listing = len(description) + len(fields.get("when_to_use", ""))
    require(listing <= LISTING_MAX, f"Description plus when_to_use is {listing} characters, over the {LISTING_MAX} listing cap", failures)


def check_file_count(root: Path, profile: str, files: list[Path], failures: list[str]) -> None:
    if profile == "chatweb":
        require(
            len(files) <= CHATWEB_MAX_FILES,
            f"Package holds {len(files)} files, over the claude.ai {CHATWEB_MAX_FILES} file cap",
            failures,
        )


def check_path_length(root: Path, profile: str, files: list[Path], failures: list[str]) -> None:
    """full profile 不供安裝，因此只回報最長路徑，不擋。"""
    longest = 0
    offender = ""
    for path in files:
        relative = path.relative_to(root.parent).as_posix().replace("/", "\\")
        length = WINDOWS_BASE_LENGTH + len(relative)
        if length > longest:
            longest, offender = length, relative
    print(f"Longest simulated Windows install path: {longest} characters")
    if profile == "full":
        if longest >= WINDOWS_PATH_MAX:
            print(f"NOTE: full profile is verification only, do not install it under ~/.claude/skills ({offender})")
        return
    require(
        longest < WINDOWS_PATH_MAX,
        f"Simulated install path reaches {longest} characters, at or over the Windows {WINDOWS_PATH_MAX} limit: {offender}",
        failures,
    )


def check_encoding(root: Path, files: list[Path], failures: list[str]) -> None:
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root).as_posix()
        if relative.startswith(FROZEN_SUBTREE):
            continue
        raw = path.read_bytes()
        require(not raw.startswith(b"\xef\xbb\xbf"), f"File carries a UTF-8 BOM: {relative}", failures)
        require(b"\r\n" not in raw, f"File uses CRLF line endings: {relative}", failures)
        try:
            raw.decode("utf-8")
        except UnicodeDecodeError as error:
            failures.append(f"File is not valid UTF-8: {relative} ({error})")


def check_dependencies(root: Path, files: list[Path], failures: list[str]) -> None:
    """只擋第三方相依。本包自己的模組（例如測試檔 import 同包腳本）不算外部相依。"""
    stdlib = set(getattr(sys, "stdlib_module_names", ())) | EXTRA_STDLIB
    local = {path.stem for path in root.rglob("*.py")}
    for path in files:
        if path.suffix != ".py":
            continue
        relative = path.relative_to(root).as_posix()
        if relative.startswith(FROZEN_SUBTREE):
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in ast.walk(tree):
            modules: list[str] = []
            if isinstance(node, ast.Import):
                modules = [alias.name.split(".")[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                modules = [node.module.split(".")[0]]
            for module in modules:
                if stdlib and module not in stdlib and module not in local:
                    failures.append(f"Non standard library import {module} in {relative}")


def main() -> int:
    force_utf8_stdout()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=None, help="skill 根目錄，省略時取本腳本的上層目錄")
    parser.add_argument("--profile", choices=PROFILES, default=None, help="省略時依目錄內容自動判定")
    args = parser.parse_args()
    root = Path(args.root if args.root else Path(__file__).resolve().parents[1]).resolve()
    if args.profile:
        profile = args.profile
    elif (root / "knowledge" / "rag").is_dir():
        profile = "full"
    elif (root / "knowledge" / "chat-web-knowledge.md").is_file():
        profile = "runtime"
    else:
        profile = "chatweb"
    print(f"Profile: {profile}")

    if not (root / "SKILL.md").is_file():
        print("FAIL: Missing required file: SKILL.md")
        return 1
    files = sorted(path for path in root.rglob("*") if path.is_file())
    print(f"File count: {len(files)}")
    failures: list[str] = []
    check_identity(root, failures)
    check_file_count(root, profile, files, failures)
    check_path_length(root, profile, files, failures)
    check_encoding(root, files, failures)
    check_dependencies(root, files, failures)
    if failures:
        for failure in failures:
            print("FAIL: " + failure)
        return 1
    print("Deploy targets: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
