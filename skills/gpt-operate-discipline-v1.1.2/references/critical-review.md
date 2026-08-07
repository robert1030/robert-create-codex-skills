# v1.1.2 最終批判審查

## 何時執行

只在本 Skill 已依 SKILL.md frontmatter `description` 觸發後，且回覆含實質分析、判斷、研究、技術、數字或決策內容時，於原本八節、五題自測、第二路徑驗證與證據分級都完成後執行。本節不建立新的觸發清單，也不取代既有程序。

## 六項核心問題

1. 主要主張是否有足夠證據支持？
2. 結論是否超出當前證據範圍？
3. 是否存在未說明的重要假設？
4. 重要名詞的定義是否前後一致？
5. 是否混淆相關關係與因果關係？
6. 是否存在資訊缺口、適用限制或可能的重要反例？

## 條件問題

**Conditional 7：** 若任務涉及修改既有 Skill、程式、流程、文件契約、架構、設定或工作成果，檢查「是否破壞原有架構、設計、工作紀錄或平台相容性？」至少涵蓋 backward compatibility、frozen contract、workflow、user-visible behavior、metadata、existing tests、platform compatibility 與 reproducibility。

**Conditional 8：** 若任務涉及多個 runtime、platform、OS、file format、API variant、configuration 或 output／rendering variant，檢查「修正是否涵蓋所有聲稱支援的變體？」不得只測最方便的變體，就宣稱整體 PASS。

**Conditional 9：** 若修改涉及 Python、PowerShell、Shell、JavaScript、executable YAML／configuration、installer、bootstrap、subprocess、file operations、external commands 或 network operations，檢查「目前與修改後的程式是否存在可達的安全風險？」至少檢查 command／shell injection、path traversal、zip-slip、symlink handling、unsafe temp files、arbitrary overwrite、unsafe deserialization、insecure download／installation、dependency risk、secrets exposure、permission escalation、untrusted input execution、destructive commands 與 encoding-induced corruption。即使舊程式本次未修改，也要檢查本次變更是否使原有風險變得可達。

沒有觸發條件的 Conditional 7、8、9 必須標記為不適用，不得把它們偽裝成已完成的無條件問題。

## 產出與分類

只記錄可驗證且會影響使用者決定的發現：

- **Major contradiction：** 結論、關鍵證據、計算、版本、適用條件或可執行行為彼此衝突，足以推翻或實質改變結論。必須停止確定性宣稱，修正、降級或請求必要資料。
- **Material limitation：** 證據、工具、權限、Runtime、測試覆蓋或適用範圍不足，會限制可信度或可執行性。必須放在結論附近並說明影響與可行下一步。
- **Minor observation：** 不改變結論的清楚度、維護性或呈現改善。不得把它升格成阻礙交付的風險。

不得表演式批評或捏造反例。不得為了顯得嚴格而挑剔無關措辭、重複既有檢查，或把純假設寫成發現。不得強迫產生反例、捏造風險、為反對而反對、對證據已充分的結論製造虛假的兩面平衡，或把 Minor observation 誇大成 blocker。若沒有 Major contradiction，必須明確寫：`未發現重大矛盾。`

正常使用者回覆不需要展示 private chain-of-thought。允許保存或呈現的是 conclusion、evidence、assumptions、contradiction、limitations、counterexamples、PASS／FAIL 與 required fixes。
