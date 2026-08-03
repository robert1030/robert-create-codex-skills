---
name: gpt-skill-conventions
description: "joan skill 開發房規在 chatgpt 的移植版。use when the user asks to create, update, review, refactor, package, validate, freeze, regression test, or inspect a skill, including 開新 skill、做一個 skill、寫一支 skill、升級 skill、檢視 skill、重構 skill、skill 房規、skill 規範、驗證器、凍結契約、回歸測試、交付前檢查。hard gate：if a new skill request only gives a topic, only says joan style or @gpt-skill-conventions, or asks to directly start or directly produce, do not produce a complete skill artifact, skill.zip, full SKILL.md, file tree, scripts, tests, or package. first run the focus gate and ask missing required inputs. apply seven rules：凍結契約另開新版、驗證即閘門、全形標點與禁破折號、引擎皮膚內容三層正交、能力邊界誠實與降級階梯、透明自動安裝與離線自包含交付、生成前強制對焦閘門。compose with skill-creator instead of replacing it."
---

# gpt-skill-conventions

> **v1.2.2｜2026-07-12**：保留 ChatGPT Web 介面 metadata，補上 Codex 介面 metadata 與預設提示；bootstrap 改為依 Windows、Linux、PEP 668 與虛擬環境決定 pip 參數，並對 pip、npm 與 Chromium 安裝失敗留下 log、回傳失敗與停止後續依賴流程。
> **v1.2.1（ChatGPT 移植版）｜2026-07-09**：補強房規七「生成前強制對焦閘門」。明定只有 skill 主題、只有「Joan 風格」或 `@gpt-skill-conventions`、或只有要求直接產出時，不得產出完整 skill 產物，包括完整 `SKILL.md`、檔案樹、參考文件、腳本、測試、封裝檔或交付包。必須先完成對焦閘門。同時移除 Claude `connector` 術語殘留，統一改為 ChatGPT 應用程式（Apps）、MCP 工具、工作區代理程式可用工具與上傳檔案來源。
> **v1.2.1（ChatGPT 移植版）｜2026-07-08**：從 `joan-skill-conventions` v1.2.1 移植到 ChatGPT Skills。保留七條房規、三種模式、滿意度確認迴圈、多格式交付、新技能開工檢查表、交付前驗證清單、共用資產與回歸測試。ChatGPT 版技術調整：技能包可攜帶 Python 腳本與資源，但每次使用時能否執行腳本、能否存取使用者本機檔案、能否取得長期唯讀掛載目錄，取決於當下 ChatGPT 工具與沙盒能力；因此本技能必須先嘗試可行的原生工具與腳本執行，若不可行，改走明示的降級階梯，不得假裝已執行。
> **v1.2.1｜2026-07-08**（patch，只改文件）：精確化多格式交付的驗證推定。寫死成立前提（PDF／PNG 須由通過驗證且其後未再修改的同一份 HTML 直接匯出，匯出腳本注入文字即推定斷裂）與適用範圍（僅內容類驗證；版面類永遠實測，PNG 須以實際輸出尺寸檢查裁切），並建議匯出腳本自行重跑 `validate_punct.py` 把推定變回實測。docx 明文不適用任何推定。
> **v1.2｜2026-07-08**：體檢修正版。統一頁面溢出門檻為 ≦ 2px 並寫死量測定義；破折號規則明確為全文禁用（半形連字號不在此限）；明文「驗證失敗不得請示放行」；新增 bootstrap 正本（`assets/bootstrap.py`）與 `assets/manifest.json`，`sync_validator.py` 泛化為依 manifest 同步多個正本；本包補上自身回歸測試 `tests/`；版號規則補 major 定義；對焦閘門改為三欄決策表；降級階梯 `resolve_visual` 補完整可複製實作；新增凍結雜湊守門範式；三種模式明文接上 registry 擴充路徑；自動安裝必留 log。
> **v1.1｜2026-06-20**：把三個已落地的做法寫進房規：凍結可擴充版型庫（registry＋FROZEN＋FROZEN.md，房規一）、回歸自測即閘門（`tests/test_*.py`，房規二）、相依自動安裝 `bootstrap.ensure_*`（ensure 在 import 之前，房規六）。新增 `references/canonical-snippets.md` 第 8 至 10 段範式。
> **v1.0｜2026-06-20**：從 cornell-notes-generator、constructivist-lesson-builder、knowledge-map-generator、knowledge-card-generator、dex-card-generator 五包抽取出的共用規範，由 Joan（酒 Ann）維護；附 `scripts/sync_validator.py` 一鍵同步驗證器正本到各包。

