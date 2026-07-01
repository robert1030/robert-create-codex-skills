# Validation Report

- 產生時間：2026-07-01T04:18:16.200384
- text chunks 總數：2891
- image chunks 總數：1221

## Blocking Issues
- 無

## Warnings
- ⚠️ TOC 中有 href 指向不存在檔案的項目：2 筆
- ⚠️ contexts.xml 中 href／anchor 無法對應到實際內容：16 筆
- ⚠️ index.xml 有 294 筆 keyword 的 anchor 在對應 topic 中找不到（unresolved_index_anchor），topic 層級對應仍成立，僅 anchor 層級精度受影響。
- ⚠️ topic 內文中 730 個內部連結指向不存在的檔案（broken_href，多為文件本身既有的失效連結，非本次轉換造成）。
- ⚠️ HTML 中引用但實際檔案遺失／無法解析的圖片參照：5 筆（missing_image）。
- ⚠️ 發現 1 組同檔案內容雜湊重複的 chunk（可能為重複段落）。
- ⚠️ 有 46 個 chunk 超過 6000 字元（過大 chunk），建議人工檢視是否需要再切分。

## Info
- ℹ️ 所有 topics/popups HTML 檔案解析成功，無解析失敗。
- ℹ️ TOC 對應成功的 topic 數：736
- ℹ️ 存在但未被 toc.xml 引用的 topic/popup 檔案：549 筆（多數為 popups，僅被 contexts 引用，屬正常情況）
- ℹ️ index.xml 解析完成，共 1900 筆 keyword→topic 對應，其中成功 1606 筆。
- ℹ️ index.xml 無 orphan_index_keyword（每個 keyword 節點都有 topic 或子 entry）。
- ℹ️ index_manifest.jsonl 是否存在：True
- ℹ️ 保留完整巢狀 keyword path 的紀錄數：1500 / 1900
- ℹ️ 圖片分類統計：{'screenshot': 875, 'decorative': 527, 'inline_icon': 142, 'unknown': 178, 'diagram': 26}
- ℹ️ 有 178 張圖片因無法自動判讀被標記為 unknown（未腦補內容，符合安全規則）。
- ℹ️ screenshot／diagram 圖片已執行 Tesseract OCR（英文語言包）：共 901 張，成功擷取文字 849 張、未偵測到文字 52 張、OCR 失敗 0 張。OCR 結果未經人工校對，可能有辨識誤差，尤其是低解析度或特殊符號。
- ℹ️ 表格區塊完整性檢查：0 個空表格（0 為正常）。
- ℹ️ 殘留 script/style 內容檢查：1 筆可疑殘留（0 為正常，script/style 標籤已於解析階段移除）。
- ℹ️ 所有 text chunk 均具備 source_file、source_original_path、heading_path。
- ℹ️ 沒有 toc_path 的 text chunk 數：575（原因：多為 popups/*.html，本質上不屬於 toc.xml 目錄樹，僅透過 contexts.xml 掛接，屬正常情況，非用 source_file 假冒 toc_path）。
- ℹ️ 所有 text chunk 首行標題皆為 breadcrumb 格式。
