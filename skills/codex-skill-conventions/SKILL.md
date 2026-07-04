---
name: codex-skill-conventions
description: "Joan（酒 Ann／vibe-expert.com）在 Codex 平台上開發 skill 的房規與轉換器。當使用者在 Codex 環境要新開一支 skill、把既有的 Claude skill（尤其是套用 joan-skill-conventions 房規的包）移植到 Codex、檢視或升級既有 Codex skill、為 skill 補齊 agents/openai.yaml、寫驗證器或回歸測試、或討論 skill 的版型／驗證／交付架構時，立即讀此 skill，套用以下十條房規：①凍結契約＋另開新版（絕不就地改定版）②驗證即閘門、絕不靠肉眼③全形標點＋禁破折號鐵則④引擎／皮膚／內容三層正交、跨學科通用⑤能力邊界誠實＋降級階梯不造假⑥透明自動安裝、偵測執行環境不寫死旗標⑦生成前強制對焦閘門⑧重試上限三輪、超過就升級回報⑨驗收不自驗（fresh-context 驗收）⑩Codex 外殼契約，agents/openai.yaml 與 name／description frontmatter 不可省。內含可執行的轉換器 scripts/convert_from_claude_skill.py，能讀取一支 Claude skill 資料夾，自動產生 agents/openai.yaml 草稿、掃出需要人工改寫的 Claude 專屬用語、並跑 frontmatter 格式檢查。觸發詞包含：開新 skill、做一個 skill、寫一支 skill、升級 skill、檢視 skill、重構 skill、skill 房規、skill 規範、驗證器、凍結契約、回歸測試、重試上限、fresh-context 驗收、交付前檢查、移植到 Codex、轉成 Codex skill、agents openai yaml 等。即使只說『幫我把這支 skill 弄到 Codex 上』也應先讀此 skill 套用房規。通用的 skill 製作流程（draft→test→iterate→package）仍走 Codex 自帶的 skill-creator；本 skill 只在其上疊加房規、品味與轉換工具，兩者並用。"
---

# Codex Skill Conventions（Joan 房規．Codex 版）

> **v1.2.1｜2026-07-04**：跨平台指令措辭修正。文件與測試說明不再寫死 python3；Linux／Ubuntu 的 python3 是指向 python3.x 的符號連結，Windows 官方安裝器只有 python 與 py 啟動器（PEP 397），預設沒有 python3。程式邏輯不變（測試內部本就使用 sys.executable）。
> **v1.2｜2026-07-04**：對齊 `joan-skill-conventions` v1.2。驗證器同步為 v2.1 正本（自我合規＋補四個偵測盲區）；`sync_validator.py` 自動探索路徑修正（上兩層才找得到兄弟包）；新增房規八（重試上限三輪）、房規九（驗收不自驗）、維護協議與 `LESSONS.md` 教訓帳本；原第八條「Codex 外殼契約」改列第十條；新增本包自己的 `tests/test_validate_punct.py` 回歸測試；修正 `convert_from_claude_skill.py` 內文的半形標點。
> **v1.1｜2026-07-01**：把 `joan-skill-conventions`（Claude 版房規）移植到 Codex skill 格式。七條房規原則保留，第六條改寫成環境偵測版；新增第八條「Codex 外殼契約」；明確補上 Codex 對焦閘門不依賴特定互動式 UI，以及開工檢查表是交付閘門、不是建議清單；附一支可執行轉換器 `scripts/convert_from_claude_skill.py`，能把任何遵守 Joan 房規的 Claude skill 轉成 Codex skill 骨架。

這是一份**房規（house rules）**，疊加在 Codex 自帶的 `skill-creator` 之上。Codex 的 `skill-creator` 教「怎麼在 Codex 上做出一支 skill」（`init_skill.py`→編輯→`quick_validate.py`→迭代）；本 skill 教「Joan 的 skill 在 Codex 上長什麼樣、守什麼規矩」。兩者並用：先依 Codex `skill-creator` 的流程走，每一步用本房規把關品味與正確性。

