# Multiformat RAG Chunker 凍結契約

## 目錄

- v1.1.x：相容、開發與正式凍結契約。
- v1.2.0：collection 契約。
- v1.2.1：多格式與圖片語意契約。
- v1.2.2：視覺、dense-text 與統一多格式契約。
- v1.2.3：capability、切片、驗收、通用解析與正式凍結契約。
- 舊版基準。

## v1.1.0 相容契約

下列項目延續 v1.1.0，不得在 patch 或 minor 版本中破壞：

- Skill 名稱為 `multiformat-rag-chunker`。
- 支援 PDF、DOCX、DOC、HTML、HTM、XML、CSV、Markdown、MP4、JPG、JPEG、PNG、HEIF、HEIC、ZIP、巢狀 ZIP 及目錄。
- 每個來源獨立處理，ZIP 來源依 SHA-256 去重。
- 原始語言保真，不自動翻譯或簡繁轉換。
- Heading 優先切片，表格、清單、程式碼、圖片及字幕視為原子單元。
- 目標 Chunk 為 1,000 至 1,400 Token。
- 預設 overlap 為 100 Token，可調範圍為 80 至 120 Token。
- 一般模式最多三次不同策略重試。
- 預設 OCR 語言為 `chi_tra+chi_sim+eng`。
- 退出碼：`success = 0`、`fatal_error = 1`、`partial_success = 2`。
- 不依賴付費 API，不破解加密或密碼保護文件。

對應程式常數位於 `scripts/constants.py` 的 `FROZEN_CONTRACT_KEYS`，回歸測試必須直接斷言。

## v1.1.1-dev-r2 新增凍結契約

下列項目為本版新增的外部契約：

- 原始來源不得直接進入 Chunker。
- 每個 Adapter 只能輸出統一 Document IR，不得自行切片。
- 每個來源必須先產生獨立 `normalized-document.md`。
- Chunk 前必須檢查來源單元 100％對帳、必要內容至少 95％、關鍵內容 100％。
- 0／0 指標必須輸出 `null` 及 `not_applicable`。
- Chunk 後必須驗證所有合格 Block 完整映射，且沒有額外內容或原子單元破壞。
- LLM 視覺摘要必須標記為 `llm_visual_summary` 及 `verbatim: false`。
- 正式輸出只使用固定七類檔案，不把開發驗證檔污染每份使用者輸出。
- `partial_success` 預設不產生正式 Chunk，只有 `--allow-partial-chunks` 可對已驗證 Block 切片。

## v1.1.1-dev-r3 修正契約

- Chunk 的 `heading_path` 必須等於所有非 overlap `source_block_ids` 所對應 Block 的最長共同 Heading 前綴。
- Validator 必須獨立重算並驗證上述語意，不得只檢查欄位非空。
- 不存在於原始來源的合成章節標題必須使用 `derived_normalization`、`verbatim: false` 及明確 derivation metadata。
- 本版只修正共用 Chunker、Validator、衍生 Heading 標示及回歸測試，不擴張 OCR、Adapter 架構、輸出檔案或研究型指標。

## v1.1.1-dev-r4 限定修正契約

- 只對表格中的一般文字定義欄位統一連續空白及詞性分隔斜線，不修改 IPA、URL、Hash、程式碼、數學式或 combining marks。
- 使用 `drawingml_shape_parser` 時，`processing-report.json` 必須包含 `docx_drawingml_rendering_caution`。
- 本版不得修改 Chunker、Validator、Token 門檻、overlap、OCR backend、圖片閱讀順序或固定七類輸出。

## v1.1.1-dev-r5 限定修正契約

- 核心 Python 相依必須包含 `cv2` 對應的 `opencv-python-headless`。
- pip 安裝參數必須依平台、虛擬環境及 externally managed 狀態決定；Windows 與虛擬環境不得加入 `--break-system-packages`。
- 影像載入或視覺分類因核心相依缺失而失敗時，該影像單元必須列為必要失敗，整體至少降級為 `partial_success`，不得輸出完整成功。
- 本版不修改 Chunker、Validator、Token 門檻、overlap、OCR backend、圖片閱讀順序或固定七類輸出。

## v1.1.1 正式凍結契約

- 正式版完整承接 v1.1.0 相容契約，以及 dev-r2、dev-r3、dev-r4、dev-r5 的新增與修正契約。
- `scripts/constants.py` 的 `SKILL_VERSION` 固定為 `1.1.1`。
- 正式版不得就地修改。後續任何程式、契約或輸出行為變更，至少另開 v1.1.2 開發版。
- 正式交付物固定為單一 `skill.zip`，ZIP 內只能有一個 `SKILL.md`，且不得包含 `__pycache__` 或 `.pyc`。

## v1.1.2-dev-r1 開發契約

- v1.1.1 正式凍結契約保持不變，本開發版不得回寫或改名既有正式版。
- DOCX Parser 必須為合格 Block 產生可稽核且唯一的 `source_order`，並依原始容器或 DrawingML 幾何建立邏輯閱讀順序。
- DOCX 圖片及 QR Code 必須記錄 `associated_heading_block_id`、`associated_heading_path`、relationship 與關聯方法。
- Word 內建 `Title` 樣式必須成為唯一文件根標題。存在根標題時，原始 `Heading 1` 必須成為下一層章節，不得覆寫文件標題。
- Validator 必須獨立驗證閱讀順序、`source_order` metadata、圖文 Heading 關聯及文件標題語意。任一違規不得回報完整 `success`。
- `chunks.jsonl` 與 Chunk Markdown frontmatter 的 `title`、`heading_path`、`source_block_ids` 及 `content_sha256` 必須一致。
- 本版維持固定七類輸出，不修改支援格式、Token 門檻、overlap、OCR 語言、OCR backend 或退出碼。
- 本節為開發契約，尚未構成 v1.1.2 正式凍結。

## v1.1.2-dev-r2 開發契約

