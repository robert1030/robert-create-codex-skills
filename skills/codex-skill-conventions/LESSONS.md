# LESSONS

Format and compaction rules are defined in `references/maintenance-protocol.md`. Lessons that can be converted into tests should become tests.

## 2026-07-07｜v1.6.1-codex 不得抽象化 GPT validator 契約
- 現象：移植分析若只寫「domain validators」或「rendering checks」，容易漏掉 `check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、`measure_bands.py`。
- 根因：摘要式移植把 GPT v1.6.1 的具名 hard gate 泛化，降低了房規二與凍結契約強度。
- 對策：主檔、`FROZEN.md`、traceability、acceptance checklist 與 contract tests 全部保留具名 gate。
- 已固化：`tests/test_skill_contract.py`、`scripts/skill_gate.py`、房規二。

## 2026-07-07｜CLI 互動式 UI 必須可鍵入選項或需求
- 現象：只寫「互動式 UI」會讓 Codex CLI 使用者誤以為有固定彈窗或選單。
- 根因：未區分 Codex-Desktop 和 codex-cli 的互動表面。
- 對策：CLI 互動定義為 decision table 加上「輸入 A、B、C，或直接輸入需求」，並保留建議選項與理由。
- 已固化：`SKILL.md` interactive recommendation flow、`references/acceptance-checklists.md`。

## 2026-07-03｜驗證器正本自己違反房規三
- 現象：`validate_punct.py` v1 掃自己 exit=1，說明文字使用禁用標點。
- 根因：正本從未被自己掃過。
- 對策：v2.1 自我合規，並把掃自己必須 exit=0 寫進回歸測試。
- 已固化：tests/test_validate_punct.py

## 2026-07-03｜閘門有四個偵測盲區
- 現象：半形句號、半形雙引號、半形單引號、緊鄰中文的雙連字號，v1 全放行。
- 根因：規則文字宣稱的範圍大於程式實作的範圍。
- 對策：v2.1 補齊四類，並用髒樣本測試守住。
- 已固化：tests/test_validate_punct.py

## 2026-07-03｜sync 自動探索永遠找不到兄弟包
- 現象：無參數執行 `sync_validator.py` 時回報沒有探索到任何包。
- 根因：探索起點少上一層。
- 對策：路徑修正為上兩層，並用模擬多包環境測試守住。
- 已固化：tests/test_validate_punct.py

## 2026-07-03｜交付了要手動合併的補丁
- 現象：使用者收到 addendum 檔後不知道如何安裝。
- 根因：skill 應以整包重新安裝，不應交付手動補丁。
- 對策：維護協議明定交付一律是完整可安裝包。
- 已固化：references/maintenance-protocol.md

## 2026-07-05｜Claude Skill 移植到 ChatGPT 時必須改執行檔位置
- 現象：原包把可執行的 punctuation validator 放在 `assets/`。
- 根因：Claude 原語意把正本視為資產，但 Codex Skill 較適合把可執行檢查放在 `scripts/`。
- 對策：移植版把正本改為 `scripts/validate_punct.py`，並更新 sync 與 tests。
- 已固化：tests/test_validate_punct.py

## 2026-07-05｜Skill 名稱改為 codex-skill-conventions
- 現象：移植版仍沿用來源命名，與實際 Codex 用途不一致。
- 根因：第一次移植保留來源名稱，未把安裝後觸發名稱改為 GPT 專用慣例。
- 對策：目錄、frontmatter、metadata、範例 token、測試路徑與文件標題同步改名。
- 已固化：tests/test_validate_punct.py

## 2026-07-06｜外部 validator CLI 被誤設為主流程
- 現象：v1.4.0 要求地端外部驗證工具才能形成 hard gate，偏離 Web Skill 直接使用體驗。
- 根因：把 repository 級 CI 思維套進單一 Codex Skill，造成不必要的地端依賴。
- 對策：v1.5.0 移除 CLI 資產與主流程，驗證收斂回 Skill 內建 scripts、tests 與 packager。
- 已固化：FROZEN.md 與 SKILL.md 的 self-contained default。

## 2026-07-06｜v1.5.0 過度簡化主檔高權重規則
- 現象：中文觸發詞、Joan 原始生態、多格式交付、檢查表與維護細則被降到 references 或被淡化。
- 根因：過度追求 ChatGPT progressive loading，忽略這些規則必須在主檔直接提醒模型。
- 對策：v1.5.1 把觸發詞、硬閘門、Joan 生態、交付規則、檢查表與維護協議拉回 SKILL.md。
- 已固化：FROZEN.md 與 SKILL.md 主檔規則。

## 2026-07-06｜互動式決策與驗收模板必須主檔可見
- 現象：v1.5.1 雖有 focus gate 與 acceptance 規則，但互動式建議流程與可複製 acceptance prompt template 不夠明確。
- 根因：把方向判斷與驗收 prompt 視為一般流程細節，沒有提升成主檔可見的執行規則。
- 對策：v1.5.2 在 SKILL.md 新增 Interactive recommendation flow 與 Acceptance prompt template，並補充 references 的驗收檢查。
- 已固化：SKILL.md 與 references/acceptance-checklists.md

## 2026-07-06｜Codex runtime split 不能沿用單一 ChatGPT 假設
- 現象：Codex 技能移植若只改名稱，會忽略 Codex-Desktop（Windows）、codex-cli（Windows）、codex-cli（Linux）的命令與互動差異。
- 根因：原 GPT 版沒有必要區分 Codex 執行表面。
- 對策：v1.5.2-codex 在 SKILL.md 主檔新增 runtime matrix 與 runtime focus gate。
- 已固化：SKILL.md、FROZEN.md、references/migration-notes.md

## 2026-07-06｜Codex 部署前 metadata 與轉換工具必須回補
- 現象：`agents/openai.yaml` 的 short description 過長且缺 default prompt，`SKILL.md` frontmatter 含 metadata，且 v1.5.2 未回補 v1.2.1 的 bootstrap 與轉換器工具。
- 根因：第一次 Codex 移植偏重主檔治理，未把 Codex 外殼 metadata 與早期轉換工具納入同一個 hard gate。
- 對策：移除 `SKILL.md` metadata，補 `agents/openai.yaml` default prompt，回補 `scripts/bootstrap.py` 與 `scripts/convert_from_claude_skill.py`，並把 metadata、bootstrap、converter 納入回歸測試與 `skill_gate.py`。
- 已固化：tests/test_validate_punct.py、scripts/skill_gate.py、FROZEN.md
## 2026-07-07｜主檔偏重時先強化優先序而非硬砍
- 現象：`SKILL.md` 接近五百行時，單純追求三百三十至三百七十行可能削弱主檔可見契約。
- 根因：長度風險和契約流失風險需要分開處理，不能用行數取代治理優先順序。
- 對策：新增 `Execution priority block`，只合併重複文字，保留觸發詞、runtime matrix、九條房規、驗證硬閘門、檢查表、維護協議與 acceptance template。
- 已固化：SKILL.md、FROZEN.md、scripts/skill_gate.py

## 2026-07-07｜回歸測試不得硬編碼 Linux 暫存目錄
- 現象：Codex-Desktop（Windows）執行 `skill_gate.py` 時，`TemporaryDirectory(dir="/tmp")` 造成 `FileNotFoundError`。
- 根因：測試把 codex-cli（Linux）常見路徑誤當成 Codex-Desktop（Windows）與 codex-cli（Windows）也存在的跨平台路徑。
- 對策：改用 Python 預設暫存目錄選擇，讓 Codex-Desktop（Windows）、codex-cli（Windows）、codex-cli（Linux）各自使用平台正確位置。
- 已固化：tests/test_validate_punct.py