這是一份房規，疊加在 `skill-creator` 之上。`skill-creator` 教「怎麼做出一支 skill」（draft→test→iterate→package）；本技能教「Joan 的 skill 長什麼樣、守什麼規矩」。兩者並用：先依 `skill-creator` 的流程走，每一步用本房規把關品味與正確性。

新開、升級、檢視或重構任何 Joan 風格的 skill 前，先套用本檔，再對照文末兩張檢查表動工。

## 最高優先閘門

新開 skill 時，先判斷規格是否足夠，不得先順著「直接開始」產完整 skill。若使用者只給主題、只說「Joan 風格」或 `@gpt-skill-conventions`、或只要求直接開始／直接產出，第一則回覆必須擋下完整產出，只能輸出對焦閘門、缺口清單與必要問題。完整 skill 產物包含完整 `SKILL.md`、完整檔案樹、參考文件、腳本、測試、封裝檔、`skill.zip` 或交付包。只有在輸入、輸出、驗證層、能力邊界、交付格式、升級契約與必要外部能力都已足夠時，才可產出完整 skill。

## ChatGPT 版能力邊界與降級階梯

- **可攜帶**：本技能可以封裝 `SKILL.md`、`assets/`、`scripts/`、`references/`、`tests/` 與 `agents/openai.yaml`。
- **可嘗試執行**：若當次 ChatGPT 環境提供可執行 Python 的工具，優先實際執行 `assets/validate_punct.py`、`tests/test_conventions.py` 與必要腳本。
- **不可假裝**：若當次環境無法執行腳本、無法存取使用者本機檔案，或無法像 Claude 固定掛載唯讀目錄，必須明說限制，改為人工核對清單、原生檔案工具、或請使用者在可執行環境跑同名腳本。
- **ChatGPT 版技術調整：原因**：ChatGPT Skill 是可攜帶的技能包；實際工具能力由使用者當下方案、工作區設定與對話環境決定。房規五要求誠實降級，因此不得把技能包內的腳本存在，等同宣稱每次都已自動執行。

## ChatGPT 版術語對照

- Claude `connector` 在本移植版不得原樣沿用；ChatGPT 版統一改寫為「應用程式（Apps）」、MCP 工具、工作區代理程式可用工具或上傳檔案來源。
- 「應用程式（Apps）」指 ChatGPT 可連接的外部服務或資料來源。
- 「代理程式」或「工作區代理程式」是任務執行容器，不等同外部資料來源；若要存取外部資料，仍須確認其可用工具或應用程式權限。
- 未確認可用權限前，不得假設能讀取 Gmail、Google Drive、Sheets、Slack、GitHub、本機路徑或任何外部系統。

## 七條房規（每條都附「怎麼落實」與「反例」）

### 一、凍結契約，另開新版，絕不就地改定版

一旦某個版型、座標、色票、皮膚定版，就寫死成凍結契約，之後要改一律另開新版本，不動凍結版。

- **怎麼落實**：把定版的固定值（座標表、色票、皮膚 token）集中寫死，並在程式裡用一個 `FROZEN` 集合或常數標記（如 kcg 的 `FROZEN = {"joan-coral"}`）。每包放一份 `FROZEN.md` 當帳本，記下每個版本鎖了什麼、定版檔是哪幾個。`SKILL.md` 開頭放版號戳記。
- **回歸守門**：把凍結值寫成測試斷言（例：`assert SKINS["joan-coral"]["bg"] == "#E8856E"`），有人改色就紅燈。
- **凍結可擴充版型庫（已實證做法）**：版型與皮膚做成一個具名 registry（kcg 的 `SKINS` 字典、kmap 的 `scripts/preset_*.py`、dex 的 `scripts/skins.py`），用 `spec["skin"]` 或指名函式套用；其中一個以上設為凍結（`FROZEN` 集合）。擴充等於往 registry 加一組 token 或一支 preset，不動凍結項。設計時讓「不指定等於沿用 DEFAULTS 或舊視覺」，新增不破壞既有產出（向後相容）。範式見 `references/canonical-snippets.md` 第 10 段。
- **ChatGPT 版技術調整：原因**：ChatGPT 技能包沒有保證存在長期共享的唯讀目錄；因此凍結契約必須放在技能包檔案與回歸測試內，交付或更新時重新封裝，不能只依賴外部掛載路徑。
- **反例**：直接在原檔改色票或改座標，說只是「順手調一下」。這會讓既有產出無法重現，是大忌。