- 保留 v1.1.2-dev-r1 已完成的 DOCX 圖片順序、圖文關聯及 Word `Title` 語意，不得回退。
- DOC 經 LibreOffice 轉成 DOCX 後，必須沿用相同的 `source_order`、Heading 關聯及文件標題驗證。轉換失敗時不得回報完整 `success`。
- PDF 必須依頁面座標、Block 類型及 Heading cluster 建立可稽核的邏輯閱讀順序。頁首 QR Code 或 Barcode 位於正文起點之前時，必須置於文件標題及文章標題之後、第一個正文區塊之前。
- DOCX、DOC、PDF 的成功 Block 必須具有唯一整數 `source_order`。圖片必須具有 `associated_heading_block_id`、`associated_heading_path` 及關聯方法。
- Validator 不得再以 DOCX 副檔名作為唯一適用條件。來源宣告 `layout_semantics_status: reliable` 時，必須檢查閱讀順序及圖文關聯；來源宣告 `document_title_semantics_status: reliable` 時，必須檢查文件根標題。
- DOCX、DOC、PDF 必須各有實檔正向測試。PDF 必須另有交換 Block 順序及改掛錯誤 Heading 的負向測試。
- 正式回歸命令 `python -m unittest discover -s tests -v`、標點驗證及 Skill 封裝驗證必須取得退出碼 0，否則不得升為正式 v1.1.2。
- 本版不得建立通用 LLM 排版引擎，不擴張至所有 VML、頁首頁尾、跨頁浮動物件、跨欄資訊圖或未知巢狀版面。
- 固定七類輸出、支援格式、Token 門檻、overlap、OCR 語言、OCR backend 及退出碼維持不變。
- 本節仍為開發契約，全部閘門通過後才可另行凍結為正式 v1.1.2。

## v1.1.2-dev-r3 開發契約

- 保留 v1.1.1 正式凍結契約及 v1.1.2-dev-r1、dev-r2 的已完成修正，不得回退。
- DOCX、DOC、PDF 只有在 `layout_semantics_status` 與 `document_title_semantics_status` 都為 `reliable` 時，才可回報 `success`。`needs_review`、`inferred`、缺少旗標或無法可靠判定時，至少降級為 `partial_success`。
- 使用檔名建立文件根標題只能標示 `document_title_semantics_status: inferred`，不得冒充已查證的文件標題。
- 偵測到 PDF 左右欄內容在相同垂直區間重疊，且目前排序器無法可靠重建欄內閱讀順序時，必須標示 `layout_semantics_status: needs_review` 及 `pdf_multicolumn_layout_caution`。
- 對宣告可靠版面語意的來源，每個合格 Block 都必須具備唯一整數 `source_order`。全部移除、部分缺漏、重複或順序錯誤都必須由外部 Validator 拒絕。
- 成功圖片 Block 必須同時具有正確的 `associated_heading_block_id`、`associated_heading_path` 及非空 `association_method`。缺少或不一致時不得通過。
- `processing-report.json` 必須包含版面與標題語意旗標，以及四項 Chunk 後語意違規指標。外部 Validator 必須由 IR 與 Chunk 獨立重算，欄位缺少不得以預設 0 或不適用放行。
- VML 只存在於 `mc:Fallback`，且同一相容性區塊已有可解析的 DrawingML Choice 時，不因 fallback 本身自動降級。實際依賴未支援 VML、頁首頁尾圖片、跨頁浮動物件或未知巢狀群組時，仍須降級。
- 本版新增複雜跨欄 PDF、檔名推定 DOCX 標題及輸出竄改負向測試。固定七類輸出、完整支援格式、Token 門檻、overlap、OCR 語言、OCR backend 及退出碼不變。
- 本節仍為開發契約，尚未構成 v1.1.2 正式凍結。

## v1.1.2 正式凍結契約

- 正式版完整承接 v1.1.1 正式凍結契約，以及 v1.1.2-dev-r1、dev-r2、dev-r3 的新增、修正、降級與 Validator 防繞過契約。
- `scripts/constants.py` 的 `SKILL_VERSION` 固定為 `1.1.2`。
- DOCX、DOC、PDF 只有在版面與文件標題語意均為 `reliable`，且閱讀順序、`source_order`、圖片 Heading 關聯、根標題語意及四項 Chunk 後違規指標全部通過時，才可回報 `success`。
- 使用檔名推定根標題、偵測到目前無法可靠重建的複雜跨欄 PDF、實際依賴未支援 VML 或其他無法可靠判定的版面時，至少降級為 `partial_success`，不得冒充完整成功。
- 外部 Validator 必須由 Document IR、Chunk 與報告獨立重算必要條件。缺少語意旗標、`source_order`、圖片 Heading 關聯或四項 Chunk 後違規指標時，不得以預設值放行。
- 完整支援格式、固定七類輸出、目標 1,000 至 1,400 Token、預設 overlap 100 Token、三次重試、OCR 語言及退出碼契約維持不變。
- `references/test-coverage.md` 所列未直接覆蓋項目屬測試覆蓋缺口，不縮減正式支援格式，也不得被描述為已證明零回歸。
- 正式版不得就地修改。後續任何程式、契約或輸出行為變更，至少另開 v1.1.3 開發版。
- 正式交付物固定為單一 `skill.zip`，ZIP 內只能有一個 `SKILL.md`，且不得包含 `__pycache__` 或 `.pyc`。

## v1.2.0-dev-r1 collection 開發契約

- v1.1.2 正式凍結契約完整保留。不得回寫、改名或宣稱已由本開發候選修正正式版。
- collection 是多成員來源的協調層，可用於 ZIP、巢狀 ZIP 或目錄。它不以 iTest、Eclipse Help、HTML 或 XML 作為必要前提。
- generic collection inventory 必須保留每個 member 的相對路徑、來源雜湊、virtual base path、alias 關係及資源可用性。內容雜湊相同不允許抹除 alias 的相對路徑語意。
- 特定 collection profile 必須由可驗證的結構訊號選用。未命中時必須回退 generic profile，不得以單一 fixture 的路徑或檔名推定其他集合的語意。
- HTML／XML 的文字去重不得只以文字值判定。DOM 或 XML occurrence、來源位置、上下文與順序必須可稽核。
- collection relationship 必須保留原始參照、來源 member、occurrence、關聯類型、解析策略、目標、fragment 及解析狀態。來源本身缺少的目標必須標記，不能靜默忽略。
- 圖片、物件與嵌入式資源的關聯保存，與是否 OCR 或是否進入正式 Chunk 分開判定。不得因不需 OCR 而遺失來源引用。
- 本開發版的 collection 骨架尚未接入主流程，不得產生新的 runtime collection 成功宣告、固定輸出或 CLI 行為。
- collection 實作接入前，必須先完成 generic、linked markup 與可辨識 profile 的正向、負向及獨立驗證測試，並更新 migration、coverage、輸出與品質閘門文件。

## v1.2.0-dev-r2 collection 接入契約

