# v1.2.0 原包內部關聯復原契約

## 目的

RAG collection 的正常輸入是原始 ZIP、巢狀 ZIP 或目錄，不要求使用者預先產生 `collection-supplement.json`。當 raw reference 的精確相對路徑找不到目標時，r4 只使用同一原包已存在且可重算的證據，嘗試解析已移動或重複的 member。

這不是補造檔案、重寫文件或下載內容。目標 member 必須已在目前 collection 的 Package IR 中，並保留原始 member 身分與 SHA-256。

## 解析順序

1. 先使用既有精確相對路徑、collection root、`help::` URI 與 `.htm`／`.html` 替代。
2. 只有結果為 `source_missing_target` 時，依下列兩種證據嘗試原包內部復原。
3. 任一條件不足、候選為零或候選超過一個時，保留原結果，不得降級成模糊猜測。

## 可接受證據

| Strategy | 必要條件 | 稽核 evidence |
|---|---|---|
| `equivalent_source_alias` | 來源 member 與另一 member 的 SHA-256 相同，且該 alias 的 virtual base path 可直接解析同一 raw reference。 | alias member、alias SHA-256。 |
| `semantic_fragment_title` | raw reference 含 fragment；來源元素明確提供 `title` 或 `label`；唯一 HTML／HTM member 同時含該 fragment 與完全相同的文件標題。 | hint、target title、target SHA-256。 |

標題比較只做 Unicode 空白正規化與大小寫無關比較，不採相似度、關鍵字包含、檔名近似或人工猜測。alias 解析同樣必須沿用原本的精確 resolver，不可改寫 raw reference。

## 明確拒絕

- 只有相同 basename 或副檔名。
- 多個候選具有相同 fragment 或標題。
- 只有 OCR、圖片內容、檔案大小或視覺相似。
- 其他 collection、其他產品版本、網路來源或使用者未提供的檔案。
- 以 empty file、placeholder、LLM 文字或重畫圖片填補目標。

## iTest Help 26.2.0 的實檔判讀

本節只是原包實測證據，不是 profile 規則。

| 原始 occurrence | 原包內的驗證候選 | 預期 strategy |
|---|---|---|
| `topics/popups/scriptget.html` → `../images/scriptget.jpg` | `popups/scriptget.html` bytes 相同，且 `images/scriptget.jpg` 存在。 | `equivalent_source_alias`。 |
| `topics/popups/scriptset.html` → `../images/scriptset.jpg` | `popups/scriptset.html` bytes 相同，且 `images/scriptset.jpg` 存在。 | `equivalent_source_alias`。 |
| 兩個 `preferences.14.htm#1256571` | `topics/preferences.13.htm` 的 title 為 `Preferences: Install/Update`，且含 fragment `1256571`。 | `semantic_fragment_title`。 |
| `contexts.xml` → `topics/stc_sessions_and_rest_api_mapping.htm#1420396` | `topics/stc_rest_api_commands.htm` 的 title 為 `REST API Commands`，且含 fragment `1420396`；來源 `topic` 的 label 相同。 | `semantic_fragment_title`。 |
| `popups/appium_send_to_background.html` → `../images/appium_send_to_background.png` | 原包無同名 member、無相同來源 alias 的可解析圖片，也無合格的語意目標。 | 保留 `source_missing_target`。 |

實際完整執行已將五個 occurrence 解析為原包既有 member，最後一個圖片關聯維持明示缺失。整包結果為 `partial_success`，獨立 Validator 無 errors 或 warnings，退出碼為 2；此降級只反映原始包仍不存在該圖片目標。

## 驗證

- 單元測試必須覆蓋兩種正向 strategy、候選不唯一拒絕、無顯式 hint 拒絕、非 `source_missing_target` 不進入復原，以及 strict resolver 原行為。
- collection 端到端測試必須保存每筆 evidence，獨立 Validator 必須從來源包重算同一結果。
- 真實 iTest ZIP 驗收必須使用兩個全新輸出目錄，分別跑 Chunker 與獨立 Validator。若環境缺少必要相依，必須留下安裝或缺件證據，不得把環境錯誤寫成程式結論。
