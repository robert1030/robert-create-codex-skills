# v1.1.1 正式版重構與修正盤點

## 輸入版本

本次實際收到的技能包只包含 v1.1.0。沒有找到 v1.1.1-dev 的 `SKILL.md`、版號或獨立程式樹，因此無法做真實的 v1.1.0 對 v1.1.1-dev 差異比較。

原始 v1.1.0 已完整保存於 `legacy/v1.1.0-original.zip`。本次以其外部契約為基底建立 v1.1.1-dev-r2，依獨立驗證結果修正為 v1.1.1-dev-r3，再以限定範圍建立 v1.1.1-dev-r4。依實際 RAG 輸出發現 OpenCV 缺失可造成 QR 遺漏但仍回報成功，因此另開 v1.1.1-dev-r5。

## 保留

| 類別 | 保留項目 |
|---|---|
| 格式 | PDF、DOCX、DOC、HTML、HTM、XML、CSV、Markdown、MP4、JPG、JPEG、PNG、HEIF、HEIC、ZIP、巢狀 ZIP、目錄。 |
| 行為 | 來源隔離、安全解壓、SHA-256 去重、原始語言保真、Heading 優先切片、原子單元、來源追蹤、失敗隔離。 |
| 參數 | 1,000 至 1,400 Token、約 100 Token overlap、最多三次重試、`chi_tra+chi_sim+eng`。 |
| 狀態 | `success`、`partial_success`、`fatal_error` 及退出碼 0、2、1。 |
| 限制 | 不使用付費 API、不破解加密或密碼保護文件。 |

## 重構

| 舊結構 | 新結構 | 原因 |
|---|---|---|
| `parsers.py` 集中多格式解析 | `scripts/adapters/*.py` | 格式解析解耦，Adapter 只輸出 Document IR。 |
| `core.py` 混合模型、切片及輸出 | `models.py`、`normalize.py`、`coverage.py`、`chunker.py`、`output.py` | 讓每個階段可獨立驗證。 |
| 直接由 parser 產生 Chunk | 先 Document IR 及 normalized Markdown | 防止來源不完整仍直接切片。 |
| 單一驗證層 | Chunk 前及 Chunk 後雙閘門 | 分開來源完整度與 Chunk mapping。 |
| DOCX 只依一般 Paragraph／Table | 加入 DrawingML 文字方塊解析 | 避免 Shape-heavy DOCX 只得到空段落。 |

## 重寫

- OCR 重試及品質判定，移除有輸出就成功的假設。
- Provenance、MIME、magic bytes、SHA-256 及 snapshot 判定。
- `normalized-document.md` 產生及失敗占位。
- 共用 Chunker 與 Block mapping 驗證。
- 固定輸出 hash 及最終驗證器。

## 移除或不再強制

- Adapter 內 Chunking。
- PDF Markdown snapshot 冒充原始 PDF 成功。
- LLM 圖形摘要冒充逐字 OCR。
- 0／0 比例自動標成 1.0。
- 必要內容失敗但整體仍標示 success。
- 每次使用者輸出中的 `invocation.json`、`validation-log.txt`、`unit-test-report.json`、`process-exit-code.txt`、`transform-log.jsonl`、`retrieval-validation.json`。

## 未採用的過度設計

- 沒有建立新的 OCR Framework。
- 沒有新增研究型 Benchmark 系統。
- 沒有把每個格式複製一份 Chunker。
- 沒有使用無法驗證的全域 candidate veto 或複雜 provisional threshold。

## v1.1.1-dev-r3 限定修正