- 保留 v1.1.2 正式凍結契約與 v1.2.0-dev-r1 的通用 collection 邊界，不得將 iTest、Eclipse Help、HTML 或 XML 寫成 collection 的必要結構。
- 僅 ZIP、巢狀 ZIP 與目錄輸入建立 collection runtime。單一檔案沿用既有 intake、Adapter、Normalizer、Chunker、Validator 與輸出流程。
- collection inventory 必須列出所有 member。內容 member 必須各自輸出既有七類檔案，control 與 resource member 必須在 collection report 內明確列為已盤點，不得因雜湊 alias、資源或控制檔而靜默消失。
- 相同內容雜湊只可作為 canonical alias 關係，不得排除 alias 內容 member 的獨立輸出，也不得改變其 virtual base path。
- 已驗證 Eclipse Help profile 的視覺二進位檔屬資源 member，內容來源必須保留關聯、章節與 OCR 判定，且此規則涵蓋 CSS 或執行期引用。generic、linked markup 或僅影像 collection 的圖片仍是直接內容來源，既有圖片格式支援不縮減。
- linked markup 與已驗證 Eclipse Help profile 的 XML 支援檔，只有在 XML 結構顯示沒有可讀文字或為生成診斷 vocabulary 時才可列為 resource；不得以 fixture 路徑、檔名或產品名稱分類。無法解析的 XML 必須保留為內容來源並使失敗可見。
- HTML／HTM 必須保留 DOM preorder 的語意 occurrence，包含原本位於 body、div、span 或 br 後的裸文字。XML 必須保留 XPath occurrence。collection 內不得再以純文字相同為由標記 `duplicate_text`。
- collection occurrence 經已辨識頁首頁尾或重複品牌標頭移除後，必須保留 `raw_text`、轉換摘要與 `normalization_only_noise` 跳過原因，並轉為非必要 `skipped` Block。不得將空白正規化結果留作必要內容。
- HTML／HTM 與 XML 的 `href`、`src`、`data` 及契約指定 XML 參照屬性，必須在每來源 report 保存 raw reference、來源、位置、類型、策略、目標、fragment 與狀態。控制檔關聯必須保留在 collection report。
- 含明確 bundle identifier 的 `help::` URI 若在本 collection 沒有對應 member，必須是 `external`，不得錯稱 `source_missing_target`。相對檔案或圖片目標不存在時仍必須明示為 `source_missing_target`。
- Eclipse Help profile 只在根層 `toc.xml`、`contexts.xml`、`index.xml` 與實際 Eclipse signature 同時成立時使用。僅該 profile 可將 TOC preorder 和階層補入目標 member 的 Heading context。
- 每個 collection 必須在輸出根目錄產生 `collection-report-<collection-id>.json`。這是 collection 層稽核檔，不取代或增加每內容來源固定七類輸出。
- `validate_collection.py INPUT OUTPUT` 必須使用原始 DOM、XML tree 與 member catalog 獨立重算 member、關聯 occurrence、source order 與 metrics。缺少 report、member、occurrence、關聯或不一致指標時退出碼必須為 1。
- collection hard gate 的六項既有指標維持不變。已宣告的 `source_missing_target` 不得靜默忽略，collection 至少為 `partial_success`；未記錄、順序錯誤、對帳不足或 gate 未通過時為 `fatal_error`。
- 本開發版不合併不同來源正文、不建立通用網站猜測器、不新增第八類每來源輸出、不調整 Token、overlap、OCR、DOCX／DOC／PDF 版面語意契約或退出碼定義。

## v1.2.0-dev-r3 補件與異質回歸契約

- 保留 v1.1.2 正式凍結契約，以及 v1.2.0-dev-r1、dev-r2 的通用 collection 與 runtime 行為。r3 不得以 iTest 的缺失目標、網站結構或單一測試資料改寫既有格式範圍。
- 補件只能宣告並覆蓋原始 collection 已記錄的 `source_missing_target` occurrence。每一筆指派必須保留 source member、raw reference、關聯型別、fragment、位置與由 relative reference 重新推導的 target member。
- 補件 manifest 必須綁定原始 collection SHA-256，且每個補件 member 必須具備自身內容 SHA-256 與來源 artifact SHA-256。未知 occurrence、重複指派、target 路徑不一致、base 不一致或 SHA-256 格式不正確時，補件驗證必須失敗。
- 一個補件 target 可覆蓋多個不同的原始 occurrence。只覆蓋部分缺失 occurrence 時，未覆蓋清單必須保留，正式 runtime 仍必須回報 `partial_success`。
- r3 的 supplement manifest validator 尚未接入 Package IR 或 CLI。它不得讀取或改寫 collection runtime，不得讓 r2 iTest collection 從 `partial_success` 升為 `success`。
- 未來補件 runtime 接入時，必須重新驗證補件 bytes、Package IR provenance、content Adapter、Chunk 前後硬閘門與獨立 collection Validator。無法取得可驗證目標時不得使用占位內容、其他版本同名檔、LLM 生成內容或網路猜測下載。
- r3 必須新增異質非 Eclipse 實檔驗收。未取得至少一個具多格式內容、資源與跨成員關聯的真實 collection 前，只能標記覆蓋缺口，不得宣稱跨 collection 零回歸或凍結本版。
- 固定七類每來源輸出、支援格式、Token 門檻、overlap、OCR 語言、DOCX／DOC／PDF 語意契約及退出碼定義均維持不變。

## v1.2.0-dev-r4 原包內部關聯復原契約

- 保留 v1.1.2 正式凍結契約，以及 v1.2.0-dev-r1 至 dev-r3 的通用 collection、runtime 與明示失敗邊界。r4 不得以 iTest 的檔名、路徑、文字或圖像特徵建立產品專屬規則。
- 正常 ZIP、巢狀 ZIP 或目錄 collection 不得要求使用者提供 `collection-supplement.json`。關聯復原只能由已收集的原始 member、member SHA-256、raw reference、fragment 與來源文件可讀到的顯式標題或標籤推導。
- 直接解析必須永遠優先。只有直接結果為 `source_missing_target` 時，才可嘗試原包內部復原；`external`、`non_file_identifier`、可直接解析與其他錯誤狀態不得進入復原分支。
- source alias 復原的必要條件是來源 member bytes 完全相同，且同一 raw reference 在 alias 的 virtual base path 可直接解析。紀錄必須保存 alias member 與 alias SHA-256。
- 語意目標復原的必要條件是 raw reference 含 fragment、來源關聯具有顯式 `title` 或 `label`，且本包恰有一個 HTML／HTM member 同時包含該 fragment 與完全相符的文件標題。紀錄必須保存 hint、target title 與 target SHA-256。
- 同檔名、模糊標題、可疑 OCR、視覺相似、另一個 collection、另一版本、網路下載、手寫 placeholder 或 LLM 生成內容均不得作為復原證據。零個或多個候選時一律保留 `source_missing_target`。
- 每筆內部復原都必須保存 raw reference、來源 member、位置、關聯型別、實際 target member、fragment、strategy 與 evidence。`validate_collection.py` 必須以原始包重建同一證據，不能只相信輸出 report。
- 已記錄但無法復原的目標仍使 collection 成為 `partial_success`。r4 不得因部分復原而把 collection 升為 `success`。
- 固定七類每來源輸出、Package IR member identity、alias virtual base path、Token 門檻、overlap、OCR、DOCX／DOC／PDF 語意契約及退出碼定義均維持不變。