### 二、驗證即閘門，絕不靠肉眼

每支 skill 的交付都要有強制驗證器，退出碼非 0 一律不准交付。正確性外包給程式，不信任目視。

- **怎麼落實**：依 skill 需要疊加標準驗證層。基本盤是 `validate_punct.py`，檢查全形標點與禁破折號。含固定版面時，列印模式逐頁量溢出，溢出 > 2px 即擋；溢出定義為該頁內容最底元素的 bottom 座標，超出可列印區底邊的像素數，門檻訂 2px 是為了容忍子像素渲染與量測浮點雜訊。含數理時，用 SymPy 重算比對宣稱答案。含 KaTeX 時，檢查無殘留佔位 token、無未渲染公式、無 katex-error。含領域結構時，先做領域驗證再繪圖。每支 skill 放 `tests/test_*.py`，把純邏輯函式、凍結契約斷言、缺料降級分支與自動安裝邏輯寫成回歸測試。
- **不得請示放行**：驗證器退出碼非 0 時，一律修到綠燈，不得回頭問使用者要不要放行，也不得以「滿意度迴圈之後再修」為由先交付。滿意度迴圈處理的是品味與內容方向，正確性閘門沒有討價還價空間。
- **ChatGPT 版技術調整：原因**：若當次 ChatGPT 可執行 Python，必須實際跑驗證器與測試；若不可執行，回報中必須標示「未能實測」，並提供使用者可複製的執行指令與人工核對結果。不能把人工掃描說成程式驗證。
- **反例**：「看起來對就交付」。尤其數值與頁面截斷，肉眼最常漏。另一反例是驗證失敗時問使用者「這個小問題可以接受嗎」。

### 三、全形標點＋禁破折號（個人排版鐵則）

中文一律全形標點，只有英數之間用半形；破折號一律禁用。

- **怎麼落實**：逗號「，」句號「。」頓號「、」冒號「：」分號「；」問號「？」驚嘆號「！」引號「「」『』」括號「（）」全用全形。`1,000`、`KaTeX`、`CO₂` 這種英數之間才用半形。不得用雙連續長破折號、單個 em dash（U+2014）或 en dash（U+2013），英文段落也一樣禁；英文的 pages 3 至 5 請改寫成 pages 3 to 5 或 pages 3-5。需要斷句改用全形句號、逗號、冒號或頓號。半形連字號 `-`（U+002D）不在禁令內。
- **驗證器接線**：用共用的 `validate_punct.py`（`assets/validate_punct.py`，已含禁破折號偵測），交付前必跑、非 0 不交付。新 skill 直接複製這支，或跑 `sync_validator.py`，不要各寫一份。驗證器支援 HTML 與 Markdown；`.md` 會自動略過程式碼區塊。驗證器涵蓋範圍的誠實聲明：半形逗號、分號、冒號、驚嘆號、問號、括號、句點夾中文都會被抓；半形引號因與程式碼、英寸符號難以機器區分，不在自動偵測內，屬人工留意項，規則本身仍要求全形引號。
- **ChatGPT 版技術調整：原因**：ChatGPT 生成內容、技能文件與交付文件都受同一條規則約束；若是程式碼、YAML frontmatter 或命令列語法必須使用半形符號，應放入程式碼區塊或 inline code，避免把必要語法誤當中文排版文字。
- **反例**：在中文裡夾半形逗號、用破折號斷句。連 `SKILL.md` 自身與驗證器訊息都要守。

### 四、引擎／皮膚／內容三層正交，跨學科通用

引擎只管骨架、皮膚與版型，內容是什麼學科都能填。把視覺和內容徹底解耦。