本 skill 的知識內容（十條房規、三種模式、驗證清單）和 `joan-skill-conventions` 完全一致，因為房規本身跟執行 skill 的模型無關；差異只在**外殼結構**（Codex 需要 `agents/openai.yaml`）和**少數幾句預設讀者是 Claude 的用語**。若你手上的來源是一支 Claude skill，直接用本 skill 的轉換器（見下）處理外殼，房規內文照搬。

---

## 十條房規（一至九沿用 joan-skill-conventions v1.2，第十條為 Codex 新增）

### 一、凍結契約，另開新版，絕不就地改定版
一旦某個版型／座標／色票／皮膚定版，就**寫死成凍結契約**，之後要改一律另開新版本，不動凍結版。

- **怎麼落實**：把定版的固定值集中寫死，並在程式裡用一個 `FROZEN` 集合或常數標記。每包放一份 `FROZEN.md` 當帳本，記下每個版本鎖了什麼、定版檔是哪幾個。SKILL.md 開頭放版號戳記。
- **回歸守門**：把凍結值寫成測試斷言，有人改色就紅燈。
- **凍結可擴充版型庫**：版型／皮膚做成一個**具名 registry**，其中一個以上設為凍結。擴充＝往 registry 加一組 token，**不動凍結項**；不指定＝沿用 `DEFAULTS`，向後相容。範式見 `references/canonical-snippets.md` 第十段。
- **反例**：直接在原檔改色票／改座標「順手調一下」。這會讓既有產出無法重現，是大忌。

### 二、驗證即閘門，絕不靠肉眼
每支 skill 的交付都要有**強制驗證器**，退出碼非零一律不准交付。正確性外包給程式，不信任目視。

- **標準驗證層**：全形標點＋禁破折號（`assets/validate_punct.py`，共用資產）、頁面截斷量測、數理正確性（SymPy 重算比對）、KaTeX 渲染檢查、領域正確性（且驗證先於繪圖）。
- **回歸自測**：每支 skill 放 `tests/test_*.py`，把純邏輯函式、凍結契約斷言、缺料降級分支、自動安裝邏輯（攔截 `_pip`／subprocess，不觸發真實安裝）全寫成測試。改動引擎後必跑、全 PASS 才算沒踩到既有契約。範式見 `references/canonical-snippets.md` 第九段。
- **Codex 額外一道**：交付前另跑 Codex 自帶的 `quick_validate.py <skill 目錄>`，確認 frontmatter 只有 `name`／`description`（或允許清單內欄位）且格式合規，這是 Claude 版沒有的第三方驗證層。
- **反例**：「看起來對就交付」。尤其數值與頁面截斷，肉眼最常漏。

### 三、全形標點＋禁破折號（個人排版鐵則）
中文一律全形標點，只有英數之間用半形；**破折號一律禁用**。

- **規則**：逗號「，」句號「。」頓號「、」冒號「：」分號「；」問號「？」驚嘆號「！」引號「「」『』」括號「（）」全用全形。`1,000`、`KaTeX`、`CO₂` 這種英數之間才用半形。
- **禁破折號**：不得用雙連續長破折號、單個 em dash（U+2014）或 en dash（U+2013）。需要斷句改用全形句號、逗號、冒號或頓號。
- **怎麼落實**：用共用的 `assets/validate_punct.py`，交付前必跑、非零不交付。新 skill 直接複製這支，不要各寫一份。這條規則和平台無關，Codex 對全形標點的理解不會比 Claude 差，純粹是排版鐵則，不是相容性問題。
- **反例**：在中文裡夾半形逗號、用破折號斷句。連 SKILL.md 自身與驗證器訊息都要守。

### 四、引擎／皮膚／內容三層正交，跨學科通用
**引擎只管骨架、皮膚與版型，內容是什麼學科都能填。** 把視覺和內容徹底解耦。

- **三層**：骨架（固定結構）× 皮膚（可換的色彩 token 組）× 版型（依內容形狀選）。再外層是「系列」（一套皮膚 × N 張）。
- **跨學科**：引擎不綁科目；用「學科 → 預設」對照表自動帶視覺工具與主色，使用者沒指定就照預設。
- **反例**：把某個學科的內容寫死進引擎，換科目就要改引擎。

