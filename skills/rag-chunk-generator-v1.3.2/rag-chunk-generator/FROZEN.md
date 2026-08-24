# FROZEN.md｜rag-chunk-generator 凍結帳本

## v1.0（2026-06-26，初始定版）

### 凍結項目

| 凍結類別 | 凍結值 | 定版檔 |
|---|---|---|
| metadata 欄位清單 | chunk_id、text、source_file、file_type、chunk_index、page_number、start_time、end_time、section_title、prev_chunk_id、next_chunk_id、token_count、summary | SKILL.md §Metadata 規格 |
| chunk_id 格式 | `{slug}_{定位碼}_{序號:04d}` | SKILL.md §Metadata 規格 |
| 交付格式 | `{stem}_chunks.md` ＋ `{stem}_chunks.zip` | SKILL.md §交付格式 |
| 預設參數 | chunk_size=256、overlap=40、min_len=30 | scripts/run_chunker.py |
| LlamaIndex 主鍵 | node_id（= chunk_id）、text、metadata | SKILL.md §Metadata 規格 |
| LangChain 主鍵 | page_content（= text）、metadata | SKILL.md §Metadata 規格 |

### 回歸測試守門
`tests/test_chunker.py` 中的以下測試是凍結斷言守門，改動上述任何項目會讓測試變紅：
- `test_frozen_metadata_keys`
- `test_frozen_default_params`
- `test_chunk_id_format`

### 擴充規則
- 新增 metadata 欄位：另開下一版，在既有 schema 上增欄，不刪欄
- 新增格式支援：另開下一版，新增對應 adapter
- 調整預設參數：另開下一版，更新對應的凍結斷言
- **絕不在 v1.0 定版檔上就地修改已凍結值**

---

## v1.1（2026-07-20，實戰回饋版）

來源：SME AOS Day 1 講義 PDF 切片實戰，暴露出四個問題，全部以「加層」方式修正，v1.0 凍結項一項未動。

### 新增（不影響凍結契約）

| 新增項 | 檔案 | 說明 |
|---|---|---|
| 文字前處理層 | `scripts/preprocess.py` | 部首字修復、頁眉頁尾濾除、章節雙層標題追蹤、破折號統一 |
| token 編碼降級層 | `scripts/enc_compat.py` | tiktoken 不可用時改離線近似編碼器，encode／decode 可逆 |
| summary 抽取式降級 | `scripts/generate_summary.py` | `extractive_summary()`：章節標題＋核心句 |

### 修正（bug fix，非契約變更）

- `chunk_pdf.py`／`chunk_docx.py`／`chunk_mp4.py`：`import scripts.bootstrap` 改為 `import bootstrap`（原寫法在 scripts 目錄下直接執行必定 ModuleNotFoundError）
- `scripts/validate_punct.py`：收斂回 joan-skill-conventions 正本（v1.2），`validate_output.py` 改呼叫正本的 `check()`

### v1.1 凍結項

| 凍結類別 | 凍結值 | 定版檔 |
|---|---|---|
| 部首補充區對照表鍵值 | U+2ED1、U+2ED2、U+2EBA、U+2EBF、U+2EE2、U+2EE4、U+2EE8 | scripts/preprocess.py |
| 離線編碼器切分規則 | CJK 一字一 token、拉丁 4 字、數字 3 字 | scripts/enc_compat.py |
| section_title 組合格式 | `章｜節`（全形分隔線） | scripts/preprocess.py `compose_heading()` |

### 回歸測試守門（v1.1 新增）

- `test_normalize_radicals`：部首字修復且全形標點不被打成半形
- `test_offline_encoding_roundtrip`：離線編碼器 encode／decode 可逆
- `test_footer_filter`：頁眉頁尾樣式命中
- `test_heading_compose`：章節雙層組合格式
- `test_extractive_summary_fallback`：降級摘要非空且不含錯誤字串

### 擴充規則（沿用 v1.0）

- 要加新的頁尾／標題樣式：往 `preprocess.py` 的樣式庫清單加，不動引擎
- 要改 metadata 欄位、chunk_id 格式、交付格式、預設參數：另開下一版，**絕不就地改**

## v1.2（2026-08-21，token 驗證暗洞修補，未動任何凍結值）

- validate_output.py token 檢查：自我循環（同一把 enc_compat 重算）→ 契約範圍檢查（[min_len, (chunk_size＋overlap)×1.2]）。
- enc_compat 交叉核對改為可選，缺席不誤報。
- preprocess.py／enc_compat.py（v1.1）與 v1.0 凍結項（metadata、chunk_id 格式、交付格式、預設參數 256／40／30、主鍵）全數不變。
- 新增回歸：test_v12_token_*（爆量擋、界內過、低於 min_len 擋、不再恆過）。

