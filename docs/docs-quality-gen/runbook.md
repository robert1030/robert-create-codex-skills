# docs-quality-gen Runbook

這份 runbook 說明如何建立、更新、同步與檢查 robert 個人的 `docs-quality-gen` 文件品質 gate。照著做時，先確認文件類型，再讀對應規則，最後做一致性、Windows/Linux 指令對照、HTML 基礎美化與可讀性檢查。

## 目標

產生或維護 `docs-quality-gen` 的文件時，結果應該包含：

```text
docs-quality-gen/
  SPEC.md
  runbook.md
  runbook.htm
```

這三份文件的分工：

- `SPEC.md` 說明 `docs-quality-gen` 必須做到什麼。
- `runbook.md` 說明如何操作與檢查文件。
- `runbook.htm` 是 `runbook.md` 的 HTML 同步版本，文字意思必須一致，也可以有基礎文件樣式。

## 目前環境範例

以下路徑是目前環境或常見環境的例子，不是所有電腦都適用。換到其他電腦時，請替換使用者名稱、磁碟代號與 workspace 路徑。

```text
Windows skill 位置:
C:\Users\robert\.codex\skills\docs-quality-gen

Windows 文件位置:
F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen

Ubuntu Bash 原生文件位置範例:
<workspace>/robert-create-codex-skills/docs/docs-quality-gen

WSL 對應目前 Windows F: 磁碟的文件位置範例:
/mnt/f/MyCode/robert-create-codex-skills/docs/docs-quality-gen
```

本 runbook 的指令分成 Windows PowerShell 與 Ubuntu Bash/sh。不要把 PowerShell 語法混進 Bash 區塊，也不要把 Bash 語法混進 PowerShell 區塊。`/mnt/f/...` 是 WSL 範例，不是原生 Ubuntu 的通用路徑。

## Step 1: 確認文件類型

目的：先判斷這次要做的是 SPEC、runbook、Markdown/HTML 同步、HTML/HTM 基礎美化、文件 review，還是最終交付檢查。

動作：

Windows PowerShell：

```powershell
Get-ChildItem -Path "F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen"
```

Ubuntu Bash/sh：

```bash
# Native Ubuntu example: replace <workspace> with the actual workspace path.
DOCS_DIR="<workspace>/robert-create-codex-skills/docs/docs-quality-gen"
ls -la "$DOCS_DIR"

# WSL example for the current Windows F: drive:
DOCS_DIR="/mnt/f/MyCode/robert-create-codex-skills/docs/docs-quality-gen"
ls -la "$DOCS_DIR"
```

預期輸出：

```text
SPEC.md
runbook.md
runbook.htm
```

驗證方式：

- 如果要改規格，主要檔案是 `SPEC.md`。
- 如果要改操作流程，主要檔案是 `runbook.md`，並同步 `runbook.htm`。
- 如果只做 review，不要順手改文件以外的交付物。

## Step 2: 讀取對應 reference

目的：只讀這次需要的規則，避免把不相關內容混進文件。

目前 skill reference 位於目前環境範例路徑：

```text
Windows:
C:\Users\robert\.codex\skills\docs-quality-gen\references

Ubuntu Bash native example:
<home>/.codex/skills/docs-quality-gen/references

WSL example for this Windows user profile:
/mnt/c/Users/robert/.codex/skills/docs-quality-gen/references
```

依文件類型讀取：

- SPEC：`spec-rules.md`
- Runbook：`runbook-rules.md`
- Markdown/HTML 同步：`markdown-html-sync.md`
- HTML/HTM 基礎美化：`html-basic-style.md`
- 指令環境對照：`command-environments.md`
- 交接或操作文件：`readability-grade7.md`
- 最終交付檢查：`final-review-checklist.md`

驗證方式：

- 本次文件類型有對應 reference。
- 沒有把 Word、iTest、公開通用風格指南或完整 HTML 視覺設計規則加入 v1.2。
- 如果要處理 `.htm/.html` 樣式，已讀取 `html-basic-style.md`。
- 如果要處理可執行指令，已讀取 `command-environments.md`。

## Step 3: 修改前確認成功標準

目的：先說清楚完成條件，避免做過頭或漏掉同步檢查。

每次修改前，先確認：

