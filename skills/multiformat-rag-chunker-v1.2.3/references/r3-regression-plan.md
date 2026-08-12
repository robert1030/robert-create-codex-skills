# v1.2.0-dev-r3 補件與異質 collection 歷史回歸計畫

> 本文件記錄 r3 當時尚未接入 runtime 的候選限制。r4 改以原包內可重算 evidence 完成 iTest 關聯復原後，v1.2.0 已正式凍結；非 Eclipse 真實異質 collection 保留為未來擴大回歸項目，不是本版凍結前置。

## 本版範圍

r3 是補件契約與回歸設計候選。它加入可執行的補件 manifest 驗證骨架與負向測試，但尚未將補件套用到 runtime。沒有取得 5 個具來源證據的缺失目標，也沒有取得異質非 Eclipse 實檔時，不得把 r3 寫成已修復 iTest 或已完成跨 collection 回歸。

## r2 證據基線

| 項目 | r2 查證結果 |
|---|---:|
| collection member | 7,004 |
| content source | 1,301 |
| alias | 190 |
| 關聯 occurrence | 14,202 |
| 已解析關聯 | 13,764 |
| external 關聯 | 432 |
| 已揭露缺失 occurrence | 6 |
| collection hard gate | 通過 |
| 最終狀態 | `partial_success` |

這些值由 r2 的 validation report、critical content audit 與獨立 `validate_collection.py` 交叉比對。6 個缺失不是 RAG 漏處理，而是原始 package 未包含目標 member。

## r2 發現事項防回歸登錄

| ID | r2 發現事項 | r3 保留或新增的驗證 |
|---|---|---|
| R2-01 | 雜湊去重會消除 alias 的相對路徑語意。 | 既有 alias inventory 與獨立輸出回歸必須持續通過。 |
| R2-02 | HTML body、div、span 或 br 後的裸文字會漏進 Document IR。 | 既有 generic linked markup 端到端回歸必須持續通過。 |
| R2-03 | 跨檔 href、src、data 與 XML 關係 occurrence 會遺失。 | 原始關聯重算、補件 occurrence 精確指派與負向刪 edge 測試。 |
| R2-04 | 截斷後相同的長路徑輸出 ID 會覆寫來源目錄。 | 既有長路徑 source ID 防碰撞測試必須持續通過。 |
| R2-05 | XML comment 與支援 XML 會造成解析例外或誤送入內容 Adapter。 | 既有 XML structural classification 測試與異質實檔 XML 成員對帳。 |
| R2-06 | Eclipse Help 的 CSS 或執行期視覺資產會被誤當成獨立圖片來源。 | Eclipse profile 視覺 resource 對帳回歸，加上 generic collection 圖片仍為直接來源的對照。 |
| R2-07 | 外部 Help bundle URI 會被誤標為本包缺檔。 | 跨 bundle URI、裸 email、相對缺檔三者的分類回歸。 |
| R2-08 | 頁首頁尾與非斷行空白移除後仍被保留為必要空 Block。 | collection occurrence 正規化後必須保留 raw text、跳過理由並變成非必要 Block。 |
| R2-09 | DOC 轉檔共用 LibreOffice profile 會在隔離環境失敗。 | 完整 DOC Fixture 回歸必須使用來源隔離 profile。 |
| R2-10 | 前景長時間實檔執行可能在沒有退出碼時中止。 | 實檔回歸必須保留 PID、最終退出碼、stderr、collection report 與獨立 Validator 證據。 |
| R2-11 | 原始 iTest 有 6 個缺失 relationship occurrence。 | 補件 manifest 的 SHA-256、base binding、目標路徑、六個 occurrence 與部分覆蓋降級測試。 |

## 異質非 Eclipse 實檔要求

下一個外部 fixture 必須是實際使用的 collection，而非只為測試手寫的合成目錄，且不得含 Eclipse Help 的控制檔與 signature。它至少需具備：

1. 至少 3 種內容格式，從 HTML／HTM、XML、Markdown、CSV、PDF、DOCX、PNG、MP4 中選擇。
2. 至少 1 個跨成員相對關聯、1 個資源引用與 1 個外部 URI。
3. 至少 1 個非內容資源，例如 CSS、圖片、設定檔、JS 或其他二進位 member。
4. 已知來源、授權或測試使用權、原始 ZIP 或目錄 SHA-256、完整 member catalog。
5. 用全新輸出目錄執行兩次，兩次都必須各自通過每來源 Validator 與獨立 collection Validator。

若 fixture 同時含 HTML／HTM 與 XML，預期只在證據成立時選用 `linked_markup_collection`，不得因缺少 Eclipse controls 而猜成 Eclipse profile。若 collection 沒有 linked markup，預期回退 `generic_collection`，並保留各格式既有單檔契約。

## 驗收矩陣

| 層級 | 必要測試 | 成功條件 |
|---|---|---|
| 補件宣告 | 同一 target 對應多個 occurrence。 | `topics/preferences.14.htm` 類型可覆蓋兩個原始 edge。 |
| 補件負向 | base SHA、origin SHA、未知 edge、錯誤 target、重複 edge。 | manifest validator 必須拒絕。 |
| 部分補件 | 只補其中一個缺失 target。 | 宣告有效，但未覆蓋 edge 清單保留，最終 runtime 不得升為 success。 |
| iTest 完整補件 | 5 個目標、6 個 occurrence、原始輸入與來源 artifact 均可驗證。 | 全部補件 member 通過既有格式閘門，獨立 Validator 重算為 success。 |
| 異質實檔 | 不具 Eclipse signals 的真實 collection。 | profile 不誤判、所有 member 對帳、每來源固定七類輸出、關聯 occurrence 完整。 |
| 反竄改 | 刪除輸出 relationship、交換 target、竄改補件 hash 或 member bytes。 | collection 或補件 Validator 必須以非 0 失敗。 |
| 全格式回歸 | 既有 PDF、DOCX、DOC、HTML、XML、CSV、Markdown、PNG、MP4、ZIP、巢狀 ZIP。 | 全部既有 unittest 與凍結契約通過。 |

## r3 當時的升級與凍結門檻

r3 的規劃與 skeleton 測試通過後，只能稱為「補件接入前候選」。以下兩項尚未完成前不得凍結：

1. 取得 5 個可驗證的 iTest 缺失目標，完成 iTest 補件端到端與獨立 Validator 實測。
2. 取得至少 1 個異質非 Eclipse 真實 collection，完成兩次全新輸出目錄的端到端回歸與負向竄改驗證。

這兩項均屬 r3 當時的外部輸入缺口。此歷史門檻不回溯否定 v1.2.0 的 r4 runtime 驗證；後續若擴張驗收範圍，仍不得以合成 fixture 或文字審閱替代實檔證據。
