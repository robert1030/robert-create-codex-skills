# iTest Help 知識庫驗證摘要

## 識別資訊

- 產品：iTest Help。
- 文件版本：26.2.0。
- RAG archive：`itest-help_26.2.0-rag-v1.2.1.zip`。
- RAG SHA-256：`309BA7AACF41000C242FD0FBD1AF0B8B548F1EAB14A055284A3615DDE82BBC70`。
- Collection ID：`itest-help_26.2.0.zip-79edef31c6908df0`。
- Supporting evidence SHA-256：`4F9E65907C5958E9B5576325EE5418E589A0E21ACE33A14E735E0B41B3A6F91E`。

## 來源身份比對

原始 `itest-help_26.2.0.zip` 的 ZIP 容器 SHA-256 為 `3CA1B2A6807776080842CEC3D87E16781469E4353C6A6D0871793AE100122073`。容器雜湊和 collection ID 尾碼不同，但不是內容差異：7,004 個 source member 的路徑、存在性與逐一 member SHA-256 和 collection manifest 全數相符，缺漏、未預期 member 與內容雜湊不符均為 0。

## Validation Report 與 Validation Manifest 一致性

RAG 內的 collection report 與 supporting evidence 的獨立 `validate_collection` 結果一致：

- collection gate：`passed`。
- critical occurrence coverage：`1.0`。
- existing target resolution：`1.0`。
- member accounting：`1.0`。
- relationship occurrence accounting：`1.0`。
- source semantic coverage：`1.0`。
- source semantic critical coverage：`1.0`。
- semantic order inversions：`0`。
- 未揭露 relationship failure：`0`。
- 獨立 collection validator：零 errors、零 warnings。
- 全庫 visual retrieval smoke：通過，5 個案例均返回預期來源。
- 開發回歸：80 個測試通過，2 個因 optional OCR capability 跳過。

## 已知限制

collection gate 是通過的，但 collection 狀態為 `partial_success`，exit code 為 `2`。原始 Help 包包含 1 個 `source_missing_target`，且沒有唯一且可驗證的原包內目標。這是來源資料的已揭露限制，不是可由 skill 猜測補齊的缺口。

本 skill 可使用所有已驗證 Chunk 回答問題；遇到該未解析關聯、版本不符或知識庫沒有答案時，必須走外部官方查證或無答案降級流程。

## 來源文件本身的已知矛盾與缺口

以下是原始 iTest Help 26.2.0 內部的問題，不是切分或索引造成的。回答涉及這些主題時，必須向使用者揭露，不得逕自選一種說法當作定論。

- **Analysis Rule 的 `Extraction group number` 起算基準互相矛盾**（2026-08-09 查證）。同一個範例 `ab(c|d)fg`，`topics/arules_extractor_properties.htm` 寫 `c|d` is group number **1**，`topics/arw_extractor_selection_page.htm` 寫的卻是 group number **zero**。兩者同屬 26.2.0，不是版本差異。知識庫沒有可裁定的第三份來源，回答時應同時說明兩種寫法並要求使用者實測確認。
- **Analysis Rule Wizard 沒有記載分支路徑**（2026-08-09 查證）。`topics/add_analysis_rule_wizard.htm` 的頁面清單只列 7 個名稱，實際有 12 個 `arw_*` 頁面，`Custom Extractor page` 與 `Processor page` 都不在清單內，也沒有任何一頁記載進入條件。`Custom Extractor` 一詞在全庫 1,522 個 Chunk 中只出現 1 次，就在該頁自己的標題。因此 `Use line mode`、`Portion of matches to extract`、`Extraction group number` 這些欄位屬於哪一條分支，知識庫沒有明文，回答 wizard 操作步驟時必須把這個缺口說出來。
