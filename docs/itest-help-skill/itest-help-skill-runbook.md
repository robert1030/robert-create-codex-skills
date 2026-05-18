# iTest Help Skill 更新流程 Runbook

這份文件記錄如何從 Spirent iTest Automation help HTML 產生可攜式 `itest-help` Codex skill。下次更新到 iTest 26.5 或其他版本時，照這份流程替換版本路徑並重跑即可，不需要重新推導整個流程。

## 目標

產出一個可安裝到 Codex CLI / Codex Desktop 的 skill：

```text
itest-help/
  SKILL.md
  agents/openai.yaml
  scripts/search_help.py
  references/help_pages.jsonl
  references/search_index.json
  references/search_index_summary.json
```

重要原則：

- skill 必須自足，不依賴原始 `topics/` HTML 目錄。
- zip 檔名可以帶版本，例如 `itest-help_v25.4.zip`。
- zip 內部頂層資料夾必須仍是 `itest-help/`。
- 解壓後必須是 `.codex/skills/itest-help/SKILL.md`。
- `SKILL.md` frontmatter 的 `name` 必須是 `itest-help`。

## 目前 25.4 版本來源

原始 iTest help HTML：

```text
F:\MyCode\Java\iTest25.4\com.fnfr.svt.help_25.4.0.202512121840\topics
```

目前 25.4 中，`topics` 遞迴 `.htm` + `.html` 應為：

```text
963
```

25.4 的分布：

```text
topics                  761
topics\popups           166
topics\popups\arules     36
```

工作區版 skill：

```text
F:\MyCode\Java\iTest25.4\itest-help
```

已安裝版 skill：

```text
C:\Users\robert\.codex\skills\itest-help
```

打包輸出：

```text
F:\MyCode\robert-create-codex-skills\dist\itest-help.zip
```

## 更新到新版本時的建議資料夾

以 iTest 26.5 為例，建議先整理成類似：

```text
F:\MyCode\Java\iTest26.5\
  com.fnfr.svt.help_<actual-version>\
    topics\
  itest_help_inventory\
  itest_help_skill_data\
  itest-help\
```

`<actual-version>` 以實際解出的 help plugin 資料夾名稱為準。

## Step 1: 建立 Inventory

目的：列出 `topics` 底下所有遞迴 `.htm/.html`，抽出檔名、相對路徑、title、H1、doc_set、可能分類。

可重用 25.4 產生的腳本：

```text
F:\MyCode\Java\iTest25.4\itest_help_inventory\build_inventory.ps1
```

對新版本執行時，帶入新路徑：

```powershell
& "F:\MyCode\Java\iTest25.4\itest_help_inventory\build_inventory.ps1" `
  -SourceDir "F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_<actual-version>\topics" `
  -OutputDir "F:\MyCode\Java\iTest26.5\itest_help_inventory"
```

預期輸出：

```text
itest_help_inventory.csv
itest_help_inventory.json
category_summary.csv
```

驗證：

```powershell
Import-Csv "F:\MyCode\Java\iTest26.5\itest_help_inventory\itest_help_inventory.csv" | Measure-Object
Import-Csv "F:\MyCode\Java\iTest26.5\itest_help_inventory\itest_help_inventory.csv" | Where-Object { [string]::IsNullOrWhiteSpace($_.title) } | Measure-Object
```

確認：

- inventory 筆數等於新版本 `topics` 遞迴 `.htm/.html` 數量。
- `relative_path` 必須保留子目錄，例如 `popups/query.html`，因為子目錄中可能有同名檔案。
- 空白 title 可以存在於 popup 類短文件；先抽樣確認文字內容可用，不要只用空白 title 判定失敗。

## Step 2: 建立純文字資料與搜尋索引

目的：把 HTML 轉成 skill 可查詢的資料。skill 後續查 `help_pages.jsonl` 與 `search_index.json`，不直接查原始 HTML。

可重用 25.4 產生的腳本：

```text
F:\MyCode\Java\iTest25.4\itest_help_skill_data\build_search_index.py
F:\MyCode\Java\iTest25.4\itest_help_skill_data\search_help.py
```

