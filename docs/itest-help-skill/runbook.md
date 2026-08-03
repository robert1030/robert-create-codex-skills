# iTest Help Skill 操作手冊

本手冊說明如何在 Windows PowerShell 使用 `itest-help`。它的主線很簡單：先查本機知識庫，確認來源，再回答。若本機證據不足，只能查官方外部資料；外部資料不可用時，要明確說明無法確認。

規格與可驗證條件見 `SPEC.md`。

## 1. 準備工作

### 目的

確認目前操作的是完整的 skill 資料夾，並讓後續指令使用一致的根目錄。

### 操作

```powershell
$SkillRoot = Join-Path $env:USERPROFILE '.codex\skills\itest-help'
Set-Location -LiteralPath $SkillRoot
python scripts\bootstrap.py
```

### 預期結果

`bootstrap.py` 回報 Python 環境可用，且不需要額外相依套件。

### 驗證

```powershell
Test-Path -LiteralPath .\SKILL.md
Test-Path -LiteralPath .\knowledge\retrieval-index.jsonl
```

兩個指令都應回傳 `True`。

> 注意：`$env:USERPROFILE\.codex\skills\itest-help` 是 Windows 的可攜寫法。若 skill 安裝在其他位置，請把 `$SkillRoot` 改成實際路徑；不要只複製目前電腦的使用者名稱或磁碟代號。

## 2. 查詢本機知識庫

### 目的

先取得與問題相關的已驗證 Chunk，避免用未查證記憶回答。

### 操作

```powershell
python scripts\search_itest_help.py "Tcl Test Step" --limit 5
```

將查詢字串換成使用者的問題。必要時以 `--full` 顯示較完整的結果內容。

### 預期結果

每筆結果應包含 `chunk_id`、`source_file`、`document_version`、標題、章節或位置，以及來源與內容雜湊。

### 驗證

確認要採用的結果是 iTest Help 26.2.0，且文字能直接支持你的結論。相似關鍵字不代表可以下結論。

## 3. 讀取完整 Chunk 與建立引用

### 目的

在回答前補足上下文，並保留使用者可追溯的來源。

### 操作

把 `<chunk-id>` 換成上一步輸出的實際值：

```powershell
python scripts\inspect_chunk.py <chunk-id>
```

### 預期結果

輸出能讓你確認原始檔案、文件版本、章節或位置與內容。

### 驗證

回答中的每個技術結論都要有能直接支持它的來源，並加入：

```text
【知識庫來源】

- 檔案：
- 文件版本：
- 章節：
- 頁碼或位置：
- Chunk ID：
```

沒有頁碼時，填入可驗證的位置並標示「未提供頁碼」。不要推測頁碼。

## 4. 本機結果不足時

### 目的

避免把未知資訊寫成已確認的 iTest 指令或設定。

### 操作

依序確認：結果是否為空、是否只回答到一部分、使用者版本是否不同、或來源是否互相衝突。

只有符合上述情況，且執行環境真的提供 Web Search 時，才查 iTest 官方 Help、官方文件、Support Portal、Knowledge Base、Release Notes、API Reference、Command Reference 或官方整合文件。

### 預期結果

外部內容與本機內容分開標示：

```text
【外部查證聲明】

本答案有部分內容無法由目前的 iTest 知識庫完整支持。以下資訊來自外部官方資料。

- 資料名稱：
- 發布單位：
- 適用版本：
- URL：
- 查詢日期：
- 使用範圍：
```

### 驗證

外部來源必須是官方來源，且每項外部結論要對應其 URL 與版本。論壇、部落格或未標示版本的範例不能當主要依據。

### 如果外部查證不可用

直接說明：「目前執行環境無法存取外部官方資料，因此無法完成外部查證。」接著列出已確認內容與知識缺口。不得以模型記憶補出 Cmdlet、API、Regex、Ixia 參數或操作步驟。

## 5. AI Chat Web 配置

### 目的

讓 Chat Web 只使用實際提供的 iTest 26.2.0 知識檔案。

### 操作

在平台的知識檔案或檢索資料來源設定中，上傳並啟用：

```text
knowledge/chat-web-knowledge.md
```

套用 `../adapters/chat-web/instructions.md` 的流程。詳細設定見 `../adapters/chat-web/knowledge-configuration.md`。

### 預期結果

Chat Web 可檢索到 `Chunk ID`、`Source file`、`Document version` 與 `Location` 欄位。

### 驗證

用下列問題之一測試，並確認回答附有可追溯的內部來源：

- 如何新增 Tcl Test Step？
- PowerShell Test Step 有哪些前置條件？
- Analysis Rule 的 Regex 設定有哪些注意事項？

> 注意：Chat Web 不保證具有本機檔案存取、Python 或 Web Search。未實際提供的能力不能假設存在。

## 6. 驗證封裝內容

### 目的

確認文件沒有改變 skill 的來源鏈、固定版本或已知限制。

### 操作

```powershell
python scripts\validate_itest_help.py .
python scripts\run_regression_tests.py .
```

### 預期結果

第一個命令輸出 `Validation: PASS`。第二個命令輸出所有封裝內回歸案例通過。

### 驗證

這些檢查通過只代表 skill 契約、來源鏈與測試符合封裝規則。原始 collection 仍保留 1 個 `source_missing_target`，collection 狀態為 `partial_success`；不可把它寫成完整成功。

## 7. 常見狀態與處理

| 狀態 | 要做什麼 | 不可做什麼 |
| --- | --- | --- |
| `tool_unavailable` | 說明工具缺少，使用仍可讀的資料或無答案格式。 | 假裝已經檢索。 |
| `permission_denied` | 說明未授權，停止讀取該資料。 | 繞過權限。 |
| `no_results` | 用同義詞或版本條件重查；仍無結果再評估官方外部查證。 | 用模型記憶補答案。 |
| `integrity_error` | 停止引用受影響資料，僅使用仍可驗證的內容。 | 把部分結果當完整答案。 |
| `network_unavailable` | 說明無法完成官方外部查證。 | 以未標示的外部資訊替代。 |
| `version_conflict` | 分開列出版本與來源，要求版本資訊或說明不能混用。 | 混合不同版本的步驟。 |

## 8. 更新注意事項

`knowledge/rag/`、`knowledge/retrieval-index.jsonl` 和 `knowledge/chat-web-knowledge.md` 屬於驗證資料鏈。替換知識檔案時，必須同步更新來源 manifest、provenance map、validation report、版本矩陣與回歸測試，再依 `../FROZEN.md` 建立新版本並重新封裝。
