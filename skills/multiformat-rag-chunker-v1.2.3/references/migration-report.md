# Multiformat RAG Chunker 版本遷移與修正紀錄

## 目錄

- v1.1.1：基礎重構與修正。
- v1.1.2：閱讀順序、版面與 Validator 修正。
- v1.2.0：collection 契約。
- v1.2.2：多格式、視覺與 dense-text 契約。
- v1.2.3：capability、切片、驗收、通用解析修正與正式凍結。

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
| DOCX 圖片及 QR Code 依 media 檔名附加到文件尾端。 | 改由 OOXML relationship occurrence、容器順序與 DrawingML 幾何建立圖片 Block，並記錄 Heading 關聯。 | 代表性 DrawingML fixture 驗證 QR 位於所屬標題之後與下一個來源章節之前；一般 inline QR 位於下一個 Heading 之前。 |
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

## v1.2.2-dev-r1 PDF 原生視覺與防繞過修補

| 已重現缺口 | 修正方式 | 明確不擴張項目 |
|---|---|---|
| PDF Adapter 沒有消費原生視覺 sidecar，掃描頁只能落入 OCR。 | 新增固定倍率頁面工作單、頁面 asset Hash 與 `full_page_scan` 視覺摘要接線。 | 不建立通用逐字 LLM OCR，不改其他格式 Adapter。 |
| 同頁 QR 成功會阻止全頁掃描處理，QR 並被算成有效主體。 | 將機器載荷與主要內容分開；存在未完成主要單元時，QR 不得阻止 `no_effective_main_content`。 | QR／Barcode decoder payload 與 critical 契約不變。 |
| PDF 圖片缺少 `asset_sha256`、`machine_payloads` 或 decoder evidence，既有 Validator 仍可放行。 | Producer 補齊 PDF 圖片 metadata；Validator 獨立檢查欄位、Hash、decoder、screen capture OCR 與空白頁狀態。 | 本開發版不宣稱其他 Adapter 的歷史圖片 metadata 已全面重驗。 |
| Agent 可自行加入 `--allow-partial-chunks`。 | CLI 與 Validator 同時要求 `--partial-authorization explicit_user_request`，並由獨立 Subagent 對照原始需求。 | 不新增 top-level status，不改退出碼。 |
| `validate_output.py` 只核對輸出內部，不能證明 Chunk 代表原 PDF。 | 新增 `validate_against_source.py`，由原始 PDF 重算來源 Hash、頁數、掃描頁、空白頁與主要 Block mapping。 | 固定七類每來源輸出不增加第八類檔案。 |

本節只記錄開發修補內容。實際回歸、代表性掃描 PDF、RAG Chunk、Validator 與來源對照結果必須由指定 Subagent 執行後再分級報告。

## v1.2.2-dev-r2 Dense-text 與 Recall 修補

| 已重現缺口 | 修正方式 | 明確不擴張項目 |
|---|---|---|
| 非逐字頁面摘要無法讓英文單字、音標、中文定義與例句逐項檢索。 | 新增逐單元 `llm_visual_text`、連續 reading order、結構欄位及雙 sidecar Hash evidence。 | 不把模型視覺轉錄標為 `verbatim: true`，不修改一般非 dense 來源路徑。 |
| Extraction Agent 自行複核會形成自我批准。 | 要求不同 Validation Agent 逐頁、逐單元核對，並以 extraction manifest SHA-256 綁定驗證結果。 | 不以欄位存在或摘要可檢索替代內容核對。 |
| Coverage 通過不能證明單字級 retrieval。 | 新增綁定來源與 extraction Hash 的 golden，以及 headword Recall@1、定義與例句 Recall@3、anchor 與頁碼硬閘門。 | 不改既有 Token、overlap、Chunk mapping 或退出碼定義。 |

## v1.2.2 前次發布候選與 dev-r3 語意修補

