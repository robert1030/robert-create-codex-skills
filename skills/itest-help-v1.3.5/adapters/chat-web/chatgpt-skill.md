# ChatGPT Chat Web Skills 上傳 Adapter

本檔只補 ChatGPT 自訂 Skills 這條路徑的前提、步驟與限制，基礎流程請先讀 [instructions.md](instructions.md)

ChatGPT Chat Web 有兩條可行路徑，先用下面的判斷樹選一條：

```text
方案支援 Personal Skills（見下方前提），且已在該裝置安裝過本 skill
  → 走本檔的 Skills 上傳路徑，已實測可正確檢索並附 Chunk ID
否則
  → 走 Project 知識庫路徑，見 knowledge-configuration.md
```

## 已實測確認（2026-08-01）

使用者在 ChatGPT Chat Web 安裝 `chatweb` profile 後，實測 [conversation-starters.md](conversation-starters.md) 的兩題：

1. 「請用 iTest 26.2 Help 說明如何新增 Tcl Test Step，並附 Chunk ID」，取回 `itest-help_26.2.0.zip-topics-tcl_steps_adding.htm-1a19b63fc240-9e7a0b5ff50a-chunk-0001`。
2. 「iTest Analysis Rule 的 Regex 設定有哪些已驗證注意事項」，取回 `itest-help_26.2.0.zip-topics-arules_extractor_properties.htm-c63fae3d7086-b0842ab66efe-chunk-0002` 與同一來源檔的 `-chunk-0001`。

兩組 Chunk ID、來源檔案與章節路徑均與本包 `knowledge/retrieval-index.jsonl` 的實際記錄完全吻合，非模型憑空生成的格式。這證實 ChatGPT Chat Web 端確實能正確存取索引內容並回傳可追溯引用，`chatweb` profile 在此路徑可用。

在此之前，官方文件只寫明 skill 的 `scripts/` 資料夾用途是「需要決定性行為或外部工具時使用」，未明確交代 ChatGPT 消費端的腳本執行環境細節，因此這條路徑原本標「未測」。上述兩則測試把它轉為「實測」。

## 前提

- Personal Skills 官方 GA 名單為 ChatGPT Business、Enterprise、Healthcare、Edu；Free、Plus、Pro 不在官方公告名單內，但已有帳號回報在名單外仍看得到 Skills 分頁，實際可用範圍可能比官方名單寬，需自行確認。
- Enterprise 與 Edu 預設關閉，需管理員在 Permissions 與 Roles 開啟。
- Skills 不跨裝置同步，web、桌面 app、手機各自要安裝一次。
- 上傳前 ChatGPT 會先掃描，結果可能是 Needs Review 或 Blocked。

## 上傳步驟

1. 取得 `chatweb` profile 的 zip，即 `itest-help-v1.1.0-chatweb.zip`。zip 內最外層是單一 `itest-help/` 目錄，內含 `SKILL.md`，不要重新壓縮成別的層次。
2. 在 ChatGPT 點頭像，進入 Skills，選擇 Upload from your computer，上傳該 zip。
3. 掃描通過後確認 skill 顯示為 `itest-help`。
4. 用 [conversation-starters.md](conversation-starters.md) 的任一題實測，確認回覆能附上 Chunk ID 與來源檔案。

## 為什麼是 chatweb profile

OpenAI 官方 Skills API 文件公布的硬性上限為 zip 壓縮後 50 MB、單一 skill 版本 500 檔、單檔未壓縮 25 MB。`chatweb` profile 46 檔、壓縮後 1.13 MB、最大單檔（`retrieval-index.jsonl`）未壓縮 7.44 MB，三項都留有數量級的安全邊際。

`chatweb` profile 移除了 `chat-web-knowledge.md`，改由沙箱直接查 `retrieval-index.jsonl`，引用完整度比丟給平台切塊更高，已由上方的實測確認。

## 檢索

先切到 skill 目錄再執行：

```bash
python3 scripts/search_itest_help.py "<query>" --limit 5
python3 scripts/inspect_chunk.py "<chunk-id>"
```

檢索腳本只用 Python 標準函式庫，不需要安裝任何套件。

## 外部官方查證

沙箱的網路存取與工具能力由平台與方案決定，呼叫前必須先確認實際可用，不可假設。無法存取時，依 [instructions.md](instructions.md) 第 5 點寫出「目前執行環境無法存取外部官方資料，因此無法完成外部查證。」

## 已知限制

- `chatweb` profile 不含 `knowledge/rag/` 與 `chat-web-knowledge.md`，本地只能做凍結雜湊比對，不能宣稱完成完整來源鏈驗證。
- 目前只確認了 ChatGPT Chat Web 這一個 surface。ChatGPT 桌面 app、手機 app 與 ChatGPT 工作是否同樣能執行 `scripts/`，尚未實測，細節見 [../../docs/platform-matrix.md](../../docs/platform-matrix.md)
- 使用者實測時的實際方案層級未確認，官方名單與社群回報之間的落差仍待更多樣本釐清。
