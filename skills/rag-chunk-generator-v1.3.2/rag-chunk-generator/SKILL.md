---
name: rag-chunk-generator
metadata:
  version: "1.3.2"
description: >
  接受 PDF、DOCX、HTML、XML 與 MP4，將來源抽取成可驗證的高細緻度 RAG Markdown 切片，交付單份彙整 .md 與多檔 .zip。
  PDF 預設使用 Docling，另提供可選 Marker 與 legacy 路由；DOCX 預設使用 MarkItDown，HTML 依 document 或 article 模式路由，XML 使用安全 lxml parser，MP4 使用 Whisper。
  預設 chunk_size／overlap／min_len 為 256／40／30 token，品質警告預設不阻斷原有 .md／.zip 交付。
---

# rag-chunk-generator

> **v1.3.2｜2026-08-24**：補齊 HTML／XML 的工作紀律、路由策略、執行流程、工具矩陣與安全／品質閘門；輸出契約不變。版本歷史與前版變動請參考 `references/version.md`。

## 能力邊界

**支援範圍：**

- PDF：以文字層為前提，Docling 為預設，Marker 為可選純文字層比較 adapter，legacy 僅供診斷。各路由需提供定位資訊。
- DOCX：MarkItDown 為預設 adapter；python-docx 只作明確指定的相容路徑。
- HTML：MarkItDown `document` 模式保留一般文件內容；Trafilatura `article` 模式只抽取網頁主文。
- XML：預設 lxml 安全 parser，保留元素階層、屬性與 XPath-like locator；可明確指定 MarkItDown 一般轉換路徑。
- MP4：Whisper 轉逐字稿並保留時間戳記。

**界外或不保證：**

- 沒有文字層的掃描 PDF、加密 PDF，以及 Docling 無法提供 provenance 的 PDF。這些情況停止，不輸出看似成功的空切片。
- MarkItDown 的目標是文字分析，不是高保真排版複製；複雜版面、圖片內文字與特殊嵌入物仍需人工或獨立比較驗證。
- Trafilatura 只適合文章型網頁，不適合需要完整 DOM、屬性或技術標記的 HTML。
- XML parser 不解析外部 DTD、不展開外部 entity、不連線取檔；惡意或不完整 XML 會停止。
- 不支援跨檔案合併，也不把付費桌面軟體、雲端服務或 OCR server 當作必要依賴。Marker 只在明確指定時安裝，且固定使用純文字層路徑。

## Backend 路由

| 格式 | 預設路由 | 可選路由 | 目的 |
|---|---|---|---|
| PDF | Docling | `--pdf_backend marker` 或 `legacy` | Docling 預設；Marker 可選純文字層比較；legacy 只供診斷 |
| DOCX | MarkItDown | `--docx_backend legacy` 使用 python-docx | 語意 Markdown；舊路徑保留相容性 |
| HTML | MarkItDown document | `--html_mode article` 使用 Trafilatura | 一般文件與文章主文分流 |
| XML | lxml-safe | `--xml_backend markitdown` | 預設保留階層與屬性，fallback 才用一般轉換 |
| MP4 | Whisper | 無 | 保留逐字稿時間戳記 |

Marker 是可選純文字層比較 adapter，不是預設路由，也不執行 OCR。它不改變 chunk、Markdown 或 ZIP 契約；這個 skill 不使用 PyMuPDF4LLM。

## HTML 工作規格

### 工作紀律

- 預設只處理本機檔案，不自行抓取 URL 或執行網頁中的 script。
- `document` 模式保留一般文件語意；`article` 模式才允許移除網頁樣板雜訊。
- HTML 必須先通過檔案大小與嚴格編碼預檢；不以 `errors="replace"` 掩蓋解碼遺失。
- 轉換後的每個非空 block 必須有 `converted-line` 定位；這是轉換串流定位，不宣稱等同原始 DOM 行號。
- 不把模型式 HTML 壓縮、embedding pruning 或 reranking 當成抽取層必要步驟。

### 工作策略

- 文件型 HTML 使用 MarkItDown，保留 heading、paragraph、list、table、link 與 code 的 Markdown 語意。
- 文章型 HTML 使用 Trafilatura，保留主文、標題、清單與表格，但不保證完整 DOM 或屬性。
- 兩種模式共用同一個 normalized block 與 chunk 引擎，因此切片參數與交付檔名不分流。

