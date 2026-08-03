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
| PDF | 原生 TikTok Fixture、掃描 PDF OCR、交換順序、錯誤 Heading、雙欄降級。 | 正向、負向與降級。 |
| DOCX | 原生 TikTok Fixture、Title 樣式、inline QR、交換順序、檔名標題降級。 | 正向、負向與降級。 |
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

## 尚未直接證明的缺口

- JPG、JPEG、HEIF、HEIC 的端到端影像處理。
- 一般非 QR、非 OCR 文字圖片的正向行為。
- 含可轉錄音訊的 MP4 正向路徑。
- 巢狀 ZIP 經完整 CLI 展開、Adapter、Chunk 與固定七類輸出的端到端路徑。
- 一般非 QR、非 OCR 文字圖片、物件與嵌入資源的完整 collection 正向路徑。
- 非 Eclipse 真實異質 collection 的長時間端到端回歸。此為後續擴大驗證，不是 v1.2.0 凍結閘門。

上述缺口在補齊直接 Fixture 與斷言前，只能標示為測試覆蓋不足，不得寫成已證明零回歸。
