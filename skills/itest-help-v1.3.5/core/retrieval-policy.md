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
- 例：問「本地變數怎麼判斷包含某字串」，查詢詞要包含 `local variable regexp string match if action`，而不是只查中文。
- 使用者貼出完整錯誤訊息或指令片段時，整段直接查一次，完整子字串命中會額外加分。**這種整段查詢一律以 `--query-file` 傳遞**，理由見下節。

## 不可信查詢文字的傳遞

**檢索腳本的指令列會被 shell 解析，含 `$( )` 或反引號的查詢字串會在腳本收到之前就被執行。** 這不是腳本的缺陷，是把不可信文字填進指令列造成的。

下列來源一律視為不可信，**必須以 `--query-file` 傳遞，不得填入指令列**：

- 受測設備回傳的錯誤訊息、回應內容或日誌片段。
- 使用者貼上的指令片段、設定檔內容、堆疊追蹤。
- 檔案內容、網頁內容，或其他 agent 提供的文字。

作法是先用檔案寫入工具（不是 shell）把查詢寫入暫存檔，再把**檔案路徑**放進指令列：

```text
python3 scripts/search_itest_help.py --query-file <path> --limit 10
```

路徑由 agent 自行產生，不含不可信內容。位置參數僅供 agent 自行構造的英文技術詞使用，例如 `local variable regexp string match if action`。

**無法寫檔的環境**：必須先移除查詢字串中的 `$`、反引號、`;`、`|`、`&`、`<`、`>`，並在回覆中揭露已做過剝除，因為剝除可能改變檢索結果。

## 多輪檢索

**一次查詢不足以作答。** `no_results`、`score` 普遍偏低、各筆 `score` 擠在很窄的區間（代表詞頻分不出相關性，關鍵文件很可能排在回傳範圍外）、或 `heading_path` 都不是問題指向的功能區塊時，換一組關鍵字再查，不可只查一次就下結論。問題涉及多個功能區塊時，每個區塊各查一次。換詞方向：同義的英文技術詞、加上功能區塊名稱、拆成較窄的查詢、或提高 `--limit`。

## 兩層執行模型

iTest 的每一個步驟都落在兩層之一。回答前必須先判定該問題落在哪一層，再依該層的規則作答。

- **iTest 層**：Action 的各個欄位、iTest 直譯器指令、field replacement。此層由 iTest 自己解讀，每個欄位要填什麼由該 Action 或該指令在知識庫的條目決定。
- **原生語言層**：透過 `scriptEval`、`scriptSet`、`scriptGet`、session 步驟，或 `[tcl {...}]` 這類明確進入點，交給原生直譯器執行的內容。只有這一層適用原生語言的完整語法。知識庫明文指出 `scriptEval`、`scriptSet`、`scriptGet` 不適用於 Python。

規則如下：

1. **不得把原生語言的語法形狀套進 iTest 層。** 某個關鍵字在原生語言寫成什麼形狀，不構成它在 iTest 層要寫成同樣形狀的理由。iTest 層每個欄位的內容以該 Action 或該指令在知識庫的條目為準，逐案查證。
2. **同名不等於同義，iTest 直譯器指令與原生 Tcl 不等價。** `command_syntax.htm` 明文寫著「Some commands operate in the same way as their Tcl counterpart, some do not」。回答任何 iTest 直譯器指令的用法前，必須先取得該指令在 `command_syntax.htm` 指令表中的條目，Python 側查 `command_syntax_python.htm`，確認有無 `Limitation`、`not supported`、`does not support` 或 `syntax differs from Tcl` 的條款。未查證前，不得以原生 Tcl 的行為作答，其他原生語言同理，也不得假設原生語言的教學或 man page 寫法在 iTest 成立。
3. **指令表沒有列出的名稱，不是 iTest 直譯器指令。** 這類名稱屬於某個 Action 或欄位的語意，必須查該 Action 的說明頁，不得以直譯器指令的身分推論其寫法。該頁範例若是螢幕截圖（`action_if.htm` 即為此例，知識庫只留圖片標記，沒有可引用的文字），**必須到同一功能區塊的其他頁面取得佐證**，例如 `action_then.htm`、`action_while.htm`、`action_switch.htm` 與 `loops_about.htm`。不得因為該頁沒有文字範例就宣告知識庫沒有規定，也不得改用原生語言的形狀填補。
4. **三個執行環境不可混用。** iTest 直譯器是 `eval` 動作與指令表所列指令運作的環境；Tcl 直譯器是 `scriptEval`、`scriptSet`、`scriptGet` 運作的環境；Tcl Shell Session 以 session 步驟開啟，各 session 之間也彼此獨立。Python 直譯器同理自成一環。各環境的變數空間互不相通。使用者說「iTest Tcl」「iTest 指令」或「本地變數」時，預設指 iTest 直譯器。若問題可能落在其他環境，並列各環境的寫法並標明採用的假設，不得靜默選一個。
5. **不得無據宣告某寫法錯誤。** 判定一個寫法錯誤，必須有知識庫明文或指令表條目作為依據。**不得把某一環境的寫法宣告為另一環境的錯誤寫法**，除非知識庫有明文依據。