### 工作流程

1. 驗證副檔名、本機檔案與安全大小。
2. 讀取 BOM 或 HTML `meta charset`，嚴格解碼並拒絕 replacement character。
3. 依 `--html_mode` 選擇 MarkItDown 或 Trafilatura。
4. 將轉換結果拆成 heading、paragraph、list、table blocks，附轉換行定位。
5. 交給共用層做短段合併、長段切分、overlap、摘要、品質檢查與原有 `.md`／`.zip` render。

### 工具

| 目的 | 工具 | 使用條件 |
|---|---|---|
| 文件型 HTML | MarkItDown | 預設 `document` 模式 |
| 文章主文 | Trafilatura | 明確指定 `--html_mode article` |
| 共用切片與驗證 | `adapter_common.py`、`quality_gate.py` | 所有 HTML 路由 |

詳細的編碼限制、模式選擇與已知限制請讀 `references/html-xml.md` 的 HTML 節。

## XML 工作規格

### 工作紀律

- 預設只處理本機 XML，使用 lxml 安全 parser，禁止 DOCTYPE、ENTITY、外部 DTD、外部 entity 與網路存取。
- 檔案大小、元素數與巢狀深度超過安全上限時停止，不輸出不完整的 XML 切片。
- 保留元素順序、namespace、屬性、同名兄弟索引與 mixed content 的文字順序。
- safe 路由的 namespace locator 使用 Clark notation，例如 `/{urn:example}catalog/{urn:example}book[1]`；無 namespace 時維持 `/catalog/book[1]`。
- `--xml_backend markitdown` 只作明確指定的一般文字轉換 fallback，不取代安全預設。

### 工作策略

- lxml-safe 以元素階層與屬性形成語意 blocks，讓 XML 標籤本身不在轉換時消失。
- 有 mixed content 的元素保留其 inline 文字順序，子元素另以自己的 locator 成為可檢索 block。
- namespace 相同才計入同名兄弟索引，避免不同 vocabulary 的同名元素互相碰撞。
- XML 只負責結構化抽取與切片，不在 skill 內加入 XML 專用 embedding、retrieval 或 reranking 演算法。

### 工作流程

1. 驗證副檔名、本機檔案與安全大小，拒絕 DTD／entity 宣告。
2. 以 `recover=False` 解析 XML，並獨立檢查元素數與巢狀深度。
3. 遍歷元素，產生 namespace-aware locator、屬性行與 mixed-content 文字。
4. 將元素 blocks 交給共用層做短段合併、長段切分、overlap、摘要、品質檢查與原有 `.md`／`.zip` render。
5. 解析或安全限制失敗時回報明確錯誤，不以修復模式產生看似完整資料。

### 工具

| 目的 | 工具 | 使用條件 |
|---|---|---|
| 安全 XML 抽取 | `lxml.etree` | 預設 `--xml_backend safe` |
| 一般文字 fallback | MarkItDown | 明確指定 `--xml_backend markitdown` |
| 共用切片與驗證 | `adapter_common.py`、`quality_gate.py` | 所有 XML 路由 |

詳細的 namespace、mixed content、安全上限與限制請讀 `references/html-xml.md` 的 XML 節。

## 開場對焦閘門

生成前確認：

1. 副檔名與實際格式相符。
2. 沿用 `chunk_size=256`、`overlap=40`、`min_len=30`，除非使用者指定其他值。
3. 摘要預設為本地抽取式；只有使用者明確指定 API 模式時才使用外部 API。
4. 已知關鍵詞或句子可用 `--quality_anchor` 重複指定，作為抽取品質的精確驗證。

若輸入是掃描 PDF 或需求明確要求 OCR，先說明本版範圍，不把 OCR 結果假裝成已驗證的文字層結果。

## Adapter 契約

每個新格式 adapter 只負責抽取與定位，回傳 normalized blocks：

```text
text              必填，非空正文
section_title     可為 null
    source_locator    新格式必須提供，例如 p005、converted-line:0003-0005 或 /catalog/book[1]
block_type        paragraph、heading、table、list 或 xml_element 等
page_number       PDF 頁碼；其他格式為 null
```

共用切片層再負責超長切分、短段合併、overlap、token_count、chunk_id 與 prev／next 指針。這樣 backend 替換不會同時改動輸出契約。

