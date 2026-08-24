---
name: joan-skill-conventions
description: "Joan（酒 Ann／vibe-expert.com）開發 Claude Skill or ChatGPT Skill or Hermes Skill 的內部房規與品味指南。當使用者要新開一支 skill、檢視／升級／重構既有 skill、為 skill 寫驗證器或回歸測試、或在討論 skill 的版型／驗證／交付架構時，立即讀此 skill，把以下七條房規套用上去：① 凍結契約＋另開新版（絕不就地改定版）② 驗證即閘門、絕不靠肉眼 ③ 全形標點＋禁破折號鐵則 ④ 引擎／皮膚／內容三層正交、跨學科通用 ⑤ 能力邊界誠實＋降級階梯不造假 ⑥ 透明自動安裝＋離線自包含交付 ⑦ 生成前強制對焦閘門。另含三種模式（套用／探索／模仿）、滿意度確認迴圈、多格式交付。觸發詞包含：開新 skill、做一個 skill、寫一支 skill、升級 skill、檢視 skill、重構 skill、skill 房規、skill 規範、驗證器、凍結契約、回歸測試、交付前檢查 等。即使只說『幫我做一個 XXX 的 skill』也應先讀此 skill 套用房規。注意：通用的 skill 製作流程（draft→test→iterate→package）仍走 skill-creator；本 skill 只在其上疊加 Joan 的房規與品味，兩者並用。"
---

# Joan Skill Conventions（Joan 的 skill 開發房規）

> **v1.4.1｜2026-08-22**：metadata的描述部分，開發 Claude Skill 修改為 開發 Claude Skill or ChatGPT Skill or Hermes Skill。
> **v1.4｜2026-08-21**：房規二長出「閘門要有牙齒」一節，把全 library 驗證器稽核歸納的三種假閘門樣式（自我循環／缺輸入放行／驗到別的東西）寫成反例並配正面判準（獨立重算＋fail-closed＋驗當前產出）。交付前驗證清單新增第 6 條「驗證器自稽」，新 skill 開工檢查表第 5 點擴充成驗證器設計三問，`references/canonical-snippets.md` 新增第 12 段「驗證器自稽範式」。這是自 v1.1 以來房規本文第一次更動。
> **v1.3｜2026-07-25**：新增 `assets/pack_skill.py`，跨平台 zip 打包器正本（全 ASCII、Windows 非法字元與保留名稱、大小寫碰撞、路徑長度、回讀 CRC 自檢，不過就不產出檔案）。交付前驗證清單新增第 10 條打包閘門。七條房規本文未動一字。
> **v1.2.1｜2026-07-20**：交付前驗證清單新增 zip 打包路徑鐵則，壓縮包內所有路徑一律 ASCII（skill 上傳器硬限制，非 ASCII 路徑整包退件），打包後用 `zipfile.namelist()` 自檢。
> **v1.2｜2026-07-07**：生態系同步版。全生態系 26 支 skill 的 validate_punct.py 收斂至本包正本（原況為 10 個分歧版本）；references/canonical-snippets.md 新增第 11 段「回歸測試雙相容範式」（pytest 可收集＋python 直跑並存的標準寫法）。七條房規本文未動一字。
> **v1.1｜2026-06-20**：把三個已落地的做法寫進房規：凍結可擴充版型庫（registry＋FROZEN＋FROZEN.md，房規一）、回歸自測即閘門（`tests/test_*.py`，房規二）、相依自動安裝 `bootstrap.ensure_*`（ensure 在 import 之前，房規六）。新增 `references/canonical-snippets.md` 第 8 至 10 段範式。
> **v1.0｜2026-06-20**：從 cornell-notes-generator、constructivist-lesson-builder、knowledge-map-generator、knowledge-card-generator、dex-card-generator 五包抽取出的共用規範，由 Joan（酒 Ann）維護；附 `scripts/sync_validator.py` 一鍵同步驗證器正本到各包。

這是一份**房規（house rules）**，疊加在 `skill-creator` 之上。`skill-creator` 教「怎麼做出一支 skill」（draft→test→iterate→package）；本 skill 教「Joan 的 skill 長什麼樣、守什麼規矩」。兩者並用：先依 skill-creator 的流程走，每一步用本房規把關品味與正確性。

新開或升級任何一支 Joan 的 skill 前，先讀完本檔，再對照文末兩張檢查表動工。

---

## 七條房規（每條都附「怎麼落實」與「反例」）

### 一、凍結契約，另開新版，絕不就地改定版
一旦某個版型／座標／色票／皮膚定版，就**寫死成凍結契約**，之後要改一律另開新版本，不動凍結版。

