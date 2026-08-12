# 失敗與重試政策

## 能力補足先於內容重試

在宣告來源或工具失敗前，Agent 必須依序：

1. 觀察當前 runtime 已暴露與已授權的能力。
2. 調用適合的技能包 scripts、references、assets 與既有工具。
3. 在已確認隔離、受限且可回復的範圍內，自行補足必要相依並實測。
4. 嘗試可保留等效來源證據的替代能力。

不可因使用者沒有手動安裝工具而跳過上述路徑，也不可要求使用者自行執行技能內的同一腳本。不能列舉完整工具清單不構成能力不可用的證據。

原生 multimodal 能力未提供 machine-readable evidence 時必須標記 `unknown`。只有明確不可用、權限拒絕、媒體不支援，或已實際嘗試 LLM 視覺且保存失敗原因，才能進入 OCR fallback。Tesseract 未安裝只能說明 OCR backend 不可用，不能反向證明 LLM 視覺不可用。

## 一般模式

每個失敗單元最多三次，且不得使用完全相同設定盲目重跑。

### Attempt 1

- 原生解析。
- 已授權原生視覺與 hash-bound 工作單。
- 預設語言。
- 標準解析度。

### Attempt 2

- 需要逐字內容時執行標準 OCR。
- 只處理失敗頁面、圖片或區域。
- 合理提高解析度。
- Crop、Deskew、Contrast enhancement、Adaptive threshold。
- 適合的 OCR 語言及版面模式。

### Attempt 3

- 替代 parser 或 OCR backend。
- 必要時使用第二條 OCR、轉檔、影音或檔案理解路徑。
- 可使用 LLM 視覺理解補充非逐字語意，但不得冒充原文。

## Forensic 模式

最多五次，只供人工調查。額外保存：

- 原圖。
- Crop。
- 前處理圖。
- OCR 候選。
- bbox。
- overlay。
- 錯誤訊息。
- 各次參數。

## 三次後的狀態

### fatal_error

- 關鍵內容失敗。
- 沒有有效主體內容。
- 原始必要來源無法取得。
- 來源單元無法對帳。
- `normalized-document.md` 不可信。
- Chunk mapping 或固定輸出驗證失敗。
- 所有安全可行能力與等效路徑都不足，且沒有可可靠交付的主體內容。failure reason 必須記錄 `needs_capability` 或 `needs_source`。

### partial_success

- 有可用內容。
- 必要非關鍵內容仍失敗。
- 必要內容涵蓋率低於 95％。
- 使用衍生 snapshot。
- 使用者啟用 `--allow-partial-chunks`。
- 上述啟用必須同時具備 `--partial-authorization explicit_user_request`；Producer Agent 不得自行建立授權。
- 有可靠部分產物，但所有安全可行能力與等效路徑仍不足。`partial_reasons` 必須記錄 `needs_capability` 或 `needs_source`。

## 禁止行為

- 猜測原文以湊滿 95％。
- 將低品質 OCR 寫入正文。
- 靜默略過失敗單元。
- 用 LLM 摘要填補逐字缺口後宣稱完整。
- 一個低品質 region 否決整張圖片。
- 只依賴 Tesseract confidence 判定成功。
- OCR 有輸出就視為成功。
- 將低信心加上明顯括號、引號或標點結構垃圾的 OCR 候選標記為成功。
- 將使用者未配置本機工具視為使用者錯誤，或要求使用者自行安裝技能可調用的相依。
- 以同頁 QR／Barcode 成功掩蓋 PDF 掃描正文尚未完成。
- 在原生視覺工作單仍可完成時，以 OCR backend 缺失作為處理終點。
- 未經 capability evidence 與共用 admission 直接呼叫 OCR，或由 Adapter 自行偽造 unavailable。
- 將 `unknown` 改寫成 `unavailable`，或在 `available` 狀態下建立 Tesseract attempt。