| 已知缺陷 | 修正方式 | 未擴張範圍 |
|---|---|---|
| 跨兄弟章節的小文件使用最後一個 Block 的 Heading，導致整個 Chunk 錯掛在末節。 | 共用 Chunker 改以所有非 overlap 來源 Block 的最長共同 Heading 前綴。 | 不新增格式專屬 Chunker。 |
| Validator 只檢查 `heading_path` 非空。 | Validator 由 `document-ir.jsonl` 與 `source_block_ids` 獨立重算預期路徑，錯誤時退出非 0。 | 不新增研究型品質分數。 |
| PDF 合成的「英文段落」被標成 `native_text`。 | 改為 `derived_normalization`、`verbatim: false`，並加入 derivation metadata。 | 不修改 OCR 流程或視覺分類。 |

本版不新增輸出檔案、不改變支援格式、不調整 Token 門檻、不增加 OCR backend，也不建立 Benchmark 系統。

## v1.1.1-dev-r4 限定修正

| 已知改善項目 | 修正方式 | 未擴張範圍 |
|---|---|---|
| PDF 與 DOCX 的一般文字定義欄位存在斜線前後空白差異。 | 在共用正規化層只處理表格一般文字定義欄位，統一連續空白及詞性分隔斜線。 | 不修改 IPA、URL、程式碼、數學式或 combining marks。 |
| DrawingML Shape 文字可能在第三方 Renderer 顯示不同。 | 使用 `drawingml_shape_parser` 時，在處理報告加入 `docx_drawingml_rendering_caution`。 | 不宣稱已偵測裁切，不新增 Renderer、OCR 比對或版面分析。 |

本版不修改 Chunker、Validator、Token 門檻、overlap、圖片順序、輸出 Schema 或跨格式去重。

## v1.1.1-dev-r5 限定修正

| 已重現缺陷 | 修正方式 | 未擴張範圍 |
|---|---|---|
| 執行環境缺少 `cv2` 時，PDF 與 DOCX 的 QR Code 未解碼，但輸出仍標示 `success`。 | 將無法完成視覺檢查的影像列為必要失敗，使來源至少降級為 `partial_success`。 | 不改圖片閱讀順序、OCR backend 或 Validator。 |
| `references/dependencies.md` 宣告 OpenCV 為核心相依，但 `bootstrap.py` 未安裝。 | 新增 `cv2` 對應 `opencv-python-headless`，並加入回歸測試。 | 不新增新的影像 Framework。 |
| pip 指令無條件加入 `--break-system-packages`。 | 只在非虛擬環境且 externally managed 時加入；Windows 不加入。 | 不改外部系統套件清單。 |

本版不修改 Chunker、Validator、Token 門檻、overlap、圖片排序、輸出 Schema 或跨格式去重。

## v1.1.1 正式定版

- 以 v1.1.1-dev-r5 的程式行為為正式基準。
- 正式版只調整版號與凍結文件，不再修改 Adapter、Chunker、Validator、OCR、圖片排序、Token 門檻或輸出 Schema。
- 正式版必須通過完整回歸、標點驗證、Skill validator，以及 PDF 與 DOCX 的成功與缺少 OpenCV 降級路徑。

## v1.1.2-dev-r1 三項 P2 修正

| 已重現缺陷 | 修正方式 | 驗證方式 |
|---|---|---|
| DOCX 圖片及 QR Code 依 media 檔名附加到文件尾端。 | 改由 OOXML relationship occurrence、容器順序與 DrawingML 幾何建立圖片 Block，並記錄 Heading 關聯。 | TikTok DOCX 的 QR 位於文章標題之後、影片單字之前；一般 inline QR 位於下一個 Heading 之前。 |
| Validator 只用集合比對 Block，錯誤順序仍可通過。 | 新增 exact sequence、`source_order`、圖文關聯及文件標題四組獨立驗證，並檢查 Chunk frontmatter 與 JSON 一致性。 | 交換兩個 `source_block_ids`、改掛錯誤 Heading 或移除 Title semantic role 時，Validator 必須失敗。 |
| 原生 DOCX Parser 未辨識 Word `Title`。 | 依 style id、style name、Core Properties、Heading 1 及檔名依序決定根標題。 | `Title` 成為 level 1，原始 Heading 1 成為 level 2，Chunk title 使用真正文件標題。 |