- **怎麼落實**：把定版的固定值（座標表、色票、皮膚 token）集中寫死，並在程式裡用一個 `FROZEN` 集合或常數標記（如 kcg 的 `FROZEN = {"joan-coral"}`）。每包放一份 `FROZEN.md` 當帳本，記下每個版本鎖了什麼、定版檔是哪幾個。SKILL.md 開頭放版號戳記。
- **回歸守門**：把凍結值寫成測試斷言（例：`assert SKINS["joan-coral"]["bg"] == "#E8856E"`），有人改色就紅燈。
- **凍結可擴充版型庫（已實證做法）**：版型／皮膚做成一個**具名 registry**（kcg 的 `SKINS` 字典、kmap 的 `scripts/preset_*.py`、dex 的 `scripts/skins.py`），用 `spec["skin"]`／指名函式套用；其中一個以上設為凍結（`FROZEN` 集合）。擴充＝往 registry 加一組 token／一支 preset，**不動凍結項**。設計時讓「不指定＝沿用 DEFAULTS／舊視覺」，新增不破壞既有產出（向後相容）。範式見 `references/canonical-snippets.md` 第 10 段。
- **反例**：直接在原檔改色票／改座標「順手調一下」。這會讓既有產出無法重現，是大忌。

### 二、驗證即閘門，絕不靠肉眼
每支 skill 的交付都要有**強制驗證器**，退出碼非 0 一律不准交付。正確性外包給程式，不信任目視。

- **標準驗證層（依 skill 需要疊加）**：
  - `validate_punct.py`：全形標點＋禁破折號（見房規三，**共用資產**）。
  - 頁面截斷：列印模式逐頁量溢出（螢幕截圖看不出來的裁切），溢出 > 2px 即擋（參考 constructivist `check_pages.py`）。
  - 數理正確性：每題用 **SymPy 重算比對**宣稱答案，不符即擋（參考 constructivist `check_math.py`、cornell `verify_math.py`）。「答案絕不靠肉眼」。
  - KaTeX 渲染：無殘留佔位 token、無未渲染 `$$`／`\(`、無 katex-error（參考 `check_katex.py`）。
  - 領域正確性：如化學的碳骨架數、反應平衡、標籤對齊（cornell `verify_structures.py`），且**驗證先於繪圖**。
  - **回歸自測（已實證做法）**：每支 skill 放 `tests/test_*.py`，把「能在沒裝重相依下跑的部分」全寫成測試：純邏輯函式、**凍結契約斷言**（守住色票／座標／registry）、缺料降級分支、以及**自動安裝邏輯**（攔截 `_pip`／subprocess，驗「裝過不重裝、缺了會嘗試裝」而不觸發真實安裝）。改動引擎後必跑、全 PASS 才算沒踩到既有契約。範式見 `references/canonical-snippets.md` 第 9 段。
  - 版面量測：教學牆量各帶寬度補卡到差距 < 一張卡（kmap `measure_bands.py`）。
- **閘門要有牙齒（有驗證器 ≠ 擋得住壞產出）**：驗收一支驗證器的唯一尺是「餵一份故意錯的產出，它會不會紅燈」。不會紅的驗證器等於沒有，而且更危險，因為它給假的安全感。全 library 逐行稽核歸納出三種假閘門樣式，開 skill 或升級時逐支自查：
  - **假閘門一・自我循環**：用同一個方法算出宣稱值、又用同一個方法重算來比對，恆等式永遠成立、永不紅燈（例：rag-chunk 舊版用同一支 tokenizer 算 chunk 長度、又用同一支重算來比）。正解：驗證器要用**獨立來源或獨立方法**重算，再和產出自報的值比對。
  - **假閘門二・可選輸入缺就靜靜放行**：最關鍵的檢查依賴一個可選輸入，沒給就 `return []`、略過、或當作通過（例：academic 舊版 C7 拿不到 cards 就靜默放行，等於引文防造假整個沒作用）。正解：關鍵檢查的前提缺席時要 **fail-closed**（擋下、要求補齊），不是 fail-open（放行）。
  - **假閘門三・驗到別的東西**：驗的是寫死的範例、上一份產出、或無關常數，不是這次要交付的產出本身（例：cornell 舊版 verify_math 驗的是寫死的力學例題，不是本份筆記的答案）。正解：驗證器讀的物件必須綁定**當前這份待交付的產出**（讀交付檔本身，不讀寫死樣本）。
  - **正面判準（模範）**：獨立重算、fail-closed、驗當前產出，三者齊備才算有牙齒。範例：en-zh-translator 三閘門、academic C1 至 C9、constructivist `check_math.py`、cornell v1.7 `verify_math.py`（讀 answers.json 逐題 SymPy 獨立重算）。
  - **落實**：每支驗證器都配一組**負向測試**（造一份故意錯的產出，斷言驗證器非 0），放進 `tests/`。過不了負向測試的驗證器不准上線。範式見 `references/canonical-snippets.md` 第 12 段。
- **反例**：「看起來對就交付」（尤其數值與頁面截斷，肉眼最常漏）；或「有寫驗證器就安心」，卻是上面三種假閘門之一，綠燈綠得毫無意義。

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

### 六、透明自動安裝，離線自包含交付
相依套件自動裝、對使用者透明；交付物單檔自包含、離線可印。