- 前次 v1.2.2 發布候選雖凍結 dev-r1 與 dev-r2 的 PDF 原生視覺、防繞過、dense-text admission、來源對照及 retrieval 行為，但高權重說明過度聚焦 PDF，未獲使用者接受為正式版。
- dev-r3 把 v1.2.1 的 LLM-first、runtime-aware 能力選擇與完整支援格式恢復為 frontmatter、預設提示與主流程開頭的主範圍；PDF 修正明確改列為條件式 Adapter lane。
- 本次不修改 `bootstrap.py`、Adapter、Normalizer、Chunker、Validator 或輸出 Schema，也不新增作業系統專屬安裝路徑。固定七類輸出、Token、overlap、OCR 語言、三次策略及退出碼全部保留。
- 新增語意回歸守門與非 PDF、混合多格式前向測試要求，防止日後因單一測試 fixture 或最新 patch 再次限縮整支 Skill。

## v1.2.2 正式凍結

- 正式版凍結 dev-r1、dev-r2 與 dev-r3。v1.2.1 的統一多格式能力階梯是主範圍，PDF 視覺、來源對照與 dense-text 是條件式格式分支。
- 正式化只把已驗證的版本常數與凍結戳記切換為 `1.2.2`。除版本文字外，runtime Python 與 dev-r3 完全一致。

## v1.2.3-dev-r1 capability routing 修補

| 已重現根因 | 最小修正 | 契約保留 |
|---|---|---|
| `rag_chunker.py` 只載入 visual sidecar，沒有 Agent capability handshake。Sidecar 缺失會讓 PDF、DOCX、HTML、Markdown、獨立圖片與 MP4 直接呼叫 OCR。 | 新增 `--capability-evidence` 與嚴格 schema loader。缺少 evidence 明確為 `unknown`。 | 不改支援格式、來源盤點、Adapter registry 或固定輸出。 |
| `ocr_image` 不要求 admission，任何 Adapter 都可直接執行 Tesseract。 | 新增必要 `OCRAdmission`，所有 Adapter 經 `AdapterContext.visual_route` 取得 admission。 | OCR 三次策略、語言、品質檢查與 attempts schema 不變。 |
| Validator 只檢查部分 PDF 圖片契約，不知道 LLM 與 OCR 的實際選路優先序。 | 在既有報告新增逐 asset routing evidence，Validator 與 IR Block 交叉核對並拒絕 priority violation。 | 不新增第八類檔案，不改 top-level status 或退出碼。 |
| 掃描 PDF 在原生 LLM multimodal 尚未嘗試前便逐頁呼叫 Tesseract，之後才回報原生視覺需求。 | 原生 LLM multimodal 為 available 或 unknown 時 OCR backend 完全不啟動；review sidecar 本身可作為已實際使用 LLM 視覺的 hash-bound evidence。 | v1.2.2 dense-text extraction、獨立 validation、來源對照與 retrieval gate 完整保留。 |

新增 `tests/test_v123_capability_routing.py` 是根因必要回歸，不是一般框架擴張。v1.2.2 正式來源與發布包保持不可變更；本候選通過正式驗收前仍是開發版。

## v1.2.3-dev-r2 驗收完整性與切片策略修補

| 已確認缺口 | 最小修正 | 明確不變項目 |
|---|---|---|
| dev-r1 Validator prompt 直接揭露兩份來源的路由、數量、coverage、retrieval metrics 與 PASS 條件。 | 撤回該次 acceptance 與正式發布結論；新 Validator 只接收原檔、全新輸出及人類任務要求，從來源重新建立判準。 | dev-r1 artifact 與報告不覆寫，只降級為白箱回歸和錯誤流程證據。 |
| Skill 有固定 Token 與 overlap 預設，但未要求 Agent 先判斷來源章節與查詢粒度是否適合。 | 在高權重流程、預設提示與 workflow 加入每來源切片策略對焦；預設不適合時，先提出替代大小、細緻度、overlap 與取捨。 | 不改全域預設、不改 Chunker、固定輸出、Schema、Adapter、dependency 或退出碼。 |

