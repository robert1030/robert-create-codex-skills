# iTest Help Skill

這個 skill 以已驗證的 iTest Help 26.2.0 知識庫回答技術問題。它先找本機證據，再給答案；沒有可靠證據時，不以模型記憶補造語法或操作。

## 快速開始

在 AI Agent 環境中，從 skill 根目錄執行：

```powershell
python scripts\search_itest_help.py "Tcl Test Step" --limit 5
```

檢查結果的 Chunk ID、來源檔案與版本後，再回答問題並附上 `【知識庫來源】`。完整步驟見 `docs/runbook.md`。

AI Chat Web 必須先上傳並啟用 `knowledge/chat-web-knowledge.md`；它不能假設可存取本機資料夾或執行 Python。配置說明見 `adapters/chat-web/knowledge-configuration.md`。

## 文件索引

| 文件 | 用途 |
| --- | --- |
| `docs/SPEC.md` | 產品範圍、來源與可驗證契約。 |
| `docs/runbook.md` | Windows PowerShell 操作、查詢、驗證與故障處理。 |
| `docs/runbook.html` | 與 runbook.md 同步的瀏覽器閱讀版。 |
| `knowledge/validation-report.md` | 知識庫身份與已知限制。 |

## 適用範圍

- 產品：iTest Help。
- 已驗證知識庫版本：26.2.0。
- RAG 版本：1.2.1。
- 主題：iTest 功能、專案、Test Case、Tcl、Python 與 PowerShell Test Step、Settings、Analysis Rule、Regex、Ixia、Session、參數、變數、日誌、結果與錯誤排除。

`PS Test Step` 預設代表 `PowerShell Test Step`。其他 iTest 版本不可自動套用此知識庫的語法或 UI 步驟。

## 回答與來源規則

1. 先檢索本機已驗證知識庫。
2. 只使用能直接支持結論的 Chunk。
3. 技術性答案列出 `【知識庫來源】`，包含檔案、文件版本、章節或位置與 Chunk ID。
4. 本機結果不足、版本不符、內容衝突或使用者要求較新資訊時，才能查官方外部資料，並加入 `【外部查證聲明】`。
5. 沒有本機或官方外部證據時，明確說明知識缺口。

詳細規則見 `SKILL.md` 與 `core/`。

## 驗證

```powershell
python scripts\validate_itest_help.py .
python scripts\run_regression_tests.py .
```

驗證成功代表 skill 契約、來源鏈與測試案例符合本封裝規則。原始 collection 仍有 1 個已揭露的 `source_missing_target`，因此狀態是 `partial_success`，不能宣稱為完整成功。
