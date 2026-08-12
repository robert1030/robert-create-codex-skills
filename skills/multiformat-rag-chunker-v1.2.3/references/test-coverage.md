# v1.2.1-dev-r4 回歸覆蓋矩陣

本表只描述目前自動測試實際覆蓋，不改變 `FROZEN.md` 的完整支援格式契約。沒有直接測試不等於不支援，也不等於已證明無回歸。

## v1.2.1-dev-r4 圖片語意路由

| 類別 | 回歸證據 | 覆蓋性質 |
|---|---|---|
| 通用介面版面 | `tests/test_image_semantic_contract.py` 生成結構化 UI，確認 `screen_capture`、`skipped`、空 machine payload 與無 OCR attempts。 | 可重現單元與 CLI 整合。 |
| QR decoder | 同一測試使用既有可解碼 QR fixture，確認 payload、symbology、來源 SHA-256、decoder backend 與無 OCR attempts。 | 可重現單元與 CLI 整合。 |
| 真實 iTest UI 圖片 | 工作區 `image-semantics-harness` 對獨立 r4 副本執行五張已釘選 SHA-256 的 golden。 | 實檔 release 前置，不是已封裝的 fixture。 |
| Barcode decoder | `barcode-ean13.png` 以固定 EAN-13 值驗證 payload、symbology、來源 SHA-256、decoder backend、無 OCR 與 Chunk。 | 可重現單元與 CLI 整合。 |

## v1.2.1-dev-r3 collection 關聯 occurrence 對帳

| 缺口 | 回歸證據 | 覆蓋性質 |
|---|---|---|
| XML `param[name=path]` | `test_collection_integration.py` 在同一 XML 驗證一般 `target`、有效 `param[name=path]` 與必須忽略的非 path `param`。Producer 先保存兩筆關聯，再由獨立 Validator 重算並通過 occurrence ratio。 | 正向、誤算防護與獨立驗證。 |

## v1.2.1-dev-r1 來源語意回歸

| 缺口 | 回歸證據 | 覆蓋性質 |
|---|---|---|
| Cheat Sheet XML 可見屬性 | `test_source_semantic_regression.py` 驗證 composite 標題、task group 與 11 個 task 名稱的順序與原始語意 audit。 | 正向。 |
| 非標準 HTML 清單 | 同一測試驗證 `<ul>` 下的直接 `<p>`、`<b>`、文字及 `<br>` 前後可見內容保留。 | 正向。 |
| Table Caption | 同一測試驗證 Caption 寫入 Table IR metadata 與 normalized Markdown。 | 正向。 |
| OCR 結構垃圾 | 同一測試驗證極低信心加未配對符號時拒絕，低信心本身不會拒絕正常文字。 | 正向與誤判防護。 |
| 獨立來源 Validator | 清空已輸出的 XML 語意後，`validate_collection.py` 由原始來源重新解析並拒絕。 | 負向與防繞過。 |

## v1.2.1-dev-r2 runtime-aware Harness

| 條件 | Harness 行為 | 驗收目的 |
|---|---|---|
| 無法安全證明某外部工具 lane 可用 | 對應 DOC、掃描 PDF OCR、MP4 工具 lane 測試標為 skipped，不把本機缺少工具算成技能失敗。 | 使用者不需準備本機相依。 |
| 可觀察到缺少 runtime 能力 | 維持既有 `success`／`partial_success`／`fatal_error`，在既有原因欄位加 `needs_capability`。 | 不新增平行 status。 |
| 可觀察到來源不可讀或缺少必要附檔 | 既有原因欄位加 `needs_source`，保留實際原因與嘗試紀錄。 | 不把來源問題偽稱完整擷取。 |
| 外部工具 lane 已可用 | 執行既有 DOC、OCR、MP4 實檔回歸。 | 驗證實際工具能力而非假設工具名稱。 |

Harness 不負責替所有平台安裝系統工具；執行 Agent 必須依 `FROZEN.md` 判定隔離性、權限、持久性與可回復性，安全時自行補足並重跑相應 lane。跳過只表示當次 runtime 無法證明該 lane，不能被寫成格式不支援或使用者錯誤。

## 已有直接回歸

