# Collection 處理契約

## 定位

Collection 是多成員來源的關係協調層，適用於 ZIP、巢狀 ZIP 與目錄。它不把任何單一 HTML、XML、網站產生器或資料夾命名視為通用前提。

單一來源 Adapter、Document IR、必要內容補強、標準化 Markdown、雙完整度閘門、共用 Chunker、固定七類每來源輸出、Token、overlap、OCR、失敗政策及退出碼契約保持有效。Collection 只能補入可驗證的跨成員語意，不能取代或扁平化既有流程。

## Profile 選用

1. 一律先建立 generic collection inventory。
2. 只有 HTML／HTM 或 XML 成員並存時，可選用 linked markup profile。
3. 特定 profile 必須同時符合多個結構訊號與內容標記。檔名、資料夾名或單一 fixture 特徵不足以推定 profile。
4. 未命中特定 profile、訊號互相矛盾或控制檔無法可靠解析時，回退 generic collection profile，並留下 `needs_review` 或失敗紀錄。

Eclipse Help 只是一種可辨識 profile。它可使用 TOC、Context、Index、Cheatsheet 與 `help::` URI，但不得被寫成所有 HTML／XML collection 的模型。

## Package IR

每個 collection 必須先建立以下可稽核資料：

- collection ID、原始上傳名稱、整包 SHA-256 與 derivation chain。
- 每個 member 的相對路徑、媒體類型、來源 SHA-256、virtual base path 及存在狀態。
- 內容相同 alias 的 member ID、canonical member 與各自的 virtual base path。
- 控制文件、正文文件、資源、外部 URI 與未支援成員的分類。

內容雜湊去重只能共用解析工作，不得消除 alias 的 member 身分或改變相對連結的解析基準。

## 語意與順序

HTML 與 XML 必須依原始樹狀 preorder 產生 occurrence。每個可保留語意單元至少記錄 source member、DOM 或 XML path、occurrence index、source order、heading context 與正規化前後文字雜湊。

不得只因文字內容相同，就把不同 occurrence 標成 `duplicate_text`。重複內容由語意樹的正確建模避免重複產生，不由事後刪除有意義的位置。

控制文件提供的章節階層必須保留來源控制檔、preorder、sibling index、depth、父節點與目標 member。不得將路徑字典排序當成章節順序。

## 關聯

每個關聯 occurrence 都必須保存 raw reference、來源 member、位置、關聯類型、解析策略、目標 member、fragment 及狀態。

至少涵蓋 HTML／HTM 的 `href`、`src`、`data`、嵌入資源、圖片、XML target attribute、Context、Index、Cheatsheet 參照與 profile 特有 URI。

圖片關聯與圖片文字處理分開判定。Logo、裝飾圖、純照片及不需 OCR 的圖片仍必須保留引用、目標、章節與跳過原因。來源自身不存在的目標必須標為 `source_missing_target`，不得靜默遺失。

含明確 bundle identifier 的 `help::` URI 若不在本 collection 中，必須列為 `external` 與 `help_external_bundle`，不得錯稱本來源缺檔。沒有 bundle identifier 的本地參照，以及相對檔案或圖片目標不存在時，仍必須是 `source_missing_target`。裸 email 同樣屬外部關聯。

## Collection 硬閘門

只有下列條件全部成立，collection 才可宣稱完整成功：

- `member_accounting_ratio = 1.0`。
- `critical_occurrence_coverage_ratio = 1.0`。
- `source_semantic_coverage_ratio = 1.0`。
- `source_semantic_critical_coverage_ratio = 1.0`。
- `semantic_order_inversion_count = 0`。
- `relationship_occurrence_accounting_ratio = 1.0`。
- `existing_target_resolution_ratio = 1.0`。
- `unreported_relationship_failure_count = 0`。

外部 Validator 必須從原始 DOM、XML 與 resource catalog 重新計算上述指標。不得只驗證 Adapter 已接受的 Block，也不得用缺少欄位的預設值放行。

## v1.2.0-dev-r1 邊界

v1.2.0-dev-r1 只建立資料模型、profile 選用、關聯 resolver 及閘門的可測骨架，未接入 CLI、Adapter、Normalizer、Chunker、輸出器或正式 Validator。此節保留為版本界線，不得把 r2 的 runtime 行為回寫成 r1 已完成事項。

## v1.2.0-dev-r2 接入範圍