對新版本執行：

```powershell
python "F:\MyCode\Java\iTest25.4\itest_help_skill_data\build_search_index.py" `
  --source-dir "F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_<actual-version>\topics" `
  --inventory "F:\MyCode\Java\iTest26.5\itest_help_inventory\itest_help_inventory.csv" `
  --output-dir "F:\MyCode\Java\iTest26.5\itest_help_skill_data"
```

預期輸出：

```text
help_pages.jsonl
search_index.json
search_index_summary.json
```

驗證：

```powershell
(Get-Content "F:\MyCode\Java\iTest26.5\itest_help_skill_data\help_pages.jsonl" | Measure-Object -Line).Lines
python "F:\MyCode\Java\iTest25.4\itest_help_skill_data\search_help.py" "parameter merging logic" --data-dir "F:\MyCode\Java\iTest26.5\itest_help_skill_data" --top 3
python "F:\MyCode\Java\iTest25.4\itest_help_skill_data\search_help.py" "QuickCall arguments" --data-dir "F:\MyCode\Java\iTest26.5\itest_help_skill_data" --top 3
python "F:\MyCode\Java\iTest25.4\itest_help_skill_data\search_help.py" "response map" --data-dir "F:\MyCode\Java\iTest26.5\itest_help_skill_data" --top 3
python "F:\MyCode\Java\iTest25.4\itest_help_skill_data\search_help.py" "query" --data-dir "F:\MyCode\Java\iTest26.5\itest_help_skill_data" --top 5
python "F:\MyCode\Java\iTest25.4\itest_help_skill_data\search_help.py" --show-file "topics/popups/query.html" --data-dir "F:\MyCode\Java\iTest26.5\itest_help_skill_data" --text
```

確認：

- `help_pages.jsonl` 行數等於 inventory 筆數。
- 常用查詢能找回合理 help page。
- 同名檔案必須用 `topics/...` 或 `relative_path` 查，例如 `topics/popups/query.html`；只查 `query.html` 可能會回報多筆相符。

## Step 3: 建立或更新 Skill 資料夾

新版本可以複製既有 25.4 skill 當基底：

```powershell
Copy-Item "F:\MyCode\Java\iTest25.4\itest-help" "F:\MyCode\Java\iTest26.5\itest-help" -Recurse -Force
```

然後覆蓋 references：

```powershell
Copy-Item "F:\MyCode\Java\iTest26.5\itest_help_skill_data\help_pages.jsonl" "F:\MyCode\Java\iTest26.5\itest-help\references\help_pages.jsonl" -Force
Copy-Item "F:\MyCode\Java\iTest26.5\itest_help_skill_data\search_index.json" "F:\MyCode\Java\iTest26.5\itest-help\references\search_index.json" -Force
Copy-Item "F:\MyCode\Java\iTest26.5\itest_help_skill_data\search_index_summary.json" "F:\MyCode\Java\iTest26.5\itest-help\references\search_index_summary.json" -Force
```

如果 `SKILL.md` description 要標明版本，可以把 `25.4` 改成 `26.5`，但 skill name 不要改：

```yaml
name: itest-help
```

## Step 4: 清理可攜性

打包前，references 不應保留本機絕對路徑，例如 `F:\MyCode\...`。

檢查：

```powershell
Select-String -Path "F:\MyCode\Java\iTest26.5\itest-help\references\*.json*" -Pattern "F:\\MyCode|com.fnfr.svt.help" | Measure-Object
```

若有殘留，將 `source_path` 或 Eclipse help link 改成邏輯來源：

```text
source_ref: topics/<relative_path>
```

25.4 時已採用這個格式。查詢結果應該看到：

```text
source_ref: topics/quickcalls_arguments_in_quickcall_steps.htm
source_ref: topics/popups/arules/query.html
```

## Step 5: 安裝到本機 Codex Skills

同步工作區版到本機 skills：

```powershell
Copy-Item "F:\MyCode\Java\iTest26.5\itest-help" "C:\Users\robert\.codex\skills\itest-help" -Recurse -Force
```

驗證安裝版：

```powershell
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" "parameter merging logic" --top 2
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" --show-file "topics/popups/query.html" --text
(Get-Content "C:\Users\robert\.codex\skills\itest-help\references\help_pages.jsonl" | Measure-Object -Line).Lines
```

## Step 6: 打包

使用 `$skill-packager`：

```powershell
python "C:\Users\robert\.codex\skills\skill-packager\scripts\package_skill.py" `
  "C:\Users\robert\.codex\skills\itest-help" `
  "F:\MyCode\robert-create-codex-skills\dist"