## v1.2.0 正式凍結契約

- 正式版完整承接 v1.1.2 正式凍結契約，以及 v1.2.0-dev-r1、dev-r2、dev-r3、dev-r4 的通用 collection、關聯稽核與嚴格內部復原行為。
- 正常 ZIP、巢狀 ZIP 或目錄 collection 不得要求使用者提供 `collection-supplement.json`。r3 的 manifest skeleton 僅保留為歷史驗證資源，正式 runtime 不得依賴它。
- 直接解析優先。只有 `source_missing_target` 可進入內部復原，且只接受完全相同來源 alias，或唯一 fragment 加來源端完全相符 title／label 的目標。模糊名稱、OCR、視覺相似、其他版本、網路來源與 LLM 生成內容一律拒絕。
- 每筆復原必須保存 target、strategy 與 SHA-256 evidence；獨立 collection Validator 必須由原始來源重算。沒有唯一證據時，必須保留 `source_missing_target`，collection 維持 `partial_success`，不得冒充 `success`。
- iTest Help 26.2.0 原包的 6 個缺失 occurrence 中，5 個以原包可重算 evidence 復原，最後 1 個 Appium 圖片仍無可驗證 target。此為來源資料的明示缺失，不構成 runtime 未完成，也不阻礙本版凍結。
- 非 Eclipse 真實異質 collection 是未來擴大回歸範圍，並非 v1.2.0 的凍結閘門。它未被直接實檔覆蓋時，僅能標示為測試覆蓋不足，不得反向宣稱現有驗證失效。
- `scripts/constants.py` 的 `SKILL_VERSION` 固定為 `1.2.0`。正式版不得就地修改；後續任何程式、契約或輸出行為變更，至少另開 v1.2.1 開發版。
- 正式交付物固定為單一 `skill.zip`，ZIP 內只能有一個 `SKILL.md`，且不得包含 `__pycache__` 或 `.pyc`。

## v1.2.1-dev-r1 來源語意完整度修補契約

- v1.2.0 正式凍結的支援格式、固定七類每來源輸出、Token、overlap、OCR 語言、三次策略與退出碼全部保留，不得藉此版重構無關 Adapter、Chunker 或關聯復原。
- XML Adapter 必須將 `cheatsheet.title`、`compositeCheatsheet.name`、`taskGroup.name`、`task.name`、`item.title`、`subitem.label` 轉為有 XPath 的可見 Document IR Block，並保留原始 preorder。`contextId`、`param.value` 與 `serialization` 只能作為可稽核 metadata 或 relationship，不得靜默捨棄。
- HTML／HTM Adapter 必須保留 `<ul>`／`<ol>` 下非 `<li>` 的可見直接子內容，包括段落、強調文字、換行前後文字，並維持 DOM 順序。不得以產品路徑、檔名或 selector 清單做特例。
- Table Block 必須保存 `caption`、`header`、`rows` 與當下 Heading context。Caption 必須出現在 `normalized-document.md`，但非語意表格名稱不自動升格為關鍵內容。
- OCR 成功需要 backend 回傳、文字品質與結構可讀性同時成立。低信心只能作為風險訊號；只有低信心加上明顯結構垃圾等獨立證據才可拒絕，拒絕後必須繼續既有替代策略，仍失敗則以 `low_quality` 或 `failed` 留痕，不得進入正式 Chunk。
- 每個 HTML、HTM 或 XML 來源必須由獨立原始解析器比對本版涵蓋的來源語意與 Document IR、normalized Markdown。缺少關鍵 XML 程序語意必須使來源為 `fatal_error`；缺少非關鍵清單或 Caption 語意至少為 `partial_success`，不得回報 `success`。
- Collection report 與 `validate_collection.py` 必須獨立重算 `source_semantic_coverage_ratio` 與 `source_semantic_critical_coverage_ratio`。兩者非 1.0 時 collection gate 不得通過。
- 必須保留正向 XML、非標準 HTML、Caption 與 OCR 結構垃圾回歸，以及刪除輸出語意後由獨立 collection Validator 拒絕的負向回歸。
- 本節是 v1.2.1-dev-r1 開發契約。完整跨格式回歸、標點驗證、封裝驗證與實際 iTest 原包重跑全部通過前，不得宣稱 v1.2.1 正式凍結。

## v1.2.1-dev-r2 LLM-first、runtime-aware 多格式處理契約

- 本節規範所有既有支援格式的 runtime 能力選擇、驗證與誠實回報，不改變正常格式支援、Markdown 規則、Chunk 邏輯、命名、manifest 欄位、固定七類輸出或既有狀態欄位。
- 使用者只需提供來源檔與任務要求。Python、LibreOffice、FFmpeg、Tesseract、OCR、影音、轉檔與連接器是 Agent 可調用的資源，不得列為使用者手動安裝或執行的前置。
- Agent 必須依目前對話實際暴露且已授權的檔案理解、視覺、程式、轉檔、OCR、影音、已安裝工具與連接器能力選擇路徑。介面明確提供、安全且不改變使用者持久環境的測試成功，或前一步已成功完成，任一項都可作為能力可用證據。不能列舉完整工具清單不得單獨證明能力不可用。
- Agent 必須依序使用原生能力、技能包既有 scripts、references、assets、安全可自動補足的相依與等效能力。工具名稱不是成功條件；未用特定工具不代表失敗，使用特定工具也不代表可宣稱完整成功。
- Agent 必須依實際權限、隔離性、持久性與可回復性判斷是否自動補足能力，不得以 Codex、Claude Code 或其他產品名稱作為判斷捷徑。隔離 sandbox 或已確認受限且可回復的範圍可自行安裝並實測；持久或共享環境優先使用既有工具、暫存路徑、工作區隔離環境或等效能力，不得修改全域設定、移除或升級無關相依。
- 安裝、權限、網路或政策阻擋時，Agent 必須嘗試等效能力。只有所有安全可行路徑都不足，才可回報能力或來源不足；不得要求使用者自行執行技能內的同一腳本，也不得把使用者未配置本機工具視為使用者錯誤。
- `success` 表示可驗證來源範圍已完整處理，等同本節的 `complete`。有可靠部分產物但能力、權限、來源或保真度不足時維持 `partial_success`，並在既有 `partial_reasons` 記錄 `needs_capability` 或 `needs_source`。沒有可可靠交付主體內容時維持 `fatal_error`，並在既有 failure reason 記錄相同原因。不得新增平行 top-level 狀態欄位。
- 每次非 `success` 結果必須在既有 manifest 或驗證紀錄保留已完成與未完成範圍、實際使用能力、已嘗試路徑與下一個可行動作。runtime 未揭露版本、內部實作或完整能力清單時，只能記錄可觀察證據，不得編造細節。
- v1.2.1-dev-r1 的 XML 可見屬性、非標準 HTML 清單、Table Caption 與 OCR 結構垃圾規則是跨格式服務的已知回歸案例，不得被誤寫成技能只處理 XML、HTML 或 OCR 的範圍限制。
- 本節是 v1.2.1-dev-r2 開發契約。v1.2.1 正式凍結前，必須完成無使用者本機前置的 runtime-aware acceptance、可用工具 lane 的回歸、既有來源與 Chunk 對帳、標點與封裝驗證。

