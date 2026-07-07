# LESSONS

Lessons that can become validation checks should be added to `scripts/validate_docs_quality_gen.py`.

## 2026-07-07｜鏡像文件路徑不得寫死舊 skill 名稱
- 現象：v1.1 validator 要求舊版鏡像文件路徑，但 repo 的鏡像文件位於 `docs/docs-quality-gen-v1-2/...`。
- 根因：skill identity 與文件鏡像路徑沒有同時納入 release gate。
- 對策：v1.2 validator 改用實際 skill name 對應鏡像路徑，且鏡像文件存在時必須檢查 v1.2 token。
- 已固化：scripts/validate_docs_quality_gen.py

## 2026-07-07｜文件品質 gate 需要明確房規
- 現象：v1.1 有 Word 與同步規則，但缺少主檔可見的凍結契約、維護紀錄、三次失敗停止、驗收誠實性與 release gate。
- 根因：規則散在 workflow 與 references，未形成可維護契約。
- 對策：v1.2 新增 `FROZEN.md`、`LESSONS.md`、House Rules、Execution Priority 與 validator checks。
- 已固化：SKILL.md、FROZEN.md、scripts/validate_docs_quality_gen.py
