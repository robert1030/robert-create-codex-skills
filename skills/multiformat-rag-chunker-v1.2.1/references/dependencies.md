# Runtime 能力、Agent 補足與降級

## 原則

使用者只提供來源檔與任務要求。Agent 必須先觀察當前 runtime 已暴露且已授權的能力，再主動選擇原生檔案理解、視覺、程式、轉檔、OCR、影音、已安裝工具、連接器或技能包資源。

技能包內的 Python 套件、外部程式與 scripts 都是 Agent 可優先調用的資源，不是使用者手動安裝或執行的前置。工具名稱不是成功條件，實際來源證據與輸出驗證才是。

## 能力階梯

1. 使用 runtime 明確提供的原生檔案理解、視覺、程式或連接器能力。
2. 使用技能包的 `scripts/`、`references/`、`assets/` 與已存在的工具。
3. 若 Agent 已確認安裝範圍隔離、受限且可回復，自行補足必要相依並實測。
4. 改用可保留同等來源語意、結構、頁面或時間範圍證據的等效能力。
5. 僅在以上路徑均不足時，依既有狀態欄位記錄 `needs_capability` 或 `needs_source`。

不能列舉完整工具清單，不是能力不可用的證據。已由介面提供、安全測試成功或前一步成功完成，任一項都是能力可用證據。

## 可選工具資源

| 資源 | 適用能力 | Agent 行為 |
|---|---|---|
| PyMuPDF、python-docx、lxml、Beautiful Soup、Pillow、OpenCV | PDF、Office、XML、HTML、圖片、QR 與 Barcode decoder | 可用時優先調用，未可用時改走原生理解或等效工具。 |
| Tesseract、pytesseract | 逐字 OCR 與候選品質檢查 | 可用時可調用，不可用時嘗試視覺或其他 OCR；不得把未驗證視覺摘要當逐字內容。 |
| LibreOffice | DOC 轉 DOCX、特定 Office 轉檔 | 可用時保留 derivation chain；不可用時嘗試 runtime 的文件理解或要求可擷取副本。 |
| FFmpeg、ffprobe、faster-whisper | MP4 streams、字幕、音訊、影格與轉錄 | 可用時保留時間範圍證據；不可用時嘗試 runtime 的影音能力或保留能力不足原因。 |
| `scripts/bootstrap.py` | Agent 補足可用相依 | 只在 Agent 已確認當前安裝範圍安全時執行，禁止把它交給使用者手動執行。 |

## 安裝與持久環境

Agent 必須依實際權限、隔離性、持久性與可回復性判斷是否安裝，而不是依產品名稱判斷。

- 隔離 sandbox 或已確認受限且可回復的範圍：自行安裝缺少相依、實測、記錄結果。
- 持久或共享環境：優先既有工具、暫存路徑、工作區隔離環境或等效能力；不得修改全域設定、移除或升級無關相依。
- 安裝遭權限、網路、政策或安全限制阻擋：繼續嘗試等效能力，不得要求使用者自行安裝同一工具。

## 結果映射

| 可觀察結果 | 既有輸出狀態 | 既有原因欄位 |
|---|---|---|
| 可驗證範圍完整處理 | `success` | 不需新增欄位。 |
| 有可靠部分產物，但能力或來源範圍不足 | `partial_success` | `partial_reasons` 記錄 `needs_capability` 或 `needs_source`。 |
| 沒有可可靠交付的主體內容 | `fatal_error` | failure reason 記錄 `needs_capability` 或 `needs_source`。 |

每次非 `success` 都必須保留已完成範圍、未完成範圍、實際使用能力、已嘗試路徑與下一個可行動作。
