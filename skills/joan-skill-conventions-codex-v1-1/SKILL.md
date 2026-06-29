---
name: joan-skill-conventions-codex-v1-1
description: "Joan（酒 Ann／vibe-expert.com）開發 Codex Skill 的內部房規與品味指南。當使用者要新開一支 skill、檢視／升級／重構既有 skill、為 skill 寫驗證器或回歸測試、或在討論 skill 的版型／驗證／交付架構時，立即讀此 skill，且必須套用七條房規。特別強制：凡是新建、檢視、升級或重構 skill，必須同步設計、建立或更新驗證器與回歸測試，至少包含 scripts/validate_punct.py、tests/test_*.py、凍結契約斷言、缺料降級測試、bootstrap ensure_* 測試；若使用者只要求檢視，仍必須檢查是否缺驗證器或回歸測試，並把缺口列為阻斷項或待修項。觸發詞包含：開新 skill、做一個 skill、寫一支 skill、升級 skill、檢視 skill、重構 skill、skill 房規、skill 規範、驗證器、凍結契約、回歸測試、交付前檢查。通用 skill 製作流程仍走 skill-creator；本 skill 疊加 Joan 房規與驗證測試閘門。"
---
# Joan Skill Conventions Codex v1.1（Joan 的 skill 開發房規）

> **Codex v1.1｜2026-06-29**：修正 Codex v1.0 容易把驗證器與回歸測試視為建議清單的問題。新增「驗證測試強制流程」：新建、檢視、升級、重構 skill 時，必須同步設計、建立或更新驗證器與 `tests/test_*.py`，沒有測試即列為阻斷項，不得只交付 SKILL.md 或口頭建議。
> **Codex v1.0｜2026-06-28**：基於 Joan 原版 v1.1 的 Codex 適配首版。改用 Codex 的交付與工具慣例；相依安裝增加明確授權及環境隔離閘門；保留原有觸發範圍、對焦流程、多格式交付與同步驗證器行為。
> **v1.1｜2026-06-20**：把三個已落地的做法寫進房規：凍結可擴充版型庫（registry＋FROZEN＋FROZEN.md，房規一）、回歸自測即閘門（`tests/test_*.py`，房規二）、相依自動安裝 `bootstrap.ensure_*`（ensure 在 import 之前，房規六）。新增 `references/canonical-snippets.md` 第 8 至 10 段範式。
> **v1.0｜2026-06-20**：從 cornell-notes-generator、constructivist-lesson-builder、knowledge-map-generator、knowledge-card-generator、dex-card-generator 五包抽取出的共用規範，由 Joan（酒 Ann）維護；附 `scripts/sync_validator.py` 一鍵同步驗證器正本到各包。

這是一份**房規（house rules）**，疊加在 `skill-creator` 之上。`skill-creator` 教「怎麼做出一支 skill」（draft→test→iterate→package）；本 skill 教「Joan 的 skill 長什麼樣、守什麼規矩」。兩者並用：先依 skill-creator 的流程走，每一步用本房規把關品味與正確性。

新開、檢視、升級或重構任何一支 Joan 的 skill 前，先讀完本檔，再執行下一節的「驗證測試強制流程」。不得只修改 `SKILL.md`、不得只給文字建議、不得把驗證器與回歸測試留到使用者提醒後才做。


---

## 驗證測試強制流程（Codex v1.1 必做）

只要任務屬於「新建 skill」、「檢視既有 skill」、「升級 skill」、「重構 skill」、「為 skill 寫驗證器或回歸測試」、「討論交付架構或驗證架構」，必須先做以下流程。這是交付門檻，不是建議清單。

```text
使用者要求 skill 相關工作
        ↓
立即讀取本 skill 與 skill-creator
        ↓
盤點目標 skill 的檔案結構
        ↓
檢查是否已有 scripts/validate_punct.py、tests/test_*.py、FROZEN.md 或等價凍結契約
        ↓
依任務建立或更新驗證器與回歸測試
        ↓
執行可離線、可重現的測試
        ↓
測試通過才可交付；測試未過要先回報阻斷原因與修正方向
```

### 依任務類型的最低行為

| 任務類型 | 必須做的事 | 不可接受的行為 |
|---|---|---|
| 新建 skill | 建立 `SKILL.md`、`agents/openai.yaml`，並同步建立 `scripts/validate_punct.py` 與至少一支 `tests/test_*.py`。測試至少涵蓋觸發條件、全形標點／禁破折號、凍結契約占位或實際斷言、能力邊界、降級階梯。 | 只寫 `SKILL.md`。 |
| 檢視 skill | 檢查觸發條件、房規落實度、驗證器、回歸測試、凍結契約、bootstrap 授權式相依。缺任何一項都要列為缺口。 | 只評論文字品質，不檢查 tests。 |
| 升級 skill | 另開新版或明確維持相容版號，更新指令後同步更新驗證器與回歸測試。新增規則必須有對應測試。 | 改規則但不改測試。 |
| 重構 skill | 先凍結既有契約，再修改架構。重構前後都要跑回歸測試。 | 只重排檔案或改程式，不證明相容。 |
| 只要求驗證器或回歸測試 | 直接補齊驗證器與 `tests/test_*.py`，並說明覆蓋範圍與尚未覆蓋的風險。 | 要求使用者再次提醒測試需求。 |