本開發版不增加第八類固定輸出，不改 Token 門檻、overlap、OCR 語言或退出碼。VML、頁首頁尾圖片、跨頁浮動物件及未覆蓋的巢狀群組仍屬能力邊界，不能由本次測試推論為全面支援。

## v1.1.2-dev-r2 跨格式收斂修正

| 未完成範圍 | 修正方式 | 明確不擴張項目 |
|---|---|---|
| v1.1.2-dev-r1 的閱讀順序及圖文關聯 Validator 只對 DOCX 生效。 | 改以來源能力旗標決定適用性，DOCX、DOC、PDF 只要宣告版面語意可靠，就必須通過相同硬閘門。 | 不建立通用 LLM 排版引擎。 |
| PDF 內嵌圖片在文字與表格處理後才附加，頁首 QR Code 被放到表格之後。 | 依頁面 bbox、Block 類型與 Heading cluster 排序，頁首 QR Code 置於標題群組之後、第一個正文區塊之前。 | 不宣稱支援所有跨欄、資訊圖或未知巢狀版面。 |
| DOC 路徑未納入實檔驗收。 | 新增 Word 97 DOC Fixture，確認 LibreOffice 轉 DOCX 後保留 `source_order`、圖文關聯及根標題語意。 | 不新增另一套 DOC Parser。 |
| PDF 缺少順序與錯誤 Heading 的負向測試。 | 新增交換 `source_block_ids` 及竄改 QR Heading 關聯的輸出驗證測試。 | 不增加第八類固定輸出。 |

本版保留 v1.1.1 正式凍結契約及 v1.1.2-dev-r1 的 DOCX 修正，不改 Token 門檻、overlap、OCR 語言、OCR backend 或退出碼。

## v1.1.2-dev-r3 語意可靠度與 Validator 防繞過修正

| 已重現缺陷 | 修正方式 | 明確不擴張項目 |
|---|---|---|
| 複雜雙欄 PDF 依列位置交錯輸出，仍回報 `layout_semantics_status: reliable` 及 `success`。 | 新增可重現的左右欄重疊風險偵測。命中時標示 `needs_review`、加入 caution，Chunk 前降級為 `partial_success`。 | 不建立通用 AI 版面理解引擎，不宣稱涵蓋所有多欄樣式。 |
| DOCX 無 Title、Core Properties title 或 Heading 1 時，以檔名當根標題仍宣告可靠。 | 檔名 fallback 改為 `document_title_semantics_status: inferred`，加入明確 warning，來源不得完整成功。 | 不以 OCR 或 LLM 猜測文件標題。 |
| 外部 Validator 可在重新計算 manifest Hash 後，因移除所有 `source_order`、圖文關聯 metadata、語意旗標或 Chunk 後指標而繞過檢查。 | 由 IR 與 Chunk 獨立要求完整 metadata，檢查圖片 Heading path 與關聯方法，要求語意旗標及四項報告指標存在。 | 不把報告欄位存在等同內容正確，仍保留獨立重算。 |
| DOCX 的現代 DrawingML Choice 同時帶 VML fallback，被粗略字串掃描誤判成未支援 VML。 | 只偵測 `mc:Fallback` 外的實際 VML 依賴；已有可解析 DrawingML Choice 的 fallback 不單獨降級。 | 不宣稱實際 VML 路徑已支援。 |

本版新增兩個語意降級測試及四組輸出竄改負向測試。完整格式契約不變。未直接覆蓋的格式及路徑記錄於 `references/test-coverage.md`，不得宣稱已證明零回歸。

## v1.1.2 正式定版

