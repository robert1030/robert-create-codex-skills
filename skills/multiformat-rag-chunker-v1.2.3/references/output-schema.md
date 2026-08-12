# 固定輸出 Schema

## 每個來源的固定檔案

```text
source-output/
├── normalized-document.md
├── document-ir.jsonl
├── chunks/
│   └── *.md
├── chunks.jsonl
├── failed-items.jsonl
├── processing-report.json
└── manifest.json
```

## chunks.jsonl

每筆至少包含：

- `chunk_id`
- `source_id`
- `title`
- `heading_path`：所有非 overlap `source_block_ids` 對應 Block Heading path 的最長共同前綴。
- `section_titles`：Chunk 內實際包含的所有 Heading 標題。
- `source_block_ids`
- `overlap_block_ids`
- `overlap_text`
- `overlap_token_count`
- `token_estimate`
- `locators`
- `source_hash`
- `normalized_document_hash`
- `content_status`
- `text`
- `markdown_body`
- `content_sha256`
- `markdown_file`

## processing-report.json

至少包含：

- Skill 版本及來源資訊。
- 實際 Adapter。
- Block、Chunk、失敗數量。
- OCR、QR 及 fallback 統計。
- Chunk 前完整度指標。
- Chunk 後 mapping 指標。
- 最終狀態。
- 警告及錯誤。
- 實際參數。
- 輸出驗證摘要。
- `source_metadata.capability_routing`：保存 capability schema、原生 LLM multimodal evidence、逐 asset routing event、selected lane、LLM 視覺嘗試與 OCR admission。這是既有報告內欄位，不新增固定輸出檔。

使用 `--allow-partial-chunks` 時，`parameters.partial_authorization` 必須精確為 `explicit_user_request`。缺少授權證據時，Producer 與 Validator 都必須拒絕 partial Chunk。

`chunk_pre_validation.partial_reasons` 與 `fatal_reasons` 是既有狀態原因陣列。當實際觀察到的失敗是所有安全可行路徑後仍缺少 runtime 能力或來源時，分別使用 `needs_capability` 或 `needs_source`；不得另建 `complete`、`needs_capability` 或 `needs_source` 的 top-level status。

## failed-items.jsonl

每筆保留既有 `failure_reason`、位置、attempt history 與 `details`。若 `fatal_error` 沒有可靠主體內容，`failure_reason` 使用 `needs_capability` 或 `needs_source`，而 `details.observed_failure_reason` 保留實際觀察到的工具、權限或來源錯誤。`details` 必須能指出已完成範圍、未完成單元、已嘗試路徑及下一個可行動作；不得編造未揭露的 runtime 版本或能力清單。

## manifest.json

至少包含：

- 原始來源 Provenance。
- 原始 SHA-256。
- 衍生檔案清單。
- Skill 版本。
- Parser 及 OCR 套件版本。
- 實際參數。
- 輸出檔案 SHA-256。
- 最終退出碼。
- `normalized-document.md` SHA-256。

## 圖片 Block metadata

圖片 Block 延用既有 `metadata` 容器，不新增 top-level schema 欄位。所有圖片至少保存 `asset_id`、`visual_class`、width、height、`asset_sha256` 與 `machine_payloads`。

- decoder 成功時，`machine_payloads` 的每筆資料保存 kind、symbology、payload 與 `source_asset_sha256`；`decoder_evidence` 記錄實際 backend。
- `screen_capture` 無 decoder payload 時，`machine_payloads` 為空，並保存 `skip_reason: no_verified_machine_payload` 與通用 `layout_evidence`。
- OCR 路由保存既有 `ocr_confidence`、`ocr_quality` 與 `ocr_semantic_status`。只有 `ocr_semantic_status: accepted` 的 OCR 文字可搭配成功 Block。
- LLM 視覺或 OCR 路由另保存 `capability_route`，其 event ID、asset SHA-256、能力狀態、selected lane 與 admission 必須和 `processing-report.json` 精確一致。
- PDF 全頁視覺審核保存 `reference`、`content_role: primary` 與 `visual_summary_evidence`。其中來源 INPUT SHA-256、頁面 `asset_sha256`、review manifest SHA-256 與 `native_visual_nonverbatim` 方法必須完整。
- PDF dense-text Block 保存 `reference`、unit ID、unit type、一基制閱讀順序、結構欄位與 `visual_text_evidence`。Evidence 必須包含 extraction 與獨立 validation manifest SHA-256，且 validation status 必須為 `passed`。
- 空白 PDF 頁保存 `skip_reason: blank_page`、`content_role: blank` 與可重算 `blank_metrics`，且必須是非必要 `skipped`。

## 不再強制的使用者輸出

下列開發檔案不得成為每次正式輸出的固定內容：

- `invocation.json`
- `validation-log.txt`
- `unit-test-report.json`
- `process-exit-code.txt`
- `transform-log.jsonl`
- `retrieval-validation.json`
- `visual-review-request.json`
- `REVIEW.json`
- `VALIDATION.json`
- `GOLDEN.json`

`visual-review-request.json` 是 Agent 的暫存審核工作單，不是每份正式來源輸出的固定第八類檔案。

`REVIEW.json`、`VALIDATION.json` 與 `GOLDEN.json` 是 dense-text 生產及驗收的外部 evidence sidecar，也不是固定第八類輸出。正式報告必須保存其 SHA-256，固定七類來源輸出不得改名或增加。

## Forensic 模式附加輸出

啟用 `--forensic` 時，來源目錄額外包含：

```text
forensic/
├── source-assets/
├── rendered-pages/
├── crops/
├── preprocessed/
├── ocr-candidates/
├── overlays/
└── debug-report.json
```

只有實際執行的 backend 才會產生中間檔。空目錄不得被解讀為該 backend 已執行。

## v1.1.2-dev-r2 一致性要求

`source_block_ids` 不只是集合，亦是有序序列。將所有 Chunk 的非 overlap `source_block_ids` 依 Chunk 順序展平後，必須與 `document-ir.jsonl` 中合格 Block 的 `metadata.source_order` 完全一致。

Chunk Markdown frontmatter 必須與 `chunks.jsonl` 的下列欄位逐項一致：

- `title`
- `heading_path`
- `source_block_ids`
- `content_sha256`

`processing-report.json` 的 Chunk 後指標必須包含閱讀順序、source order metadata、圖文 Heading 關聯及文件標題語意的違規數量。

對 DOCX、DOC、PDF，`processing-report.json` 的 `source_metadata` 必須明確包含：

- `layout_semantics_status`
- `document_title_semantics_status`
- `document_title`
- `title_source`

只有值為 `reliable` 的語意能力可被 Validator 視為已建立。缺少能力旗標不得被推定為通過。

## v1.1.2-dev-r3 外部驗證要求

對 DOCX、DOC、PDF，外部 Validator 必須拒絕下列輸出：

- `layout_semantics_status` 或 `document_title_semantics_status` 缺少，或來源以 `success` 搭配非 `reliable` 值。
- 任何合格 Block 缺少唯一整數 `source_order`，包括全部 metadata 被移除。
- 成功圖片 Block 缺少 `associated_heading_block_id`、`associated_heading_path` 或非空 `association_method`，或關聯內容與最近前置成功 Heading 不一致。
- Chunk 後報告缺少 `reading_order_violation_count`、`source_order_metadata_violation_count`、`visual_heading_relation_violation_count` 或 `document_title_mismatch_count`。

即使竄改後重新計算 `manifest.json` 內的檔案 Hash，上述語意缺陷仍必須由內容驗證拒絕。
