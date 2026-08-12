# Document IR

## Block Schema

```json
{
  "block_id": "source-001-block-007",
  "type": "paragraph",
  "text": "A complete paragraph.",
  "location": {
    "page": 2,
    "bbox": [30, 100, 540, 180],
    "dom_path": null,
    "xml_path": null,
    "time_start": null,
    "time_end": null,
    "asset_id": null
  },
  "heading_path": [
    "Chapter 1",
    "Overview"
  ],
  "content_origin": "native_text",
  "required": true,
  "critical": false,
  "status": "success",
  "verbatim": true,
  "raw_text": "A complete paragraph.",
  "transformation_summary": [
    "unicode_nfc"
  ],
  "metadata": {},
  "attempts": []
}
```

## 共用 Block type

- `heading`
- `paragraph`
- `list`
- `table`
- `image`
- `code`
- `transcript`
- `placeholder`

## Content origin

- `native_text`
- `native_table`
- `ocr`
- `qr_decoder`
- `transcript`
- `llm_visual_summary`
- `llm_visual_text`
- `derived_normalization`
- `placeholder`

`llm_visual_summary` 必須搭配：

```json
{
  "verbatim": false
}
```

PDF 掃描頁的 `llm_visual_summary` 另須在既有 `metadata` 保存 `content_role: primary`、頁面 `reference`、`asset_sha256`、空陣列 `machine_payloads` 與 `visual_summary_evidence`。QR／Barcode 使用 `content_role: machine_payload`；空白頁使用 `content_role: blank`，不得以機器載荷或空白頁滿足未完成正文的主體內容閘門。

Dense-text 頁面的 `llm_visual_text` 使用既有 `paragraph` 或 `heading` Block，且 `verbatim` 固定為 `false`。每個 Block 的 `metadata` 必須保存 `reference`、`asset_sha256`、`visual_text_unit_id`、`visual_text_unit_type`、`visual_text_reading_order`、`visual_text_fields`、`dense_text_required: true` 與 `visual_text_evidence`。Evidence 必須同時綁定來源、頁面、extraction manifest 與獨立 validation manifest SHA-256。

合成章節標題不是原始逐字內容，必須使用：

```json
{
  "content_origin": "derived_normalization",
  "verbatim": false,
  "metadata": {
    "derived": true,
    "derivation_type": "synthetic_section_heading"
  }
}
```

## Status

- `success`：內容通過品質檢查。
- `skipped`：已對帳，但依政策不需要進入正文。
- `low_quality`：有候選內容，但品質未達門檻。
- `failed`：無法取得可信內容。

## Table metadata

```json
{
  "caption": "表格判讀規則",
  "header": ["欄位一", "欄位二"],
  "rows": [["A", "B"]],
  "logical_column_count": 2,
  "data_row_count": 1,
  "heading_context": ["文件標題", "章節"]
}
```

Caption、Header、Rows 與 Heading context 共同構成 Table Block。Caption 不得只留在原始 HTML 而未進入 IR 或 normalized Markdown。

## Attempt record

只有真正呼叫 parser、Decoder 或 OCR backend 才增加 attempt count：

```json
{
  "attempt": 2,
  "backend": "tesseract",
  "strategy": "crop_deskew_adaptive_threshold",
  "status": "failed",
  "parameters": {},
  "quality": {},
  "error": "quality_gate_failed"
}
```

## 閱讀順序與版面語意 metadata

當 Adapter 能可靠建立版面語意時，每個 DOCX、DOC、PDF Block 必須有唯一整數 `metadata.source_order`。正式 Chunk 的 `source_block_ids` 依此順序展平後，必須與所有合格 Block 的來源順序完全一致。

文件根標題範例：

```json
{
  "type": "heading",
  "text": "真正的文件標題",
  "heading_path": ["真正的文件標題"],
  "metadata": {
    "source_order": 1,
    "level": 1,
    "semantic_role": "document_title",
    "source_style_id": "Title",
    "source_style_name": "Title"
  }
}
```

圖片或 QR Code 範例：

```json
{
  "type": "image",
  "content_origin": "qr_decoder",
  "heading_path": ["真正的文件標題", "文章標題"],
  "metadata": {
    "source_order": 4,
    "associated_heading_block_id": "source-001-block-002",
    "associated_heading_path": ["真正的文件標題", "文章標題"],
    "relationship_id": "rId6",
    "association_method": "ooxml_container_order"
  }
}
```

來源層 metadata 必須明確宣告能力：

```json
{
  "layout_semantics_status": "reliable",
  "document_title_semantics_status": "reliable"
}
```

DOCX、DOC、PDF 必須提供這兩個旗標。只有兩者都宣告為 `reliable`，來源才有資格回報 `success`，並進入詳細順序與標題語意硬閘門。旗標缺少、值為 `inferred` 或 `needs_review` 時，必須降級或留下失敗紀錄，不得以省略 metadata、空 Chunk 或報告預設值冒充通過。
