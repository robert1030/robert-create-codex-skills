# 品質閘門

## Chunk 前指標

```json
{
  "source_unit_total": 10,
  "source_unit_accounted": 10,
  "source_unit_accounting_ratio": 1.0,
  "required_unit_total": 8,
  "required_unit_verified": 8,
  "required_content_coverage_ratio": 1.0,
  "critical_unit_total": 3,
  "critical_unit_verified": 3,
  "critical_content_coverage_ratio": 1.0,
  "text": {},
  "table": {},
  "visual": {},
  "structural": {},
  "content_completeness_status": "success"
}
```

成功門檻：

```text
source_unit_accounting_ratio = 1.0
required_content_coverage_ratio >= 0.95
critical_content_coverage_ratio = 1.0
normalized_document_valid = true
undisclosed_required_failures = []
source_semantic_audit.status = passed 或 not_applicable
primary_content.has_effective_main_content = true
```

此閘門只判定可觀察的來源與產物，不得把缺少某個指定工具直接視為來源已完整處理。若所有已授權、已驗證及安全可補足的路徑都不足，沿用既有結果：有可靠主體內容時為 `partial_success`，並在 `partial_reasons` 記錄 `needs_capability` 或 `needs_source`；沒有可靠主體內容時為 `fatal_error`，並在 `failed-items.jsonl` 的既有 `failure_reason` 記錄同一代碼。

沒有符合資格的單元時：

```json
{
  "eligible_count": 0,
  "verified_count": 0,
  "coverage_ratio": null,
  "metric_status": "not_applicable"
}
```

## 關鍵內容

關鍵內容包括：

- 文件標題及章節標題。
- 日期、版本及編號。
- 表格表頭。
- 命令、程式碼及安全參數。
- 警告及禁止事項。
- QR Code 或 Barcode payload。
- 使用者指定的必要內容。

整體涵蓋率即使超過 95％，關鍵內容失敗仍不得通過。

## 主體內容

主要正文、表格、清單、程式碼、轉錄、通過品質閘門的 OCR、hash-bound `llm_visual_summary`，以及通過獨立逐項驗證的 `llm_visual_text` 可構成主體內容。QR／Barcode 是機器載荷；若同一來源仍有必要主要單元為 `failed` 或 `low_quality`，它們不得單獨使 `has_effective_main_content` 成立。只有來源確實只含機器載荷，且沒有未解決主要單元時，機器載荷才可成為有效主體。

沒有有效主體內容時固定為 `fatal_error`。`--allow-partial-chunks` 不得覆寫此結果。

## 圖片語意路由

獨立圖片必須先完成 decoder 與通用版面路由，再決定是否 OCR。

- decoder 確認的 QR 或 Barcode：`machine_payloads` 必須逐筆有 kind、symbology、payload、來源 asset SHA-256 與 decoder evidence。payload 是關鍵內容，decoder 成功時不得再 OCR。
- `screen_capture`：只有可重現的通用介面版面 evidence、且沒有已驗證機器載荷時才可使用。它必須是非必要、非關鍵、`skipped`、非逐字的 `derived_normalization` Block，`skip_reason` 為 `no_verified_machine_payload`；不得 OCR 或進入 Chunk。
- 其他圖片：沿用 OCR 品質閘門。只有 OCR 結果通過既有品質檢查時可成為成功 Block；被拒絕的結果必須保留既有 attempts 與品質資訊，不能以 schema 合法冒充內容成功。
- PDF 掃描頁：非空白頁必須由原始文字、通過品質閘門的全頁 OCR，或來源與頁面 asset Hash 精確相符的原生視覺摘要覆蓋。空白頁必須是非必要 `skipped`，不得列成 OCR failure。
- PDF dense-text 頁：`dense_text.eligible_page_count` 非零時，`dense_text.coverage_ratio` 必須為 1.0、`unresolved_references` 必須為空，且所有單元都具獨立 validation evidence。

圖片分類只決定處理路徑，不是圖片文字已被理解的證明。完整規則見 `image-semantics-gate.md`。

## 原始來源語意稽核

所有格式都必須以適合其來源的可回溯範圍證據完成對帳。HTML、HTM 與 XML 另外由獨立原始解析器檢查本版已知的易遺失語意：Cheat Sheet 可見屬性、清單的非標準直接子內容及 Table Caption。這些是回歸案例，不是格式範圍限制。

Collection gate 另有：

```text
source_semantic_coverage_ratio = 1.0
source_semantic_critical_coverage_ratio = 1.0
```

這兩項由原始來源重算，不能以 Adapter 自報、Block mapping 或輸出 Schema 通過代替。缺少關鍵 XML 程序語意為 `fatal_error`；非關鍵 Caption 或非標準清單內容遺失至少為 `partial_success`。

## Chunk 後指標