- **自動安裝（已實證做法）**：每包放一支 `scripts/bootstrap.py`，提供**分顆粒的 `ensure_*` 函式**（`ensure_export` 補 playwright＋chromium、`ensure_katex` 補 npm katex、`ensure_math` 補 sympy、`ensure_font_tools` 補 fonttools＋brotli…），偵測缺哪個裝哪個、裝過秒跳過。pip 一律帶 `--break-system-packages`，setup.sh 設計成**冪等**。**關鍵接線：`ensure_*` 必須在對應的 `import` 之前呼叫**（頂層 `from playwright import …` 在套件缺席時會直接 ImportError，所以先 `import bootstrap; bootstrap.ensure_export()` 再 import）。驗證器正本只放一處，用 `sync_validator.py` 同步到各包，不要各寫一份。範式見 `references/canonical-snippets.md` 第 8 段。
- **離線自包含**：字型依本份用字**子集化為 woff2 後 base64 內嵌**；KaTeX **伺服端預渲染**並內嵌字型，絕不讓瀏覽器開檔時才從 CDN 載。產出列印就緒（`print-color-adjust:exact`、`@page` 尺寸、`margin:0`）。
- **反例**：叫使用者自己 `pip install`；HTML 開檔才連網載字型／KaTeX，離線就破版。

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
5. **驗證層**：要疊哪些驗證器（全形＋禁破折號是基本盤；含數理加 SymPy；含頁面加截斷量測）？且每支都要回答驗證器三問：靠什麼**獨立來源**判對錯（不是同一方法算兩次）？關鍵前提缺席時 **fail-closed 還是 fail-open**（缺料要擋，不能放行）？驗的是**當前產出還是寫死範例**？
6. **相依**：用到哪些重套件？bootstrap 怎麼自動裝？
7. **交付格式**：哪幾種格式？
8. **回歸測試**：純邏輯（不需重相依的部分）怎麼寫成 `tests/test_*.py`？凍結契約要不要寫成斷言守門？

## 交付前驗證清單

1. [ ] `validate_punct.py` 全形＋禁破折號，退出碼 0。
2. [ ] 含數理：SymPy 重算每題，全對。
3. [ ] 含 KaTeX：無殘留佔位、無 katex-error。
4. [ ] 含固定版面：頁面截斷逐頁量測，溢出全 0。
5. [ ] 含領域結構（化學等）：先過結構／反應驗證再繪圖。
6. [ ] **驗證器自稽**：上面每支驗證器都跑過「餵壞產出」負向測試，故意給一份錯的必定紅燈；三種假閘門（自我循環／缺輸入放行／驗到別的東西）逐條排除，做到獨立重算＋fail-closed＋驗當前產出。
7. [ ] 凍結契約沒被動到（跑 `tests/test_*.py` 回歸測試，凍結值斷言全綠）。
8. [ ] 相依由 `bootstrap.ensure_*` 自動安裝（ensure 在 import 之前）、字型／KaTeX 內嵌，離線可印、免手動 pip。
9. [ ] 多格式齊備，全部 present_files。
10. [ ] 打包一律走 `assets/pack_skill.py`，**禁用任何 GUI 壓縮軟體**。全 ASCII 路徑、無 Windows 非法字元與保留名稱、無大小寫碰撞、路徑長度過關、回讀 CRC 自檢通過，退出碼 0 才算完成。
11. [ ] 交付後問使用者是否滿意。

---

## 共用資產與參考
- `assets/validate_punct.py`：**唯一正本**的全形＋禁破折號驗證器。新 skill 直接複製到自己的 `scripts/`，不要各寫一份分歧版本。
- `assets/pack_skill.py`：**唯一正本**的跨平台 zip 打包器。打包前全量檢查路徑合法性（全 ASCII、Windows 非法字元 `< > : " | ? *`、保留名稱 `CON`／`PRN`／`COM1` 等、結尾句點或空格、大小寫碰撞、路徑長度、符號連結），任一不過就不產出檔案；打包後重新開檔回讀，比對名單與 CRC，確認沒有靜默漏檔。一律 Deflate、不加密，自動排除 `__MACOSX`、`.DS_Store`、`__pycache__`。用法：`python3 pack_skill.py <skill 目錄>`、`--check-only` 只檢查、`--audit <既有 zip>` 稽核舊包。**與驗證器不同，這支不同步到各包**：它是對 skill 包做事的中央工具，只留一份就沒有分歧風險。
- `scripts/sync_validator.py`：把上面的正本一鍵同步到各包的 `scripts/validate_punct.py`，避免分歧。`--check` 只檢查漂移不寫入（可接 CI）；不傳目標會自動探索同層含 `scripts/validate_punct.py` 的包。
- `references/canonical-snippets.md`：可複製的標準片段（凍結契約寫法、bootstrap 自動安裝、對焦閘門模板、能力邊界模板、回歸測試骨架、版號戳記格式）。
- 通用 skill 製作流程（draft→test→iterate→package）見 `skill-creator`，本房規與它並用。