### 五、能力邊界誠實，降級階梯不造假
明白宣告做不到的事，不硬做、不假裝；缺料就**有尊嚴地降級**，不留醜空洞、不編造。

- **怎麼落實**：每支 skill 寫一段「能力邊界（先講清楚，別硬做）」，列出界外項。視覺走**降級階梯**，缺料降級成字形大字。數值「不確定標（需查證），絕不編造」。
- **轉換器也守這條**：`scripts/convert_from_claude_skill.py` 掃到疑似 Claude 專屬用語時，只列清單交人工改寫，**不自動代寫**，因為自動代寫語意容易失真，等於編造。
- **反例**：使用者要 AI 插畫卡就硬生一張來源不明的圖；分子量沒把握就填一個看起來合理的數字。

### 六、透明自動安裝，偵測執行環境，不寫死旗標（Codex 改寫版）
相依套件自動裝、對使用者透明；交付物單檔自包含、離線可印。**Claude 版固定在同一個 Ubuntu 沙箱，可以放心寫死 `pip ... --break-system-packages`；Codex 常跑在使用者自己的機器上，作業系統與 Python 安裝方式都不一定，所以每次安裝前才判斷這個環境需不需要、允許不允許那個旗標，不能照抄 Claude 版的假設。**

- **環境偵測**：`scripts/bootstrap.py` 提供 `ensure(*modules, pip_names=..., log=...)`，內部用 PEP 668 的 `EXTERNALLY-MANAGED` 標記檔判斷是否需要 `--break-system-packages`，並判斷是否已在虛擬環境中；裝不了就誠實回報、建議手動建立虛擬環境，不假裝成功（呼應房規五）。
- **關鍵接線**：`ensure_*` 必須在對應的 `import` 之前呼叫（頂層 `from playwright import …` 在套件缺席時會直接 `ImportError`）。
- **離線自包含**：字型子集化為 woff2 後 base64 內嵌；KaTeX 伺服端預渲染並內嵌字型，絕不讓瀏覽器開檔時才從 CDN 載。產出列印就緒。
- **驗證器正本只放一處**：用 `scripts/sync_validator.py` 同步到各包，不要各寫一份。
- **反例**：叫使用者自己 `pip install`；把 `--break-system-packages` 寫死在每一支 `_pip()` 裡，換到非 Debian／非 externally-managed 環境會直接安裝失敗或裝進錯的環境。

### 七、生成前強制對焦閘門
**嚴禁拿到主題就直接生。** 開場先停下來，把結構與規格對焦清楚，得到同意才動工。

- **怎麼落實**：依 skill 性質設一道必須停下的閘門。能從語意判斷的就不問，問得少、問得準。
- **Codex 表面差異**：對焦閘門不依賴特定 UI。Codex 不保證像 Claude AI 一樣跳出互動式選擇對話框；若目前環境沒有互動式選項工具，必須改用一般對話提出最少必要問題。若問題可由上下文判斷，必須明列假設再繼續，不得因為沒有互動式對話框就跳過對焦閘門。
- **轉換器也守這條**：轉換器只產生草稿與報告，**不自動覆蓋房規知識本身的判斷**，人工確認 `agents/openai.yaml` 字數與用詞、改寫疑似 Claude 用語之後才算轉換完成。
- **反例**：拿到「分數加法」就直接生一份，沒問是國小三年級還是國中補救，深度全錯、整份重做。

### 八、重試上限三輪，超過就升級回報
任何「修正→重跑驗證」的迴圈，**同一個失敗原因最多重試三輪**。第三輪仍紅燈，停止修改，向使用者回報，回報必含三件事：失敗的驗證器名稱與完整輸出、三輪各改了什麼、你猜測的根因。

- **判準**：「同一個失敗原因」以驗證器輸出的錯誤類別認定（例：同樣是頁面溢出就算同一原因，即使溢出的頁碼不同）。換了失敗原因，計數歸零重算。
- **與滿意度迴圈的分界**：使用者主動要求重做，不受三輪限制（那是需求變更，不是失敗重試）。三輪限制只管「模型自己修自己的錯」。
- **反例**：驗證器連紅七輪還在原地換寫法硬試，燒光額度又交不了差。