本版除版本常數外不修改 runtime Python。新增行為屬 Agent 的來源分析與使用者對焦責任；實際 CLI 已可用 `--min-tokens`、`--max-tokens` 與 `--overlap-tokens` 套用每份來源的確認值。

本次 PDF 與 DOCX 僅是用來證明通用切片策略與來源對輸出驗證的代表性 fixtures。dev-r2 不得加入任何檔名、頁數、章節文字、預期數量或來源專屬捷徑；其他格式與平台的支援聲明仍以既有凍結契約和各自可得證據為界。

## v1.2.3-dev-r3 範本非產品規則修補

dev-r2 封裝候選已由獨立 Package Validator 判定 `FAIL／FIX_REQUIRED`。失敗 ZIP 與報告保持不變；dev-r3 只修正該報告揭露的通用性缺陷及其同類根因。

| 已確認缺口 | dev-r3 最小修正 | 契約保留 |
|---|---|---|
| PDF adapter 以代表性 fixture 的產品文字、章節文字與固定資料列數辨識文章標題及表格。 | 由文件標題後至第一個連號結構前的來源順序推導文章標題；由連號表格前置文字推導章節；以實際連續列序比對重建結果。 | 不改 PDF Adapter 選路、Document IR、原子表格、Chunker 或固定輸出。 |
| DrawingML DOCX adapter 以代表性 fixture 的產品文字與固定章節文字建立 Heading，並寫死詞彙表欄名。 | 由文件標題、結構化區塊位置、表格前置文字及資料實際欄數推導標題與一般欄名。 | 保留 OOXML relationship、DrawingML geometry、圖片關聯、閱讀順序與標題語意閘門。 |
| 共用 Normalizer 與 DrawingML parser 以單一 fixture 的品牌文字清單移除頁首。 | 一般頁碼仍由通用格式移除；其他短頁首必須由同一文件跨頁重複與版面位置重算。 | 不改 Unicode NFC、軟換行、表格文字與重複 Block 契約。 |
| 已通過獨立 admission 的 dense `llm_visual_text` 重複標題被通用 repeated-header 正規化改成 `skipped`，使 Coverage 只承認未含重複標題的頁面。 | Normalizer 保護 `content_origin=llm_visual_text` 且 `dense_text_required=true` 的單元，不讓 repeated-header 或 duplicate-text 規則降級。 | 不放寬 Coverage、Validator 或 validation sidecar 契約；一般原生來源的重複頁首移除行為不變。 |
| 既有回歸能驗證 fixture 輸出，卻不能防止其內容被寫成 runtime policy。 | 新增 runtime source scope guard，拒絕 fixture 專屬產品文字、品牌字典與固定列數條件。 | fixtures 仍只作為測試輸入，不是服務範圍或固定答案。 |

本版不新增格式、固定輸出、Adapter、dependency、script、framework、MCP、API、付費服務或 parser family。Linux、WSL、macOS 與平台 upload／UI 是否通過，仍須以各自直接證據判定。

## v1.2.3 正式凍結

- 正式版完整承接 v1.2.2，以及 v1.2.3-dev-r1 的 capability routing、dev-r2 的每來源切片策略與未洩題驗證、dev-r3 的 fixture 非產品規則及 dense-text 正規化保護。
- 正式化只更新 `SKILL.md` 的目前版號戳記、漸進式揭露索引、`FROZEN.md`、本遷移紀錄、版本常數與對應回歸斷言；除 `scripts/constants.py` 的 `SKILL_VERSION` 外，runtime Python 與通過 Chain 4、Chain 5 的 dev-r3 repack 保持一致。
- `SKILL.md` 不再重複歷代版本敘述。修改、驗證、封裝、凍結或升版時才讀取本檔與 `FROZEN.md`；一般 RAG 任務只載入目前流程與契約。
- 正式發布仍須以最新 ZIP 的 SHA-256 綁定全新部署、封裝安全、版本一致性、全回歸及 packaged-artifact acceptance。該驗收不得沿用舊 ZIP 的結論。