- 要改哪些文件。
- 哪些內容必須保持同步。
- 要用什麼方式驗證。
- 是否需要 Windows PowerShell 與 Ubuntu Bash/sh 兩種指令。
- 哪些事情不做，例如不打包、不安裝、不同步到 `.codex\skills`。

驗證方式：

- 成功標準中有明確的檔名。
- 如果有 Markdown/HTML 成對文件，成功標準有提到同步。
- 如果有可執行指令，成功標準有提到 Windows/Linux 指令對照，或說明為何只支援單一平台。
- 如果文件面向交接或操作，成功標準有提到七年級可讀性檢查。

## Step 4: 修改 SPEC

目的：讓 `SPEC.md` 說清楚 `docs-quality-gen` 的契約，不把操作步驟塞進規格。

動作：

1. 讀 `SPEC.md` 的相關段落。
2. 檢查範圍、非範圍、必要結構、必要流程與驗收條件。
3. 把本機路徑寫成目前環境範例，不要寫成永久規格。
4. 把觀察結果、範例與正式要求分清楚。

驗證方式：

- `SPEC.md` 沒有變成逐步操作手冊。
- 每個重要要求都能被檢查。
- `SPEC.md` 沒有加入 Word `.doc/.docx`、iTest 專案規則或公開通用文件規格。

## Step 5: 修改 runbook.md

目的：讓 `runbook.md` 成為照著做的流程。讀者要知道每一步的目的、動作、預期輸出與驗證方式。

動作：

1. 讀要修改步驟的前後文。
2. 確認前置條件先出現。
3. 確認檔名、路徑與輸出名稱前後一致。
4. 對容易誤解的地方加白話提醒。
5. 如果使用本機路徑，標示為目前環境範例。

驗證方式：

- 步驟順序沒有跳躍。
- 前一步產出的檔名，後一步沒有突然換名。
- PowerShell 指令與 Windows 路徑格式一致。
- Bash/sh 指令與 POSIX 路徑格式一致。
- WSL 路徑有標示為 WSL 範例。
- 高風險或容易誤解的操作有提醒。

## Step 6: 同步 runbook.htm

目的：讓 HTML 版本和 Markdown 版本表達同一件事。HTML 不是另一份自由改寫版。

動作：

1. 以 `runbook.md` 作為主要來源，確認每個標題與清單。
2. 在 `runbook.htm` 保留相同段落意思。
3. 用 `<code>` 標示短程式碼、路徑與檔名。
4. 用 `<pre><code>` 標示多行指令或目錄結構。
5. 如果要美化 HTML，先確認樣式不改變 Markdown 原意。

驗證方式：

Windows PowerShell：

```powershell
Select-String -Path "F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen\runbook.md","F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen\runbook.htm" -Pattern "Word","iTest","runbook.htm","七年級","PowerShell","html-basic-style","Ubuntu","Bash","command-environments.md"
```

Ubuntu Bash/sh：

```bash
# Native Ubuntu example: replace <workspace> with the actual workspace path.
DOCS_DIR="<workspace>/robert-create-codex-skills/docs/docs-quality-gen"
grep -RInE "Word|iTest|runbook\\.htm|七年級|PowerShell|html-basic-style|Ubuntu|Bash" "$DOCS_DIR/runbook.md" "$DOCS_DIR/runbook.htm"

# WSL example for the current Windows F: drive:
DOCS_DIR="/mnt/f/MyCode/robert-create-codex-skills/docs/docs-quality-gen"
grep -RInE "Word|iTest|runbook\\.htm|七年級|PowerShell|html-basic-style|Ubuntu|Bash" "$DOCS_DIR/runbook.md" "$DOCS_DIR/runbook.htm"
```

確認：

- 關鍵警告在兩邊都有。
- 路徑、檔名與不做事項在兩邊一致。
- Windows/Linux 指令對照在兩邊都有。
- HTML 沒有保留舊路徑、舊檔名或舊規則。

## Step 7: 做 HTML/HTM 基礎美化

目的：讓 HTML 文件更容易閱讀和掃描，但不改變內容意思，也不做完整網站設計。

動作：