- 以 v1.1.2-dev-r3 的程式行為為正式基準，只將版本 metadata、凍結帳本、正式回歸斷言及覆蓋矩陣標題正式化。
- 正式化過程不修改 Adapter、Document IR、Normalizer、Chunker、Validator、OCR、圖片排序、Token 門檻、輸出 Schema 或退出碼。
- 正式版完整保留 DOCX、DOC、PDF 的閱讀順序、圖片與 QR Code Heading 關聯、Word `Title` 語意、複雜跨欄 PDF 降級、檔名推定標題降級及輸出竄改拒絕行為。
- 未直接覆蓋的格式與路徑仍依 `references/test-coverage.md` 明示為覆蓋缺口，不得宣稱已證明全面零回歸。

## v1.2.0-dev-r1 collection 骨架

| 項目 | 本開發版處理方式 | 不變項目 |
|---|---|---|
| 多成員來源 | 新增通用 collection inventory、profile 選用與關聯 resolver 骨架。 | 不把 collection 限縮為 iTest、Eclipse Help 或 HTML／XML。 |
| 特定結構 | 只有明確訊號成立時才規劃選用 profile。 | generic collection 保持可用，單檔 Adapter 不被替換。 |
| 關聯驗證 | 新增 member、critical、順序及 relationship gate 骨架與負向測試。 | 不把 Adapter 自報成功當成外部完整度證明。 |
| 主流程 | 本版不接入 CLI。 | v1.1.2 的所有格式、輸出、Token、OCR 與退出碼行為不變。 |

## v1.2.0-dev-r2 collection 接入

| 已重現缺口 | 修正方式 | 明確不擴張項目 |
|---|---|---|
| ZIP 或目錄 intake 以 SHA-256 直接刪除重複 member，alias 的相對連結基準消失。 | collection runtime 保留每個 member、canonical alias 與 virtual base path，內容 alias 各自處理及輸出。 | 不改單一檔案或非 collection intake 的既有去重行為。 |
| HTML Adapter 漏掉 body、div、span 或 br 後的裸文字。 | 依 DOM preorder 處理語意容器與未被容器涵蓋的文字節點。 | 不建立特定網站的 selector 清單。 |
| HTML／XML 的跨檔關聯未進入 IR 或輸出，無法驗證相對連結、錨點與缺失目標。 | 將 relationship occurrence 寫入 per-source report，control 關聯寫入 collection report，並以獨立 Validator 重算。 | 不把所有圖片文字強制 OCR 或強制寫入 Chunk。 |
| TOC 以檔名或字典順序推定 hierarchy。 | 僅在已驗證 Eclipse Help profile 使用 XML preorder、sibling index、depth 與 target resolution。 | generic collection 不猜測控制檔語意。 |
| collection gate 僅是 pure function，CLI 可繞過。 | CLI 寫入 collection report 並納入整體退出碼；獨立 Validator 可由原始輸入重算。 | 不改每來源七類輸出、Token、overlap、OCR 或其他 Adapter。 |
| 長共同路徑的 member 在可讀輸出 slug 截斷後共用 source ID，導致不同來源覆寫同一輸出目錄。 | collection source ID 另外納入完整 display path 與二進位雜湊的固定長度指紋，並新增截斷碰撞回歸。 | 不改單檔既有 source ID 規則。 |
| XML comment 會進入 lxml iterator，且 XML 支援檔與生成診斷檔被送往內容 Adapter。 | 跳過非元素節點；以 XML 結構與可讀文字判斷 resource，保留無法解析 XML 為內容來源。 | 不用 iTest 路徑或檔名建立排除清單。 |
| 已驗證 Eclipse Help 的圖片可經 CSS 或執行期引用，僅掃描 HTML `src` 會誤判為數千份獨立來源。 | 已驗證 profile 將視覺二進位檔 catalogued 為資源；generic 與 linked markup collection 的圖片仍維持直接來源。 | 不限縮一般圖片格式支援，不強制圖片進入 Chunk。 |
| bundle-qualified `help::` URI 的目標不在本壓縮包時，被錯稱為來源缺檔。 | 能解析為本 collection member 時維持 resolved；否則將明確 bundle URI 標為 external，裸 email 同樣記錄為外部關聯。 | 相對檔案、圖片或未帶 bundle 的本地目標仍保留 `source_missing_target`。 |
| 已移除的 HTML 頁尾仍是必要 Block，導致 Chunk 硬閘門拒絕空白內容。 | collection occurrence 的已辨識頁首頁尾保留原文、移除摘要及跳過原因，並轉為非必要 `skipped` Block。 | 不改單檔正規化或任意刪除一般文字。 |
| DOC 轉檔共用 LibreOffice 使用者設定檔在隔離環境無法建立。 | 為每個來源使用 work directory 內的隔離 profile。 | 不替換 DOC 轉換路徑、不改 DOCX 的語意或輸出。 |

