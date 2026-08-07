#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全形標點與禁破折號驗證。"""

import re
import sys


HALF = {',': '，', ';': '；', ':': '：', '!': '！', '?': '？', '(': '（', ')': '）', '.': '。'}
CJK = r'\u4e00-\u9fff\u3000-\u303f\uff00-\uffef'
DASH = re.compile(r'\u2014\u2014|\u2014|\u2013')


def _blank_keep_lines(match):
    return '\n' * match.group(0).count('\n')


def check(path: str) -> int:
    with open(path, encoding='utf-8') as handle:
        raw = handle.read()
    if path.lower().endswith(('.md', '.markdown')):
        text = re.sub(r'```.*?```', _blank_keep_lines, raw, flags=re.DOTALL)
        text = re.sub(r'`[^`\n]*`', '', text)
    else:
        text = re.sub(r'<style[^>]*>.*?</style>', _blank_keep_lines, raw, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<script[^>]*>.*?</script>', _blank_keep_lines, text, flags=re.DOTALL | re.IGNORECASE)

    issues = []
    dashes = []
    for line_number, line in enumerate(text.splitlines(), 1):
        visible = re.sub(r'<[^>]+>', '', line)
        for character, full_width in HALF.items():
            for match in re.finditer(re.escape(character), visible):
                index = match.start()
                before = visible[index - 1] if index > 0 else ''
                after = visible[index + 1] if index + 1 < len(visible) else ''
                if re.match(f'[{CJK}]', before) or re.match(f'[{CJK}]', after):
                    issues.append((line_number, character, full_width, visible[max(0, index - 12):index + 12].strip()))
        for match in DASH.finditer(visible):
            dashes.append((line_number, match.group(0), visible[max(0, match.start() - 12):match.start() + 12].strip()))

    if not issues and not dashes:
        print('全形標點驗證通過，中文裡沒有半形標點，也沒有破折號。')
        return 0
    for line_number, character, full_width, snippet in issues:
        print(f'L{line_number}: 半形「{character}」應為全形「{full_width}」：...{snippet}...')
    for line_number, dash, snippet in dashes:
        print(f'L{line_number}: 破折號「{dash}」：...{snippet}...')
    return 1


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('用法：python scripts/validate_punct.py <handout.html|doc.md>')
        sys.exit(2)
    sys.exit(check(sys.argv[1]))