```json
{
  "normalized_block_total": 8,
  "chunk_mapped_block_total": 8,
  "chunk_block_mapping_ratio": 1.0,
  "omitted_verified_blocks": [],
  "unexpected_chunk_content_count": 0,
  "atomic_unit_violation_count": 0,
  "orphan_heading_context_count": 0,
  "chunk_validation_status": "passed"
}
```

成功門檻：

```text
chunk_block_mapping_ratio = 1.0
omitted_verified_blocks = 0
unexpected_chunk_content_count = 0
atomic_unit_violation_count = 0
orphan_heading_context_count = 0
```

`orphan_heading_context_count` 同時涵蓋缺少 Heading context，以及 Chunk `heading_path` 不等於所有非 overlap 來源 Block 最長共同 Heading 前綴的情況。

## 內容品質不是 Schema 品質

JSON 可解析、欄位存在及程式正常結束，只能證明結構可讀。內容完整度必須由來源對帳、關鍵內容檢查、Block mapping、文字品質及 Golden Assertions 共同證明。

## v1.1.2-dev-r2 語意順序硬閘門

Chunk 後報告新增四項指標：

```json
{
  "reading_order_violation_count": 0,
  "source_order_metadata_violation_count": 0,
  "visual_heading_relation_violation_count": 0,
  "document_title_mismatch_count": 0
}
```

成功門檻全部為 0：

- `reading_order_violation_count`：Chunk 展平後的 Block ID 與來源順序不一致的數量。
- `source_order_metadata_violation_count`：缺少、重複或非遞增 `source_order` 的數量。
- `visual_heading_relation_violation_count`：具可靠版面語意的 DOCX、DOC、PDF 圖片未關聯到最近前置成功 Heading，或 `heading_path` 不一致的數量。
- `document_title_mismatch_count`：具可靠標題語意的 DOCX、DOC、PDF 文件根標題缺少、重複、文字錯誤、level 錯誤或 Chunk title 不一致的數量。

Validator 必須由 `document-ir.jsonl` 與 `chunks.jsonl` 獨立重算，不得只相信 `processing-report.json`。若來源因必要內容失敗而沒有產生 Chunk，閱讀順序 mapping 為尚未執行，不得將空 Chunk 誤判成順序錯誤；其餘可由 IR 獨立驗證的語意仍須檢查。

## v1.1.2-dev-r3 成功資格與欄位完整性

DOCX、DOC、PDF 的 Chunk 前成功資格另包含：

```text
layout_semantics_status = reliable
document_title_semantics_status = reliable
```

不可靠或只能推定時，內容即使完整對帳也只能是 `partial_success`。預設不得產生正式 Chunk，除非使用者明確啟用 `--allow-partial-chunks`。

四項 Chunk 後語意指標必須實際存在，不能用 `.get(..., 0)` 類預設值把缺欄位當成零違規。對可靠版面來源，`source_order` 必須覆蓋每個合格 Block；圖片的 Heading ID、Heading path 及關聯方法必須一起核對。

## v1.2.2-dev-r1 PDF 來源對照硬閘門

PDF 完整交付除既有 Validator 外，必須執行 `validate_against_source.py INPUT.pdf OUTPUT_SOURCE_DIR --require-complete`。它由原始 PDF 重算來源 Hash、頁數、原生文字不足頁、空白頁、必要掃描頁、主要 Block 與 Chunk mapping。兩個 Validator 任一退出碼非 0，都不得宣稱完整完成。

## v1.2.2-dev-r2 Dense-text retrieval 硬閘門

Dense-text 完整交付另須執行 `validate_dense_retrieval.py OUTPUT_SOURCE_DIR --golden GOLDEN.json`。Golden 必須綁定來源與 extraction manifest SHA-256。成功門檻固定為：

```text
critical_anchor_preservation_ratio = 1.0
headword_recall_at_1 = 1.0
definition_recall_at_3 = 1.0
example_recall_at_3 = 1.0
citation_page_accuracy = 1.0
```

沒有對應 query 類型時，該項為 `null` 與 `not_applicable` 語意，不得偽造 1.0。真實 PDF 缺少作者 ground truth 時，雙 Agent 全量核對與 golden 只能證明本次已檢查範圍，不得宣稱零錯誤。

## v1.2.3-dev-r1 capability routing 硬閘門

Validator 必須由 `processing-report.json` 的 routing event 與 `document-ir.jsonl` 的視覺 Block 交叉重算。下列任一情況直接拒絕：原生 multimodal 為 `available` 卻出現 OCR admission 或 Tesseract attempt、OCR Block 缺少 admission、`failed` 缺少先前 LLM 視覺嘗試、LLM 視覺 Block 未綁定 native lane、asset Hash 不合法、Block 與 routing event 不一致。

缺少 capability evidence 必須維持 `unknown`，不得由 OCR backend 是否存在推定為 `unavailable`。純原生結構來源沒有視覺補強需求時，routing event 可為空，不影響既有成功資格。
