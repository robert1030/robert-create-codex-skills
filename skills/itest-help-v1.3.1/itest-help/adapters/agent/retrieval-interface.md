# Retrieval Interface

本地 reference implementation 是，從 skill 根目錄執行：

```text
python3 scripts/search_itest_help.py "<query>" --limit 10
```

`--limit` 預設為 10。分數常擠在很窄的區間，設得更低會把切題但詞頻略低的來源擋在回傳範圍外。查詢構詞與多輪檢索的規則見 [../../core/retrieval-policy.md](../../core/retrieval-policy.md)

`text` 是**片段**，由查詢詞命中位置附近的數個視窗組成，視窗之間以 `…` 分隔。`text_length` 為全文字元數，`text_truncated` 為 `true` 時代表尚有未顯示內容，需以 `inspect_chunk.py` 或 `--full` 取得完整 Chunk 後才可判斷證據充分性。

Claude Code 與 Claude CLI 改帶 `${CLAUDE_SKILL_DIR}`，Windows 一律改用 `py -3`，不要用 `python3`。腳本以自身位置定位索引，工作目錄不影響結果。

等效的邏輯工具請接受：

```json
{
  "query": "Tcl Test Step",
  "version": "26.2.0",
  "component": "Tcl Test Step",
  "limit": 5
}
```

成功回應必須包含：

```json
{
  "status": "ok",
  "results": [
    {
      "chunk_id": "...",
      "source_file": "topics/...",
      "document_version": "26.2.0",
      "title": "...",
      "heading_path": ["..."],
      "locators": [{"dom_path": "..."}],
      "source_sha256": "...",
      "content_sha256": "...",
      "text": "...",
      "text_length": 30499,
      "text_truncated": true
    }
  ]
}
```

沒有結果時回傳 `{"status":"no_results","results":[]}`。索引或來源資料不完整時回傳 `status: integrity_error`，不能把部分結果包裝成完整答案。