## v1.2.1-dev-r3 獨立 XML 關聯 occurrence 對帳契約

- 保留 v1.2.1-dev-r2 的 runtime-aware 能力階梯與所有既有格式、固定七類每來源輸出、Markdown、Chunk、命名、manifest 欄位及狀態欄位。不得將任何 runtime 相依轉嫁為使用者安裝前置。
- XML producer 已將 `<param name="path" value="…">` 記錄為 `xml_param_value` 關聯時，`validate_collection.py` 必須由原始 XML tree 獨立重算同一筆 occurrence。不得匯入或共用 Adapter 的 relationship helper。
- 只有 local name 為 `param`、`name` 精確為 `path` 且 `value` 非空時形成此關聯。其他 `param` 不得因有 `value` 而被誤算。
- 回歸必須在同一 XML 同時保有一般 attribute 關聯、有效 `param[name=path]` 與非 path `param`，並驗證 producer 關聯清單與獨立 Validator 的 occurrence ratio 都為 1.0。
- 本節是 v1.2.1-dev-r3 開發契約。完成全部回歸、標點驗證、封裝驗證及符合 runtime-aware 契約的實際來源驗收前，不得宣稱 v1.2.1 正式凍結。

## v1.2.1-dev-r4 圖片語意與 decoder provenance 契約

- 保留 v1.2.1-dev-r3 的 runtime-aware 能力階梯與所有既有格式、固定七類每來源輸出、Markdown、Chunk、命名、manifest 欄位及狀態欄位。不得將任何 runtime 相依轉嫁為使用者安裝前置。
- QR 或 Barcode 只有在實際 decoder 回傳非空 payload 時，才可建立必要且關鍵的 `qr_decoder` Block。每筆 `machine_payloads` 必須保存 kind、symbology、payload 與來源 asset SHA-256，並保存 decoder backend evidence。
- 已建立 decoder Block 的圖片不得再執行 OCR。禁止由 OCR、檔名、路徑、視覺相似、產品名稱或 LLM 猜測補造 QR／Barcode payload。
- 有足夠可重現介面版面 evidence 而沒有已驗證機器載荷或雜湊綁定原生視覺審核的獨立圖片，必須分類為 `screen_capture`，輸出既有非必要、非關鍵、`skipped`、非逐字的 `derived_normalization` Block，`skip_reason` 固定為 `no_verified_machine_payload`。該 Block 不得觸發 OCR 或進入正式 Chunk。
- 介面版面 evidence 只能是通用、可重現的圖片結構訊號，不得依 iTest 或其他產品的檔名、路徑、文案或特徵建立特例。它只決定 OCR 路由，不宣稱已讀取圖片中的文字。
- 只有具可重現 `text_block` evidence 的圖片才可進入 OCR；像素尺寸本身不得作為 OCR 或截圖判定。OCR 成功必須保存既有 quality evidence；被拒絕的 OCR 不得成為成功文字或正式 Chunk。
- 本節是 v1.2.1-dev-r4 開發契約。只有圖片 golden、decoder control、OCR、Chunk、原始來源與 release evidence 各自通過所屬閘門後，才可另行討論正式凍結。

## v1.2.1 正式凍結契約

- 正式版完整承接 v1.2.0 正式凍結契約及 v1.2.1-dev-r1、dev-r2、dev-r3、dev-r4 的來源語意、runtime-aware、XML occurrence、圖片語意與 decoder provenance 行為。
- 使用者只需提供來源與任務。持久或共享環境不得為滿足 OCR 而修改全域設定或強迫安裝 Tesseract；必須優先使用已授權能力、工作區隔離或等效路徑，並誠實保留 `needs_capability` 或 `needs_source`。
- `screen_capture` 只有在審核 sidecar 的來源 INPUT SHA-256 與個別 asset SHA-256 都精確相符、審核方法為 `native_visual_nonverbatim`、摘要非空且非逐字時，才可成為必要 `success` 的 `llm_visual_summary` Block。它不是 OCR、不是 decoder payload，且必須保存 review manifest SHA-256。
- 每個上述視覺摘要必須在不重複來源 Block 的前提下形成獨立 Chunk；未審核的 `screen_capture` 保持 `skipped` 且不得進入 Chunk 或觸發 OCR。QR／Barcode 仍只接受真實 decoder 的非空 payload，並永遠禁止後續 OCR。
- 正式 release 必須同時完成跨格式回歸、標點驗證、封裝與 SHA-256 驗證、獨立 collection Validator、原始來源 corpus 驗收、圖片 golden、decoder control、OCR control、雜湊綁定視覺摘要、全 corpus retrieval smoke 與 release evidence。不得以 schema、coverage 或單一結構測試取代任一語意閘門。
- iTest Help 26.2.0 原包仍有 1 個明示的 `source_missing_target`，因此 corpus 結果正確為 `partial_success`；1301 個可處理內容來源成功及所有 collection coverage 指標為 1.0 時，這是來源資料狀態，不是本版 runtime 未完成。
- `scripts/constants.py` 的 `SKILL_VERSION` 固定為 `1.2.1`。正式版不得就地修改；後續任何程式、契約或輸出行為變更，至少另開 v1.2.2 開發版。
- 正式交付物固定為單一 `skill.zip`，ZIP 內只能有一個 `SKILL.md`，且不得包含 `__pycache__` 或 `.pyc`。