```

預設輸出：

```text
F:\MyCode\robert-create-codex-skills\dist\itest-help.zip
```

如果要版本化 zip 檔名，可以打包後重新命名：

```powershell
Rename-Item `
  "F:\MyCode\robert-create-codex-skills\dist\itest-help.zip" `
  "itest-help_v26.5.zip"
```

注意：只改 zip 檔名，不要改 zip 內部的 `itest-help/` 資料夾名稱。

## Step 7: 驗證 Zip

檢查 zip 內容：

```powershell
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead("F:\MyCode\robert-create-codex-skills\dist\itest-help_v26.5.zip")
$zip.Entries | Select-Object FullName,Length | Format-Table -AutoSize
$zip.Dispose()
```

必須包含：

```text
itest-help/SKILL.md
itest-help/agents/openai.yaml
itest-help/scripts/search_help.py
itest-help/references/help_pages.jsonl
itest-help/references/search_index.json
itest-help/references/search_index_summary.json
```

檢查 zip 展開後沒有本機絕對路徑：

```powershell
$tmp = Join-Path $env:TEMP "itest-help-zip-check"
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
Expand-Archive "F:\MyCode\robert-create-codex-skills\dist\itest-help_v26.5.zip" -DestinationPath $tmp -Force
Select-String -Path (Join-Path $tmp "itest-help\references\*.json*") -Pattern "F:\\MyCode|com.fnfr.svt.help" | Measure-Object
Remove-Item $tmp -Recurse -Force
```

結果應為：

```text
0
```

## 搬到別台機器

把 zip 複製到目標機器後，解壓到該機器的 Codex user skills 目錄，結果必須是：

```text
C:\Users\<user>\.codex\skills\itest-help\SKILL.md
```

不要變成：

```text
C:\Users\<user>\.codex\skills\itest-help_v26.5\SKILL.md
```

否則資料夾名稱會和 skill name 不一致。

## 下次請 Codex 接手時可以貼的提示

最簡單版：

```text
請依照 F:\MyCode\robert-create-codex-skills\docs\itest-help-skill-runbook.md
把 iTest Help skill 更新到 iTest 26.5。
新的 help topics 目錄是：<新路徑>
```

使用時，把 `<新路徑>` 換成實際的 `topics` 資料夾路徑。不要保留 `<` 和 `>`。

例如：

```text
請依照 F:\MyCode\robert-create-codex-skills\docs\itest-help-skill-runbook.md
把 iTest Help skill 更新到 iTest 26.5。
新的 help topics 目錄是：F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_26.5.0.xxxxxxxxxxxx\topics
```

完整任務版：

```text
請依照 F:\MyCode\robert-create-codex-skills\docs\itest-help-skill-runbook.md
把 iTest Help skill 更新到 iTest <version>。

新的 help topics 目錄是：
<貼上新版本 topics 路徑>

請完成 inventory、search index、可攜 skill 更新、安裝到本機 skills、
並用 skill-packager 打包成 itest-help_v<version>.zip。
```

## 常見風險

- 只改 zip 檔名可以，不能改 skill 資料夾名稱。
- `SKILL.md` 的 `name` 必須維持 `itest-help`。
- references 裡不能留下本機絕對路徑。
- 子目錄納入後會有同名檔案；搜尋結果與引用要使用 `source_ref` / `relative_path`，不要只依賴 `file_name`。
- 原始 HTML 可以不打包；目前 skill 查的是清理後的 `help_pages.jsonl` 與 `search_index.json`。
- 如果新版本 help 結構大改，先抽樣檢查 title/H1/doc_set 是否仍能正確抽出。
