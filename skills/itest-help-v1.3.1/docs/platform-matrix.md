# 平台能力矩陣

> 驗證基準日：2026-08-01。本表的每一格都標示證據等級，不得把推論寫成實測。

## 證據等級定義

- **實測**：在該平台上實際執行過並看到輸出。
- **推論**：依官方文件或程式碼機制推導，未在該平台現地重現。
- **未測**：沒有執行過，也沒有足以推導的依據。

## 能力矩陣

| 平台 | 建議 profile | 本地檢索 | 執行 Python | 檔案系統 | 外部官方查證 | 引用完整度 |
| --- | --- | --- | --- | --- | --- | --- |
| Claude Code | `runtime` | 可用（實測） | 可（實測） | 有（實測） | 有 WebSearch 與 WebFetch（推論） | Chunk ID 完整（實測） |
| Claude CLI | `runtime` | 可用（推論） | 可（推論） | 有（推論） | 同 Claude Code（推論） | Chunk ID 完整（推論） |
| Claude Chat Web，Skills 上傳 | `chatweb` | 可用（實測） | 可（實測） | 有（推論） | 依使用者與管理員設定，可能無（推論） | Chunk ID 完整（實測） |
| Claude Chat Web，Project 知識庫 | 取 `runtime` 的知識檔 | 由平台 RAG 代勞（未測） | 否 | 否 | 依平台設定（推論） | 視平台切塊而定，可能失真（未測） |
| ChatGPT Codex CLI | `runtime` | 可用（推論） | 可（推論） | 有（推論） | 依環境設定（推論） | Chunk ID 完整（推論，由 Codex Desktop 實測結果推導） |
| ChatGPT Codex Desktop | `runtime` | 可用（實測） | 可（實測） | 有（推論） | 依環境設定（推論） | Chunk ID 完整（實測） |
| ChatGPT Chat Web，Personal Skills 上傳 | `chatweb` | 可用（實測） | 可（實測） | 有（推論） | 依方案與管理員設定（推論） | Chunk ID 完整（實測） |
| ChatGPT Chat Web，無 Skills 存取權 | 取 `runtime` 的知識檔 | 由平台 RAG 代勞（未測） | 否 | 否 | 依平台設定（推論） | 視平台切塊而定，可能失真（未測） |
| ChatGPT 工作 | 取 `runtime` 的知識檔 | 由平台 RAG 代勞（未測） | 否 | 否 | 依平台設定（推論） | 視平台切塊而定，可能失真（未測） |

Claude CLI 與 Claude Code 是同一套 skill 機制，個人 skill 都放 `~/.claude/skills/`，因此 Claude CLI 一列由 Claude Code 的實測結果推導。Codex CLI 與 Codex Desktop 用同一套 skill 檔案格式，因此 Codex CLI 一列由 Codex Desktop 的實測結果推導。

## ChatGPT Codex Desktop 實測紀錄（2026-08-02）

使用者以 `runtime` profile 安裝到 ChatGPT Codex Desktop 後，實測 [conversation-starters.md](../adapters/chat-web/conversation-starters.md) 對應的兩題：

| 查詢 | 取回的 Chunk ID | 比對結果 |
| --- | --- | --- |
| 請用 iTest 26.2 Help 說明如何新增 Tcl Test Step，並附 Chunk ID | `topics/test_case_editor_steps_page.htm-dac9c14398f7-4f7a3e000bb4-chunk-0001`、`topics/tcl_steps_adding.htm-1a19b63fc240-9e7a0b5ff50a-chunk-0001` | 與稍早 ChatGPT Chat Web、Claude Code 實測取回的 chunk_id 完全一致 |
| iTest Analysis Rule 的 Regex 設定有哪些已驗證注意事項，並列出對應原始 htm 檔名 | `arules_extractor_properties.htm-c63fae3d7086-b0842ab66efe-chunk-0001`、`-chunk-0002`、`popups/regexp.html-80ce55fb4c7a-a2a64710daa3-chunk-0001` | 與稍早 ChatGPT Chat Web、Claude Chat Web、CP950 對照測試取回的 chunk_id 完全一致 |

第二題的回答額外示範了證據分級的紀律：明確區分「iTest `regexp` 指令使用 Java regex」（本地文件證實）與「Analysis Rule 的 regex extractor 引擎」（extractor 章節未明示，不可直接延伸），沒有把相似關鍵字當成證據充分。這把「ChatGPT Codex Desktop」由未測轉為實測，Codex CLI 因共用同一套格式由此推導為推論級。

**尚未確認的部分**：Codex CLI 終端機介面尚未實機測過；Windows 上是否會踩到 `python3` 空殼程式或 CP950 編碼問題，取決於 Codex Desktop 實際呼叫檢索腳本用的直譯器與主控台編碼，這次測試沒有揭露呼叫細節，仍待確認。

## Claude Chat Web 實測紀錄（2026-08-02）

使用者在 Claude Chat Web 上傳 `itest-help-v1.1.0-chatweb.zip` 後，實測 [conversation-starters.md](../adapters/chat-web/conversation-starters.md) 的兩題：

