# iTest Help → RAG Markdown 轉換清單（manifest.md）

- 產生時間：2026-07-01T04:18:16.270929
- 來源壓縮檔：help_26_2_0.zip
- 輸出根目錄：itest-help/

## 輸出結構

```
itest-help/
  manifest.md
  validation_report.md
  chunk_manifest.jsonl
  inventory.json
  index_manifest.jsonl
  text/          # 文字 RAG chunk（*.md）
  images/        # 圖片 RAG chunk（*.md）
```

## 統計
- text chunk 數量：2891
- image chunk 數量：1221
- Blocking issues：0
- Warnings：7

## Chain 執行摘要
- Chain 00：初始化任務資料夾。✅
- Chain 01：安全解壓縮（zip-slip 防護），建立 inventory.json。✅ 7004 個檔案，0 筆被阻擋。
- Chain 02：解析 toc.xml（875 節點）、contexts.xml（633 個 context）、index.xml（1900 筆 keyword→topic 對應，巢狀路徑完整保留）、cheatsheets/*.xml（15 份）。✅
- Chain 03：解析 topics/*.htm(l)、popups/*.html，共 1285 個檔案，0 筆解析失敗。✅
- Chain 04：整併 TOC／Context／Index／HTML，建立 source graph，記錄 orphan／broken 連結。✅
- Chain 05：圖片分類（decorative／inline_icon／screenshot／diagram／unknown），共 1748 張已引用圖片。✅
- Chain 06：依 TOC／heading／語意區塊切分 chunk，不跨 topic、不跨 toc_path、不跨不相關 heading_path。✅
- Chain 07：輸出 text/、images/、chunk_manifest.jsonl、index_manifest.jsonl、manifest.md、inventory.json。✅
- Chain 08：產生 validation_report.md。✅ 0 筆 blocking issue。
- Chain 09：blocking issue 為 0，無需修復輪次。✅
- Chain 10：本文件，最終交付報告。✅

## 剩餘已知問題（非 blocking，詳見 validation_report.md）
- TOC 中有 href 指向不存在檔案的項目：2 筆
- contexts.xml 中 href／anchor 無法對應到實際內容：16 筆
- index.xml 有 294 筆 keyword 的 anchor 在對應 topic 中找不到（unresolved_index_anchor），topic 層級對應仍成立，僅 anchor 層級精度受影響。
- topic 內文中 730 個內部連結指向不存在的檔案（broken_href，多為文件本身既有的失效連結，非本次轉換造成）。
- HTML 中引用但實際檔案遺失／無法解析的圖片參照：5 筆（missing_image）。
- 發現 1 組同檔案內容雜湊重複的 chunk（可能為重複段落）。
- 有 46 個 chunk 超過 6000 字元（過大 chunk），建議人工檢視是否需要再切分。

## 匯入 RAG 建議
- 本次輸出結構已將文字與圖片 chunk 分離，且每個 text chunk 皆帶有 toc_path、heading_path、breadcrumb 標題、context_ids、index_keywords 等 metadata，可直接依 chunk_manifest.jsonl 匯入向量資料庫。
- 46 個超過 6000 字元的 chunk 建議先人工抽查是否需要再拆分（多半是內容本來就很長的參考頁，例如動作參數總表），是否切分可依下游 embedding 模型的 context window 需求決定。
- 730 筆內文中的失效連結（broken_href）是原始文件本身既有的問題（例如指向已移除的 topic），建議匯入 RAG 前不需修復，但下游若要做『相關文件跳轉』功能時應過濾這批連結。
- unresolved_index_anchor（294 筆）僅影響錨點層級的精確度，topic 層級的對應仍然有效，不影響以 topic 為單位的檢索品質。