## v1.3.0-dev（2026-08-24，候選，不是定版）

### 新增

| 新增項 | 實作 | 說明 |
|---|---|---|
| PDF primary adapter | `scripts/chunk_pdf_docling.py` | Docling 抽取，要求 page provenance；沒有定位就停止 |
| DOCX adapter | `scripts/chunk_markup.py` | MarkItDown 預設；python-docx 仍為 explicit legacy |
| HTML adapter | `scripts/chunk_markup.py` | MarkItDown document；Trafilatura article |
| XML adapter | `scripts/chunk_markup.py` | lxml-safe 預設，禁止 DTD、entity expansion 與 network |
| 共用切片層 | `scripts/adapter_common.py` | adapter 只回傳 blocks，避免格式路由重複 chunk 邏輯 |
| 品質閘門 | `scripts/quality_gate.py` | 空內容、定位、相容字元、Private Use Area、品質錨點 |
| 新版 metadata | `render_md.py` | 可附 source_locator、block_type、extraction_backend、quality_status |
| 本地摘要預設 | `generate_summary.py` | `extractive` 預設；API 僅明確指定才啟用 |
| 安裝後能力驗證 | `scripts/bootstrap.py` | `_pip()` 安裝後重新 import；MarkItDown DOCX 另跑最小 conversion smoke test |

### 不納入 runtime

- PyMuPDF4LLM：不納入本候選。
- Marker：只作定版前比較候選，不由 CLI 路由呼叫。
- Acrobat 或其他付費桌面 OCR／轉檔：不納入 skill 相依。

### 定版前必要驗證

- 靜態測試與 `quick_validate.py` 通過。
- 在隔離環境實際安裝並執行 Docling、MarkItDown、Trafilatura 與 lxml-safe XML fixture。
- 用 source-bound GOLDEN 錨點驗證英文片語空格、apostrophe、頁碼定位與 XML hierarchy。
- 若任一 runtime backend 或品質錨點失敗，候選維持 `PARTIAL`，不得宣稱已定版。

## v1.3.1-dev（2026-08-24，候選，不是定版）

### 新增

- `scripts/chunk_pdf_marker.py`：可選 Marker 純文字層比較 adapter，明確使用 `--disable_ocr`。
- `--marker_page_range`：只影響 Marker 路由。
- `quality_gate.py`：預設品質異常標記 `REVIEW` 並繼續原有 `.md`／`.zip` 交付。
- `--strict_quality`：明確要求時才恢復品質異常阻擋。
- `references/version.md`：版本歷史與相容性說明，SKILL.md 只保留目前版。

### 不變

- v1.0 metadata 欄位、chunk 參數、chunk_id 規則與兩種交付檔名不變。
- 不新增正常／異常 chunk 隔離資料夾。
- Docling 仍是 PDF 預設 backend，Marker 不取代預設路由。

## v1.3.2-dev（2026-08-24，候選，不是定版）

### 新增

- `SKILL.md` 補齊 HTML／XML 的工作紀律、工作策略、流程與工具矩陣，詳細規格移至 `references/html-xml.md`。
- HTML 加入 BOM／`meta charset` 嚴格解碼與檔案大小預檢，拒絕以 replacement character 掩蓋資料遺失。
- XML safe 路由加入 DOCTYPE／ENTITY 拒絕、檔案大小、元素數與巢狀深度限制。
- XML locator 保留 namespace、屬性、同名兄弟索引與 mixed content 順序。
- 新增 HTML／XML fixture、正向測試與 fail-closed 負向測試。

### 不變

- v1.0 metadata 欄位、chunk 參數、chunk_id 規則與兩種交付檔名不變。
- 不新增正常／異常 chunk 隔離資料夾。
- 不新增 HTML／XML 專用 embedding、retrieval、reranking 或模型相依。
- v1.3.1-dev 與更早凍結版本的來源檔案不修改。

## v1.3.2（2026-08-24，定版）

- v1.3.2-dev 候選已通過 49 項回歸測試、compile、quick validation、負向安全測試、HTML／XML runtime fixture 與獨立 ZIP acceptance。
- HTML document／article、XML safe／MarkItDown fallback 都維持原有 `.md`／`.zip` 交付契約。
- v1.0 metadata、chunk_size／overlap／min_len 預設、chunk_id 規則與不增加 chunk 隔離格式全部凍結。