| 格式或路徑 | 目前證據 | 覆蓋性質 |
|---|---|---|
| PDF | 原生版面 fixture、掃描 PDF OCR、交換順序、錯誤 Heading、雙欄降級。 | 正向、負向與降級。 |
| DOCX | 原生 DrawingML fixture、Title 樣式、inline QR、交換順序、檔名標題降級。 | 正向、負向與降級。 |
| DOC | Word 97 Fixture 經 LibreOffice 轉 DOCX。 | 正向及 fallback。 |
| HTML | `sample.html` 端到端。 | 正向。 |
| XML | `sample.xml` 端到端。 | 正向。 |
| CSV | `sample.csv` 端到端。 | 正向。 |
| Markdown | `sample.md` 端到端。 | 正向。 |
| PNG | QR Decoder Fixture、OCR 文字 Fixture。 | 正向。 |
| MP4 | 無音訊 Fixture 不得誤報成功。 | 負向降級。 |
| ZIP | 巢狀 ZIP、SHA-256 去重及 path traversal 拒絕。 | Intake 正向與安全負向。 |

## v1.2.0-dev-r1 已完成的 collection 骨架測試

| 類別 | 目前證據 | 覆蓋性質 |
|---|---|---|
| Generic collection 分類 | `test_collection_contract.py`。 | 正向與回退。 |
| Linked markup collection 分類 | HTML／HTM 與 XML 共存但沒有特定 profile 的集合。 | 正向。 |
| 特定 profile 選用 | 只有控制檔與明確標記同時成立時才選用 Eclipse Help profile。 | 正向與防誤判。 |
| 關聯 resolver 骨架 | 相對路徑、`help::`、`.html`／`.htm` 替代、外部 URI 與 source missing。 | 正向與降級。 |
| Collection gate 骨架 | member 對帳、critical 覆蓋、順序、關聯與未揭露失敗。 | 正向與負向。 |

上述骨架測試保留為 r1 的建立證據，不代表單獨完成 runtime 驗收。

## v1.2.0-dev-r2 已完成的 collection 接入測試

| 類別 | 目前證據 | 覆蓋性質 |
|---|---|---|
| Generic linked markup 端到端 | 目錄輸入含 HTML、HTM、XML、裸文字、相對連結與同雜湊 alias。 | 正向。 |
| Alias 保留 | 相同內容的 `.htm` alias 各自輸出來源目錄，且 collection report 記錄 canonical member。 | 正向。 |
| 關聯 occurrence | HTML 與 XML 關聯保存於 per-source report，並由獨立 Validator 以原始 DOM／XML tree 重算；涵蓋相對路徑、錨點、`.html`／`.htm` fallback、跨 bundle `help::` URI 與裸 email。 | 正向與獨立驗證。 |
| 已驗證 Eclipse Help | 根層 controls 加 Eclipse signature 時，TOC hierarchy 補入目標 topic；control 檔與視覺資產不混入正文 Chunk。 | 正向。 |
| XML resource 分類 | 無可讀文字的 XML mapping 為資源；具標題與敘述的 XML guide 保持內容來源。 | 正向與防誤排除。 |
| 長路徑輸出 ID | 兩個 slug 截斷後相同的 XML member 仍各自產生不同來源目錄。 | 正向與覆寫防護。 |
| 缺失目標 | 已記錄 `source_missing_target` 時 collection 降級為 `partial_success`，不得靜默 success。 | 負向與降級。 |
| iTest Help 26.2.0 整包 | 7,004 個 member，其中 1,301 個內容、3 個 control、5,700 個 resource；1,301 個內容來源皆成功，190 個 alias 保留。 | 完整 ZIP 端到端。 |
| iTest Help 內部復原與獨立驗證 | 14,202 個關聯 occurrence：13,769 resolved、432 external、1 source missing。五個原包內目標保存可重算 evidence；六項 collection gate 指標均通過，獨立 Validator 無 errors／warnings。 | 原始輸入重算、反竄改與正確 partial 降級。 |

## v1.2.0-dev-r3 已完成的補件骨架測試

| 類別 | 目前證據 | 覆蓋性質 |
|---|---|---|
| 多 occurrence 補件 | 同一補件 target 可精確覆蓋兩個不同原始缺失 occurrence。 | 正向。 |
| 部分補件 | 補件宣告本身可通過，但未覆蓋 edge 必須回傳。 | 降級保留。 |
| 補件篡改 | base SHA、origin SHA、未知 edge 與錯誤 target member 被拒絕。 | 負向。 |
| Relative target 推導 | 從 source member 與 relative reference 重建補件虛擬路徑。 | 正向。 |