知識庫已明文列出的不等價項目，此處非窮舉，仍須逐案查證：

- `regexp` 與 `regsub` 使用 **Java** 正規表示式，不是 Tcl ARE。
- `string match` 只支援 `*` 與 `?`，不支援 `[chars]` 與 `\x`；`string replace` 不接受 Tcl 的 `end`；`string trim $attrs ,` 不支援。
- `array names` 的語法與 Tcl 不同：Tcl 有 `mode` 參數，iTest 沒有，永遠是 glob。
- `array`、`parray`、`lsearch` 的 pattern 同樣不支援 `[chars]` 與 `\x`。
- `lsort` 的 `-command` 選項不支援。
- `subst`、`unset`、`gunset` 一律不接受額外引數。
- `expr` 的數學函式語法與 Tcl 不同：iTest 寫 `[math.sin $i]`，Tcl 寫 `sin($i)`。

## 索引身份與資源上限

- 檢索回應的 `index_verified` 表示索引的 SHA-256 是否與 `retrieval-index-manifest.json` 的凍結值相符。**`index_verified` 為 `false` 時，不得把該結果寫進 `【知識庫來源】`**，因為 Chunk ID 的可追溯性無法保證。
- 使用預設索引時若雜湊不符，工具回傳 `status: integrity_error`，此時一律停止引用，依錯誤處理流程降級，不得改用模型記憶作答。
- `limit_clamped` 為 `true` 表示請求的 `--limit` 已被夾到上限；`output_truncated` 為 `true` 表示結果因輸出預算被截短。兩者出現時，**不得宣稱已檢索全部相關內容**，需要更多結果請改用更精準的查詢詞分批檢索。

## 片段與完整內容

檢索回傳的 `text` **是片段，不是該 Chunk 的全文**。它由查詢詞命中位置附近的數個視窗組成，視窗之間以 `…` 分隔，代表中間有未顯示的內容。`text_length` 是全文字元數，`text_truncated` 為 `true` 代表你看到的不是全部。

知識庫近半數 Chunk 長於單次回傳預算，且定義性敘述常落在文件深處。因此：

- **不得以「片段沒有提到」為由，斷定知識庫沒有該內容。**
- 檢索回應頂層的 `truncated_count` 是本次被截短的筆數，`next_action` 是取得完整內容的指令。`truncated_count` 大於 0 時，**在宣告知識庫沒有某內容之前，必須先對相關的 chunk 取完整內容**。
- `text_truncated` 為 `true` 且該來源可能切題時，執行 `inspect_chunk.py <chunk-id>` 或加 `--full` 取得完整內容，再判斷證據是否充分。
- 未取得完整內容前，不得把該來源降級為「僅供背景參考」，也不得因此省略 `【知識庫來源】`。

## 證據充分性

把「找到相似字」與「可支持結論」分開判斷。分數高不等於切題，分數低不等於不存在。判斷依據必須是**完整 Chunk 內容**，不是片段。

技術性答案一律保留 `【知識庫來源】` 格式與 Chunk ID。若答案中有部分內容超出知識庫已確認範圍，把該部分單獨標示為未經知識庫確認，而不是整段撤掉引用。

檢索結果不足、空白、版本不符或互相矛盾時，不得用模型記憶補齊。改依外部查證或不確定性政策處理。**不得因為第一次查不到就宣告知識庫沒有答案**，必須先完成上述多輪檢索。