- ZIP、巢狀 ZIP 與目錄先建立 Package IR。單檔不啟用 collection runtime，沿用既有處理路徑。
- Package IR 列出所有檔案 member。內容 member 產生既有七類每來源輸出；control 與 resource member 在 collection report 中列為 `catalogued`。
- 同雜湊 alias 仍是獨立 member，保留自身 virtual base path，並各自產生來源輸出。r2 不以 cache 共用為理由隱藏 alias。
- 已驗證 Eclipse Help profile 的 JPG、JPEG、PNG、HEIF、HEIC 是資源 member，由內容來源保留關聯、章節、OCR 判定與跳過原因；此規則涵蓋 CSS 或執行期引用而不只 HTML `src`。generic 與 linked markup profile 的圖片仍是直接內容來源，完整保留既有圖片支援。
- linked markup 與已驗證 Eclipse Help profile 中，沒有可讀文字節點的 XML 支援檔、具生成診斷 vocabulary 的報告檔，以及由 root element 或 namespace 可辨識的 catalog、config、locale、manifest、map、MIME、plugin、schema、settings、style 或 stylesheet 支援資料，必須 catalogued 為 resource。判斷只能依 XML 結構與內容，不能依 iTest 路徑或檔名；無法解析的 XML 保持內容來源，使失敗可見。
- HTML／HTM Adapter 依 DOM preorder 保留 heading、段落、清單、表格、程式碼、圖片及裸文字 occurrence。XML Adapter 依 XPath 保留語意 occurrence。collection 內不以純文字相同去重。
- collection occurrence 的已辨識頁首頁尾或重複品牌標頭若被正規化移除，必須留在 Document IR 供來源對帳，保存 `raw_text`、移除摘要與 `normalization_only_noise`，並成為非必要 `skipped` Block。不得讓空白正規化結果阻擋 Chunk 完整度閘門。
- HTML／HTM 的 `href`、`src`、`data` 與 XML 的 `href`、`src`、`data`、`target`、`link`、`url`、`uri`、`topic`、`context`、`file` 必須紀錄每個 occurrence。單純 identifier 以 `non_file_identifier` 記錄，不得冒充檔案遺失。
- 已驗證 Eclipse Help profile 才可解析根層 TOC，並以 preorder、sibling index、depth 與 heading path 補入目標 topic。generic 與 linked markup profile 不推定文件階層。
- 輸出根目錄產生 `collection-report-<collection-id>.json`。它保存 Package IR、profile、TOC occurrence、control relationship、關聯摘要、八項 metrics、來源語意摘要、gate 及 collection status；每來源的完整 relation records 留在既有 `processing-report.json`。
- `python scripts/validate_collection.py INPUT OUTPUT --json` 必須使用與 Adapter 不同的 HTML parser 及 XML tree 重新盤點原始關聯、member identity、source order、來源語意與 gate metrics。它不得將 report 缺欄位視為通過。
- 所有八項 gate 指標通過，且內容來源均成功時，collection 才為 `success`。已記錄 `source_missing_target` 時為 `partial_success`；遺漏 occurrence、member、來源語意、順序、指標或 gate 失敗時為 `fatal_error`。

## v1.2.0-dev-r3 補件邊界

補件是保留原始 collection 與失效 edge 的附加來源，不是將缺失內容寫入原始 package。每個補件必須有原始 collection、來源 artifact 與補件 member 的 SHA-256，並精確指派到既有 `source_missing_target` occurrence。詳細 schema、iTest 的 5 個 target、6 個 occurrence 與未來 runtime gate 見 `references/supplement-contract.md`。

r3 只提供 manifest validator skeleton，尚未把補件加到 Package IR、CLI 或獨立 Validator。因此補件宣告通過不能改變目前 collection status。異質非 Eclipse collection 的實檔驗收要求與 r2 問題防回歸登錄見 `references/r3-regression-plan.md`。

## v1.2.0-dev-r4 原包內部關聯復原

r4 不把 `collection-supplement.json` 當成正常 RAG collection 的輸入。直接解析失敗時，只能以同一 Package IR 的 member、SHA-256、fragment 與來源端明確的 title 或 label 復原既有目標。可接受的條件、evidence 欄位、拒絕規則與 iTest 實檔判讀見 `references/r4-internal-resolution-contract.md`。

復原不建立虛構 member，也不改寫 raw reference。collection report 必須保存實際 target member 與 strategy，獨立 Validator 必須由原始 ZIP 或目錄重算相同結果。無法以唯一證據復原的 edge 繼續是 `source_missing_target`。

## v1.2.0 正式範圍

v1.2.0 凍結上述 collection runtime。r3 的補件與異質 collection 計畫是當時的候選範圍記錄，不得被解讀成正常 collection 必須有使用者 manifest，也不得將未提供的異質實檔變成本版凍結前置。未直接覆蓋的格式組合只記錄於測試覆蓋矩陣；它們不否定本版對既有單檔格式、generic linked markup fixture 與 iTest Help 26.2.0 原包的已完成驗證。
