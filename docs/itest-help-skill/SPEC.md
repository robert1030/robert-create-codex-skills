# iTest Help Skill 規格

## 目的

本文件定義 `itest-help` skill 必須提供的範圍、證據規則與可驗證條件。操作指令與故障處理見 `runbook.md`。

## 已驗證身份

下列是本封裝的目前版本事實，不是其他版本的通用規則。

| 項目 | 值 |
| --- | --- |
| Skill 名稱 | `itest-help` |
| Skill 版本 | `1.0.0` |
| 產品 | iTest Help |
| 知識庫文件版本 | `26.2.0` |
| RAG 版本 | `1.2.1` |
| RAG archive | `itest-help_26.2.0-rag-v1.2.1.zip` |
| RAG SHA-256 | `309BA7AACF41000C242FD0FBD1AF0B8B548F1EAB14A055284A3615DDE82BBC70` |
| Collection ID | `itest-help_26.2.0.zip-79edef31c6908df0` |

完整來源身份與驗證結果見 `../knowledge/source-manifest.json` 和 `../knowledge/validation-report.md`。

## 功能需求

### 範圍

Skill 必須以 iTest Help 26.2.0 的已驗證本機知識庫處理 iTest 技術問題，包括專案、Test Case、Tcl、Python 與 PowerShell Test Step、Settings、Analysis Rule、Regex、Ixia、Session、參數、變數、日誌、結果、版本差異與錯誤排除。

`PS Test Step` 預設解讀為 `PowerShell Test Step`，但知識庫若有不同定義，必須以知識庫為準。

### 檢索與證據

1. Agent 有檔案與 Python 能力時，必須先搜尋 `knowledge/retrieval-index.jsonl`。
2. 每個採用的結果必須可追溯到 Chunk ID、來源檔案、文件版本、章節或位置、來源雜湊與內容雜湊。
3. 相似關鍵字不足以支持結論；只有直接支持答案的內容可以引用。
4. `knowledge/rag/` 是驗證後的唯讀資料。不得加入未驗證內容或修改其來源記錄。

### 回答與引用

技術性答案必須使用 `【知識庫來源】`，至少列出來源檔案、文件版本、章節或位置與 Chunk ID。沒有頁碼時，必須標示可驗證的原始位置，不得推測頁碼。

使用外部資料時，答案必須額外使用 `【外部查證聲明】`，列出資料名稱、發布單位、適用版本、URL、查詢日期與使用範圍。

### 版本與不確定性

- 不得混用不同 iTest 版本的語法或 UI 步驟。
- 版本未提供且可能影響正確性時，必須說明需要確認版本。
- 本機結果不足、版本不符、內容衝突或需要較新資訊時，才可查官方外部資料。
- 外部工具不可用時，必須說明無法完成外部查證。
- 本機與外部資料都不足時，必須說明已確認內容、知識缺口與外部查證狀態；不得猜測。

## 執行環境需求

| 環境 | 必要行為 | 不可假設的能力 |
| --- | --- | --- |
| AI Agent | 可用時先執行本機檢索與來源檢查。 | 不可假設檔案、Python、檢索、Web Search 或引用工具必然可用。 |
| AI Chat Web | 只使用實際上傳並啟用的 `knowledge/chat-web-knowledge.md`。 | 不可假設本機路徑、ZIP 解壓、Python 或 Web Search。 |

## 資料完整性與已知限制

原始 source ZIP 的 7,004 個 member 路徑與 member SHA-256 已和 collection manifest 全數對齊。RAG collection gate 已通過；但原始 Help 包有 1 個沒有唯一可驗證目標的 `source_missing_target`。因此 collection 狀態為 `partial_success`，不能把此限制隱藏、補造或宣稱為完整成功。

## 驗收條件

下列條件都成立時，才可宣稱本 skill 的文件與行為契約一致。

1. `SKILL.md`、`manifest.json`、來源 manifest 與版本矩陣都標示 iTest Help 26.2.0。
2. `python scripts\validate_itest_help.py .` 回傳 `Validation: PASS`。
3. `python scripts\run_regression_tests.py .` 通過全部封裝內回歸案例。
4. 回答測試可驗證每個技術結論都有正確的內部來源，或已標示官方外部資料。
5. 本文件、`runbook.md` 與 `../README.md` 不得與凍結契約衝突。

## 變更規則

變更知識庫、產品或文件版本、來源優先順序、引用格式、外部查證規則或不確定性降級流程時，必須建立新的 skill 版本、重跑驗證，並重新封裝。詳見 `../FROZEN.md`。
