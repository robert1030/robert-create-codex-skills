# Claude Chat Web Skills 上傳 Adapter

本檔只補 claude.ai 自訂 Skills 這條路徑的前提、步驟與限制，基礎流程請先讀 [instructions.md](instructions.md)

Claude Chat Web 有兩條可行路徑，先用下面的判斷樹選一條：

```text
方案是 Pro、Max、Team 或 Enterprise，且已啟用 code execution
  → 走本檔的 Skills 上傳路徑，引用完整度最高
否則
  → 走 Project 知識庫路徑，見 knowledge-configuration.md
```

## 已實測確認（2026-08-02）

使用者在 Claude Chat Web 安裝 `chatweb` profile 後，實測 [conversation-starters.md](conversation-starters.md) 的兩題：

1. 「我在 Windows 上使用 iTest PowerShell Test Step，請先確認知識庫是否有對應內容與前置條件」，取回 `itest-help_26.2.0.zip-topics-overview_session_types.htm-0436c0784363-3c6ac59414a7-chunk-0002`，回答正確示範了不確定性政策：確認 PowerShell 是內建 Session 類型，但誠實聲明查不到專屬前置條件頁面，沒有用模型記憶補造。
2. 「iTest Analysis Rule 的 Regex 設定有哪些已驗證注意事項」，取回 `arules_extractor_properties.htm-c63fae3d7086-b0842ab66efe-chunk-0001`、`-chunk-0002` 與 `popups/regexp.html-80ce55fb4c7a-a2a64710daa3-chunk-0001`。前兩筆與稍早 ChatGPT Chat Web 實測取回的 chunk_id 完全一致。

兩組結果的 Chunk ID、來源檔案與章節路徑均可對回 `knowledge/retrieval-index.jsonl` 的實際記錄，證實 Claude Chat Web 的 Skills 沙箱確實執行了 `scripts/search_itest_help.py`，不是退化成純指令集靠模型記憶回答。詳見 [../../docs/platform-matrix.md](../../docs/platform-matrix.md) 的「Claude Chat Web 實測紀錄」一節。

## 前提

- 方案：Pro、Max、Team 或 Enterprise。
- 必須啟用 code execution。未啟用時 Skills 會呈灰色不可用；Team 與 Enterprise 可能由組織管理員在組織層級關閉。
- 自訂 Skills 在 claude.ai 是個人層級，不跨使用者共用，也不會與 Claude Code 或 Claude API 同步。團隊每個人都要各自上傳一次。

## 上傳步驟

1. 取得 `chatweb` profile 的 zip，即 `itest-help-v1.1.0-chatweb-skill.zip`。zip 內最外層是 `itest-help/` 目錄，內含 `SKILL.md`，不要重新壓縮成別的層次。
2. 在 claude.ai 開啟 Settings，進入 Skills 設定頁，新增自訂 skill 並上傳該 zip。
3. 上傳後確認 skill 名稱顯示為 `itest-help`，說明文字提到 iTest 26.2 與可追溯引用。
4. 用 [conversation-starters.md](conversation-starters.md) 的任一題實測，確認回覆能附上 Chunk ID 與來源檔案。

## 為什麼是 chatweb profile

claude.ai 的 skill zip 有硬性檔案數上限 200。完整包 9,370 檔會直接被拒，錯誤訊息為 `Zip contains too many files (maximum 200)`。`chatweb` profile 約 40 檔，並移除 6.5 MB 的 `chat-web-knowledge.md`，改由沙箱直接查索引。

**這則 200 檔上限來自多筆一致的社群回報，官方文件只寫「ZIP file exceeds size limits」而未公布數字。** 官方也未公布位元組上限，`chatweb` profile 壓縮後控制在數 MB 以內作為安全邊際。若上傳仍被拒，退回 Project 知識庫路徑。

## 沙箱內的檢索

claude.ai 的 Skills 跑在具備檔案系統與 bash 的 code execution 沙箱裡，可直接執行本包的檢索腳本。先切到 skill 目錄再執行：

```bash
python3 scripts/search_itest_help.py "<query>" --limit 5
python3 scripts/inspect_chunk.py "<chunk-id>"
```

檢索腳本只用 Python 標準函式庫，不需要安裝任何套件，符合沙箱不得安裝執行期套件的限制。

## 外部官方查證

沙箱的網路存取由使用者與管理員設定決定，可能是完整、部分或完全沒有。呼叫前必須先確認實際可用，不可假設。無法存取時，依 [instructions.md](instructions.md) 第 5 點寫出「目前執行環境無法存取外部官方資料，因此無法完成外部查證。」

## 已知限制

- `chatweb` profile 不含 `knowledge/rag/` 與 `chat-web-knowledge.md`，本地只能做凍結雜湊比對，不能宣稱完成完整來源鏈驗證。
- 沙箱重啟後檔案仍在，但每次對話的容器是獨立的，不要假設上一輪的檢索結果還在。
- claude.ai 的自訂 Skills 無法由管理員集中派送，也不支援組織層級共用。
