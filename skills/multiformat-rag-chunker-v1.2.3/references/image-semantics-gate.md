# 圖片語意 release gate

## 目的

把圖片的處理路徑、逐字文字與可檢索圖片語意分開。JSON 欄位存在、OCR 有輸出或分類器命中，都不是內容可進入 RAG 的證明；原生視覺摘要也必須有來源輸入與 asset SHA-256 的可重跑證據。

## 路由順序

1. 先由原生結構 parser、圖片 loader 與實際 QR／Barcode decoder 建立可重現 evidence。非空 payload 才是 decoder evidence。
2. 需要視覺語意時，讀取 Agent 提供的 capability evidence。`available` 必須先走 hash-bound 原生 LLM multimodal review；缺少 evidence 保持 `unknown`。
3. `screen_capture` 位於已有可靠原生正文的容器時，可保留既有非必要 `skipped` 對帳，但仍要記錄選路。獨立圖片或必要主要視覺不得用 skip 掩蓋內容缺口。
4. 只有 `unavailable`、`denied`、`unsupported`，或已實際嘗試 LLM 視覺且保存失敗原因的 `failed`，才能取得 OCR admission。
5. 取得 admission 的 `text_block` 或必要掃描內容才進入既有 OCR 品質流程；其餘圖片依既有非文字規則跳過或降級。

PDF 掃描頁另採頁面層路由。原生文字不足時，先渲染固定倍率頁面並計算 asset SHA-256。空白頁以非必要 `skipped` 對帳；非空白頁依工作單指定 `semantic_summary` 或 `dense_text`。前者建立 `llm_visual_summary`；後者必須經不同 Agent 逐單元驗證後建立多個 `llm_visual_text`。沒有審核時先查 capability evidence，不得直接進入 OCR。頁面內 QR／Barcode 仍獨立保存，但不能替代整頁主要內容。

此順序避免已確認的 QR 被 OCR 覆寫，也避免未審核介面截圖因 OCR 雜訊變成檢索內容。版面分類不用檔名、路徑、產品名稱或人工產品規則。

## 成功與跳過規則

| 情況 | Block 行為 | OCR | Chunk |
|---|---|---|---|
| decoder 已驗證 QR／Barcode | 必要、關鍵、`success`、`qr_decoder`；保存 machine payload 與 decoder evidence。 | 禁止。 | 必須保留。 |
| `screen_capture` 有 hash-bound 原生視覺審核 | 必要、`success`、非逐字 `llm_visual_summary`；保存來源 INPUT SHA-256、asset SHA-256、審核 manifest SHA-256 與 `native_visual_nonverbatim` 方法。 | 禁止。 | 必須以該來源 Block 的獨立 Chunk 保留。 |
| `screen_capture` 無機器載荷且無上述審核 | 非必要、非關鍵、`skipped`、非逐字 `derived_normalization`；`skip_reason` 為 `no_verified_machine_payload`。 | 禁止。 | 不得保留該圖片內容。 |
| PDF `full_page_scan` 有 hash-bound 原生視覺審核 | 必要、`success`、主要內容、非逐字 `llm_visual_summary`；來源與頁面 asset SHA-256 必須相符。 | 禁止。 | 必須以獨立原子 Chunk 保留。 |
| PDF dense-text 有 extraction 與獨立 validation | 每個單元建立必要、`success`、非逐字 `llm_visual_text`；來源、頁面與兩份 sidecar Hash 必須相符。 | 禁止。 | 依單元 Block 邏輯分組，不得跨 Block 拆分。 |
| PDF dense-text 只有摘要或自我驗證 | 拒絕 admission，不得建立成功正文。 | 不以單一 OCR backend 缺失結案。 | 不得建立完整 Chunk。 |
| PDF 空白頁 | 非必要、非關鍵、`skipped`；`skip_reason` 為 `blank_page`，保存可重算空白指標。 | 禁止。 | 不得建立內容 Chunk。 |
| 原生 LLM multimodal 可用但 review 尚未完成 | 必要主要視覺維持失敗或待補強，保存 `native_visual_review_required` 與 routing evidence。 | 禁止。 | 不得建立未驗證視覺 Chunk。 |
| `text_block` 且 fallback evidence 合法 | 依既有 OCR result 成功或降級。 | admission 後允許。 | 只有通過品質閘門的成功文字可保留。 |
| 其他非文字圖片 | 依既有非文字圖片規則跳過或降級。 | 不因尺寸自動執行。 | 不得以圖片猜測補入。 |

## Release 前檢查

每次 release candidate 必須分開報告圖片、OCR、Chunk、原始來源、RAG artifact 與 package 的證據。至少需要：

- 未審核 UI golden 的 asset SHA-256、分類、空 machine payload、無 OCR 與無圖片 Chunk assertion。
- 已審核 UI 的來源 INPUT SHA-256、asset SHA-256、非逐字摘要、審核方法、獨立 Chunk assertion 與全 corpus retrieval smoke。
- PDF 掃描頁的原始頁數、非空白掃描頁、空白頁、頁面 asset SHA-256、原生視覺摘要與主要 Block mapping 必須由 `validate_against_source.py` 重新計算。
- Dense-text 頁面的 unit ID、順序、missing、unexpected、mismatch、uncertainty、extraction Hash 與 validation Hash 必須由不同 Agent 核對。RAG 另以 `validate_dense_retrieval.py` 驗證 anchor、Recall 與頁碼。
- 可解碼 QR 與 Barcode control 的 payload、symbology、來源 asset SHA-256、decoder evidence、無 OCR 與 Chunk assertion。
- OCR golden 的語意接受或拒絕 assertion，不得只檢查非空文字或信心分數。
- 原始來源 SHA-256、確切 RAG artifact SHA-256、確切 package SHA-256，以及對應的 validator、hash、圖片、retrieval 與 corpus 結果。

工作區的 image semantics harness 用於上述實檔檢查；它不會成為每份使用者輸出的固定檔案。原始 RAG 中看到的 markup token 必須由原始脈絡逐筆分類；不得沿用未能重現的歷史計數。
