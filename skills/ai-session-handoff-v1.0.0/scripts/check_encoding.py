#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""編碼檢查與安全讀檔：canonical 為 UTF-8 without BOM ＋ LF。

政策說明見 references/encoding-policy.md，本檔負責可執行的判定。
硬性原則：
  1. 一律明確指定編碼，不依賴系統預設。
  2. 偵測並回報 UTF-8 BOM，不靜默吞掉。
  3. 遇非 UTF-8 檔案，明確判定為 CP950 後才正規化，並回報這件事。
  4. 兩種編碼都失敗時，回報檔名、嘗試過的編碼與出錯的 byte 位置，
     絕不以替換字元靜默略過。

用法：
  python scripts/check_encoding.py <路徑>        檢查單檔或整個目錄樹
"""
import os
import sys

CANONICAL = "utf-8"
FALLBACK = "cp950"
BOM = b"\xef\xbb\xbf"

TEXT_SUFFIXES = (".md", ".py", ".json", ".yaml", ".yml", ".txt", ".cfg", ".toml")
TEXT_FILENAMES = ("LICENSE",)

# 刻意帶有 BOM／CP950／不可解碼位元組的測試素材，不納入 canonical 檢查。
ENCODING_FIXTURE_DIR = os.path.join("tests", "fixtures", "encoding")


class DecodeFailure(Exception):
    """解碼失敗：帶著檔名、嘗試過的編碼與出錯位置往上拋。"""


def _is_text_file(path):
    name = os.path.basename(path)
    return name in TEXT_FILENAMES or name.lower().endswith(TEXT_SUFFIXES)


def read_text(path, allow_bom=False):
    """安全讀檔，回傳 (text, issues)。issues 為編碼相關的觀察，不代表致命錯誤。"""
    with open(path, "rb") as handle:
        raw = handle.read()
    issues = []
    if raw.startswith(BOM):
        raw = raw[len(BOM):]
        if not allow_bom:
            issues.append("含 UTF-8 BOM，canonical 為 UTF-8 without BOM")
    if b"\r\n" in raw:
        issues.append("含 CRLF 換行，canonical 為 LF")
    try:
        return raw.decode(CANONICAL), issues
    except UnicodeDecodeError as first:
        try:
            text = raw.decode(FALLBACK)
        except UnicodeDecodeError as second:
            raise DecodeFailure(
                "{0}：以 {1} 解碼失敗於 byte {2}；以 {3} 解碼亦失敗於 byte {4}。"
                "請確認原始編碼後再轉為 UTF-8，內容未被替換或略過。".format(
                    path, CANONICAL, first.start, FALLBACK, second.start)
            )
        issues.append(
            "非 UTF-8：以 {0} 解碼失敗於 byte {1}，已明確判定為 {2} 並正規化為 UTF-8".format(
                CANONICAL, first.start, FALLBACK)
        )
        return text, issues


def check_file(path, canonical=True):
    """回傳該檔的問題清單。canonical=False 時只驗可解碼性。"""
    try:
        _text, issues = read_text(path, allow_bom=not canonical)
    except DecodeFailure as exc:
        return [str(exc)]
    if not canonical:
        return []
    return ["{0}：{1}".format(path, issue) for issue in issues]


def _skip(root, path):
    rel = os.path.relpath(path, root)
    return rel.replace("\\", "/").startswith(ENCODING_FIXTURE_DIR.replace("\\", "/"))


def check_tree(root):
    """檢查整個套件樹，回傳 (問題清單, 已檢查檔數)。"""
    problems = []
    checked = 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in ("__pycache__", ".git")]
        for name in sorted(filenames):
            path = os.path.join(dirpath, name)
            if not _is_text_file(path):
                continue
            if _skip(root, path):
                continue
            checked += 1
            problems.extend(check_file(path))
    return problems, checked


def main(argv):
    from _console import configure_console
    configure_console()
    if len(argv) != 1:
        print("用法：python scripts/check_encoding.py <路徑>")
        return 2
    target = argv[0]
    if os.path.isdir(target):
        problems, checked = check_tree(target)
    else:
        problems, checked = check_file(target), 1
    if problems:
        print("[FAIL] 編碼檢查未過（{0} 項）：".format(len(problems)))
        for item in problems:
            print("  - {0}".format(item))
        return 1
    print("[OK] 編碼檢查通過：{0} 個文字檔皆為 UTF-8 without BOM ＋ LF。".format(checked))
    return 0


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1:]))
