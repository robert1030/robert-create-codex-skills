#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全形標點＋禁破折號驗證。交付前必跑。
抓出兩類問題：
  1) 中文字旁邊出現半形標點。數字、英文、路徑、網址、指令參數之間的半形標點不算錯。
  2) 全文出現破折號。此為硬性規則：一律不得使用破折號，包含 U+2014、U+2013，以及緊鄰中文的兩個連字號。
會略過 style／script 區塊與 HTML 標籤，只檢查可見文字。
用法：python scripts/validate_punct.py <file>
版本：v2.3-codex（2026-07-06）。
"""
import re
import sys

HALF = {',': '，', ';': '；', ':': '：', '!': '！', '?': '？', '(': '（', ')': '）', '.': '。'}
QUOTE = {'"': '「」或『』', "'": '「」'}
CJK = r'\u4e00-\u9fff\u3000-\u303f\uff00-\uffef'
DASH = re.compile(r'\u2014\u2014|\u2014|\u2013')
DDASH_CJK = re.compile(r'(?<=[\u4e00-\u9fff])--|--(?=[\u4e00-\u9fff])')
TAG = re.compile(r'<[^>]+>')
STYLE_OPEN = re.compile(r'<\s*(style|script)\b', re.I)
STYLE_CLOSE = re.compile(r'<\s*/\s*(style|script)\s*>', re.I)


def _visible_lines(raw):
    hidden = False
    for line in raw.splitlines():
        if hidden:
            if STYLE_CLOSE.search(line):
                hidden = False
            yield ''
            continue
        if STYLE_OPEN.search(line):
            hidden = True
            yield ''
            continue
        yield TAG.sub('', line)


def _is_cjk(ch):
    return bool(ch and re.match(f'[{CJK}]', ch))


def check(path: str) -> int:
    with open(path, encoding='utf-8') as f:
        raw = f.read()

    issues = []
    dashes = []
    for lineno, text in enumerate(_visible_lines(raw), 1):
        for ch, full in HALF.items():
            for m in re.finditer(re.escape(ch), text):
                i = m.start()
                before = text[i - 1] if i > 0 else ''
                after = text[i + 1] if i + 1 < len(text) else ''
                if _is_cjk(before) or _is_cjk(after):
                    snippet = text[max(0, i - 12):i + 12].strip()
                    issues.append((lineno, ch, full, snippet))
        for ch, full in QUOTE.items():
            for m in re.finditer(re.escape(ch), text):
                i = m.start()
                before = text[i - 1] if i > 0 else ''
                after = text[i + 1] if i + 1 < len(text) else ''
                if _is_cjk(before) and _is_cjk(after):
                    snippet = text[max(0, i - 12):i + 12].strip()
                    issues.append((lineno, ch, full, snippet))
        for m in DASH.finditer(text):
            snippet = text[max(0, m.start() - 12):m.start() + 12].strip()
            dashes.append((lineno, m.group(0), snippet))
        for m in DDASH_CJK.finditer(text):
            snippet = text[max(0, m.start() - 12):m.start() + 12].strip()
            dashes.append((lineno, m.group(0), snippet))

    if not issues and not dashes:
        print('✅ 全形標點驗證通過，中文裡沒有半形標點，也沒有破折號。')
        return 0

    if issues:
        print(f'⚠️  發現 {len(issues)} 處中文裡的半形標點（應改全形）：\n')
        for lineno, ch, full, snippet in issues:
            print(f'  L{lineno}：半形「{ch}」應為全形「{full}」 → …{snippet}…')
    if dashes:
        print(f'\n⚠️  發現 {len(dashes)} 處破折號（硬性規則：一律不得使用，請改全形句號／逗號／冒號／頓號）：\n')
        for lineno, d, snippet in dashes:
            print(f'  L{lineno}：破折號「{d}」 → …{snippet}…')
    return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法：python scripts/validate_punct.py <file>')
        sys.exit(2)
    sys.exit(check(sys.argv[1]))