- **怎麼落實**：以 kcg 為範本，拆成骨架（固定結構）× 皮膚（可換的色彩 token 組）× 版型（依內容形狀選）。再外層是「系列」（一套皮膚 × N 張）。引擎不綁科目；用「學科 → 預設」對照表自動帶視覺工具與主色（dex 的 `SUBJECT_DEFAULT`／`SUBJECT_ACCENT`），使用者沒指定就照預設。
- **ChatGPT 版技術調整：原因**：ChatGPT 版技能應把三層正交寫成可重用的決策規則或 reference，而不是把某個任務內容寫死在 `SKILL.md`。長範式放在 `references/canonical-snippets.md`，避免主檔過度膨脹。
- **反例**：把某個學科的內容寫死進引擎，換科目就要改引擎。

### 五、能力邊界誠實，降級階梯不造假

明白宣告做不到的事，不硬做、不假裝；缺料就有尊嚴地降級，不留醜空洞、不編造。

- **怎麼落實**：每支 skill 寫一段「能力邊界（先講清楚，別硬做）」，列出界外項，例如 AI 生成插畫、水彩手繪、bespoke 插畫等，因無法驗證或有授權問題。視覺走降級階梯（dex：smiles→katex→icon→image→glyph，缺料降級成字形大字）。數值不確定就標「（需查證）」，絕不編造。
- **ChatGPT 版技術調整：原因**：ChatGPT 能否跑 Python、能否讀本機路徑、能否使用外部連線、應用程式（Apps）、MCP 工具或工作區代理程式可用工具，均由當下對話環境決定。技能執行時應先檢查可用工具；無法執行時明說，改走人工清單或交付可複製命令，不把「腳本存在」誤報為「腳本已跑」。
- **反例**：使用者要 AI 插畫卡就硬生一張來源不明的圖；分子量沒把握就填一個看起來合理的數字。

### 六、透明自動安裝，離線自包含交付

相依套件自動裝、對使用者透明；交付物單檔自包含、離線可印。

- **怎麼落實**：每包放一支 `scripts/bootstrap.py`，提供分顆粒的 `ensure_*` 函式（`ensure_export` 補 playwright＋chromium、`ensure_katex` 補 npm katex、`ensure_math` 補 sympy、`ensure_font_tools` 補 fonttools＋brotli）。偵測缺哪個裝哪個、裝過秒跳過。pip 參數必須依平台、PEP 668 標記與虛擬環境決定：Windows 不得帶 `--break-system-packages`；Linux 只有在外部管理且不在虛擬環境時才可帶入。關鍵接線：`ensure_*` 必須在對應的 import 之前呼叫。透明不等於隱瞞，每次實際安裝都必須留 log 訊息（如 `[bootstrap] 安裝 playwright...`）。共用正本（`validate_punct.py`、`bootstrap.py`）只放本包 `assets/` 一處，列進 `assets/manifest.json`，用 `sync_validator.py` 依 manifest 同步到各包，不要各寫一份。bootstrap 正本在 `assets/bootstrap.py`，各包複製後依自身相依裁剪 `ensure_*` 顆粒。
- **離線自包含**：字型依本份用字子集化為 woff2 後 base64 內嵌；KaTeX 伺服端預渲染並內嵌字型，絕不讓瀏覽器開檔時才從 CDN 載。產出列印就緒（`print-color-adjust: exact`、`@page` 尺寸、`margin: 0`）。
- **ChatGPT 版技術調整：原因**：ChatGPT 技能包可帶 bootstrap 正本，但實際安裝是否允許，取決於當次執行沙盒。若禁止安裝，必須保留 log 與降級說明，並回報使用者「未能安裝，因此未能執行依賴該套件的驗證或匯出」。
- **反例**：叫使用者自己 `pip install` 卻不提供自動安裝器；HTML 開檔才連網載字型或 KaTeX，離線就破版。

### 七、生成前強制對焦閘門

嚴禁拿到主題就直接生。開場先停下來，把結構與規格對焦清楚，得到同意才動工。