## Metadata

v1.0 凍結欄位全部保留：

```yaml
chunk_id: "lecture_01_p003_0012"
text: "切片正文"
source_file: "lecture_01.pdf"
file_type: "pdf"                 # pdf / docx / html / xml / mp4
chunk_index: 12
page_number: 3
start_time: null
end_time: null
section_title: "第二章｜語言模型基礎"
prev_chunk_id: "lecture_01_p003_0011"
next_chunk_id: "lecture_01_p003_0013"
token_count: 243
summary: "本段核心摘要。"
```

v1.3 新增欄位只加不刪：

```yaml
source_locator: "p003:l=10.0,t=20.0,r=500.0,b=40.0"
block_type: "paragraph"
extraction_backend: "docling"
quality_status: "PASS"
```

`node_id` 等於 `chunk_id`，LlamaIndex 使用 `text` 與 `metadata`；LangChain 使用 `page_content` 與同一份 `metadata`。交付仍是 `{stem}_chunks.md` 與 `{stem}_chunks.zip`。

## 執行

```powershell
python scripts/run_chunker.py `
  --input <檔案路徑> `
  --chunk_size 256 `
  --overlap 40 `
  --min_len 30 `
  --summary_mode extractive `
  --output_dir <輸出資料夾>
```

主要選項：

- `--pdf_backend docling|marker|legacy`，預設 `docling`。
- `--marker_page_range TEXT`，Marker 純文字層路由只處理指定頁面範圍。
- `--docx_backend markitdown|legacy`，預設 `markitdown`。
- `--html_mode document|article`，預設 `document`。
- `--xml_backend safe|markitdown`，預設 `safe`。
- `--summary_mode extractive|api`，預設 `extractive`。
- `--quality_anchor TEXT` 可重複指定；所有錨點都必須在切片正文中出現。
- `--skip_summary` 保留空 summary，不執行摘要。

相依套件依格式延遲檢查與安裝。DOCX 不只檢查 `import markitdown`，還會用最小 DOCX 執行 conversion smoke test，確認 extras／plugin 真正可用。主流程不呼叫 `ensure_all()`，不因處理 HTML 而安裝 Whisper，也不因處理 XML 而安裝 Docling。

## 品質檢查

在 render 前執行 deterministic quality check：

- 切片不可為空。
- Docling、MarkItDown、Trafilatura 與 XML 路由必須有 `source_locator`。
- replacement character、Private Use Area 與已知相容標點字元會使狀態變成 `REVIEW`；只有明確指定 `--strict_quality` 才會阻擋交付。
- HTML 未宣告或無法嚴格解碼時在抽取前停止；XML DTD／entity、大小、元素數或深度限制失敗時在抽取前停止。
- `--quality_anchor` 指定的精確文字只要缺少一項就列出警告；只有 `--strict_quality` 才會停止。
- 異常時狀態為 `REVIEW`，預設列出警告後仍繼續 render，保留原有 `.md`／`.zip` 交付契約。
- 只有明確指定 `--strict_quality` 才在品質警告時停止。
- `validate_output.py` 仍驗 token 範圍、metadata、prev／next 雙向一致性、Markdown 與 ZIP 交付結構。

品質檢查通過時標記 `quality_status: PASS`，有警告時標記 `REVIEW`。這只代表抽取結構與規則檢查結果，不等於已證明每個英文單字都與原始版面完全相同。

## 摘要策略

預設使用 `generate_summary.py` 的抽取式摘要，不呼叫網路。API 模式只有明確指定 `--summary_mode api` 才啟用；API 失敗會降級為抽取式，錯誤訊息不會寫入交付物。

## 驗證與定版規則

```powershell
python -m pytest tests/ -v
python C:\Users\robert\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```

在實際 backend 未安裝的環境，靜態測試只能證明路由與解析純邏輯；不可把它寫成 backend runtime PASS。版本歷史、相容性與每版變動請讀 `references/version.md`。HTML／XML 的詳細工作規格請按需讀 `references/html-xml.md`。定版前仍須在含相依套件的隔離環境執行最小 fixture，並重新檢查 ZIP 內容。

版本凍結、舊版不可變更與 v1.3.2 定版差異以 `FROZEN.md` 為準。