### tests/test_*.py 最低覆蓋範圍

每支 skill 至少放一支可離線執行的回歸測試。重相依可以 mock，不得因為 Playwright、RDKit、npm、瀏覽器資產缺席就完全不寫測試。

最低測項：

1. 讀取並檢查 `SKILL.md` frontmatter 的 `name` 與 `description`。
2. 檢查 description 內含明確觸發條件。
3. 檢查中文標點與禁破折號規則，或呼叫 `scripts/validate_punct.py`。
4. 檢查凍結契約：有 `FROZEN.md`、`FROZEN` 常數，或測試中有明確待凍結斷言。
5. 檢查能力邊界與降級階梯段落存在。
6. 如有 `scripts/bootstrap.py`，mock `_pip`、`subprocess` 或安裝函式，驗證「已安裝不重裝、缺少會嘗試安裝、未授權不得安裝」。
7. 如有版型、皮膚、座標、色票、schema 或 prompt contract，至少一項要有斷言守門。

### 無法寫完整測試時的降級

若缺少目標 skill 原始碼或執行環境，仍不得跳過測試設計。必須至少產出：

1. `tests/test_contract.py`：檢查 `SKILL.md`、觸發條件、必要段落、禁止破折號。
2. `tests/test_validation_inventory.py`：檢查驗證器、凍結契約、bootstrap、交付清單是否存在。
3. 「尚無法覆蓋」清單：列出需要目標原始碼後才能補的測項。

---

## 七條房規（每條都附「怎麼落實」與「反例」）

### 一、凍結契約，另開新版，絕不就地改定版
一旦某個版型／座標／色票／皮膚定版，就**寫死成凍結契約**，之後要改一律另開新版本，不動凍結版。

- **怎麼落實**：把定版的固定值（座標表、色票、皮膚 token）集中寫死，並在程式裡用一個 `FROZEN` 集合或常數標記（如 kcg 的 `FROZEN = {"joan-coral"}`）。每包放一份 `FROZEN.md` 當帳本，記下每個版本鎖了什麼、定版檔是哪幾個。SKILL.md 開頭放版號戳記。
- **回歸守門**：把凍結值寫成測試斷言（例：`assert SKINS["joan-coral"]["bg"] == "#E8856E"`），有人改色就紅燈。
- **凍結可擴充版型庫（已實證做法）**：版型／皮膚做成一個**具名 registry**（kcg 的 `SKINS` 字典、kmap 的 `scripts/preset_*.py`、dex 的 `scripts/skins.py`），用 `spec["skin"]`／指名函式套用；其中一個以上設為凍結（`FROZEN` 集合）。擴充＝往 registry 加一組 token／一支 preset，**不動凍結項**。設計時讓「不指定＝沿用 DEFAULTS／舊視覺」，新增不破壞既有產出（向後相容）。範式見 `references/canonical-snippets.md` 第 10 段。
- **反例**：直接在原檔改色票／改座標「順手調一下」。這會讓既有產出無法重現，是大忌。

### 二、驗證即閘門，絕不靠肉眼
每支 skill 的交付都要有**強制驗證器與回歸測試**，退出碼非 0 一律不准交付。正確性外包給程式，不信任目視。新建、檢視、升級、重構 skill 時，必須主動建立或更新驗證器與 `tests/test_*.py`；不得等使用者再次提醒。

