# AI Agent Instructions

先確認工具存在、權限範圍與實際輸出，再宣稱已完成檢索或外部查證。優先使用已打包的本地 RAG；外部官方資料只在本地證據不足時使用。

1. 讀取 `knowledge/source-manifest.json`，確認 RAG identity、版本與已知限制。
2. 有檔案與 Python 能力時，從 skill 根目錄執行 `python3 scripts/search_itest_help.py "<query>"`。Claude Code 與 Claude CLI 改用 `python3 "${CLAUDE_SKILL_DIR}/scripts/search_itest_help.py" "<query>"`，路徑規則見 [claude-code.md](claude-code.md) 一檔。Windows 一律用 `py -3`，不要用 `python3`，因為 Windows 的同名 Microsoft Store 空殼程式退出碼 49 且零輸出，會被誤判成檢索無結果。沒有能力時，回報 `tool_unavailable`，依 [error-handling.md](error-handling.md) 降級。
3. 依 [../../core/retrieval-policy.md](../../core/retrieval-policy.md) 執行查詢構詞與多輪檢索：知識庫全文為英文，中文問題必須抽出英文技術詞一起查；無結果、分數普遍偏低、分數擠在很窄的區間，或回傳的 `heading_path` 都不是問題指向的功能區塊時，換一組關鍵字再查，不得只查一次就宣告知識庫沒有答案。
4. 檢查每筆結果的 `chunk_id`、`source_file`、`document_version`、`heading_path`、`locators`、`source_sha256` 與 `content_sha256`。回傳的 `text` 是片段，`text_truncated` 為 `true` 且該來源可能切題時，先執行 `inspect_chunk.py` 取完整內容，不得以片段未涵蓋為由省略 `【知識庫來源】`。
5. iTest 直譯器指令與同名的原生 Tcl 指令不等價。回答任何 iTest 指令用法前，先取得該指令在 `command_syntax.htm` 指令表中的條目，確認有無 `Limitation` 或 `syntax differs from Tcl` 條款，未查證前不得以原生 Tcl 行為作答。iTest 直譯器、Tcl 直譯器與 Tcl Shell Session 是三個獨立環境，不可混用。
6. 只有直接支持答案的結果可進入 `【知識庫來源】`。需要完整 Chunk 時執行 `python3 scripts/inspect_chunk.py <chunk-id>`，路徑規則同上。
7. 本地結果不充分、版本不符或衝突時，只有 `official_web_search` 實際可用時才查官方來源。否則輸出誠實的無答案狀態。
8. 使用 [../../core/response-format.md](../../core/response-format.md) 或 [../../core/uncertainty-policy.md](../../core/uncertainty-policy.md) 交付結果。

工具介面定義如下：

- [tool-contracts.md](tool-contracts.md)
- [retrieval-interface.md](retrieval-interface.md)
- [web-search-interface.md](web-search-interface.md)
