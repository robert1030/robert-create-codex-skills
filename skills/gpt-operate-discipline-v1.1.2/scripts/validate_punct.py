#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全形標點與禁破折號驗證。

支援 UTF-8、UTF-8 BOM 與 CP950 的嚴格解碼，不會忽略解碼錯誤。
用法：python scripts/validate_punct.py <handout.html|doc.md>
"""
import argparse
import re
import sys
from pathlib import Path

HALF = {",": "，", ";": "；", ":": "：", "!": "！", "?": "？", "(": "（", ")": "）", ".": "。"}
CJK = r"\u4e00-\u9fff\u3000-\u303f\uff00-\uffef"
DASH = re.compile(r"——|—|–")


def _blank_keep_lines(match):
    return "\n" * match.group(0).count("\n")


def read_text_strict(path: Path, encoding: str = "auto") -> str:
    raw = path.read_bytes()
    if encoding not in {"auto", "utf-8", "utf-8-sig", "cp950"}:
        raise ValueError(f"不支援的 encoding：{encoding}")
    if encoding != "auto":
        return raw.decode(encoding, errors="strict")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig", errors="strict")

    successful = {}
    failures = []
    for candidate in ("utf-8", "cp950"):
        try:
            successful[candidate] = raw.decode(candidate, errors="strict")
        except UnicodeDecodeError as exc:
            failures.append(f"{candidate}：{exc.reason} at byte {exc.start}")
    if len(successful) == 1:
        return next(iter(successful.values()))
    if len(successful) == 2:
        if successful["utf-8"] == successful["cp950"]:
            return successful["utf-8"]
        raise UnicodeError("auto 解碼不明確：UTF-8 與 CP950 結果不同，請以 --encoding utf-8 或 --encoding cp950 指定。")
    raise UnicodeError("；".join(failures))


def check(path: str, encoding: str = "auto") -> int:
    source = Path(path)
    try:
        raw = read_text_strict(source, encoding)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"FAIL：無法以指定 encoding 嚴格讀取「{source}」：{exc}")
        return 2

    if source.suffix.lower() in {".md", ".markdown"}:
        text = re.sub(r"```.*?```", _blank_keep_lines, raw, flags=re.DOTALL)
        text = re.sub(r"`[^`\n]*`", "", text)
    else:
        text = re.sub(r"<style[^>]*>.*?</style>", _blank_keep_lines, raw, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r"<script[^>]*>.*?</script>", _blank_keep_lines, text, flags=re.DOTALL | re.IGNORECASE)

    issues = []
    dashes = []
    for lineno, line in enumerate(text.splitlines(), 1):
        visible = re.sub(r"<[^>]+>", "", line)
        for ch, full in HALF.items():
            for match in re.finditer(re.escape(ch), visible):
                index = match.start()
                before = visible[index - 1] if index else ""
                after = visible[index + 1] if index + 1 < len(visible) else ""
                if re.match(f"[{CJK}]", before) or re.match(f"[{CJK}]", after):
                    snippet = visible[max(0, index - 12):index + 12].strip()
                    issues.append((lineno, ch, full, snippet))
        for match in DASH.finditer(visible):
            snippet = visible[max(0, match.start() - 12):match.start() + 12].strip()
            dashes.append((lineno, match.group(0), snippet))

    if not issues and not dashes:
        print("PASS：全形標點驗證通過，中文裡沒有半形標點，也沒有破折號。")
        return 0
    if issues:
        print(f"FAIL：發現 {len(issues)} 處中文裡的半形標點（應改全形）：")
        for lineno, ch, full, snippet in issues:
            print(f"  L{lineno}: 半形「{ch}」應為全形「{full}」：{snippet}")
    if dashes:
        print(f"FAIL：發現 {len(dashes)} 處破折號（硬性規則：一律不得使用）：")
        for lineno, dash, snippet in dashes:
            print(f"  L{lineno}: 破折號「{dash}」：{snippet}")
    return 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="全形標點與禁破折號驗證")
    parser.add_argument("--encoding", choices=("auto", "utf-8", "utf-8-sig", "cp950"), default="auto")
    parser.add_argument("path")
    args = parser.parse_args()
    sys.exit(check(args.path, args.encoding))