- **標準驗證層（依 skill 需要疊加）**：
  - `validate_punct.py`：全形標點＋禁破折號（見房規三，**共用資產**）。新 skill 必須複製到 `scripts/validate_punct.py`，既有 skill 缺少時列為阻斷項。
  - 頁面截斷：列印模式逐頁量溢出（螢幕截圖看不出來的裁切），溢出 > 2px 即擋（參考 constructivist `check_pages.py`）。
  - 數理正確性：每題用 **SymPy 重算比對**宣稱答案，不符即擋（參考 constructivist `check_math.py`、cornell `verify_math.py`）。「答案絕不靠肉眼」。
  - KaTeX 渲染：無殘留佔位 token、無未渲染 `$$`／`\(`、無 katex-error（參考 `check_katex.py`）。
  - 領域正確性：如化學的碳骨架數、反應平衡、標籤對齊（cornell `verify_structures.py`），且**驗證先於繪圖**。
  - **回歸自測（已實證做法，必做）**：每支 skill 放 `tests/test_*.py`，新建、升級、重構時同步新增或更新。把「能在沒裝重相依下跑的部分」全寫成測試：純邏輯函式、**凍結契約斷言**（守住色票／座標／registry）、缺料降級分支、以及**自動安裝邏輯**（攔截 `_pip`／subprocess，驗「裝過不重裝、缺了會嘗試裝」而不觸發真實安裝）。改動引擎、SKILL.md、觸發條件、驗證器、bootstrap 或交付格式後必跑、全 PASS 才算沒踩到既有契約。範式見 `references/canonical-snippets.md` 第 9 段。
  - 版面量測：教學牆量各帶寬度補卡到差距 < 一張卡（kmap `measure_bands.py`）。
- **反例**：「看起來對就交付」。尤其數值與頁面截斷，肉眼最常漏。

### 三、全形標點＋禁破折號（個人排版鐵則）
中文一律全形標點，只有英數之間用半形；**破折號一律禁用**。

- **規則**：逗號「，」句號「。」頓號「、」冒號「：」分號「；」問號「？」驚嘆號「！」引號「「」『』」括號「（）」全用全形。`1,000`、`KaTeX`、`CO₂` 這種英數之間才用半形。
- **禁破折號**：不得用雙連續長破折號、單個 em dash（U+2014）或 en dash（U+2013）。需要斷句改用全形句號、逗號、冒號或頓號。
- **怎麼落實**：用共用的 `validate_punct.py`（`assets/validate_punct.py`，已含禁破折號偵測），交付前必跑、非 0 不交付。新 skill 直接複製這支，不要各寫一份。
- **反例**：在中文裡夾半形逗號、用破折號斷句。連 SKILL.md 自身與驗證器訊息都要守。

### 四、引擎／皮膚／內容三層正交，跨學科通用
**引擎只管骨架、皮膚與版型，內容是什麼學科都能填。** 把視覺和內容徹底解耦。

- **三層（以 kcg 為範本）**：骨架（固定結構）× 皮膚（可換的色彩 token 組）× 版型（依內容形狀選）。再外層是「系列」（一套皮膚 × N 張）。
- **跨學科**：引擎不綁科目；用「學科 → 預設」對照表自動帶視覺工具與主色（dex 的 `SUBJECT_DEFAULT`／`SUBJECT_ACCENT`），使用者沒指定就照預設。
- **反例**：把某個學科的內容寫死進引擎，換科目就要改引擎。

### 五、能力邊界誠實，降級階梯不造假
明白宣告做不到的事，不硬做、不假裝；缺料就**有尊嚴地降級**，不留醜空洞、不編造。

- **怎麼落實**：每支 skill 寫一段「能力邊界（先講清楚，別硬做）」，列出界外項（AI 生成插畫、水彩手繪、bespoke 插畫等，因無法驗證或有授權問題）。視覺走**降級階梯**（dex：smiles→katex→icon→image→glyph，缺料降級成字形大字）。數值「不確定標（需查證），絕不編造」。
- **反例**：使用者要 AI 插畫卡就硬生一張來源不明的圖；分子量沒把握就填一個看起來合理的數字。

### 六、取得授權後準備相依，離線自包含交付
先偵測相依與執行環境；需要下載套件、安裝瀏覽器資產或寫入環境時，先說明變更範圍並取得使用者授權。交付物單檔自包含、離線可印。

- **授權式安裝（Codex 適配做法）**：每包放一支 `scripts/bootstrap.py`，提供**分顆粒的 `ensure_*` 函式**（`ensure_export` 補 playwright＋chromium、`ensure_katex` 補 npm katex、`ensure_math` 補 sympy、`ensure_font_tools` 補 fonttools＋brotli…）。先唯讀偵測缺少項目，未取得授權時只回報，不執行 pip、npm 或瀏覽器安裝。取得授權後優先使用既有虛擬環境或建立隔離環境；只有偵測到 `EXTERNALLY-MANAGED`、無法使用隔離環境，且使用者明確同意修改系統環境時，才允許加入 `--break-system-packages`。setup 腳本維持**冪等**。**關鍵接線：`ensure_*` 必須在對應的 `import` 之前呼叫**（頂層 `from playwright import …` 在套件缺席時會直接 ImportError，所以先執行已授權的 `bootstrap.ensure_export()`，再 import）。驗證器正本只放一處，用 `sync_validator.py` 同步到各包，不要各寫一份。範式見 `references/canonical-snippets.md` 第 8 段。
- **離線自包含**：字型依本份用字**子集化為 woff2 後 base64 內嵌**；KaTeX **伺服端預渲染**並內嵌字型，絕不讓瀏覽器開檔時才從 CDN 載。產出列印就緒（`print-color-adjust:exact`、`@page` 尺寸、`margin:0`）。
- **反例**：未告知就執行 `pip install`／`npm install`；未檢查環境就強制使用 `--break-system-packages`；HTML 開檔才連網載字型／KaTeX，離線就破版。