### 九、驗收不自驗（fresh-context 驗收）
寫的人不能自己宣布通過。驗收一律交給「沒看過生成過程的檢查者」。

- **程式碼**：跑 `tests/test_*.py` 與各驗證器（本來就是外部程序，符合本條）。
- **文件類產出**（SKILL.md、FROZEN.md、教材文字）：交付前開一個沒有生成過程脈絡的新工作階段（新對話或子代理），只給它「檔案本身＋驗收條件清單」，要它逐條回報通過／不通過與證據行號。Codex 環境可用子代理或另開 session 達成，重點是檢查者不得帶著生成脈絡。
- **高風險判斷**（動到凍結契約、刪除既有功能、改共用正本）：除上述外，再加第二意見。作法：用相同輸入產生兩個獨立答案，列出分歧點，分歧處回報使用者裁決，不自行擇一。
- **反例**：改完自己讀一遍說「看起來沒問題」就交付。這是房規二「絕不靠肉眼」的文件版。

### 十、Codex 外殼契約，`agents/openai.yaml` 不可省（Codex 新增）
Codex 只認 `SKILL.md` frontmatter 裡的 `name`／`description`（其餘允許欄位：`license`／`allowed-tools`／`metadata`），任何 UI 中繼資料一律移到 `agents/openai.yaml`，不准塞進 frontmatter。

- **命名規則**：`name` 只能小寫字母、數字、連字號，六十四字以內，不可開頭結尾連字號或連續連字號；資料夾名稱必須和 `name` 完全一致。
- **`agents/openai.yaml` 必填三欄**：`display_name`（人看的標題）、`short_description`（二十五至六十四字的一句話）、`default_prompt`（**必須**明確含 `$skill-name`，例如「使用 $codex-skill-conventions 檢查這支 skill 是否符合房規」）。選填欄位（`icon_small`／`icon_large`／`brand_color`）只在使用者明確提供時才加。
- **description 上限**：一千零二十四字，超過會被 Codex 的 `quick_validate.py` 擋下，寫房規描述時要留意篇幅。
- **明確呼叫**：Codex 使用者可以直接打 `$skill-name` 點名呼叫，這是 Claude 版沒有的機制；`policy.allow_implicit_invocation` 預設為 `true`（維持「使用者只說『幫我做一個 skill』就自動觸發」的行為），除非刻意要求只能明確呼叫才需要手動設為 `false`。
- **反例**：把 `display_name`／版本號／icon 這類欄位直接塞進 `SKILL.md` 的 YAML frontmatter；`default_prompt` 沒寫 `$skill-name`。

---

## 轉換器：把 Claude skill 轉成 Codex skill

`scripts/convert_from_claude_skill.py` 把一支**遵守 joan-skill-conventions 房規**的 Claude skill 轉成 Codex 骨架，只動外殼、不碰房規知識本身：

```bash
python scripts/convert_from_claude_skill.py <來源 Claude skill 目錄> <輸出目錄>
```

它依序做：

1. **結構補件**：整包複製到輸出目錄（`SKILL.md`／`scripts`／`references`／`assets` 結構本來就相容，不用重整）。
2. **frontmatter 對齊**：讀出 `name`／`description`，檢查命名規則與一千零二十四字上限，超標或有 Codex 不認得的欄位一律列進報告。
3. **語意與用語轉換**：掃描內文，列出疑似「另一個 Claude 實例」「讓 Claude 知道」「claude.ai」等 Claude 專屬指涉的行號與原句，**只列清單、不自動代寫**（房規五、房規七）。
4. **環境相依重寫提示**：偵測到內文寫死 `--break-system-packages` 時提醒改用 `scripts/bootstrap.py` 的環境偵測版 `ensure()`。
5. **產生 `agents/openai.yaml` 草稿**：依 `name` 猜 `display_name`、依 `description` 截出 `short_description` 草稿，兩者都標 `TODO` 待人工確認字數與用詞；`default_prompt` 自動帶入 `$skill-name`。