- **怎麼落實**：依 skill 性質設一道必須停下的閘門。教學文件用多關訪談（constructivist：語言→學齡→方向深度→例題→字詞公式→風格）；知識牆先做「結構盤點」再對焦分區（kmap）；卡片先講好欄位與視覺型別（dex／kcg）。問不問不憑感覺，照 `references/canonical-snippets.md` 第 4 段的三欄決策表（必問／可推斷／預設值）操課：落在「必問」欄的沒問到就不准動工；落在「可推斷」欄且對話中已有明確線索的直接採用並在複述時講明；其餘用預設值並講明。問得少、問得準。
- **ChatGPT 版硬 Gate**：新開 skill 時，若使用者只提供 skill 主題、只說「Joan 風格」或 `@gpt-skill-conventions`、或只要求「直接開始產出」，一律不得產出完整 skill 產物。完整 skill 產物包含完整 `SKILL.md`、檔案樹、參考文件、腳本、測試、封裝檔或交付包。必須先完成對焦閘門，確認輸入、輸出、驗證層、能力邊界、交付格式與升級契約。若缺少 ChatGPT 應用程式（Apps）權限、MCP 工具、工作區代理程式可用工具或上傳檔案來源，且會影響實作，也不得產出完整 skill 產物，必須先問。只有在使用者已提供完整移植規格書，或已提供足以定義輸入、輸出、驗證、能力邊界與交付格式的資訊時，才可產出完整 skill 產物。缺少細節但可採明確預設時，必須列出採用的預設。
- **Gate 判定表**：

| 條件 | 是否可產完整 skill 產物 | 動作 |
|---|---:|---|
| 只有 skill 主題 | 不可 | 問必問項 |
| 只有主題＋「Joan 風格」或 `@gpt-skill-conventions` | 不可 | 問必問項 |
| 只有主題＋要求直接產出 | 不可 | 拒絕直接產完整 skill 產物，先對焦 |
| 已提供輸入、輸出、驗證、能力邊界、交付格式 | 可 | 列明契約後產出 |
| 已提供完整移植規格書 | 可 | 視為對焦完成 |
| 缺少 ChatGPT 應用程式（Apps）、MCP 工具、工作區代理程式可用工具或上傳檔案來源，且會影響實作 | 不可 | 必問 |
| 缺少細節但可用明確預設 | 可 | 必須列出預設 |
| 缺少細節會影響契約 | 不可 | 必問 |

- **ChatGPT 版技術調整：原因**：若使用者的任務已像移植規格書一樣完整，視為對焦已完成，可直接執行；若規格不足，必問項不得省略。
- **反例**：拿到「分數加法」就直接生一份，沒問是國小三年級還是國中補救，深度全錯、整份重做。另一反例是只收到「Excel 測試報告整理」與「直接開始產出」就直接生成完整 skill 產物。

## 三種模式（沿用 course-handout-generator 心法，每支都支援）

- **套用**：指名既有版型／皮膚，穩定批量產出。
- **探索**：換配色／版型／密度，每次給不同調性，重做到滿意。
- **模仿**：上傳一份喜歡的參考，抽色票與版面樣式凍結成新版型（插畫部分不模仿）。

探索與模仿產生的新版型或新皮膚，一律走 registry 擴充路徑：往 `SKINS` 或 preset 加新具名項，永不觸碰 `FROZEN` 集合內的既有項。新項起初為「可調」；經使用者定版後才加入 `FROZEN` 並記入 `FROZEN.md`。「多元」與「凍結」不衝突：多元等於擴充，凍結等於既有項不動。

## 滿意度確認迴圈

每次交付後必問是否滿意。視覺問題（配色、字體）就調參數重出；內容問題就修內容重跑驗證。重做不限次數。不要省略這一步。

## 多格式交付（缺一不可，全部 present_files）