上述測試只驗證補件宣告骨架，尚未驗證補件 bytes、Package IR 合併、Adapter、Chunk、iTest 補件實檔或最終 status 升級。

## v1.2.0 原包內部關聯復原測試

| 類別 | 必要證據 | 覆蓋性質 |
|---|---|---|
| Identical source alias | 相同 SHA-256 的來源 alias 可解析相同 raw reference，並保存 alias member 與 SHA-256。 | 正向。 |
| Unique fragment and title | 來源端明確 title 或 label 與唯一 target 文件 title、fragment 同時相符。 | 正向。 |
| Ambiguous semantic target | 多個 target 同時符合 fragment 與 title 時拒絕復原。 | 負向。 |
| Missing source-side hint | 沒有明確 title 或 label 時拒絕語意復原。 | 負向。 |
| Strict resolver precedence | 已解析、external 與非檔案 identifier 不得進入復原分支。 | 防繞過。 |
| Independent validator | Validator 必須由原始 collection 重建 evidence，刪除或交換輸出 target 時不得通過。 | 端到端與反竄改。 |

真實 iTest ZIP 已完成完整執行與獨立驗證，不以這些合成單元測試取代。

## v1.2.2-dev-r1 必要回歸

| 類別 | 必要證據 | 覆蓋性質 |
|---|---|---|
| PDF 原生視覺交接 | 合成掃描 PDF 先產生頁面工作單，再以來源與頁面 Hash 綁定的非逐字審核建立 Chunk。 | 正向端到端。 |
| 空白頁 | 原始 PDF 重算為空白的頁面必須是非必要 `skipped`，不得成為 OCR failure。 | 正向與防誤判。 |
| 主體內容 | QR 成功但同來源掃描正文未完成時必須為 `fatal_error`，且不得產生 Chunk。 | 負向防繞過。 |
| PDF 圖片 metadata | 移除 `asset_sha256` 後即使重算 manifest Hash，外部 Validator 仍須拒絕。 | 負向反竄改。 |
| Partial 授權 | `allow_partial_chunks` 缺少 `explicit_user_request` 證據時，CLI 與 Validator 必須拒絕。 | 負向權限閘門。 |
| 原始來源對照 | `validate_against_source.py` 必須由原始 PDF 重算來源 Hash、頁數、必要掃描頁、空白頁與主要 Block mapping。 | 獨立端到端。 |

上述測試已加入開發樹；實際 PASS／FAIL、退出碼與代表性掃描 PDF 結果必須由獨立驗證執行後另行回報，不能由檔案存在推定通過。

## v1.2.2-dev-r2 Dense-text 必要回歸

| 類別 | 必要證據 | 覆蓋性質 |
|---|---|---|
| Dense 工作單 | 合成掃描 PDF 以像素密度與明示 profile 產生 `dense_text` 工作單，空白頁仍獨立跳過。 | 正向與分類。 |
| 雙 Agent admission | 缺少 validation sidecar、dense 頁只有摘要、checked units 不一致、missing 非空或 mode 不適合時必須拒絕。 | 負向防繞過。 |
| Unit 完整性 | unit ID 重複、reading order 不連續、未解 uncertainty、來源或 extraction Hash 竄改時必須拒絕。 | 負向反竄改。 |
| Dense Document IR | 通過雙 sidecar 的每個單元建立獨立 `llm_visual_text` Block，非逐字、具來源頁碼、結構欄位與雙 manifest evidence。 | 正向端到端。 |
| 來源對照 | `validate_against_source.py` 由原始 PDF 重算必要掃描頁與頁面 Hash，確認多個文字 Block 可共同覆蓋同一頁。 | 獨立來源驗證。 |
| Retrieval | 綁定來源與 extraction Hash 的 golden 驗證英文 headword Recall@1、中文定義 Recall@3、例句 Recall@3、anchor 與頁碼。 | 行為驗收。 |

上述測試已加入開發樹；實際 PASS／FAIL、退出碼與代表性掃描 PDF 結果仍須由指定 Subagent 執行後回報，不得由 Main Agent 或檔案存在推定通過。

## v1.2.2-dev-r3 統一多格式語意必要回歸

