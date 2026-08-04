# Adapter 與 Provenance 契約

## Adapter 責任

每個 Adapter 只做兩件事：

1. 解析自己的格式。
2. 輸出統一 Document IR。

禁止在 Adapter 內執行 Chunking。格式專屬邏輯不得改變共用狀態及輸出契約。

Adapter 是已執行的處理 lane，不是對 runtime 的預設假設。Agent 必須先依目前可用能力選擇原生檔案理解、技能資源、安全補足或等效 lane；一旦選定，Adapter 仍須輸出相同 Document IR、Provenance 與既有狀態。未使用 LibreOffice、FFmpeg、Tesseract 或其他指定工具不構成失敗；來源範圍與輸出證據才是判定基礎。

## Provenance 必填欄位

```json
{
  "source_id": "source-001",
  "user_specified_name": "example.pdf",
  "original_upload_name": "example.pdf",
  "runtime_path": "/runtime/example.pdf",
  "extension": ".pdf",
  "requested_media_type": "application/pdf",
  "runtime_media_type": "application/pdf",
  "magic_bytes": "25504446",
  "sha256": "...",
  "actual_adapter": "pdf_adapter",
  "original_binary_processed": true,
  "derived_snapshot": false,
  "input_fidelity": "original_binary",
  "derivation_chain": [],
  "source_dimensions": {
    "page_count": 2
  }
}
```

## Snapshot 判定

requested media type 與 runtime media type 不一致，且 runtime 實際是 Markdown 或純文字時，標示：

```json
{
  "original_binary_processed": false,
  "derived_snapshot": true,
  "input_fidelity": "derived_snapshot"
}
```

Snapshot 不得標示完整成功。若 `--require-original-binary` 啟用，必須為 `fatal_error`。

## 格式路由

| 格式 | Adapter | 原生優先內容 |
|---|---|---|
| PDF | `pdf_adapter` | 文字層、bbox、表格、內嵌圖片、頁碼。 |
| DOCX | `docx_adapter` | OOXML Paragraph、Heading、List、Table、DrawingML Shape、Image。 |
| DOC | `doc_adapter` | 可用時以 LibreOffice 轉 DOCX，再走 DOCX Adapter；否則選擇可保留等效證據的 runtime lane。 |
| HTML／HTM | `html_adapter` | DOM Heading、Paragraph、List、Table、Code、Local Image，以及清單下非標準可見直接子內容。 |
| XML | `xml_adapter` | XML node、XPath、階層、表格型節點、本地圖片引用，以及使用者可見的 Cheat Sheet 屬性。 |
| CSV | `csv_adapter` | Header、Row、Column。 |
| Markdown | `markdown_adapter` | Heading、List、Table、Code、Image。 |
| Image | `image_adapter` | Decoder、視覺分類、選擇性 OCR。 |
| MP4 | `video_adapter` | 字幕、離線轉錄、關鍵影格及降級狀態；可用時保留時間範圍證據。 |

## 獨立圖片語意路由

`image_adapter` 先以實際 decoder 取得 QR payload，再以通用介面版面結構判定 `screen_capture`，之後才嘗試 Barcode decoder。只有具文字區塊 evidence 的 `text_block` 才進入 OCR；圖片尺寸本身不是 OCR 路由證據。QR 或 Barcode 成功時，Block 必須有 `machine_payloads`、來源 asset SHA-256 與 decoder evidence，且不得再 OCR。

沒有已驗證機器載荷的 `screen_capture` 必須輸出既有非必要、非關鍵、`skipped`、非逐字 `derived_normalization` Block，`skip_reason` 為 `no_verified_machine_payload`。這不是圖片文字理解；不得把 OCR 猜測送入 Chunk。完整輸出和 gate 規則見 `image-semantics-gate.md`。

## DOCX DrawingML

大量內容位於文字方塊時，普通 Paragraph API 可能只看到空段落。Adapter 必須先讀取 `word/document.xml` 的 DrawingML anchor、座標及 `w:t`，重建閱讀順序、表格與編號段落。只有此路徑失敗時，才以 LibreOffice 轉 PDF，並把轉換記入 derivation chain。