| 查詢 | 取回的 Chunk ID | 比對結果 |
| --- | --- | --- |
| 我在 Windows 上使用 iTest PowerShell Test Step，請先確認知識庫是否有對應內容與前置條件 | `itest-help_26.2.0.zip-topics-overview_session_types.htm-0436c0784363-3c6ac59414a7-chunk-0002` | Chunk ID 命名格式與雜湊長度均與索引一致，屬新查得的合法記錄 |
| iTest Analysis Rule 的 Regex 設定有哪些已驗證注意事項，並標示適用版本 | `itest-help_26.2.0.zip-topics-arules_extractor_properties.htm-c63fae3d7086-b0842ab66efe-chunk-0001` 與 `-chunk-0002`，另附 `popups/regexp.html-80ce55fb4c7a-a2a64710daa3-chunk-0001` | 前兩筆與稍早 ChatGPT Chat Web 實測、CP950 對照測試取回的 chunk_id 完全一致 |

第一題的回應正確示範了不確定性政策：知識庫確認 PowerShell 是內建 Session 類型，但誠實聲明查不到專屬的前置條件頁面（版本需求、Execution Policy、WinRM 遠端啟用），沒有用模型記憶補造語法或設定值。這把「Claude Chat Web，Skills 上傳」由未測轉為實測，細節見 [../adapters/chat-web/claude-ai-skill.md](../adapters/chat-web/claude-ai-skill.md)

**尚未確認的部分**：使用者實測時的實際 Claude 方案層級（是否為 Pro、Max、Team 或 Enterprise）未知；Claude 桌面 app、手機 app 是否同樣能執行 `scripts/`，尚未實測。

## ChatGPT Chat Web 實測紀錄（2026-08-01）

使用者在 ChatGPT Chat Web 上傳 `itest-help-v1.1.0-chatweb.zip` 後，實測 [conversation-starters.md](../adapters/chat-web/conversation-starters.md) 的兩題：

| 查詢 | 取回的 Chunk ID | 比對結果 |
| --- | --- | --- |
| iTest 26.2 的 Tcl Test Step 怎麼新增，並附 Chunk ID | `itest-help_26.2.0.zip-topics-tcl_steps_adding.htm-1a19b63fc240-9e7a0b5ff50a-chunk-0001` | 與 Claude Code 實測結果的 chunk_id、來源檔案、章節路徑完全一致 |
| iTest Analysis Rule 的 Regex 設定有哪些已驗證注意事項，並標示適用版本 | `itest-help_26.2.0.zip-topics-arules_extractor_properties.htm-c63fae3d7086-b0842ab66efe-chunk-0002`，另附 `-chunk-0001` | 與稍早 CP950 對照測試取回的 chunk_id、來源檔案完全一致 |

兩組結果的 Chunk ID、來源檔案與章節路徑均可對回 `knowledge/retrieval-index.jsonl` 的實際記錄，非模型憑空生成的格式，證實 ChatGPT Chat Web 端確實執行了檢索腳本（或至少正確存取並解析了索引），而不是退化成純指令集靠模型記憶回答。這把「ChatGPT 消費端能否執行 skill 內 `scripts/`」由未測轉為實測，細節見 [../adapters/chat-web/chatgpt-skill.md](../adapters/chat-web/chatgpt-skill.md)

**尚未確認的部分**：使用者實測時的實際 ChatGPT 方案層級未知，官方名單只列 Business、Enterprise、Healthcare、Edu，社群回報範圍可能更寬；ChatGPT 桌面 app、手機 app 與 ChatGPT 工作是否同樣能執行 `scripts/`，尚未實測。

## 作業系統矩陣

| 作業系統 | 安裝 | 檢索腳本 | 直譯器 | 已知注意事項 |
| --- | --- | --- | --- | --- |
| Windows 10 與 11 繁體中文版 | 可（實測） | 可用（實測） | `py -3` 或 `python`，**不可用 `python3`** | 見下方 CP950 與直譯器兩節 |
| Windows 10 與 11 英文版 | 可（推論） | 可用（推論） | `py -3` 或 `python`，**不可用 `python3`** | 與繁中版差異只在預設字碼頁，UTF-8 強制輸出與空殼程式問題同樣適用 |
| WSL2 Ubuntu 26.04 | 可（實測） | 可用（實測） | `python3` | 以 Python 3.14.4 跑過驗證、佈署契約、29 個回歸案例與 17 個 unittest，全綠 |
| 原生 Ubuntu | 可（推論） | 可用（推論） | `python3` | 由 WSL2 結果推導。多數發行版只有 `python3` 沒有 `python`，SKILL.md 已寫明 |

所有腳本只使用 Python 標準函式庫，需要 Python 3.9 以上。已實測的直譯器版本為 Windows 的 3.12.10 與 WSL2 的 3.14.4。全部檔案為無 BOM 的 UTF-8、LF 換行，`scripts/validate_deploy_targets.py` 會逐檔把關，`knowledge/rag/` 因屬凍結原樣內容而豁免。

## Windows 的 python3 空殼程式