| 類別 | 必要證據 | 覆蓋性質 |
|---|---|---|
| Frontmatter | 明列全部支援格式，並宣告所有格式為第一級路由；PDF 視覺與 dense-text 只能是條件式 lane。 | 觸發與範圍守門。 |
| Agent 預設提示 | 要求先 inventory、依實際格式選 Adapter、逐 member 處理混合 collection，不得從最新 patch 或 fixture 推導整支 Skill 範圍。 | 多 AI Chat／Agent 指令守門。 |
| SKILL 主流程 | 全格式標準入口位於 PDF 條件式流程之前，且明文禁止把 PDF 驗收檔擴張成產品範圍。 | 指令優先序守門。 |
| 前向測試 | 全新 Subagent 分別處理非 PDF 單檔與混合多格式來源，保存實際路由、狀態、輸出及未誤用 PDF lane 的證據。 | 無診斷洩漏的行為驗收。 |
| 零程式漂移 | dev-r3 與前次候選的 runtime Python 檔除版本常數外逐檔 Hash 相符。 | 相容性守門。 |

## v1.2.2 正式凍結證據門檻

- 開發樹全回歸必須包含既有 88 項與 dev-r3 新增語意守門；只有明示的 LibreOffice 與 Tesseract optional tool lane 可在能力不可用時標記 skipped，其餘不得失敗。
- 代表性 dense-text PDF 必須由 Extraction Agent 與不同 Validation Agent 對所有必要頁面與文字單元完成全量核對；頁數、空白頁與必要頁面只能由當次原始 PDF 重算。
- 正式輸出的 dense units、failed items、source／required／critical／dense coverage 與 retrieval cases 必須由當次來源及獨立 validation evidence 重算，不得把舊數量或舊 golden 當成新候選的預期答案。
- 正式來源樹與封裝 ZIP 必須重跑全回歸、Skill quick lane、全部 Markdown 標點及封裝內容檢查。ZIP 頂層名稱、檔案排除、解壓後測試與 SHA-256 都必須保存。

## v1.2.3-dev-r1 capability routing 必要回歸

| 類別 | 必要證據 | 覆蓋性質 |
|---|---|---|
| 原生能力可用 | 掃描 PDF 回報 `available` 時選擇 native lane、OCR admission 為 false、Tesseract attempt 為 0，缺少 review 時保留 `native_visual_review_required`。 | 正向選路與負向防誤用。 |
| 能力未知 | 缺少 handshake 時維持 `unknown`，不得改判 unavailable 或直接執行 OCR。 | 防偽能力證據。 |
| 合法 fallback | `unavailable`、`denied`、`unsupported`，以及具先前 LLM attempt 的 `failed` 才能放行 OCR。 | 正向與狀態矩陣。 |
| Validator 防繞過 | available 下偽造 OCR admission、OCR Block 移除 routing evidence、Block 與 event 不一致都必須拒絕。 | 負向反竄改。 |
| Adapter anti-bypass | 以 AST 檢查所有 Adapter 的 `ocr_image` 呼叫都明示 `admission`。 | 靜態共用閘門。 |
| 實檔與多格式 | 代表性 PDF、DOCX、既有單檔圖片、HTML screenshot、Adapter registry、ZIP 與 nested ZIP 分開回報。 | 端到端與條件式覆蓋。 |

必要 routing 與 anti-bypass case 必須全數 PASS。JPG／JPEG／HEIF／HEIC、MP4 正向與完整 nested ZIP 可依實際 fixture 標示 `NOT_DIRECTLY_TESTED`，但不得用此標示掩蓋共用 admission 缺口。

## v1.2.3-dev-r2 未洩題 source-to-output 驗收

- 本次 PDF 與 DOCX 是代表性 acceptance fixtures，不是 Skill 的服務範圍或固定答案。Producer 必須從原始檔重新建立輸出，不得重用舊 chunks、REVIEW、VALIDATION、GOLDEN、acceptance report 或先前預期數字；fixture 的檔名、頁數、章節與數量不得寫入 runtime 判斷。
- 正式切片前要分別評估 PDF 與 DOCX 的章節階層、語意單元、原子 Block、內容密度及檢索粒度。若預設 1,000 至 1,400 Token 會合併不同查詢單元，必須先向使用者提出每份來源的替代 min／max Token、overlap 與取捨。
- 全新 Validation SubAgent 的派工只能包含人類任務、兩份原檔與全新輸出路徑。Prompt 不得含預期 route、Chunk／Block／unit 數量、coverage、retrieval metrics、golden、sidecar、已知缺陷、修正說明、舊報告或 PASS 答案。
- Validator 必須由原檔獨立檢查內容遺漏、虛構、重複、順序、章節邊界、原子單元、來源定位與檢索粒度，並將可重現證據回報 Main Agent。Main Agent 不得以自身測試取代這項判定。
- 只有未洩題 source-to-output 驗證完成且 mandatory gate 全數通過，才可重新考慮正式發布。先前 dev-r1 acceptance 與 v1.2.3 release 結論不計入此閘門。
- 通用行為仍須由既有 PDF、DOCX、DOC、HTML、HTM、XML、CSV、Markdown、MP4、JPG、JPEG、PNG、HEIF、HEIC、ZIP、巢狀 ZIP 與目錄回歸共同守門；兩個代表性 fixtures 的 PASS 不得擴張成全格式或全平台實測聲明。

