# 移植對照表

本表逐項對照 `joan-skill-conventions` v1.2.1 到 `gpt-skill-conventions` v1.2.2（ChatGPT Web＋Codex 跨產品版）。狀態若非完整移植，必須同時寫明降級或替代方案。

| 編號 | 來源項目 | 新技能對應位置 | 狀態與說明 |
| --- | --- | --- | --- |
| 1 | 房規一：凍結契約，另開新版，絕不就地改定版 | `SKILL.md`，七條房規，房規一；`references/canonical-snippets.md` 第 1、2、10、11 段 | 已移植。另補 ChatGPT 版技術調整，凍結契約放技能包與回歸測試，不依賴 Claude 掛載路徑。 |
| 2 | 房規二：驗證即閘門，絕不靠肉眼 | `SKILL.md`，七條房規，房規二；`assets/validate_punct.py`；`tests/test_conventions.py` | 已移植。ChatGPT 可執行時實測；不可執行時必回報未能實測並提供降級指令。 |
| 3 | 房規三：全形標點＋禁破折號 | `SKILL.md`，七條房規，房規三；`assets/validate_punct.py` | 已移植。自身文件也套用檢查。 |
| 4 | 房規四：引擎／皮膚／內容三層正交 | `SKILL.md`，七條房規，房規四；`references/canonical-snippets.md` 第 10 段 | 已移植。長範式移到 references，主檔保留決策規則。 |
| 5 | 房規五：能力邊界誠實，降級階梯不造假 | `SKILL.md`，ChatGPT 版能力邊界與降級階梯；七條房規，房規五；`references/canonical-snippets.md` 第 5 段 | 已移植。明列 ChatGPT 工具能力不固定時的降級階梯。 |
| 6 | 房規六：透明自動安裝，離線自包含交付 | `SKILL.md`，七條房規，房規六；`assets/bootstrap.py`；`assets/manifest.json` | 已移植。腳本保留，並補充當次沙盒禁止安裝時的誠實回報。 |
| 7 | 房規七：生成前強制對焦閘門 | `SKILL.md`，七條房規，房規七；`references/canonical-snippets.md` 第 4 段 | 已移植。完整規格可視為已對焦；規格不足時必問。 |
| 8 | 模式：套用 | `SKILL.md`，三種模式 | 已移植。 |
| 9 | 模式：探索 | `SKILL.md`，三種模式 | 已移植。 |
| 10 | 模式：模仿 | `SKILL.md`，三種模式 | 已移植。 |
| 11 | 滿意度確認迴圈 | `SKILL.md`，滿意度確認迴圈 | 已移植。 |
| 12 | 多格式交付規則 | `SKILL.md`，多格式交付 | 已移植。保留 v1.2.1 的驗證推定條件與 docx 不適用聲明。 |
| 13 | 新技能開工檢查表 | `SKILL.md`，新 skill 開工檢查表 | 已移植。 |
| 14 | 交付前驗證清單 | `SKILL.md`，交付前驗證清單 | 已移植。 |
| 15 | 共用資產：驗證器 | `assets/validate_punct.py`；`SKILL.md`，共用資產與參考 | 已移植。以 ChatGPT 版修正文案中的文字破折號，保留偵測功能。 |
| 16 | 共用資產：自動安裝器 | `assets/bootstrap.py`；`SKILL.md`，共用資產與參考 | 已移植。保留分顆粒 `ensure_*` 與 log，依 Windows、Linux、PEP 668 與虛擬環境分流 pip 參數；pip、npm 或 Chromium 安裝失敗時回傳失敗並停止後續依賴流程。 |
| 17 | 共用資產：manifest | `assets/manifest.json` | 已移植。保留共用正本清單。 |
| 18 | 共用資產：同步腳本 | `scripts/sync_validator.py` | 已移植。路徑仍以技能根目錄為基準。 |
| 19 | 共用資產：回歸測試 | `tests/test_conventions.py` | 已移植。測驗新技能名稱與 ChatGPT 版資產。 |