### 七、生成前強制對焦閘門
**嚴禁拿到主題就直接生。** 開場先停下來，把結構與規格對焦清楚，得到同意才動工。

- **怎麼落實**：依 skill 性質設一道必須停下的閘門。教學文件用多關訪談（constructivist：語言→學齡→方向深度→例題→字詞公式→風格）；知識牆先做「結構盤點」再對焦分區（kmap）；卡片先講好欄位與視覺型別（dex／kcg）。能從語意判斷的就不問，問得少、問得準。
- **反例**：拿到「分數加法」就直接生一份，沒問是國小三年級還是國中補救，深度全錯、整份重做。

---

## 三種模式（沿用 course-handout-generator 心法，每支都支援）
- **套用**：指名既有版型／皮膚，穩定批量產出。
- **探索**：換配色／版型／密度，每次給不同調性，重做到滿意。
- **模仿**：上傳一份喜歡的參考，抽色票與版面樣式凍結成新版型（插畫部分不模仿）。

## 滿意度確認迴圈
每次交付後**必問是否滿意**。視覺問題（配色、字體）→ 調參數重出；內容問題 → 修內容重跑驗證。重做不限次數。不要省略這一步。

## 多格式交付（缺一不可，全部 present_files）
依 skill 決定，常見組合：HTML（單檔自包含）＋ PDF（列印就緒）＋ PNG（多頁打包成 zip）。教學文件再加 docx（走 `docx` skill）。

---

## 新 skill 開工檢查表

開一支新 skill 前，先回答：

1. **定位**：和既有五包的分工？會不會和某支重疊（重疊就不要新開，去升級那支）。
2. **三層**：骨架是什麼？皮膚有哪些（哪個先凍結）？版型怎麼依內容選？
3. **能力邊界**：界外是什麼？降級階梯怎麼排？
4. **對焦閘門**：開場要停下來問哪幾關？哪些能從語意判斷不問？
5. **驗證層**：要疊哪些驗證器（全形＋禁破折號是基本盤；含數理加 SymPy；含頁面加截斷量測）？
6. **相依**：用到哪些重套件？bootstrap 怎麼做授權式安裝與唯讀偵測？
7. **交付格式**：哪幾種格式？
8. **回歸測試**：純邏輯（不需重相依的部分）怎麼寫成 `tests/test_*.py`？凍結契約、觸發條件、能力邊界、降級階梯、bootstrap 分支是否都有斷言守門？

## 交付前驗證清單

1. [ ] `validate_punct.py` 全形＋禁破折號，退出碼 0。
2. [ ] 含數理：SymPy 重算每題，全對。
3. [ ] 含 KaTeX：無殘留佔位、無 katex-error。
4. [ ] 含固定版面：頁面截斷逐頁量測，溢出全 0。
5. [ ] 含領域結構（化學等）：先過結構／反應驗證再繪圖。
6. [ ] 凍結契約沒被動到（跑 `tests/test_*.py` 回歸測試，凍結值斷言全綠）。
7. [ ] 相依由 `bootstrap.ensure_*` 先唯讀檢查；需要安裝時已取得授權並優先使用隔離環境（ensure 在 import 之前）；字型／KaTeX 內嵌，離線可印。
8. [ ] 新建、檢視、升級、重構 skill 時，已同步建立或更新 `tests/test_*.py`，並且測試結果可重現。
9. [ ] 多格式齊備，全部以 Codex 可點擊的絕對路徑連結交付。
10. [ ] 交付後問使用者是否滿意。

---

## 共用資產與參考
- `assets/validate_punct.py`：**唯一正本**的全形＋禁破折號驗證器。新 skill 直接複製到自己的 `scripts/`，不要各寫一份分歧版本。
- `scripts/sync_validator.py`：把上面的正本一鍵同步到各包的 `scripts/validate_punct.py`，避免分歧。`--check` 只檢查漂移不寫入（可接 CI）；不傳目標會自動探索同層含 `scripts/validate_punct.py` 的包。
- `references/canonical-snippets.md`：可複製的標準片段（凍結契約寫法、bootstrap 授權式安裝、對焦閘門模板、能力邊界模板、回歸測試骨架、版號戳記格式）。
- 通用 skill 製作流程（draft→test→iterate→package）見 `skill-creator`，本房規與它並用。