## v1.2.3-dev-r3 範本非產品規則必要 Gate

- Runtime scope guard 必須掃描全部 `scripts/**/*.py`，拒絕代表性 fixture 的產品文字、品牌文字、固定章節文字及固定資料列數條件。
- PDF 文章標題、數字表格章節與重建列必須由任意來源順序、前置標籤及連號結構推導；DOCX DrawingML 必須由任意標題、結構位置與表格前置文字推導，不得只驗字串不存在。
- 既有 PDF 與 DOCX binary fixture 的內容、表格、QR、閱讀順序、標題語意及負向 Validator 回歸必須維持通過；全格式回歸亦不得失敗。
- Dense `llm_visual_text` 的跨頁重複標題與同頁重複文字單元必須維持 `required: true`、`status: success`；一般原生來源的跨頁重複頁首仍必須被安全標記為 `skipped`。Coverage 與 Validator 的 dense-text 閘門維持嚴格，不得以排除錯誤取代修正 Normalizer。
- Package Validator 必須只從 dev-r3 ZIP、原始通用規格與隔離工作目錄建立驗收，不得取得人工來源、舊 acceptance、Main 筆記或預期答案。
- 人工 PDF 與 DOCX 的 Producer、dense-text Validation Agent 與最終 source-output Validator 必須使用全新目錄。最終 Validator 只能取得原檔與新輸出，並由原檔重建判準。
- 兩份人工來源的 PASS 只證明該次 fixture scope；其他格式、Linux、WSL、macOS、平台 upload／UI 與 runtime identity metadata 必須分別標示直接證據或 `UNVERIFIED`。

## v1.2.3 正式發布 Gate

- `SKILL.md` 必須只保留一條目前正式版戳記，且 `## 目的` 必須位於前 12 行。歷代版本完整保留於 `FROZEN.md` 與 `references/migration-report.md`，不得在主檔重複維護。
- `scripts/constants.py`、`SKILL.md`、`FROZEN.md`、遷移紀錄與回歸斷言必須一致標示 `1.2.3`；任何仍把目前版本標為 dev 候選的 runtime metadata 都必須拒絕。
- 除 `scripts/constants.py` 的正式版號外，runtime Python 必須與通過 Chain 4、Chain 5 的 dev-r3 repack 逐檔相符；若出現其他 runtime 差異，既有 source-to-output 證據不得直接沿用。
- 最新 ZIP 必須以新的 SHA-256 綁定全新隔離部署，並執行封裝拓撲、安全排除、技能基本驗證、全回歸與 packaged-artifact acceptance。舊 ZIP 的 PASS 不得轉移。
- 本次正式化不重新執行 PDF extraction、dense review 或 Chain 2 至 Chain 5。只有偵測到 runtime 差異、正式版 metadata smoke 失敗或 package acceptance 發現產品缺陷時，才停止發布並另行討論修正範圍。

## 尚未直接證明的缺口

- JPG、JPEG、HEIF、HEIC 的端到端影像處理。
- 一般非 QR、非 OCR 文字圖片的正向行為。
- 含可轉錄音訊的 MP4 正向路徑。
- 巢狀 ZIP 經完整 CLI 展開、Adapter、Chunk 與固定七類輸出的端到端路徑。
- 一般非 QR、非 OCR 文字圖片、物件與嵌入資源的完整 collection 正向路徑。
- 非 Eclipse 真實異質 collection 的長時間端到端回歸。此為後續擴大驗證，不是 v1.2.0 凍結閘門。

上述缺口在補齊直接 Fixture 與斷言前，只能標示為測試覆蓋不足，不得寫成已證明零回歸。