## v1.2.2-dev-r1 PDF 原生視覺與防繞過開發契約

- v1.2.1 正式凍結版完整保留，不得回寫或改名。本開發版只存在於新的 `multiformat-rag-chunker-v1.2.2-dev-r1` 來源樹。
- 支援格式、固定七類每來源輸出、Document IR Block type、目標 1,000 至 1,400 Token、預設 overlap 100 Token、三次策略、OCR 語言及退出碼 0、1、2 全部維持不變。
- PDF 原生文字不足的頁面必須建立固定倍率的頁面 asset 與 SHA-256。Agent 已具有原生視覺能力時，必須先執行 `prepare_visual_review.py`，實際查看所有必要頁面，並以來源 INPUT SHA-256、頁面 asset SHA-256 及 `native_visual_nonverbatim` 回覆接回 Producer。
- PDF 頁面視覺回覆只能建立非逐字 `llm_visual_summary`，必須保存 `content_role: primary`、頁面 reference、來源 Hash、asset Hash 與 review manifest Hash。它不得冒充逐字 OCR、QR payload 或 Barcode payload。
- 空白 PDF 頁必須以 `blank_page`、非必要、非關鍵、`skipped` 對帳。非空白掃描頁缺少原生視覺回覆時才進入全頁 OCR；OCR 失敗必須留下 `native_visual_review_required`，不得把 Tesseract 或其他單一 backend 缺失當作處理終點。
- 掃描型 PDF 的 embedded image 仍先執行真實 QR／Barcode decoder。頁面已由全頁原生視覺或全頁 OCR 處理時，其餘 constituent image 必須以 `covered_by_full_page_processing` 跳過，避免重複正文與重複 OCR。
- 每個 PDF 圖片 Block 至少保存 `asset_id`、`visual_class`、width、height、`asset_sha256` 與 `machine_payloads`。QR／Barcode 另須保存每筆 payload 的 kind、symbology、payload、來源 asset SHA-256 與 verified decoder evidence。外部 Validator 必須實際拒絕缺欄位、Hash 不符、未驗證 decoder、`screen_capture` OCR attempts 及錯誤空白頁狀態。
- QR／Barcode 不得掩蓋未完成主要正文。只要仍有必要主要單元為 `failed` 或 `low_quality`，且沒有其他已驗證主要 Block，來源必須為 `fatal_error`，`--allow-partial-chunks` 不得覆寫。
- `--allow-partial-chunks` 只有同時提供 `--partial-authorization explicit_user_request` 時可用。Producer Agent 不得自行授權；報告缺少該證據時，Validator 必須拒絕。
- PDF 完整交付必須同時通過既有 `validate_output.py` 與新的 `validate_against_source.py INPUT.pdf OUTPUT_SOURCE_DIR --require-complete`。後者由原始 PDF 獨立重算來源 Hash、頁數、非空白掃描頁、空白頁、主要 Block 與 Chunk mapping，不得只相信 Adapter 或 processing report。
- 本節是開發契約。全回歸、標點、技能基本驗證、代表性掃描 PDF 實檔 RAG、兩個 Validator、來源對照與獨立 Subagent 報告全部取得可重現證據前，不得宣稱 `v1.2.2` 正式完成或凍結。

## v1.2.2-dev-r2 Dense-text 與 Recall 開發契約

- v1.2.1 正式凍結版與 v1.2.2-dev-r1 完整保留。本開發版只存在於新的 `multiformat-rag-chunker-v1.2.2-dev-r2` 來源樹，不得回寫、改名或覆蓋已驗證 dev-r1。
- 支援格式、固定七類每來源輸出、Document IR Block type、目標 1,000 至 1,400 Token、預設 overlap 100 Token、三次策略、OCR 語言與退出碼 0、1、2 均維持不變。
- `prepare_visual_review.py` 必須以可重算像素指標標示 dense-text candidate，並提供 `auto`、`dense_text` 與 `semantic_summary` profile。使用者要求完整單字、音標、定義、片語或例句檢索時，Agent 必須使用 `dense_text`，不得以摘要 profile 取代。
- Dense-text extraction 必須綁定來源 INPUT SHA-256 與固定倍率頁面 asset SHA-256。每頁保存唯一 `unit_id`、一基制連續 `reading_order`、`unit_type`、可檢索文字、結構欄位及空的 `uncertain_spans`。任何未解決不確定片段都不得進入成功 Block。
- Extraction Agent 不得驗證自己的輸出。不同的 Validation Agent 必須以原頁逐單元核對，並產生綁定 extraction manifest SHA-256 的 `visual-text-validation.v1`。checked unit 必須精確等於 extraction 單元；missing、unexpected、mismatched 必須皆為空，reading order 與 mode appropriate 必須通過。
- 只有 extraction 與 validation sidecar 皆通過時，PDF Adapter 才可建立必要、成功、非逐字的 `llm_visual_text` paragraph 或 heading Block。每個 Block 必須保存頁面 reference、asset SHA-256、unit ID、unit type、reading order、結構欄位，以及兩份 sidecar Hash evidence。
- `llm_visual_text` 不得標為逐字模型能力證明。它代表來源綁定、逐單元視覺轉錄且已獨立逐項核對。缺少獨立驗證、Hash 不符、單元遺漏、額外單元、內容不符、順序錯誤、未解不確定片段或 dense 頁只交摘要時，必須在 Chunk 前拒絕。
- Dense-text 頁面的 `dense_text.coverage_ratio` 必須為 1.0，且每個合格單元必須精確映射一次。`validate_against_source.py` 必須由原始 PDF 重算頁面 Hash，並接受以多個 `llm_visual_text` Block 覆蓋同一必要掃描頁。
- Dense-text RAG 驗收必須使用綁定來源與 extraction manifest Hash 的 golden。關鍵 anchor preservation、headword Recall@1、中文定義 Recall@3、例句 Recall@3 與 citation page accuracy 必須皆為 1.0。欄位存在、Chunk 數量、Schema 通過或摘要可檢索均不得替代上述驗收。
- 合成掃描 Fixture 提供可確定的機器 ground truth。真實 PDF 沒有作者提供的逐字 ground truth 時，只能宣稱已完成雙 Agent 全量視覺核對與 Recall 驗收，不得宣稱數學意義的零錯誤。
- Main Agent 只可修改程式、測試與契約並整合報告。RAG 生產、完整測試及獨立驗證必須由不同 Subagent 執行，且保留原始命令、退出碼、計數、Hash 與失敗清單。
- 本節是開發契約。紅燈防繞過、正向與負向回歸、全回歸、標點、代表性掃描 PDF 逐頁 extraction、獨立 validation、兩個輸出 Validator 與 dense retrieval gate 全部取得可重現證據前，不得宣稱 `v1.2.2` 正式完成或凍結。