跑完印出轉換報告，人工照報告改完之後，再跑 Codex 自帶的 `python scripts/quick_validate.py <輸出目錄>` 做最終格式驗收（房規二）。

---

## 三種模式（沿用 course-handout-generator 心法，每支都支援）
- **套用**：指名既有版型／皮膚，穩定批量產出。
- **探索**：換配色／版型／密度，每次給不同調性，重做到滿意。
- **模仿**：上傳一份喜歡的參考，抽色票與版面樣式凍結成新版型（插畫部分不模仿）。

## 滿意度確認迴圈
每次交付後**必問是否滿意**。視覺問題（配色、字體）→ 調參數重出；內容問題 → 修內容重跑驗證。重做不限次數。不要省略這一步。

## 多格式交付（缺一不可）
依 skill 決定，常見組合：HTML（單檔自包含）＋ PDF（列印就緒）＋ PNG（多頁打包成 zip）。教學文件再加 docx。

---

## 新 skill 開工檢查表

以下檢查表是**交付閘門**，不是建議清單。建立、移植、升級或審查 skill 時，除非使用者明確要求只做草稿，否則每一項都必須回答並落實；缺少任一必要項時，不得宣稱完成，必須列為阻擋項或明確說明不適用原因。

開一支新 Codex skill 前，先回答：

1. **定位**：和既有包的分工？會不會重疊（重疊就不要新開，去升級那支）。
2. **三層**：骨架是什麼？皮膚有哪些（哪個先凍結）？版型怎麼依內容選？
3. **能力邊界**：界外是什麼？降級階梯怎麼排？
4. **對焦閘門**：開場要停下來問哪幾關？哪些能從語意判斷不問？
5. **驗證層**：要疊哪些驗證器（全形＋禁破折號是基本盤；含數理加 SymPy；含頁面加截斷量測）？
6. **相依**：用到哪些重套件？`scripts/bootstrap.py` 的 `ensure()` 要傳哪些模組名？
7. **交付格式**：哪幾種格式？
8. **回歸測試**：純邏輯怎麼寫成 `tests/test_*.py`？凍結契約要不要寫成斷言守門？
9. **Codex 外殼**：`name`／資料夾名一致嗎？`agents/openai.yaml` 三個必填欄位都填了嗎？`default_prompt` 有沒有帶 `$skill-name`？

## 交付前驗證清單

1. [ ] `assets/validate_punct.py` 全形＋禁破折號，退出碼零。
2. [ ] 含數理：SymPy 重算每題，全對。
3. [ ] 含 KaTeX：無殘留佔位、無 katex-error。
4. [ ] 含固定版面：頁面截斷逐頁量測，溢出全零。
5. [ ] 含領域結構（化學等）：先過結構／反應驗證再繪圖。
6. [ ] 凍結契約沒被動到（跑 `tests/test_*.py` 回歸測試，凍結值斷言全綠）。
7. [ ] 相依由 `scripts/bootstrap.py` 的 `ensure()` 自動安裝，且會依環境判斷旗標、裝不了會誠實回報，不寫死。
8. [ ] `name` 與資料夾名稱一致、只含小寫字母數字連字號、六十四字以內。
9. [ ] `agents/openai.yaml` 三個必填欄位齊全，`default_prompt` 含 `$skill-name`。
10. [ ] 跑過 Codex 自帶的 `quick_validate.py`，退出碼零。
11. [ ] 多格式齊備，全部交付給使用者。
12. [ ] 文件類產出（含 SKILL.md 更新）過 fresh-context read-back 驗收（房規九）。
13. [ ] 任一驗證迴圈未超過三輪重試；有超過即停手，回報驗證器輸出、三輪修改內容與根因猜測（房規八）。
14. [ ] 交付後問使用者是否滿意。

---

## 維護協議（給未來每一個 session 的模型）

### 一、可以自行改的（改完必跑 `tests/test_validate_punct.py`（用你環境的 Python 啟動器：Linux／macOS 是 python3，Windows 是 py 或 python），全綠才算改完）
- 往 registry 加新皮膚／新版型（不動 `FROZEN` 集合內的項目）。
- 在 `LESSONS.md` 追加教訓（格式見下）。
- 補新的回歸測試案例（只准加，不准刪、不准放寬既有斷言）。
- 修正錯字、補範例，且改動範圍不觸及任何「怎麼落實」的規則語意。

