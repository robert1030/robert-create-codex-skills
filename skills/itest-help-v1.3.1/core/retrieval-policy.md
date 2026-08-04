# 檢索政策

來源優先順序固定如下：

1. 使用者版本完全相符的已驗證知識庫。
2. 相同 Major／Minor 的已驗證知識庫。
3. 知識庫明確標示為跨版本適用的內容。
4. iTest 官方外部文件。
5. 官方產品整合文件。

AI Agent 有本地資源時，使用 `scripts/search_itest_help.py` 搜尋 `knowledge/retrieval-index.jsonl`，再用 Chunk ID 與來源位置檢查原始記錄。AI Chat Web 只搜尋平台已配置的 `chat-web-knowledge.md`。

## 查詢構詞

**知識庫全文為英文，中文查詢詞對它無效。** 檢索採詞頻計分，連續中文會被切成整串 token，在英文來源中永遠不命中。因此中文問題必須抽出對應的英文技術詞一起查，不可只用中文查詢。

- 抽出指令名、動作名、屬性名、精靈名稱、錯誤訊息片段等英文技術詞。
- 例：使用者問「iTest 怎麼設定正則表達式擷取」，查詢詞要包含 `regular expression extractor analysis rule`，而不是只查中文。
- 例：使用者問「本地變數怎麼判斷包含某字串」，查詢詞要包含 `local variable regexp string match if action`。
- 使用者貼出完整錯誤訊息或指令片段時，整段直接查一次，完整子字串命中會額外加分。

## 多輪檢索

**一次查詢不足以作答。** 出現下列任一情況時，必須換一組關鍵字再查，不可只查一次就下結論：

- `status` 為 `no_results`。
- 回傳結果的 `score` 普遍偏低。
- 各筆 `score` 擠在很窄的區間內，代表詞頻無法分辨相關性高低，關鍵文件很可能排在回傳範圍之外。
- 已回傳的 `heading_path` 都不是問題真正指向的功能區塊。
- 問題涉及多個功能區塊時，每個區塊各查一次，不要期待單一查詢同時涵蓋。

換關鍵字的方向：改用同義的英文技術詞、加上功能區塊名稱、拆成多個較窄的查詢、或提高 `--limit`。

## iTest 直譯器指令與原生 Tcl 不等價

`command_syntax.htm` 明文寫著「Some commands operate in the same way as their Tcl counterpart, some do not」。iTest 直譯器有自己的指令集，同名指令的行為、支援的選項與語法都可能與原生 Tcl 不同。

**回答任何 iTest 直譯器指令的用法前，必須先取得該指令在 `command_syntax.htm` 指令表中的條目**，確認有無 `Limitation`、`not supported`、`does not support` 或 `syntax differs from Tcl` 的條款。未查證前，不得以原生 Tcl 的行為作答，也不得假設 Tcl 教學或 man page 的寫法在 iTest 成立。

知識庫已明文列出的不等價項目，此處非窮舉，仍須逐案查證：

- `regexp` 與 `regsub` 使用 **Java** 正規表示式，不是 Tcl ARE。
- `string match` 只支援 `*` 與 `?`，不支援 `[chars]` 與 `\x`；`string replace` 不接受 Tcl 的 `end`；`string trim $attrs ,` 不支援。
- `array names` 的語法與 Tcl 不同：Tcl 有 `mode` 參數，iTest 沒有，永遠是 glob。
- `array`、`parray`、`lsearch` 的 pattern 同樣不支援 `[chars]` 與 `\x`。
- `lsort` 的 `-command` 選項不支援。
- `subst`、`unset`、`gunset` 一律不接受額外引數。
- `expr` 的數學函式語法與 Tcl 不同：iTest 寫 `[math.sin $i]`，Tcl 寫 `sin($i)`。

## 三個執行環境不可混用

- **iTest 直譯器**：`eval` 動作與 iTest 指令表所列指令運作的環境。
- **Tcl 直譯器**：`scriptEval`、`scriptSet`、`scriptGet` 運作的環境，變數與 iTest 直譯器完全獨立。
- **Tcl Shell Session**：以 session 步驟開啟，各 session 之間變數也彼此獨立。

使用者說「iTest Tcl」「iTest 指令」或「本地變數」時，預設指 iTest 直譯器。若問題可能落在其他環境，並列各環境的寫法並標明採用的假設，不得靜默選一個。**不得把某一環境的寫法宣告為另一環境的錯誤寫法**，除非知識庫有明文依據。

## 片段與完整內容

檢索回傳的 `text` **是片段，不是該 Chunk 的全文**。它由查詢詞命中位置附近的數個視窗組成，視窗之間以 `…` 分隔，代表中間有未顯示的內容。`text_length` 是全文字元數，`text_truncated` 為 `true` 代表你看到的不是全部。

知識庫近半數 Chunk 長於單次回傳預算，且定義性敘述常落在文件深處。因此：

- **不得以「片段沒有提到」為由，斷定知識庫沒有該內容。**
- `text_truncated` 為 `true` 且該來源可能切題時，執行 `inspect_chunk.py <chunk-id>` 或加 `--full` 取得完整內容，再判斷證據是否充分。
- 未取得完整內容前，不得把該來源降級為「僅供背景參考」，也不得因此省略 `【知識庫來源】`。

## 證據充分性

把「找到相似字」與「可支持結論」分開判斷。分數高不等於切題，分數低不等於不存在。判斷依據必須是**完整 Chunk 內容**，不是片段。

技術性答案一律保留 `【知識庫來源】` 格式與 Chunk ID。若答案中有部分內容超出知識庫已確認範圍，把該部分單獨標示為未經知識庫確認，而不是整段撤掉引用。

檢索結果不足、空白、版本不符或互相矛盾時，不得用模型記憶補齊。改依外部查證或不確定性政策處理。**不得因為第一次查不到就宣告知識庫沒有答案**，必須先完成上述多輪檢索。