## v1.2.2 前次發布候選保留紀錄

- 先前建立的 v1.2.2 來源樹與 ZIP 保留為不可變更的撤回證據，不得就地覆寫。其程式與資料契約已通過當時測試，但 `SKILL.md` 最前端版本敘述及 `agents/openai.yaml` 預設提示過度聚焦 PDF，未獲使用者接受為正式發布。
- 撤回原因屬高權重觸發與路由語意缺陷。它可能讓其他 AI Chat 或 AI Agent 忽略 v1.2.1 已凍結的統一多格式範圍，因此不能只以底層程式測試通過放行。

## v1.2.2-dev-r3 統一多格式語意修補契約

- v1.2.1 的 LLM-first、runtime-aware 多格式契約是本版主範圍。PDF、DOCX、DOC、HTML、HTM、XML、CSV、Markdown、MP4、JPG、JPEG、PNG、HEIF、HEIC、ZIP、巢狀 ZIP 及目錄全部是第一級輸入路由。
- Agent 必須先依實際輸入完成 inventory 與 Adapter 選擇，再進入共用 Document IR、Provenance、Coverage、Chunk、固定七類輸出與 Validator 契約。混合 collection 必須逐 member 路由。
- dev-r1 與 dev-r2 的 PDF 原生視覺、來源對照及 dense-text admission 只在來源與任務條件命中時啟用。最新修補、示例、測試 fixture 或 release evidence 不得重新定義 Skill 的服務範圍。
- 本開發版只可修改 frontmatter、`SKILL.md` 指令順序與標籤、`agents/openai.yaml`、凍結帳本、遷移紀錄、測試覆蓋文件及對應語意回歸測試。不得修改 Adapter、Normalizer、Chunker、Validator、Schema、支援格式、Token、overlap、OCR 語言、三次策略或退出碼行為。
- 正式發布前，除既有全回歸、標點、技能基本驗證、PDF 實檔 RAG、三個 Validator 與封裝驗證外，必須由全新 Subagent 以非 PDF 單檔與混合多格式來源執行前向測試，確認不會把 PDF 條件式 lane 套到其他格式。
- Main Agent 只負責修正與整合。測試、RAG 生產、獨立驗證及封裝後重驗必須由使用者指定的 Subagent 執行，任何必要退出碼非 0 均不得正式發布。

## v1.2.2 正式凍結契約

- 正式版必須完整承接 v1.2.1 的 LLM-first、runtime-aware 多格式能力階梯，以及 v1.2.2-dev-r1、dev-r2 的條件式 PDF 原生視覺、防繞過、dense-text 與 Recall 契約，再納入 dev-r3 的統一多格式高權重語意守門。
- 支援格式、固定七類每來源輸出、Document IR Block type、目標 1,000 至 1,400 Token、預設 overlap 100 Token、三次策略、OCR 語言與退出碼 0、1、2 全部維持不變。
- Runtime 相容性依實際暴露的檔案、視覺、程式、轉檔、OCR、影音、工具、權限、隔離性與可回復性判斷，不依 AI 產品名稱、作業系統名稱或單一 backend 推定。缺少某項能力時必須沿用既有等效能力與誠實降級契約，不得轉嫁為使用者安裝前置。
- Dense-text 是條件式新增能力。未要求完整單字、音標、定義、片語或例句檢索的來源，仍沿用既有處理路徑；要求 dense-text 時，必須取得 extraction、不同 Agent validation 與 retrieval gate，缺少任一證據不得冒充完整 corpus。
- `--allow-partial-chunks` 的明示授權是安全硬化契約。既有輸出狀態與退出碼不變，但呼叫端必須同時提供 `--partial-authorization explicit_user_request`，不得以向後相容為由恢復 Agent 自行授權。
- 正式凍結依據必須包含非 PDF 與混合多格式前向測試、全回歸、標點、技能基本驗證、代表性掃描 PDF 逐頁 extraction、獨立 validation、`validate_output.py`、`validate_against_source.py`、`validate_dense_retrieval.py`、封裝結構與 SHA-256 驗證。任何必要退出碼非 0 均不得發布。
- `scripts/constants.py` 的 `SKILL_VERSION` 固定為 `1.2.2`。正式版不得就地修改；後續任何程式、契約、輸出行為或高權重路由語意變更，至少另開 v1.2.3 開發版。
- 正式交付物固定為單一版本化 ZIP，ZIP 內只能有一個頂層 `multiformat-rag-chunker` 技能目錄與一個 `SKILL.md`，不得包含 `__pycache__`、`.pyc` 或內嵌 ZIP。

## v1.2.3-dev-r1 capability routing 開發契約

- v1.2.2 正式凍結來源樹、ZIP、固定七類輸出、Document IR Block type、目標 1,000 至 1,400 Token、預設 overlap 100、三次 OCR 策略、OCR 語言與退出碼完整保留，不得回寫或覆蓋。
- Agent 必須以 `multiformat-rag-chunker.capability-evidence.v1` 將原生 LLM multimodal 的 `available`、`unavailable`、`denied`、`unsupported` 或 `failed` 狀態交給腳本。缺少 evidence 是 `unknown`，不得視為不可用。
- 原生結構 parser 與專用 decoder 先行。需要視覺語意時，原生 LLM multimodal 優先。只有 `unavailable`、`denied`、`unsupported`，或已具 `llm_visual_attempted: true` 與失敗原因的 `failed` 才能通過共用 OCR admission。
- `scripts/ocr.py` 的 OCR 入口必須要求明示 admission。每個實際或被阻擋的視覺路由都要在既有 `processing-report.json` 保存 `native_llm_multimodal_status`、evidence、parser 與 decoder 狀態、`selected_lane`、`llm_visual_attempted`、`ocr_admitted` 與理由。
- 獨立 Validator 必須拒絕 available 能力下的 OCR、缺少 admission 的 OCR、偽造 unavailable、未實際嘗試 LLM 的 failed fallback、LLM 視覺 Block 與 routing event 不一致，以及任何 Adapter 直接繞過共用 OCR admission 的產物。
- 本節是開發契約。必要 routing、anti-bypass、全回歸、實檔 PDF 與 DOCX、封裝、隔離部署及指定自訂 SubAgent 驗收全數通過前，不得宣稱 v1.2.3 正式完成或凍結。若驗收失敗，失敗候選保持不可變更，修正必須另開 dev-r2。

