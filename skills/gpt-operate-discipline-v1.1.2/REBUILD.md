# gpt-operate-discipline 重建與跨產品修訂紀錄

## v1.1.2 最終批判審查與 Runtime 自適應｜2026-08-07

1. 以 `dist/gpt-operate-discipline-v1.1.1/` 的七個基線檔為唯一內容來源，並由 v1.1.1 ZIP SHA-256 `e7f74c8394d9717e435d0ea64a7c9a25f89e743cea092cefb433ad9f4985ff78` 識別其來源。
2. 保留 v1.0 八節與五題自測的凍結文字、雜湊、九項 description 觸發條件，以及 v1.1 的來源品質、引用對應、證據降級與通用計算第二路徑要求。
3. 新增 v1.1.2 最終批判審查。它只在原始 Skill 已觸發且內容屬實質分析、判斷、研究、技術、數字或決策時執行；詳細流程置於 `references/critical-review.md`。
4. 新增能力優先的 Runtime 自適應。它不假設 Web、檔案、Apps、MCP、Python、shell、repository、可寫工作區、網路、安裝、產物生成、subagents、sandbox 或 approval 可用；詳細流程置於 `references/runtime-adaptation.md`。
5. `agents/openai.yaml` 改為官方 Build skills 文件列示且必要的 `interface` 與 `policy` 欄位，不宣告 host-neutral core skill 不需要的 dependencies。
6. 所有正式文字檔採 UTF-8 無 BOM 與 LF；驗證器以嚴格解碼依序讀取 UTF-8、UTF-8 BOM 與 CP950，不忽略解碼錯誤。
7. 未封裝 ZIP，亦未宣稱任一平台已安裝、上傳掃描通過或使用者可見地觸發。

## v1.1.1 跨產品相容修訂｜2026-07-12

1. 以 `gpt-operate-discipline-v1.1.zip` 為唯一升級來源，沒有從 v1.0 覆蓋正文。
2. 保留 ChatGPT Web 已使用的 `icon` 與 `accent_color`。
3. 補上 Codex 介面使用的 `brand_color`、`default_prompt` 與 `policy.allow_implicit_invocation`。
4. 測試子程序明確以 UTF-8 解碼，避免 Windows CP950 造成假失敗。
5. 新增 metadata 回歸門；v1.1 最高優先執行補強、v1.0 八節準則與五題自測全文未改。

## v1.1 執行契約補強｜2026-07-10

1. 新增「最高優先執行補強」、來源品質、引用對應、證據降級與通用計算要求。
2. 擴充 `tests/test_discipline.py` 與新增 `tests/acceptance_cases.md`。
3. 擴充 `FROZEN.md` 以記錄 v1.1 外層執行契約。
4. v1.0 八節準則與五題自測由雜湊回歸測試守門，內容未改。

## v1.0 ChatGPT 重建｜2026-07-09

## 本次重建目的

將原始 `operate-discipline-v1.0.zip` 重建為 ChatGPT Skill 較完整的封裝格式，輸出檔名為 `gpt-operate-discipline-v1.0.zip`。

## 有改動

1. 資料夾名稱由 `operate-discipline/` 改為 `gpt-operate-discipline/`。
2. `SKILL.md` frontmatter 的 `name` 由 `operate-discipline` 改為 `gpt-operate-discipline`。
3. `SKILL.md` 標題由 `operate-discipline` 改為 `gpt-operate-discipline`。
4. `SKILL.md` 版本註記新增 ChatGPT rebuild 記錄，說明補齊 `agents/openai.yaml`，且未改八節準則與五題自測。
5. 新增 `agents/openai.yaml`，提供 ChatGPT Skill UI metadata。
6. 新增本檔 `REBUILD.md`，記錄重建範圍。

## 沒有改動

以下內容僅指 v1.0 當次 ChatGPT 重建，不是 v1.1 與 v1.1.1 的變更說明。

1. 八節準則正文沒有改。
2. 五題自測正文沒有改。
3. `description` 的觸發詞與觸發範圍沒有改。
4. `scripts/validate_punct.py` 沒有改。
5. `tests/test_discipline.py` 沒有改。
6. `FROZEN.md` 沒有改。

## 驗證

1. 已執行 `python3 scripts/validate_punct.py SKILL.md`。
2. 已執行 `python3 tests/test_discipline.py`。
3. 已檢查封裝後 zip 內只有一個 `SKILL.md`。
4. 已確認 zip 內含 `agents/openai.yaml`。
