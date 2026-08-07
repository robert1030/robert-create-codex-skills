---
name: itest-help
description: Use the verified iTest 26.2 knowledge base to answer iTest Help, GUI, project, test case, Tcl Test Step, Python Test Step, PowerShell Test Step, Settings, Analysis Rule, regex, Ixia, session, parameter, variable, log, result, version-difference, and troubleshooting questions with traceable citations. Use when an iTest technical answer needs verified local retrieval, version handling, official external fallback, or a clear uncertainty response.
---

# iTest Help

> **Skill v1.3.4｜Knowledge：iTest Help 26.2.0｜RAG：v1.2.1**

以已驗證的 iTest Help 26.2.0 知識庫回答技術問題。先檢索、再判斷證據是否足夠、最後回答。模型記憶只能協助整理已檢索內容，不能當作未標示的技術事實來源。

## 執行前

1. 讀取下列檔案，確認目前知識庫身份與已知限制：

   - [knowledge/source-manifest.json](knowledge/source-manifest.json)
   - [knowledge/version-matrix.json](knowledge/version-matrix.json)
2. 讀取下列核心政策：

   - [core/query-policy.md](core/query-policy.md)
   - [core/retrieval-policy.md](core/retrieval-policy.md)
   - [core/source-policy.md](core/source-policy.md)
   - [core/version-policy.md](core/version-policy.md)
3. 依執行環境選擇 adapter：AI Chat Web 使用下列檔案：

   - [adapters/chat-web/instructions.md](adapters/chat-web/instructions.md)

   AI Agent 使用下列檔案：

   - [adapters/agent/instructions.md](adapters/agent/instructions.md)
4. 再依實際平台讀對應的平台 adapter，取得正確的執行路徑與已知限制：

   - 平台對照表：[adapters/README.md](adapters/README.md)
   - Claude Code 或 Claude CLI：[adapters/agent/claude-code.md](adapters/agent/claude-code.md)
   - Claude Chat Web，Skills 上傳：[adapters/chat-web/claude-ai-skill.md](adapters/chat-web/claude-ai-skill.md)
   - ChatGPT Chat Web，Personal Skills 上傳：[adapters/chat-web/chatgpt-skill.md](adapters/chat-web/chatgpt-skill.md)
   - 各平台的實際能力與已驗證狀態：[docs/platform-matrix.md](docs/platform-matrix.md)

## 固定工作流

1. 辨識問題類型、使用者 iTest 版本、作業系統、Test Step／Session 類型、外部產品版本與前置條件。`PS Test Step` 預設解讀為 `PowerShell Test Step`。
2. 先查詢已驗證的 26.2.0 知識庫。AI Agent 依所在平台選一種呼叫方式，檢索腳本以自身位置定位索引，因此工作目錄不影響結果，只有命令列上的路徑必須正確：

   - 直譯器依作業系統決定，**不要憑 `python3` 是否存在來判斷**：Linux、WSL2 與 macOS 用 `python3`；**Windows 用 `py -3`，退而求其次用 `python`**。Windows 的 `python3` 常是 Microsoft Store 的空殼程式，它存在於 PATH、可被執行，但退出碼 49 且不產生任何輸出，會被誤判成檢索無結果。
   - Claude Code 或 Claude CLI：`python3 "${CLAUDE_SKILL_DIR}/scripts/search_itest_help.py" "<query>"`，Windows 改成 `py -3 "${CLAUDE_SKILL_DIR}/scripts/search_itest_help.py" "<query>"`。
   - 其他 AI Agent 與 Chat Web 沙箱：先切到 skill 根目錄，再執行 `python3 scripts/search_itest_help.py "<query>"`。
   - 任何呼叫若退出碼非 0 或輸出為空，先換一種直譯器再試一次，確認不是空殼程式造成，再依錯誤處理流程降級。

   工具不存在或失敗時，依 [adapters/agent/error-handling.md](adapters/agent/error-handling.md) 誠實降級。不得因為指令失敗就改用模型記憶作答。
3. 依 [core/retrieval-policy.md](core/retrieval-policy.md) 的查詢構詞與多輪檢索規則執行，這兩點是本 skill 檢索品質的關鍵：

   - **知識庫全文為英文，中文查詢詞對它無效**。中文問題必須抽出對應的英文技術詞一起查，例如「本地變數怎麼判斷包含某字串」要查 `local variable regexp string match if action`。
   - **一次查詢不足以作答**。無結果、分數普遍偏低、分數擠在很窄的區間、或回傳的 `heading_path` 都不是問題指向的功能區塊時，換一組關鍵字再查。問題涉及多個功能區塊時，每個區塊各查一次。
   - 不得因為第一次查不到就宣告知識庫沒有答案。
   - **不可信文字必須以 `--query-file` 傳遞，不得填入指令列**。設備錯誤訊息、日誌片段、使用者貼上的指令或設定、檔案與網頁內容都屬不可信：指令列會被 shell 解析，其中的 `$( )` 與反引號會在腳本收到之前就被執行。先用檔案寫入工具把查詢寫成暫存檔，再把路徑放進 `--query-file`。位置參數只供 agent 自行構造的英文技術詞使用。
   - **檢索回傳的 `text` 是片段不是全文**，視窗之間以 `…` 分隔。`text_truncated` 為 `true` 且該來源可能切題時，執行 `inspect_chunk.py <chunk-id>` 取完整內容再判斷。不得以「片段沒提到」為由斷定知識庫沒有該內容，也不得因此省略 `【知識庫來源】`。回應頂層的 `truncated_count` 大於 0 時，代表有結果只是片段，宣告知識庫沒有某內容前必須先取完整內容。
