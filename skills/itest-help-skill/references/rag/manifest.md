# itest-help RAG 切片 manifest（全量版）

## 來源
help_26_2_0.zip（Spirent iTest 26.2.0 線上說明文件，7004 個檔案，已通過 zip-slip 防護安全解壓縮）

## 處理範圍
- topics/*.htm（頂層，765 個檔案，主要說明文件內容）
- popups/**/*.html（318 個檔案，含 popups/arules 子目錄，彈出式輔助說明）
- toc.xml（738 個節點，建立 TOC 邏輯階層）
- contexts.xml（633 個 context）
- index.xml（1672 筆巢狀 keyword，保留完整 keyword_path）
- cheatsheets/*.xml（15 份，全數解析成功）

不含：topics/Formats、topics/Reports、topics/Logs、topics/META-INF、topics/css、
topics/scripts、topics/images、topics/Files、topics/popups（與頂層 popups 重複的build產物）
等範本／資源子目錄，以及 .class／.vbs／.asp／.js 等已安全解壓但不執行的危險副檔名檔案。

## 產出檔案
- inventory.json：全 ZIP 安全解壓縮清冊（7004 個檔案，跳過 9 個危險副檔名項目，皆已記錄）
- index_manifest.jsonl：index.xml 巢狀 keyword → topic/anchor 對應（1900 行，保留完整 keyword_path）
- chunk_manifest.jsonl：3012 個文字 chunk 的完整中繼資料
  （source_file / source_original_path / toc_path / heading_path / breadcrumb / anchor /
    context_ids / index_keywords / index_keyword_paths / related_links / images /
    has_table / has_step_list / content_hash / char_count / chunk_part / chunk_total_parts /
    is_heading_only / is_popup / toc_path_synthetic）
- text/*.md：3012 個文字 chunk（breadcrumb 標題格式：# Top Level > ... > Current Heading）
- images/*.md：1799 個圖片 chunk（已排除 3 個 decorative 重複性項目符號圖示）
- validation_report.md：完整驗證報告（Blocking issue 數：0）

## 已知限制（詳見 validation_report.md）
- 45 個過大 chunk（單一術語–定義表格本身超過門檻，依規則不可攔腰拆開）
- 307 張圖片分類為 unknown（尺寸較大但 OCR 文字量低，不腦補是截圖還是示意圖，供人工抽樣覆核）
- 491 筆 broken internal href（來源文件本身的失效連結，已排除 URL 編碼等假陽性）
- 16 個 chunk 內容完全重複（來源文件本身的設計性重複頁面，例如 toc.xml 中同一標籤指向兩個實體檔案）
- popups（318 個）與 29 個 topics 沒有 toc.xml 對應，已給予合成 toc_path 並標記 toc_path_synthetic=True

## 匯入建議
Blocking issue 為 0，適合直接匯入 RAG 索引。建議匯入前：
1. 抽樣覆核 unknown 分類圖片（images/ 目錄中 classification: unknown 的項目）
2. 視需求決定是否對 16 個內容完全重複的 chunk 做去重
3. 參考 broken_href 清單，評估是否需要修正來源文件