## v1.2.3-dev-r2 切片策略與未洩題驗證契約

- dev-r1 候選與 SHA-256 保持不可變更。其 Validation SubAgent prompt 洩漏指定來源的預期路由、Chunk 數量、dense unit 數量、coverage、retrieval metrics 與 PASS 條件，因此該次獨立驗收及據此形成的 v1.2.3 正式發布結論全部撤回，只保留為白箱回歸與稽核證據。
- 本版固定命名為 `v1.2.3-dev-r2`，不得因 v1.2.3 曾被錯誤宣稱正式發布而跳到 v1.2.4。`scripts/constants.py` 的 `SKILL_VERSION` 必須為 `1.2.3-dev-r2`。
- 目標 1,000 至 1,400 Token 與約 100 Token overlap 保留為相容預設。Agent 在正式切片前必須依每份來源的章節、語意單元、原子 Block、內容密度與檢索情境評估其適用性；預設不合時，必須主動提出來源專屬替代值、細緻度、理由及取捨，取得使用者確認後才套用。
- Validation SubAgent 只能取得原始來源、全新輸出與人類任務要求。不得提供預期路由、數量、metrics、golden、sidecar、先前輸出、先前報告、已知缺陷、修正內容或預期結論；所有內容完整度、章節邊界、檢索粒度與來源忠實度判準都必須由原檔重建。
- 本次 PDF 與 DOCX 只作為代表性 acceptance fixtures。它們必須重新產生輸出並寫入新的 `Rag_output` 子目錄，不得重用 Main Agent 舊輸出、舊 REVIEW、VALIDATION、GOLDEN 或舊 acceptance workspace；其檔名、頁數、章節名稱、數量與內容不得進入通用 routing、Chunk、Validator 或成功條件。
- v1.2.2 的支援格式、固定七類輸出、Document IR Block type、capability routing、OCR admission、Token 預設、overlap 預設、三次策略、OCR 語言、退出碼、collection、provenance、dense-text、partial authorization、decoder、normalized Markdown 與 Chunk mapping 契約維持不變。
- dev-r2 完成未洩題的 source-to-output 驗證前，最終決定只能是 `FIX_REQUIRED`，不得宣稱 v1.2.3 正式凍結或 release。

## v1.2.3-dev-r3 範本非產品規則與通用解析契約

- dev-r2 封裝候選的 SHA-256 `28EECE4CC1D7BE41112CB826A50FE962F683B87CBE08F7E1B9914C14B2096BE7` 與獨立失敗報告保持不可變更。其 package contract gate 因 runtime adapter 固化代表性 fixture 的內容、品牌文字、固定列數與固定章節名稱而判定 `FAIL／FIX_REQUIRED`。
- 本版固定命名為 `v1.2.3-dev-r3`。`scripts/constants.py` 的 `SKILL_VERSION` 必須為 `1.2.3-dev-r3`，不得覆寫或重新封裝為 dev-r2。
- PDF 與 DOCX 的標題、章節、表格及頁首判斷必須由來源順序、版面位置、表格前置文字、連號結構與跨頁重複證據推導。不得以 fixture 檔名、產品名稱、品牌文字、固定資料列數、固定章節文字或已知輸出數量控制 runtime 行為。
- 共用 Normalizer 只可移除通用頁碼或由同一文件跨頁重算出的重複頁首。單一 fixture 的品牌清單不得成為全域噪音字典。
- 已通過獨立 admission 且標示 `dense_text_required: true` 的 `llm_visual_text` 單元，必須在正規化後維持 `required: true` 與 `status: success`。通用 repeated-header 與 duplicate-text 規則不得將其降級；一般原生頁首的跨頁重複移除行為維持不變，Coverage 與 Validator 的 dense-text 硬閘門不得放寬。
- 開發回歸必須掃描全部 runtime Python，拒絕代表性 fixture 的專屬字串與固定列數條件，同時保留 PDF、DOCX 及其他格式的既有行為驗證。
- dev-r2 的每來源切片策略對焦、未洩題 Validation SubAgent、固定七類輸出、Document IR、capability routing、OCR admission、Token 預設、overlap 預設、三次策略、OCR 語言、退出碼與多格式契約完整保留。
- dev-r3 完成全新封裝、隔離部署、package contract 驗證及未洩題 source-to-output 驗證前，最終決定只能是 `FIX_REQUIRED`。

## v1.2.3 正式凍結契約

- 正式版完整承接 v1.2.2 正式凍結契約，以及 v1.2.3-dev-r1、dev-r2、dev-r3 的 capability handshake、共用 OCR admission、逐 asset routing evidence、Validator 防繞過、每來源切片策略、未洩題獨立驗證、fixture 非產品規則與 dense `llm_visual_text` 正規化保護。
- 支援格式、固定七類每來源輸出、Document IR Block type、目標 1,000 至 1,400 Token、預設 overlap 100 Token、三次 OCR 策略、OCR 語言、collection、provenance、partial authorization、decoder、normalized Markdown、Chunk mapping 與退出碼 0、1、2 全部維持不變。
- `SKILL.md` 只保留目前正式版戳記與執行契約。歷代版本、失敗候選與遷移原因只保留在本帳本及 `references/migration-report.md`；修改、驗證、封裝、凍結或升版前必須讀取，一般 RAG 任務不得為版本沿革額外載入。
- 正式發布證據必須綁定同一個最新 ZIP SHA-256，並包含全新部署、封裝拓撲與安全檢查、版本一致性、全回歸、標點、技能基本驗證及獨立 packaged-artifact acceptance。舊 ZIP、舊 deployment 或舊 acceptance 結論不得替代。
- `scripts/constants.py` 的 `SKILL_VERSION` 固定為 `1.2.3`。正式版不得就地修改；後續任何程式、契約、輸出行為或高權重路由語意變更至少另開 v1.2.4 開發版，破壞外部契約的修改必須另開 major 版本。
- 正式交付物固定為單一版本化 ZIP。ZIP 內只能有一個頂層 `multiformat-rag-chunker` 技能目錄與一個 `SKILL.md`，不得包含 `__pycache__`、`.pyc`、`.pyo`、路徑穿越項目、符號連結或內嵌 ZIP。

## 舊版基準

開發來源樹收到的原始技能包為 v1.1.0，保存於 `legacy/v1.1.0-original.zip`；可攜技能 ZIP 依封裝器規則只保留 `legacy/README.md` 與凍結說明，不內嵌另一個 ZIP。未收到可辨識的 v1.1.1-dev，因此本包不宣稱已完成不存在版本的程式差異比對。