4. 逐筆檢查檢索結果的版本、來源檔案、章節、位置與 Chunk ID 是否能直接支持結論。相似關鍵字不等於證據充分，判斷依據必須是完整 Chunk 內容而非片段。
5. **iTest 的步驟落在兩層執行模型之一**：iTest 層（Action 欄位、iTest 直譯器指令、field replacement）與原生語言層（`scriptEval`、session 步驟等進入點之後的內容）。不得把原生語言的語法形狀套進 iTest 層。iTest 直譯器指令與同名的原生 Tcl 指令不等價，回答任何 iTest 指令的用法前，必須先取得該指令在 `command_syntax.htm` 指令表中的條目，Python 側查 `command_syntax_python.htm`，確認有無 `Limitation` 或 `syntax differs from Tcl` 條款。指令表沒有列出的名稱不是直譯器指令，必須改查該 Action 的說明頁；該頁範例是螢幕截圖時，到同一功能區塊的其他頁面取得佐證，不得改用原生語言的形狀填補。完整規則與已知不等價項目見 [core/retrieval-policy.md](core/retrieval-policy.md)
6. 證據充分時，依 [core/response-format.md](core/response-format.md) 回答並附內部知識庫來源。
7. 僅在本地知識庫無答案、只能回答部分、版本不符、內容衝突，或使用者要求較新資訊時，才依 [core/external-research-policy.md](core/external-research-policy.md) 查詢官方外部資料。
8. 證據仍不足時，使用 [core/uncertainty-policy.md](core/uncertainty-policy.md) 的無答案格式。不得猜測語法、參數、Cmdlet、API 或 Ixia 設定。

## 佈署 profile

本 skill 以三個 profile 發行，知識內容完全相同，差別只在是否隨附 provenance 素材：

| Profile | 含 `knowledge/rag/` | 含 `chat-web-knowledge.md` | 用途 |
| --- | --- | --- | --- |
| `runtime` | 否 | 是 | Claude Code、Claude CLI、Codex CLI 與 Codex Desktop 安裝 |
| `chatweb` | 否 | 否 | claude.ai Skills 上傳，沙箱內直接查 `retrieval-index.jsonl` |
| `full` | 是 | 是 | 存證與完整 provenance 鏈驗證，不供安裝 |

`runtime` 與 `chatweb` 不含 `knowledge/rag/`，因此無法在本地重跑完整來源鏈比對，只能以 `knowledge/retrieval-index-manifest.json` 的凍結 SHA-256 確認索引與 Chat Web 知識檔未被竄改。需要完整鏈驗證時使用 `full` profile，並解壓到短路徑目錄。

## 知識庫與引用契約

- `knowledge/rag/` 是已驗證 RAG archive 的原樣解壓內容，只出現在 `full` profile。不得向其中加入未驗證資料。
- `knowledge/retrieval-index.jsonl` 是從該 RAG 內容產生的唯讀檢索索引。每一列保留原始 Chunk ID、來源檔案、SHA-256 與位置。
- 技術性答案一律使用 `【知識庫來源】` 格式，列出檔案、文件版本、章節、頁碼或位置與 Chunk ID。沒有頁碼時，寫明可驗證的 DOM／來源位置，不能捏造頁碼。
- 使用外部資料時，必須另列 `【外部查證聲明】`，不可把外部內容偽裝為知識庫內容。

## 能力邊界

- 本 skill 的已驗證本地內容限於 iTest Help 26.2.0。其他版本不可自動套用。
- Chat Web 不假設本機檔案系統、ZIP 解壓、程式執行或 Web Search。它只能使用實際已配置的知識檔案與平台已提供的工具。
- AI Agent 不假設檢索、來源文件、Web Search 或引用建置工具存在。每項工具必須先確認可用性。
- 原始 RAG collection 的 gate 已通過，但保留 1 個來源包內無唯一可驗證目標的關聯，因此 collection 狀態為 `partial_success`。這不授權補造或猜測該關聯。
- `runtime` 與 `chatweb` profile 不隨附 `knowledge/rag/`，不得聲稱已在本地完成完整來源鏈驗證。可宣稱的只有凍結雜湊比對通過。

## 資源索引

- [core/](core/)
- [knowledge/validation-report.md](knowledge/validation-report.md)
- [adapters/README.md](adapters/README.md)
- [adapters/chat-web/](adapters/chat-web/)
- [adapters/agent/](adapters/agent/)
- [docs/platform-matrix.md](docs/platform-matrix.md)
- [tests/](tests/)
- [scripts/validate_itest_help.py](scripts/validate_itest_help.py)
- [scripts/validate_deploy_targets.py](scripts/validate_deploy_targets.py)