依 skill 決定，常見組合：HTML（單檔自包含）＋ PDF（列印就緒）＋ PNG（多頁打包成 zip）。教學文件再加 docx（走 `docx` skill）。各格式的驗證推定成立條件與範圍寫死：PDF／PNG 須由通過全部驗證器、且其後未再修改的同一份 HTML 直接匯出，驗證通過與匯出之間不得有任何寫入 HTML 的步驟；若匯出腳本本身會注入文字（頁眉、頁碼、浮水印），推定即斷，須對匯出結果另行驗證。滿足前提時，內容類驗證（標點、數理、KaTeX、領域結構）視同通過，因渲染引擎不會無中生有。版面類驗證永遠不在推定範圍：PDF 截斷須在列印模式逐頁實量（門檻依房規二），PNG 須以實際輸出尺寸檢查裁切。實務上最穩的接線：匯出腳本在匯出前自行重跑一次 `validate_punct.py`，把推定變回實測。docx 為獨立產物，不適用任何推定，其中文內文須另跑一次 `validate_punct.py`（先轉出純文字或直接掃 document.xml 的文字節點）。

## 新 skill 開工檢查表

開一支新 skill 前，先回答：

1. **定位**：和既有五包的分工？會不會和某支重疊（重疊就不要新開，去升級那支）。
2. **三層**：骨架是什麼？皮膚有哪些（哪個先凍結）？版型怎麼依內容選？
3. **能力邊界**：界外是什麼？降級階梯怎麼排？
4. **對焦閘門**：開場要停下來問哪幾關？哪些能從語意判斷不問？
5. **驗證層**：要疊哪些驗證器（全形＋禁破折號是基本盤；含數理加 SymPy；含頁面加截斷量測）？
6. **相依與外部能力**：用到哪些重套件？bootstrap 怎麼自動裝？是否需要 ChatGPT 應用程式（Apps）、MCP 工具、工作區代理程式可用工具或上傳檔案？
7. **交付格式**：哪幾種格式？
8. **回歸測試**：純邏輯（不需重相依的部分）怎麼寫成 `tests/test_*.py`？凍結契約要不要寫成斷言守門？

## 交付前驗證清單

1. [ ] `validate_punct.py` 全形＋禁破折號，退出碼 0。
2. [ ] 含數理：SymPy 重算每題，全對。
3. [ ] 含 KaTeX：無殘留佔位、無 katex-error。
4. [ ] 含固定版面：頁面截斷逐頁量測，每頁溢出 ≦ 2px（溢出等於該頁內容最底元素的 bottom 座標，超出可列印區底邊的像素數；門檻定義以房規二為準）。
5. [ ] 含領域結構（化學等）：先過結構或反應驗證再繪圖。
6. [ ] 凍結契約沒被動到（跑 `tests/test_*.py` 回歸測試，凍結值斷言全綠）。
7. [ ] 相依由 `bootstrap.ensure_*` 自動安裝（ensure 在 import 之前）、字型與 KaTeX 內嵌，離線可印、免手動 pip。
8. [ ] 多格式齊備，全部 present_files。
9. [ ] 交付後問使用者是否滿意。

## 共用資產與參考

- `assets/manifest.json`：共用正本清單。列出每個正本檔與它在各包內的目標相對路徑，`sync_validator.py` 依此同步；未來新增共用資產只要加一筆，不必改同步器。
- `assets/validate_punct.py`：唯一正本的全形＋禁破折號驗證器（支援 `.html` 與 `.md`）。新 skill 直接複製到自己的 `scripts/`，不要各寫一份分歧版本。
- `assets/bootstrap.py`：唯一正本的相依自動安裝器（分顆粒 `ensure_*`、冪等、必留 log）。各包複製後依自身相依裁剪。
- `scripts/sync_validator.py`：把 manifest 內所有正本一鍵同步到各包，避免分歧。`--check` 只檢查漂移不寫入（可接 CI）；不傳目標會自動探索同層含 `scripts/validate_punct.py` 的包。
- `tests/test_conventions.py`：本包自身的回歸測試（房規二不豁免自己）。驗 `validate_punct.py` 乾淨過、髒的擋、破折號擋、連字號放行、`.md` 略過程式碼區塊；驗 bootstrap 裝過不重裝、缺了會裝（攔截不真裝）；驗 sync 的漂移偵測。改動本包任何腳本後必跑。
- `references/canonical-snippets.md`：可複製的標準片段，包含凍結契約寫法、bootstrap 自動安裝、對焦閘門模板、能力邊界模板、回歸測試骨架、版號戳記格式。
- `references/migration-map.md`：十九項移植對照表。更新技能時必同步維護。
- 通用 skill 製作流程（draft→test→iterate→package）見 `skill-creator`，本房規與它並用。
