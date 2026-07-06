# 驗證報告（全量：738 個 TOC topic 對應之 765 個 topics + 318 個 popups）

## 1. TOC / Context / Index 對應狀況

- toc.xml 解析節點數：738
- 實際 topics/*.htm 檔案數：765（含 27 個未出現在 toc.xml 的檔案，見下方 orphan 分析）
- popups/**/*.html 檔案數：318（設計上全數不在 toc.xml，只透過內文連結彈出）
- orphan topic（無 TOC 對應）總數：347，原因分布：{'no_toc_entry': 29, 'popup_not_in_toc': 318}
  - popup_not_in_toc：popups 本來就不掛在 toc.xml 下，屬於文件結構的預期特性，不是錯誤；
    已給予合成 toc_path（"Popups（來源文件無 TOC 對應，依資料夾結構歸類）"）並在 chunk 記錄的
    toc_path_synthetic 欄位標記為 True，供下游識別這不是來自 toc.xml 的真實階層。
  - no_toc_entry（29 筆）：topics/*.htm 中真的沒有被 toc.xml 引用到的檔案，
    可能是舊版殘留或僅供 popup/交叉引用使用，同樣給予合成 toc_path 並標記 toc_path_synthetic。
- broken internal href 數：491（已排除 URL 編碼、javascript: 偽協定、裸 email 造成的假陽性）
- index_manifest.jsonl 是否存在：是（1900 行）
- 巢狀 keyword path 是否保留：是（每行皆含完整 keyword_path 陣列）
- 有掛到至少一個 index keyword 的 chunk 數：187/3012
- 有掛到至少一個 context_id 的 chunk 數：663/3012

## 2. 必要欄位完整性檢查

- 檢查 chunk 數：3012
- 缺少必要欄位的 chunk：0 筆
- toc_path 根節點非 'iTest Online Help'（疑似用 source_file 假冒）：0 筆
- toc_path 來源：全部來自 toc.xml 解析結果，或（無 TOC 對應時）明確標記的合成路徑（toc_path_synthetic=True）✓
- heading_path 來源：全部來自 HTML 內 div.H1~H4 標題解析 ✓

## 3. 空 chunk / 過大 chunk

- 非預期空 chunk：0 筆
- 明確標記為 heading_only（檔案結尾懸空標題）的 chunk：1 筆（設計內允許，非缺陷）
- 過大 chunk（> 3000 字元）：45 筆（1.5%），
  皆為單一原子區塊（通常是大型術語–定義表格）本身已超過門檻，依規則不可攔腰拆開，予以保留。
- 因超過門檻而被 split_blocks_by_size 切成多 part 的 chunk 數：512

## 4. Table / Step List 完整性

- 切片策略保證：table/step_item/bullet_item/note/image/code 等原子區塊絕不被攔腰拆開，只在區塊之間切 ✓
- 含資料表格的 chunk 數：665
- 含步驟清單的 chunk 數：355
- 表格表頭語意判斷（header_row／definition_list／neutral 三類）已於範例階段驗證並修復完成 ✓

## 5. Script/Style 殘留檢查

- 解析階段已對全部 1083 個 HTML 檔案過濾 <script>/<style>，HTML 解析異常數為 0 ✓

## 6. 圖片分類與掛回檢查

- 全域相異圖片數：1802
- 分類分布：{'unknown': 307, 'screenshot': 758, 'inline_icon': 731, 'decorative': 3, 'diagram': 3}
- 已建立圖片 chunk 數（排除 decorative）：1799
- decorative 判斷已用全域引用次數統計，確認結果：
  bullet_blue_rectangle.jpg（16x16，被引用 1398 次）、bullet_blue.jpg（6x6，1205 次）、
  bullet_black_small.png（16x16，876 次）三個重複性項目符號圖示皆正確判定為 decorative，
  範例階段的樣本規模限制在全量統計下已確認自動修復 ✓
- unknown 分類（尺寸較大但 OCR 文字量低，且檔名無流程圖線索）：307 張，
  佔全域圖片 17.0%，這些圖片仍會產出 image chunk
  （因為不是 decorative），但分類欄位誠實標記為 unknown，不腦補是截圖還是示意圖，供人工抽樣覆核。
- 未發現腦補圖片內容：unknown/screenshot/diagram 分類皆有客觀依據（尺寸／OCR 文字量／檔名線索）記錄在 reason 欄位 ✓

## 7. 重複 chunk 檢查

- content_hash 重複數：16
  - 抽查確認：重複內容多半來自來源文件本身的設計性重複（例如 ui_perspective_overview.htm
    與 ui_perspective_overview_2.htm 是 toc.xml 中同一個標籤指向的兩個實體檔案，內容本來
    就完全相同），屬於原始文件結構特性，不是切片邏輯錯誤，正式匯入 RAG 前可依需求選擇
    是否要對這類完全重複的 chunk 做去重。

## 8. 結論

- Blocking issue 數：0
- 全部檢查項目通過，適合匯入 RAG 索引。
- 過大 chunk 45 筆與 unknown 圖片 307 張為已知、可接受的限制，
  已在報告中如實記錄判斷依據，不影響整體匯入可行性，但建議正式匯入前針對
  unknown 圖片與 broken_href 清單做一次人工抽樣覆核。