Windows 預設在 `%LOCALAPPDATA%\Microsoft\WindowsApps\` 放一個名為 `python3.exe` 的 Microsoft Store 轉接程式。它存在於 PATH、可被執行，但退出碼 49 且不產生任何輸出。以 `python3` 呼叫檢索腳本會得到零位元組的空回應，看起來像知識庫查不到，實際上腳本根本沒被執行，會導致錯誤的降級判斷。

本機實測（Windows 10 Pro 19045）：

| 呼叫 | 輸出 | 退出碼 |
| --- | --- | ---: |
| `py -3 -V` | `Python 3.12.10` | 0 |
| `python -V` | `Python 3.12.10` | 0 |
| `python3 -V` | 無 | 49 |

因此直譯器的選擇規則是**依作業系統決定**，不是依 `python3` 是否存在來判斷。Windows 用 `py -3`，POSIX 用 `python3`。

## CP950 輸出編碼

`knowledge/retrieval-index.jsonl` 的 1,522 筆記錄中，有 **288 筆含 CP950 無法編碼的字元**，包含 NBSP（U+00A0）、非斷字連字號（U+2011）、私用區字元（U+F008、U+F077）、商標符號與零寬空白。檢索腳本以 `ensure_ascii=False` 輸出 JSON，在 CP950 的標準輸出上會直接拋出 `UnicodeEncodeError` 並產生零位元組輸出。

本機的系統 ANSI 字碼頁已設為 UTF-8，無法原生重現，因此改以 `PYTHONIOENCODING=cp950` 精確模擬預設繁體中文 Windows 的標準輸出編碼，在 `chcp 950` 的主控台下做對照實測：

| 版本 | 結果 |
| --- | --- |
| 未加 UTF-8 強制輸出 | `UnicodeEncodeError: 'cp950' codec can't encode character '\xa0'`，退出碼 1，輸出 0 位元組 |
| 已加 UTF-8 強制輸出 | 退出碼 0，輸出 22,051 位元組的有效 JSON |

修補方式是各腳本進入 `main()` 時呼叫 `force_utf8_stdout()`，把 `sys.stdout` 與 `sys.stderr` 重設為 UTF-8 且 `errors="replace"`。此修補在任何平台皆無副作用。

## 路徑長度

| Profile | 檔案數 | 安裝後最長完整路徑 | 是否需要 Windows 長路徑支援 |
| --- | ---: | ---: | --- |
| `runtime` | 47 | 96 字元 | 否 |
| `chatweb` | 46 | 96 字元，實務上不落地安裝 | 否 |
| `full` | 9,376 | 314 字元 | 是，且不得安裝到 skill 目錄 |

上表的路徑長度以 `C:\Users\<16 字元使用者名稱>\.claude\skills\` 為基底模擬，由 `scripts/validate_deploy_targets.py` 每次驗證時重算。

`full` profile 有 1,136 個檔案路徑在安裝到使用者家目錄下的 skill 目錄後會超過 260 字元，全部落在 `knowledge/rag/` 的 `chunks/` 子目錄。它只供存證與完整驗證，請解壓到短路徑，例如 `D:\itest-verify\`。

## 平台限制的證據來源

- Claude Code 個人 skill 路徑與目錄名決定指令名：Claude Code 官方文件，查證日 2026-07-31。
- Agent Skills 的 `name` 上限 64 字元、`description` 上限 1,024 字元：Claude Platform 官方文件，查證日 2026-07-31。
- claude.ai 自訂 Skills 需 Pro 以上方案並啟用 code execution、跑在 code execution 沙箱、不跨介面同步：同上。
- claude.ai skill zip 的 200 檔上限：多筆一致的社群回報，官方文件只寫「ZIP file exceeds size limits」未給數字，屬推論級。
- claude.ai 一般檔案上傳上限 30 MB 每檔：官方說明中心，查證日 2026-07-31。
- ChatGPT Skills 的 zip 50 MB、單一 skill 版本 500 檔、單檔未壓縮 25 MB 上限：OpenAI Skills API 官方文件（developers.openai.com），查證日 2026-08-01。
- ChatGPT Personal Skills 官方 GA 名單為 Business、Enterprise、Healthcare、Edu，Enterprise 與 Edu 預設關閉需管理員開啟，且不跨裝置同步：OpenAI 官方說明中心，查證日 2026-08-01，屬查證級；社群回報名單外帳號仍可見 Skills 分頁，屬未證實的推論。
- ChatGPT Chat Web 能執行 skill 內 `scripts/` 並正確檢索：使用者實測，2026-08-01，見上方「ChatGPT Chat Web 實測紀錄」一節，屬實測級。
- Claude Chat Web 能執行 skill 內 `scripts/` 並正確檢索，且不確定性政策確實生效：使用者實測，2026-08-02，見上方「Claude Chat Web 實測紀錄」一節，屬實測級。
- ChatGPT Codex Desktop 能執行 skill 內 `scripts/` 並正確檢索，且能區分證據強弱：使用者實測，2026-08-02，見上方「ChatGPT Codex Desktop 實測紀錄」一節，屬實測級。