### v1.2.0-dev-r2 iTest Help 26.2.0 實檔結果

- 原始 ZIP 共 7,004 個 member：1,301 個內容、3 個 control、5,700 個 resource，另保留 190 個同雜湊 alias。
- 1,301 個內容來源皆為 `success`。關聯共 14,202 次：13,764 次已解析、432 次 external、6 次 `source_missing_target`。
- 六項 collection gate 指標均通過。獨立 `validate_collection.py` 無 errors 或 warnings，退出碼為 2，原因是六個來源檔中不存在的目標已誠實保留，collection 因此為 `partial_success`，不可寫成完整成功。
- 此實檔僅驗證可辨識 Eclipse Help profile 的這一個 collection；不推論其他網站產生器、一般 ZIP、目錄或非 Eclipse collection 已無回歸。

## v1.2.0-dev-r3 補件與異質實檔規劃

| r2 遺留或驗證限制 | r3 處理方式 | 尚未完成項目 |
|---|---|---|
| iTest 有 6 個已揭露 `source_missing_target` occurrence，對應 5 個目標。 | 新增 manifest schema、base SHA、來源 artifact SHA、補件內容 SHA、relative target 推導與 occurrence 精確指派驗證。 | 尚未取得可驗證的 5 個 target bytes，不能升為 success。 |
| 一個 target 可被多個頁面引用。 | 補件 validator 允許一個 target 指派多個不同 occurrence，並拒絕未知或重複 edge。 | 尚未接入 Package IR 與正式 collection Validator。 |
| r2 過程修正 alias、裸文字、長路徑、XML、視覺資源、Help URI、頁尾與 DOC profile 等問題。 | 建立 r2 問題防回歸登錄與驗收矩陣，既有回歸不得移除。 | 異質非 Eclipse 實檔尚未取得。 |
| r2 實檔只證明 Eclipse Help profile。 | 要求至少一個不含 Eclipse controls 或 signature 的真實多格式 collection，並以兩次全新輸出與獨立 Validator 驗收。 | 未取得具來源與授權資訊的外部 fixture。 |

本版不改變 r2 runtime、固定七類輸出、支援格式、Token、overlap、OCR 或退出碼。它是補件接入前的可驗證契約與測試骨架，不是 iTest 補件完成版。

## v1.2.0 正式凍結

- r4 已將原包內有唯一可重算 evidence 的 5 個 iTest 缺失 occurrence 直接接入 runtime 與獨立 Validator，不要求使用者提供 manifest 或補件。
- 原始 ZIP 的 14,202 個關聯 occurrence 實測為 13,769 resolved、432 external、1 source missing。六項 collection gate 通過，獨立 Validator 無 errors 或 warnings；整包維持 `partial_success`，只因 Appium 圖片在原包內沒有可驗證 target。
- PDF、DOCX、DOC、單一 HTML、XML、generic linked markup collection 與 iTest Eclipse Help collection 的既有回歸皆為本版凍結證據。非 Eclipse 真實異質 collection 是未來擴大回歸，未提供實檔時不得被擴張為本版的凍結阻礙。
