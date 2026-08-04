#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""敏感資訊掃描與遮蔽：規則的單一真實來源。

政策說明見 references/redaction-policy.md，本檔負責可執行的判定。
設計原則：
  1. 只抓「秘密值本身」，保留用途與存在位置。
  2. 一般識別碼（issue 編號、commit 雜湊、版號、UUID、電子郵件）不遮蔽，
     避免過度遮蔽讓下一個 agent 失去必要脈絡。
  3. 已寫成 [REDACTED]／<REDACTED>／*** 的值視為已處理，不再回報。

用法：
  python scripts/redaction.py <file>      掃描並列出明文秘密（有發現則退出碼 1）
  python scripts/redaction.py --fix <file>  輸出遮蔽後的內容到 stdout
"""
import re
import sys

REDACTION_MARK = "[REDACTED]"

# 已處理過的值：避免對 [REDACTED] 這類佔位再次告警。
_PLACEHOLDER = re.compile(r"^(\[REDACTED\]|<REDACTED\>|\*{3,}|x{3,}|X{3,}|…|\.\.\.)$")

# (名稱, 樣式, 說明)。樣式若含群組 secret，只遮蔽該群組。
PATTERNS = [
    ("openai-api-key",
     re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_\-]{20,}\b"),
     "OpenAI 型態 API key"),
    ("anthropic-api-key",
     re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}\b"),
     "Anthropic 型態 API key"),
    ("github-token",
     re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
     "GitHub personal access token"),
    ("aws-access-key-id",
     re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
     "AWS access key id"),
    ("google-api-key",
     re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b"),
     "Google API key"),
    ("slack-token",
     re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{10,}\b"),
     "Slack token"),
    ("jwt",
     re.compile(r"\beyJ[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\.[A-Za-z0-9_\-]{10,}\b"),
     "JSON Web Token"),
    ("bearer-token",
     re.compile(r"(?i)\bbearer\s+(?P<secret>[A-Za-z0-9._\-]{16,})"),
     "Authorization bearer token"),
    ("password-assignment",
     re.compile(r"(?i)\b(?:password|passwd|pwd|secret|api[_\-]?key|token)\b\s*[:=]\s*"
                r"(?P<secret>\"[^\"\n]{4,}\"|'[^'\n]{4,}'|[^\s\"',;]{4,})"),
     "密碼或金鑰指派"),
    ("password-assignment-zh",
     re.compile(r"(?:密碼|金鑰|通行碼)\s*[：:=]\s*(?P<secret>[^\s，。；、\"']{4,})"),
     "中文欄位的密碼或金鑰指派"),
    ("connection-string",
     re.compile(r"\b(?:mongodb(?:\+srv)?|postgres(?:ql)?|mysql|redis|amqp|mssql)://"
                r"[^\s:@/]+:(?P<secret>[^\s@/]+)@"),
     "連線字串內的密碼"),
    ("private-key-block",
     re.compile(r"-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----"),
     "私鑰區塊"),
    ("session-cookie",
     re.compile(r"(?i)\b(?:sessionid|session_id|sid|jsessionid|connect\.sid)=(?P<secret>[A-Za-z0-9._\-%]{12,})"),
     "session cookie"),
    ("tw-national-id",
     re.compile(r"(?<![A-Za-z0-9])[A-Z][12]\d{8}(?![A-Za-z0-9])"),
     "身分證字號型態的個人識別碼"),
]


def _span(match):
    """回傳要遮蔽的區間：有 secret 群組就只遮該群組。"""
    if "secret" in (match.re.groupindex or {}):
        return match.span("secret")
    return match.span()


def scan(text):
    """回傳 [(lineno, name, description, snippet)]，只列出仍是明文的秘密。"""
    findings = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for name, pattern, desc in PATTERNS:
            for m in pattern.finditer(line):
                start, end = _span(m)
                value = line[start:end]
                if _PLACEHOLDER.match(value.strip("\"'")):
                    continue
                snippet = line.strip()[:80]
                findings.append((lineno, name, desc, snippet))
    return findings


def redact(text):
    """回傳 (遮蔽後文字, 遮蔽次數)。用途與位置保留，只換掉秘密值。"""
    count = 0
    out_lines = []
    for line in text.splitlines(True):
        stripped = line.rstrip("\r\n")
        newline = line[len(stripped):]
        spans = []
        for _name, pattern, _desc in PATTERNS:
            for m in pattern.finditer(stripped):
                start, end = _span(m)
                value = stripped[start:end]
                if _PLACEHOLDER.match(value.strip("\"'")):
                    continue
                spans.append((start, end))
        for start, end in sorted(spans, reverse=True):
            stripped = stripped[:start] + REDACTION_MARK + stripped[end:]
            count += 1
        out_lines.append(stripped + newline)
    return "".join(out_lines), count


def main(argv):
    from _console import configure_console
    from check_encoding import DecodeFailure, read_text

    configure_console()
    fix = "--fix" in argv
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 1:
        print("用法：python scripts/redaction.py [--fix] <file>")
        return 2
    try:
        text, _issues = read_text(args[0], allow_bom=True)
    except DecodeFailure as exc:
        print("[FAIL] {0}".format(exc))
        return 1
    if fix:
        redacted, count = redact(text)
        sys.stdout.write(redacted)
        sys.stderr.write("[OK] 已遮蔽 {0} 處。\n".format(count))
        return 0
    findings = scan(text)
    if not findings:
        print("[OK] 未偵測到明文秘密。")
        return 0
    print("[FAIL] 偵測到 {0} 處明文秘密：".format(len(findings)))
    for lineno, name, desc, snippet in findings:
        print("  - L{0} {1}（{2}）：{3}".format(lineno, name, desc, snippet))
    return 1


if __name__ == "__main__":
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    sys.exit(main(sys.argv[1:]))
