# iTest Help Skill

此封裝提供 iTest Help 26.2.0 的來源優先查詢流程，可部署到 AI Chat Web 與 AI Agent。

> **Skill v1.3.4｜Knowledge：iTest Help 26.2.0｜RAG：v1.2.1**

## 使用範圍

- 產品：iTest Help。
- 知識庫版本：26.2.0。
- RAG 版本：1.2.1。
- 主要用途：iTest 功能、Test Step、Settings、Analysis Rule、Regex、Ixia、Session、參數、變數、日誌、結果與錯誤排除。

## 三個佈署 profile

知識內容完全相同，差別只在是否隨附 provenance 素材與 Chat Web 知識檔。

| Profile | 檔案數 | 含 `knowledge/rag/` | 用途 |
| --- | ---: | --- | --- |
| `runtime` | 47 | 否 | Claude Code、Claude CLI、Codex CLI 與 Codex Desktop 安裝 |
| `chatweb` | 46 | 否 | claude.ai Skills 上傳，檔案數低於 200 檔上限 |
| `full` | 9,376 | 是 | 存證與完整 provenance 鏈驗證，不供安裝 |

`full` profile 有 1,136 個檔案路徑安裝到使用者家目錄下的 skill 目錄後會超過 Windows 的 260 字元上限，請解壓到短路徑，例如 `D:\itest-verify\`，**不要**放進 `~/.claude/skills/`。

## 部署

- **Claude Code 或 Claude CLI**：`runtime` profile 解壓到 `~/.claude/skills/itest-help/`，目錄名不可改，細節見 [adapters/agent/claude-code.md](adapters/agent/claude-code.md)
- **Claude Chat Web，有 Pro 以上方案且啟用 code execution**：上傳 `chatweb` profile，步驟見 [adapters/chat-web/claude-ai-skill.md](adapters/chat-web/claude-ai-skill.md)
- **ChatGPT Chat Web，有 Personal Skills 存取權**：上傳 `chatweb` profile，已實測可正確檢索並附 Chunk ID，步驟見 [adapters/chat-web/chatgpt-skill.md](adapters/chat-web/chatgpt-skill.md)
- **Claude Chat Web 或 ChatGPT Chat Web，其他情況**：走 Project 知識庫路徑，步驟見 [adapters/chat-web/knowledge-configuration.md](adapters/chat-web/knowledge-configuration.md)
- **ChatGPT Codex CLI 或 Desktop**：保留 `runtime` profile 整個資料夾
- **ChatGPT 工作**：將 `knowledge/chat-web-knowledge.md` 設為已配置知識檔案

延伸資料：

- 平台對照表：[adapters/README.md](adapters/README.md)
- 各平台實際能力與已驗證狀態：[docs/platform-matrix.md](docs/platform-matrix.md)

## 查詢

檢索腳本以自身位置定位索引，工作目錄不影響結果：

```text
python3 scripts/search_itest_help.py "<query>" --limit 10
python3 scripts/inspect_chunk.py "<chunk-id>"
```

**知識庫全文為英文**，中文問題必須抽出對應的英文技術詞一起查，否則關鍵來源排不進回傳範圍。一次查詢不足以作答，規則見 [core/retrieval-policy.md](core/retrieval-policy.md)

Claude Code 用 `python3 "${CLAUDE_SKILL_DIR}/scripts/search_itest_help.py" "<query>"`。

**Windows 一律用 `py -3`，不要用 `python3`**：Windows 的 `python3` 通常是 Microsoft Store 空殼程式，退出碼 49 且零輸出，會被誤判成檢索無結果。細節見 [docs/platform-matrix.md](docs/platform-matrix.md)

只需要 Python 3.9 以上，不需要安裝任何套件。

## 驗證

```text
python scripts/validate_itest_help.py --profile runtime .
python scripts/validate_deploy_targets.py --profile runtime .
python scripts/run_regression_tests.py .
python -m unittest discover -s tests
```

`full` profile 另外可跑完整來源鏈比對：

```text
python scripts/validate_itest_help.py --profile full <full-profile-root>
```

驗證成功只表示 skill 契約、來源鏈與測試案例符合本封裝規則。它不把原始 collection 的 `partial_success` 限制改寫為完整成功。在 `runtime` 與 `chatweb` profile 下不含 `knowledge/rag/`，只能做凍結雜湊比對，不得聲稱完成完整來源鏈驗證。

延伸資料：

- 已知限制：[knowledge/validation-report.md](knowledge/validation-report.md)
- 凍結契約與版本差異：[FROZEN.md](FROZEN.md)