1. 確認 HTML 有清楚的 `<title>` 和一個主要 `<h1>`。
2. 檢查 `<h2>`、`<h3>` 等標題順序，不要只為了字體大小而跳級。
3. 用條列式整理步驟、檢查點與短資訊。
4. 有分類或比較時，使用表格，並加入清楚的表頭。
5. 使用基礎色調區分標題、表格、提示、警告與程式碼區塊。
6. 保持樣式在本機 HTML 內，不主動加入遠端 CSS、字型或 JavaScript。

驗證方式：

- HTML 標題、條列式、表格與 code block 都容易掃描。
- 顏色有幫助閱讀，但沒有變成品牌頁或行銷頁。
- 樣式沒有新增、刪除或弱化任何規格要求。

## Step 8: 做七年級可讀性檢查

目的：讓交接或操作文件能先看懂主線，再看技術細節。

動作：

- 每段先說白話目的，再列技術細節。
- 一句話盡量只講一件事。
- 長段落拆成清單。
- 技術詞第一次出現時補意思。
- 不為了好懂而刪掉重要限制。

驗證方式：

- 讀者不用先懂 Codex skill 內部細節，也能知道文件要做什麼。
- 高風險限制，例如「不要把本機路徑寫成通用事實」，有用白話說明。
- 文件沒有變成兒童讀物，也沒有犧牲技術正確性。

## Step 9: 最終交付前檢查

目的：交付前確認文件一致、流程一致、內容不衝突，而且誠實說明沒做的事。

檢查清單：

- 格式一致：標題層級、清單格式與 code block 合理。
- 指令環境一致：Windows PowerShell 與 Ubuntu Bash/sh 指令都有，或已說明單平台原因。
- HTML 基礎美化一致：標題、條列式、表格分類、色調與 code block 不破壞內容。
- 流程一致：前置條件、步驟順序、檔名與驗證方式一致。
- 內容一致：SPEC、runbook、Markdown/HTML 沒有互相打架。
- 可讀性：主線清楚，七年級讀者能理解大方向。
- 交付誠實：說清楚改了什麼、驗證了什麼、沒做什麼。

驗證方式：

Windows PowerShell：

```powershell
Get-ChildItem -Path "F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen" | Select-Object Name,Length
Select-String -Path "F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen\SPEC.md","F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen\runbook.md","F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen\runbook.htm" -Pattern "docx","iTest","public","generic","HTML 基礎","Ubuntu","Bash","PowerShell"
```

Ubuntu Bash/sh：

```bash
# Native Ubuntu example: replace <workspace> with the actual workspace path.
DOCS_DIR="<workspace>/robert-create-codex-skills/docs/docs-quality-gen"
find "$DOCS_DIR" -maxdepth 1 -type f -printf '%f %s bytes\n'
grep -RInE "docx|iTest|public|generic|HTML 基礎|Ubuntu|Bash|PowerShell" "$DOCS_DIR/SPEC.md" "$DOCS_DIR/runbook.md" "$DOCS_DIR/runbook.htm"

# WSL example for the current Windows F: drive:
DOCS_DIR="/mnt/f/MyCode/robert-create-codex-skills/docs/docs-quality-gen"
find "$DOCS_DIR" -maxdepth 1 -type f -printf '%f %s bytes\n'
grep -RInE "docx|iTest|public|generic|HTML 基礎|Ubuntu|Bash|PowerShell" "$DOCS_DIR/SPEC.md" "$DOCS_DIR/runbook.md" "$DOCS_DIR/runbook.htm"
```

預期結果：

- 三份文件存在。
- `docx` 只出現在 v1.2 非範圍說明中。
- `iTest` 只出現在「不加入專案專屬規則」的限制中。
- `public` 與 `generic` 只出現在「不是公開通用規格或泛用助手」的限制中。
- `HTML 基礎` 只指文件可讀性美化，不代表完整網站設計。
- `Ubuntu`、`Bash`、`PowerShell` 出現在指令環境說明或對照指令中。

## 不做事項

除非使用者明確要求，本 runbook 不要求執行下列動作：

- 打包 skill。
- 安裝 skill。
- 同步 skill 到 `.codex\skills`。
- 產生 zip。
- 建立 Word `.doc` 或 `.docx` 文件。
- 加入 iTest 或其他專案專屬文件規則。
- 做完整品牌設計、互動式 UI 或行銷頁。
