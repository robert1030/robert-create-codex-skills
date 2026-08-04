# 敏感資訊處理政策

**預設行為**：保留資訊的用途與存在位置，不保留秘密值本身。秘密值換成 `[REDACTED]`；下一個 agent 若需要該憑證，寫明安全取得方式，不複製秘密。

**判定的單一真實來源**：`scripts/redaction.py`。`scripts/validate_handoff.py` 會在交付前掃描全文（含程式碼區塊），發現明文秘密即擋下。

## 必須遮蔽

| 類型 | 樣式代號 | 範例情境 |
| --- | --- | --- |
| OpenAI 型態 API key | `openai-api-key` | 對話中貼出的金鑰字串 |
| Anthropic 型態 API key | `anthropic-api-key` | 同上 |
| GitHub token | `github-token` | 自動化腳本的憑證 |
| AWS access key id | `aws-access-key-id` | 部署設定 |
| Google API key | `google-api-key` | 第三方服務串接 |
| Slack token | `slack-token` | 通知整合 |
| JSON Web Token | `jwt` | 登入後的存取權杖 |
| Authorization bearer token | `bearer-token` | curl 指令中的標頭 |
| 密碼或金鑰指派 | `password-assignment`、`password-assignment-zh` | `password=...`、`密碼：...` |
| 連線字串內的密碼 | `connection-string` | 資料庫 URI |
| 私鑰區塊 | `private-key-block` | `BEGIN PRIVATE KEY` 開頭的內容 |
| session cookie | `session-cookie` | 除錯時貼出的 cookie |
| 身分證字號型態的個人識別碼 | `tw-national-id` | 表單測試資料 |

## 不遮蔽（避免過度遮蔽而失去脈絡）

- issue 或 PR 編號、commit 雜湊、branch 名稱、版本號。
- 檔案路徑、URL（除非 URL 本身內嵌憑證）。
- 專案代號、環境名稱、服務名稱。
- 使用者姓名與稱呼等維持對話可讀性所必需的脈絡。
- 一般識別碼，例如 `user_id=42`、UUID、訂單編號。
- 電子郵件位址預設保留，因為常是 commit 作者或聯絡窗口等必要脈絡；若使用者明講要移除，或該位址與密碼成對出現，才一併處理。

## 寫法

秘密存在的事實要留下，值不要留：

```text
- 部署需要 `DEPLOY_TOKEN` 環境變數｜值為 [REDACTED]｜由使用者的密碼管理工具取得，不寫進任何檔案 [CONFIRMED]
- 資料庫連線字串存放於 `.env`（未納入版控）｜密碼欄位 [REDACTED]｜請向維運索取 [BLOCKED]
```

## 邊界

- 遮蔽是機器輔助，不是保證。掃描規則涵蓋常見樣式，涵蓋不到的自訂格式仍需人工判斷。
- 已寫成 `[REDACTED]`、`<REDACTED>`、`***` 的值視為已處理，不重複告警。
- 發現對話中出現不該存在的憑證時，除了遮蔽，也在第八節提醒使用者輪替該憑證。

## 檢查指令

以下 `<python>` 代表當前環境可用的直譯器：

```text
<python> scripts/redaction.py <草稿路徑>
<python> scripts/redaction.py --fix <草稿路徑>
```
