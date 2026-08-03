# 圖片語意 release gate

## 目的

把圖片的處理路徑、逐字文字與可檢索圖片語意分開。JSON 欄位存在、OCR 有輸出或分類器命中，都不是內容可進入 RAG 的證明；原生視覺摘要也必須有來源輸入與 asset SHA-256 的可重跑證據。

## 路由順序

1. 先執行實際 QR decoder。非空 payload 才是 QR evidence。
2. 若不是 QR，檢查通用、可重現的介面版面結構。命中時先分類為 `screen_capture`，不將其中的文字當成 OCR。
3. 未命中前兩者時，使用實際 Barcode decoder。非空 payload 才是 Barcode evidence。
4. 具有低邊緣密度、可重現文字墨點比例的 `text_block`，才進入既有 OCR 品質流程。
5. 其餘圖片依既有非文字圖片規則跳過或降級。

此順序避免已確認的 QR 被 OCR 覆寫，也避免未審核介面截圖因 OCR 雜訊變成檢索內容。版面分類不用檔名、路徑、產品名稱或人工產品規則。

## 成功與跳過規則

| 情況 | Block 行為 | OCR | Chunk |
|---|---|---|---|
| decoder 已驗證 QR／Barcode | 必要、關鍵、`success`、`qr_decoder`；保存 machine payload 與 decoder evidence。 | 禁止。 | 必須保留。 |
| `screen_capture` 有 hash-bound 原生視覺審核 | 必要、`success`、非逐字 `llm_visual_summary`；保存來源 INPUT SHA-256、asset SHA-256、審核 manifest SHA-256 與 `native_visual_nonverbatim` 方法。 | 禁止。 | 必須以該來源 Block 的獨立 Chunk 保留。 |
| `screen_capture` 無機器載荷且無上述審核 | 非必要、非關鍵、`skipped`、非逐字 `derived_normalization`；`skip_reason` 為 `no_verified_machine_payload`。 | 禁止。 | 不得保留該圖片內容。 |
| `text_block` | 依既有 OCR result 成功或降級。 | 允許。 | 只有通過品質閘門的成功文字可保留。 |
| 其他非文字圖片 | 依既有非文字圖片規則跳過或降級。 | 不因尺寸自動執行。 | 不得以圖片猜測補入。 |

## Release 前檢查

每次 release candidate 必須分開報告圖片、OCR、Chunk、原始來源、RAG artifact 與 package 的證據。至少需要：

- 未審核 UI golden 的 asset SHA-256、分類、空 machine payload、無 OCR 與無圖片 Chunk assertion。
- 已審核 UI 的來源 INPUT SHA-256、asset SHA-256、非逐字摘要、審核方法、獨立 Chunk assertion 與全 corpus retrieval smoke。
- 可解碼 QR 與 Barcode control 的 payload、symbology、來源 asset SHA-256、decoder evidence、無 OCR 與 Chunk assertion。
- OCR golden 的語意接受或拒絕 assertion，不得只檢查非空文字或信心分數。
- 原始來源 SHA-256、確切 RAG artifact SHA-256、確切 package SHA-256，以及對應的 validator、hash、圖片、retrieval 與 corpus 結果。

工作區的 image semantics harness 用於上述實檔檢查；它不會成為每份使用者輸出的固定檔案。原始 RAG 中看到的 markup token 必須由原始脈絡逐筆分類；不得沿用未能重現的歷史計數。
