# AI Chat Web Knowledge Configuration

> 本檔描述的是「Project 知識庫」路徑，適用於 ChatGPT 工作、未啟用 code execution 的 Claude Chat Web，以及沒有 Personal Skills 存取權的 ChatGPT Chat Web。
> Claude Chat Web 若可用 Skills 上傳，引用完整度較高，優先走 [claude-ai-skill.md](claude-ai-skill.md)
> ChatGPT Chat Web 若可用 Personal Skills，已實測引用完整度較高，優先走 [chatgpt-skill.md](chatgpt-skill.md)
> `knowledge/chat-web-knowledge.md` 只隨附於 `runtime` 與 `full` profile，`chatweb` profile 不含此檔。

## 必要配置

在 AI Chat Web 的知識檔案或檢索資料來源設定中，上傳並啟用：

```text
knowledge/chat-web-knowledge.md
```

該檔案由 `knowledge/rag/` 中已驗證的 Chunk 記錄產生，保留 iTest Help 26.2.0、來源檔案、章節、位置、Chunk ID 與內容雜湊。不要改用原始 ZIP，因為 Chat Web 不應假設能解壓 ZIP。

## 配置後檢查

1. 知識檔案名稱標示為 `iTest Help 26.2.0 verified knowledge`。
2. 檢索可找到 `Chunk ID`、`Source file`、`Document version` 與 `Location` 欄位。
3. 使用 conversation starters 中至少一題，確認回答可以附上可追溯的內部來源。
4. 平台若沒有 Web Search，不可宣稱可做外部官方查證。

## 限制與更新

- 目前資料只對應 iTest Help 26.2.0。
- RAG collection 保留 1 個 `source_missing_target` 已知限制。

詳見：[../../knowledge/validation-report.md](../../knowledge/validation-report.md)
- 若替換知識檔案，必須同時更新 source manifest、provenance map、validation report、version matrix 與回歸測試，再重新封裝。
