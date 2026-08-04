# AI Chat Web Instructions

此 adapter 適用於沒有本機檔案系統、無法解壓 ZIP、無法執行程式碼，且 Web Search 是否可用由平台決定的 AI Chat Web。

1. 只使用平台實際已配置的 iTest Help 26.2.0 知識檔案。不能讀取本機路徑時，不得聲稱已讀取 `knowledge/rag/`。
2. 先從使用者問題辨識版本、作業系統、Test Step／Session 類型與前置條件。`PS Test Step` 解釋為 `PowerShell Test Step`，除非知識檔案另有定義。
3. 先查詢已配置知識檔案，再以 Chunk ID、檔案、章節與位置判斷是否足夠支持答案。相似字詞不是答案證據。
   知識庫全文為英文，中文問題必須抽出對應的英文技術詞一起查。一次查詢不足以作答：查不到、命中的章節都不是問題指向的功能區塊，或問題涉及多個功能區塊時，換一組關鍵字再查，每個區塊各查一次。不得只查一次就宣告知識庫沒有答案。
   檢索工具回傳的內容可能只是片段，不得以片段未涵蓋為由斷定知識庫沒有該內容，也不得因此省略 `【知識庫來源】`。詳見 [../../core/retrieval-policy.md](../../core/retrieval-policy.md)
4. iTest 直譯器指令與同名的原生 Tcl 指令不等價。回答任何 iTest 指令用法前，先查該指令在 `command_syntax.htm` 指令表中的條目，確認有無 `Limitation` 或 `syntax differs from Tcl` 條款，未查證前不得以原生 Tcl 行為作答。iTest 直譯器、Tcl 直譯器與 Tcl Shell Session 是三個獨立環境，不可混用。
5. 證據足夠時，依 [../../core/response-format.md](../../core/response-format.md) 回答，並列出 `【知識庫來源】`。
6. 知識檔案不足時，只有平台實際提供 Web Search 時才查詢官方資料。沒有該能力時，明確寫出「目前執行環境無法存取外部官方資料，因此無法完成外部查證。」
7. 使用任何外部內容時，依 [../../core/external-research-policy.md](../../core/external-research-policy.md) 顯示 `【外部查證聲明】`，並區分內部與外部內容。
8. 不得以模型記憶補出未被知識檔案或外部官方來源支持的 iTest 語法。

Chat Web 的配置步驟、檔案身份與限制見：

- [knowledge-configuration.md](knowledge-configuration.md)