### 二、動之前必須先問使用者的
- `FROZEN` 集合內任何值、`FROZEN.md` 既有條目。
- `assets/validate_punct.py` 正本的偵測邏輯（訊息文字可自改，規則不行）。
- 刪除或放寬任何驗證器、任何測試斷言。
- 房規一至十本身的語意。
- 版號進 major 的任何變更。

### 三、踩坑教訓寫回哪裡、用什麼格式
每次「驗證器抓到問題」或「三輪重試失敗」後，在本 skill 根目錄的 `LESSONS.md` 追加一條，固定四欄，一條不超過四行：

```markdown
## YYYY-MM-DD｜<一句話標題>
- 現象：<驗證器輸出的關鍵一行，或使用者指出的錯>
- 根因：<一句話>
- 對策：<改了哪個檔的哪條規則，或加了哪個測試>
- 已固化：<測試檔名或房規條號；寫「否」表示尚未固化，下次優先處理>
```

判準：**能寫成測試的教訓，一律寫成測試**，`LESSONS.md` 只留「還沒固化」與「無法測試化」的。

### 四、累積多長要精簡
`LESSONS.md` 超過 30 條，或「已固化」的條目超過半數時：把已固化條目濃縮成一行移到檔尾的「已固化索引」區，正文只留未固化條目。精簡屬於「可自行改」，但精簡前先跑一次 fresh-context read-back，確認沒有把未固化教訓誤刪。

### 五、交付一律是可直接安裝的完整包
不論 Codex 環境把 skill 裝在哪個目錄，所謂「更新」一律是：改好的檔案打包成完整可安裝的包交給使用者，由使用者重新安裝整包 skill。不要交付要人手動合併的補丁，也不要在未確認安裝完成前宣稱「已更新 skill」，正確說法是「已產出 vX.Y 完整包，待你重新安裝後生效」。

### 六、派工模板的歸屬（指路，不併入本檔）
搜尋、實作、重構、研究、審查五種委派模板屬於「跨 skill 的制度層」，不塞進單一房規檔。本檔只約定：凡委派出去的任務，prompt 必含三個填空：**驗收條件（可機器判定）、回報格式（固定欄位）、重試上限（預設三輪）**。缺任一項的委派 prompt 視為不合格，退回補齊。

---

## 共用資產與參考
- `assets/validate_punct.py`：**唯一正本**的全形＋禁破折號驗證器，和平台無關。新 skill 直接複製到自己的 `scripts/`，不要各寫一份分歧版本。
- `scripts/bootstrap.py`：Codex 版透明自動安裝範式，環境偵測版 `ensure()`，取代 Claude 版寫死的 `--break-system-packages`。
- `scripts/sync_validator.py`：把 `assets/validate_punct.py` 正本一鍵同步到各包的 `scripts/validate_punct.py`，避免分歧。`--check` 只檢查漂移不寫入。
- `scripts/convert_from_claude_skill.py`：把 Claude skill 轉成 Codex skill 骨架的可執行轉換器，見上方「轉換器」一節。
- `references/canonical-snippets.md`：可複製的標準片段（凍結契約寫法、Codex 版 bootstrap、對焦閘門模板、能力邊界模板、回歸測試骨架、`agents/openai.yaml` 模板、版號戳記格式）。
- `references/claude-vs-codex-diff.md`：Claude Skill 與 Codex Skill 的完整格式差異對照表，轉換遇到不確定的地方先查這份。
- `tests/test_validate_punct.py`：本包自己的回歸測試（驗證器自我合規、四類盲區、sync 探索、bootstrap 旗標邏輯、轉換器 frontmatter 檢查），改動任何腳本後必跑、全綠才交付。
- `LESSONS.md`：教訓帳本，格式與精簡規則見「維護協議」。
- 通用 skill 製作流程（`init_skill.py`→編輯→`quick_validate.py`→迭代）見 Codex 自帶的 `skill-creator`，本房規與它並用。
