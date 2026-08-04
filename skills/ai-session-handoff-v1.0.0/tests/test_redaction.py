#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""敏感資訊遮蔽測試：抓得到秘密，也不過度遮蔽。"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _harness import check, summary, temp_file  # noqa: E402
from _sample import good_doc  # noqa: E402

import redaction  # noqa: E402
import validate_handoff  # noqa: E402

# 測試素材：以組合方式建構，避免整串樣式被外部掃描工具誤判為真憑證。
OPENAI_KEY = "sk-" + "A1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6"
ANTHROPIC_KEY = "sk-ant-" + "api03-Zz9Yy8Xx7Ww6Vv5Uu4Tt3Ss2Rr1Qq0"
GITHUB_TOKEN = "ghp_" + "abcdefghijklmnopqrstuvwxyz0123456789"
AWS_KEY = "AKIA" + "ABCDEFGHIJKLMNOP"
GOOGLE_KEY = "AIza" + "SyA1b2C3d4E5f6G7h8I9j0K1l2M3n4O5p6q"
SLACK_TOKEN = "xoxb-" + "123456789012-abcdefghijklmnop"
JWT = ("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
       "eyJzdWIiOiIxMjM0NTY3ODkwIn0."
       "SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")

POSITIVE = [
    ("OpenAI 型態 API key", "金鑰是 {0} 請小心".format(OPENAI_KEY)),
    ("Anthropic 型態 API key", "ANTHROPIC_API_KEY={0}".format(ANTHROPIC_KEY)),
    ("GitHub token", "推送用 {0}".format(GITHUB_TOKEN)),
    ("AWS access key id", "部署帳號 {0}".format(AWS_KEY)),
    ("Google API key", "地圖服務 {0}".format(GOOGLE_KEY)),
    ("Slack token", "通知整合 {0}".format(SLACK_TOKEN)),
    ("JWT", "登入後拿到 {0}".format(JWT)),
    ("bearer token", "curl -H 'Authorization: Bearer abcdef0123456789abcdef'"),
    ("password 指派", "password=SuperSecret123"),
    ("中文密碼指派", "資料庫密碼：Sup3rS3cret"),
    ("連線字串密碼", "postgres://admin:Sup3rS3cret@db.internal:5432/app"),
    ("私鑰區塊", "-----BEGIN RSA PRIVATE KEY-----"),
    ("session cookie", "Cookie: sessionid=abcdef0123456789abcdef"),
    ("身分證字號型態", "測試資料 A123456789 需移除"),
]

NEGATIVE = [
    ("commit 雜湊", "修正見 commit 4f3c2b1a9d8e7f6c5b4a3928170615243546a7b8"),
    ("issue 編號", "對應 issue #1234 與 PR #56"),
    ("版本號", "升級到 v2.3.1 後重跑"),
    ("UUID", "任務 id 550e8400-e29b-41d4-a716-446655440000"),
    ("電子郵件", "作者為 someone@example.com"),
    ("一般識別碼", "查詢參數 user_id=42 與 order_no=A12"),
    ("檔案路徑", "設定檔在 config/settings.yaml"),
    ("已遮蔽值", "金鑰值 [REDACTED]，向密碼管理工具索取"),
    ("密碼欄位已遮蔽", "password=[REDACTED]"),
    ("英文散文", "The password policy requires rotation every 90 days."),
]

print("== 必須抓到 ==")
for name, text in POSITIVE:
    check("偵測 {0}".format(name), len(redaction.scan(text)) >= 1)

print("== 不得過度遮蔽 ==")
for name, text in NEGATIVE:
    found = redaction.scan(text)
    if not check("放行 {0}".format(name), found == []):
        print("      誤判內容：{0}".format(found))

print("== 遮蔽行為 ==")
redacted, count = redaction.redact("金鑰是 {0} 請小心".format(OPENAI_KEY))
check("遮蔽後不含原值", OPENAI_KEY not in redacted)
check("遮蔽後帶標記", redaction.REDACTION_MARK in redacted)
check("遮蔽計數正確", count == 1)
check("遮蔽保留脈絡", "請小心" in redacted)
again, _ = redaction.redact(redacted)
check("已遮蔽值不重複處理", again == redacted)
check("遮蔽後掃描乾淨", redaction.scan(redacted) == [])

conn_redacted, _ = redaction.redact("postgres://admin:Sup3rS3cret@db.internal:5432/app")
check("連線字串只遮密碼保留主機", "db.internal" in conn_redacted and "Sup3rS3cret" not in conn_redacted)

print("== 與交接文件驗證器整合 ==")


def errors_for(content):
    path = temp_file(content)
    try:
        return validate_handoff.check(path)[0]
    finally:
        os.unlink(path)


check("交接文件含明文秘密被擋",
      any("明文秘密" in e for e in errors_for(good_doc({2: "金鑰 {0}".format(OPENAI_KEY)}))))
check("程式碼區塊內的秘密也被擋",
      any("明文秘密" in e for e in errors_for(
          good_doc({2: "設定如下：\n\n```bash\nexport API_TOKEN=" + GITHUB_TOKEN + "\n```"}))))
check("遮蔽後的交接文件放行",
      errors_for(good_doc({2: "金鑰值 [REDACTED]，由密碼管理工具取得。"})) == [])

sys.exit(summary("test_redaction"))