## HTML、XML 與 Table 語意保留

HTML／HTM 的 `<ul>` 或 `<ol>` 不能假定只含合法 `<li>`。其可見的直接 `<p>`、`<b>`、其他文字容器及文字節點必須按 DOM 順序保留。`<br>` 本身不產生文字 Block，但不得造成前後可見文字遺失。

Table Block 必須記錄 `caption`、`header`、`rows` 與 `heading_context`。Caption 必須進入 normalized Markdown，因為它可能定義表格欄位的判讀規則。

XML 的下列使用者可見屬性必須成為具 XPath 的 Block：`cheatsheet.title`、`compositeCheatsheet.name`、`taskGroup.name`、`task.name`、`item.title`、`subitem.label`。`contextId`、`param.value` 與 `serialization` 應保留為 metadata 或 relationship，不強制混入正文。

## DOCX 標題與圖片順序

DOCX 原生路徑必須依下列優先序決定文件標題：

1. Word 內建 `Title` paragraph style。
2. Core Properties 的 title。
3. 第一個有效 `Heading 1`。
4. 檔名 fallback。

`Title` 必須標示 `semantic_role: document_title` 及 `level: 1`。存在文件根標題時，原始 `Heading 1` 的輸出 level 必須加一，保留文件根節點與章節節點的差異。

DOCX 圖片不得依 `word/media` 檔名整批附加到文件尾端。每個圖片 occurrence 必須由 `document.xml` 中的 relationship 引用位置建立，並至少記錄：

```json
{
  "source_order": 8,
  "relationship_id": "rId6",
  "package_path": "word/media/image2.png",
  "associated_heading_block_id": "source-001-block-002",
  "associated_heading_path": ["文件標題", "文章標題"],
  "association_method": "drawingml_geometry"
}
```

一般 inline image 依 paragraph 或 table 容器順序插入。DrawingML 浮動物件依頁面、幾何座標及 Heading cluster 建立邏輯閱讀順序。此契約要求語意位置，不要求逐像素重建 Word 畫面。

## DOC 與 PDF 閱讀順序

DOC 必須先記錄 `libreoffice_doc_to_docx` derivation，再沿用 DOCX 的 `source_order`、圖片 Heading 關聯及文件標題語意。若 LibreOffice 不可用、轉換失敗或轉換後無法可靠建立版面語意，不得回報完整成功。

PDF 必須以頁面、bbox、Block 類型及 Heading cluster 建立閱讀順序。位於第一個正文區塊之前的 QR Code 或 Barcode，若與頁首標題群組同頁，必須置於文件標題及文章標題之後、第一個正文區塊之前。圖片至少記錄：

```json
{
  "source_order": 3,
  "associated_heading_block_id": "source-001-block-002",
  "associated_heading_path": ["文件標題", "文章標題"],
  "association_method": "pdf_layout_header_cluster"
}
```

Adapter 只有在可重現地建立上述語意時，才能宣告：

```json
{
  "layout_semantics_status": "reliable",
  "document_title_semantics_status": "reliable"
}
```

## 可靠度旗標與強制降級

DOCX、DOC、PDF 的 `layout_semantics_status` 與 `document_title_semantics_status` 都是必要來源契約，不是可省略提示。只有兩者都為 `reliable`，且詳細語意驗證全部通過時，來源才可回報 `success`。

下列情況至少降級為 `partial_success`：

- 文件根標題只能由檔名推定，標示 `document_title_semantics_status: inferred` 及 `document_title_inferred_from_filename`。
- PDF 偵測到左右欄內容在相同垂直區間重疊，現有排序器無法可靠證明欄內順序，標示 `layout_semantics_status: needs_review` 及 `pdf_multicolumn_layout_caution`。
- DOCX 實際依賴未支援 VML、頁首頁尾圖片、跨頁浮動物件或未知巢狀群組。

若 VML 僅位於 `mc:Fallback`，且相同相容性區塊已有可解析的 DrawingML Choice，Adapter 可使用 DrawingML 路徑，不因 fallback 的存在單獨降級。
