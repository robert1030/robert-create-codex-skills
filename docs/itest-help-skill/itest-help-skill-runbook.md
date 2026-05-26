# iTest Help Skill 更新流程 Runbook

這份文件記錄如何從 Spirent iTest Automation help HTML 產生可攜式 `itest-help` Codex skill。下次更新到 iTest 26.5 或其他版本時，照這份流程替換版本路徑並重跑即可，不需要重新推導整個流程。

## 目標

產出一個可安裝到 Codex CLI / Codex Desktop 的 skill：

```text
itest-help/
  SKILL.md
  agents/openai.yaml
  scripts/search_help.py
  scripts/apply_toc_metadata.py
  references/help_pages.jsonl
  references/search_index.json
  references/search_index_summary.json
  references/toc_index.json
  references/help_index.json
  references/contexts_index.json
  references/interpreter-guide.md
  references/analysis-rule-wizard-guide.md
  references/regression-questions.md
```

重要原則：

- skill 必須自足，不依賴原始 `topics/` HTML 目錄。
- zip 檔名可以帶版本，例如 `itest-help_v25.4.zip`。
- zip 內部頂層資料夾必須仍是 `itest-help/`。
- 解壓後必須是 `.codex/skills/itest-help/SKILL.md`。
- `SKILL.md` frontmatter 的 `name` 必須是 `itest-help`。

## 執行環境

這份 runbook 目前是 Windows PowerShell 流程。原因是目前的 iTest 25.4 help plugin、inventory 腳本與安裝路徑都使用 Windows 本機路徑，例如 `F:\MyCode\...` 與 `C:\Users\robert\...`。

如果要在 Ubuntu、WSL 或其他機器更新新版 iTest help，請先把原始 `com.fnfr.svt.help_<actual-version>`、工作區路徑、Python 指令與安裝路徑改成該環境的實際路徑，再重跑 inventory、search index、TOC metadata 與驗證。不要直接把本文件中的 Windows 路徑當成 Linux 路徑使用。

## 目前 25.4 版本來源

原始 iTest help HTML：

```text
F:\MyCode\Java\iTest25.4\com.fnfr.svt.help_25.4.0.202512121840\topics
```

原始 iTest Online Help 目錄：

```text
F:\MyCode\Java\iTest25.4\com.fnfr.svt.help_25.4.0.202512121840\toc.xml
F:\MyCode\Java\iTest25.4\com.fnfr.svt.help_25.4.0.202512121840\index.xml
F:\MyCode\Java\iTest25.4\com.fnfr.svt.help_25.4.0.202512121840\contexts.xml
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

25.4 的 `toc.xml` 分布：

```text
iTest Online Help top-level labels    76
TOC topic nodes                       890
TOC href entries                      749
```

25.4 的 `index.xml` 與 `contexts.xml` 分布：

```text
Index topic refs                     1901
Index referenced topic pages          444
Index keyword paths                  1671
Contexts                              645
Context topic refs                    656
Context referenced topic pages        620
Context stale topic refs                1
Contexts without topics                 3
```

工作區版 skill：

```text
F:\MyCode\robert-create-codex-skills\skills\itest-help
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
    toc.xml
    index.xml
    contexts.xml
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

新版本可以複製目前維護中的 skill 當基底：

```powershell
Copy-Item "F:\MyCode\robert-create-codex-skills\skills\itest-help" "F:\MyCode\Java\iTest26.5\itest-help" -Recurse -Force
```

然後覆蓋 references：

```powershell
Copy-Item "F:\MyCode\Java\iTest26.5\itest_help_skill_data\help_pages.jsonl" "F:\MyCode\Java\iTest26.5\itest-help\references\help_pages.jsonl" -Force
Copy-Item "F:\MyCode\Java\iTest26.5\itest_help_skill_data\search_index.json" "F:\MyCode\Java\iTest26.5\itest-help\references\search_index.json" -Force
Copy-Item "F:\MyCode\Java\iTest26.5\itest_help_skill_data\search_index_summary.json" "F:\MyCode\Java\iTest26.5\itest-help\references\search_index_summary.json" -Force
```

如果既有 skill 已有 guardrail references，複製 skill 當基底時會一起保留：

```text
references/interpreter-guide.md
references/analysis-rule-wizard-guide.md
references/regression-questions.md
```

套用官方 iTest Online Help 目錄、index 與 context metadata：

```powershell
python "F:\MyCode\Java\iTest26.5\itest-help\scripts\apply_toc_metadata.py" `
  --toc-xml "F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_<actual-version>\toc.xml" `
  --index-xml "F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_<actual-version>\index.xml" `
  --contexts-xml "F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_<actual-version>\contexts.xml" `
  --references-dir "F:\MyCode\Java\iTest26.5\itest-help\references"
```

預期輸出會列出 `toc_root_label`、`toc_top_category_count`、`toc_href_entry_count`、`documents_with_toc`、`documents_with_index`、`documents_with_contexts`、`contexts_missing_source_ref_count` 和 `contexts_without_topic_count`。

驗證官方 help metadata：

```powershell
Get-Content "F:\MyCode\Java\iTest26.5\itest-help\references\search_index_summary.json" -Raw |
  ConvertFrom-Json |
  Select-Object document_count,toc_root_label,toc_top_category_count,toc_href_entry_count,documents_with_toc,documents_with_index,documents_with_contexts,help_index_topic_ref_count,help_index_referenced_source_count,contexts_count,contexts_missing_source_ref_count,contexts_without_topic_count

python "F:\MyCode\Java\iTest26.5\itest-help\scripts\search_help.py" "Field Replacements" --top 3
python "F:\MyCode\Java\iTest26.5\itest-help\scripts\search_help.py" "activitywiz_topo_edit_device_session" --top 3
python "F:\MyCode\Java\iTest26.5\itest-help\scripts\search_help.py" --list-scopes
python "F:\MyCode\Java\iTest26.5\itest-help\scripts\search_help.py" "Custom Extractor Custom Process" --top 4
python "F:\MyCode\Java\iTest26.5\itest-help\scripts\search_help.py" "Step Properties Analysis Rule Properties" --top 4
python "F:\MyCode\Java\iTest26.5\itest-help\scripts\search_help.py" "Step Properties Analysis Rule Properties" --top 4 --scope analysis_rule_processor_properties
```

確認：

- `toc_root_label` 應為 `iTest Online Help`，除非新版官方 help 已改名。
- 章節類查詢應顯示 `toc:` 行，例如 `iTest Online Help > Field Replacements > ...`。
- context ID 類查詢可用來定位候選頁，但回答產品行為時仍必須讀取該頁 `text`。
- `contexts_index.json` 應記錄 contexts without topics 與 missing/stale topic references。
- popup 或補充頁可以沒有 TOC path，但仍應可用 `source_ref` 查到。
- `--list-scopes` 應列出可用的 UI scope，例如 `analysis_rule_wizard_page`、`analysis_rule_processor_properties`、`step_properties_section`。
- `Custom Extractor Custom Process` 應顯示跨 UI scope 的 warning。回答時要分開說明 Analysis Rule Wizard、Analysis Rule Properties、custom session type 等不同位置。
- `Step Properties Analysis Rule Properties` 應顯示 Step Properties 與 Analysis Rule Properties 是不同 UI scope。
- `--scope` 只用來縮小候選頁；回答產品行為時仍必須讀取 help page `text`。

更新新版本時，請抽樣確認 guardrail 內列出的 source pages 在新版本仍存在；若檔名或行為改變，先更新 guardrail，再打包。

特別注意 `interpreter-guide.md` 的 clock/time conversion guardrail。這個檔案記錄 25.4 使用時觀察到的風險。

**問題**

在 iTest interpreter 直接使用 `[clock scan ...]` 做時間轉換時，近期日期可能正常。但遇到 2038 以後，或更大的未來日期，結果可能變成錯誤的負秒數。

**要驗證的情境**

這個風險不只跟 certificate expiration 或 `notAfter` 有關。只要是在處理日期、時間、秒數或時間比較，都要重新驗證：

- date/time string 轉 epoch seconds，也就是把日期文字轉成秒數
- timestamp comparison，也就是比較兩個時間誰早誰晚
- time arithmetic，也就是時間加減
- clock scan / clock format，也就是時間讀取和格式轉換
- 2041、2049 或其他 2038 以後日期

**如果新版本行為不同**

若新版本行為已改變，更新 `interpreter-guide.md` 與 `regression-questions.md`。請明確標示這是專案觀察到的行為，還是官方 help 已經明文寫出的行為。

如果 `SKILL.md` description 要標明版本，可以把 `25.4` 改成 `26.5`，但 skill name 不要改：

```yaml
name: itest-help
```

## Step 4: 清理可攜性

打包前，references 不應保留本機絕對路徑，例如 `F:\MyCode\...`。

檢查：

```powershell
Select-String -Path "F:\MyCode\Java\iTest26.5\itest-help\references\*.json*" -Pattern "F:\\MyCode|C:\\Users\\|com.fnfr.svt.help_[0-9]" | Measure-Object
```

若有殘留，將 `source_path` 或 Eclipse help link 改成邏輯來源：

```text
source_ref: topics/<relative_path>
```

`toc_index.json`、`help_index.json` 與 `contexts_index.json` 可以保留邏輯來源 `com.fnfr.svt.help/toc.xml`、`com.fnfr.svt.help/index.xml` 和 `com.fnfr.svt.help/contexts.xml`，但不能保留實際本機 plugin 版本資料夾路徑。

25.4 時已採用這個格式。查詢結果應該看到：

```text
source_ref: topics/quickcalls_arguments_in_quickcall_steps.htm
source_ref: topics/popups/arules/query.html
```

## Step 5: 安裝到本機 Codex Skills

同步工作區版到本機 skills：

```powershell
$source = "F:\MyCode\Java\iTest26.5\itest-help"
$target = "C:\Users\robert\.codex\skills\itest-help"
New-Item -ItemType Directory -Path $target -Force | Out-Null
Copy-Item "$source\*" $target -Recurse -Force
```

注意：這裡複製的是 `itest-help` 裡面的內容，不是把整個 `itest-help` 資料夾再放進目標資料夾。完成後應該看到 `C:\Users\robert\.codex\skills\itest-help\SKILL.md`，不要變成 `C:\Users\robert\.codex\skills\itest-help\itest-help\SKILL.md`。

驗證安裝版：

```powershell
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" "parameter merging logic" --top 2
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" "Field Replacements" --top 3
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" --show-file "topics/popups/query.html" --text
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" "tcl clock scan target_date 2049 time conversion" --top 4
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" "Custom Extractor Custom Process" --top 4
python "C:\Users\robert\.codex\skills\itest-help\scripts\search_help.py" "Step Properties Analysis Rule Properties" --top 4
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

下面的範例使用版本化檔名 `itest-help_v26.5.zip`。如果 Step 6 沒有重新命名，請把下面指令中的 `itest-help_v26.5.zip` 改成 `itest-help.zip`。

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
itest-help/scripts/apply_toc_metadata.py
itest-help/references/help_pages.jsonl
itest-help/references/search_index.json
itest-help/references/search_index_summary.json
itest-help/references/toc_index.json
itest-help/references/help_index.json
itest-help/references/contexts_index.json
itest-help/references/interpreter-guide.md
itest-help/references/analysis-rule-wizard-guide.md
itest-help/references/regression-questions.md
```

檢查 zip 展開後沒有本機絕對路徑：

```powershell
$tmp = Join-Path $env:TEMP "itest-help-zip-check"
if (Test-Path $tmp) { Remove-Item $tmp -Recurse -Force }
Expand-Archive "F:\MyCode\robert-create-codex-skills\dist\itest-help_v26.5.zip" -DestinationPath $tmp -Force
Select-String -Path (Join-Path $tmp "itest-help\references\*.json*") -Pattern "F:\\MyCode|C:\\Users\\|com.fnfr.svt.help_[0-9]" | Measure-Object
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
請依照 F:\MyCode\robert-create-codex-skills\docs\itest-help-skill\itest-help-skill-runbook.md
把 iTest Help skill 更新到 iTest 26.5。
新的 help topics 目錄是：<新路徑>
```

使用時，把 `<新路徑>` 換成實際的 `topics` 資料夾路徑。不要保留 `<` 和 `>`。

例如：

```text
請依照 F:\MyCode\robert-create-codex-skills\docs\itest-help-skill\itest-help-skill-runbook.md
把 iTest Help skill 更新到 iTest 26.5。
新的 help topics 目錄是：F:\MyCode\Java\iTest26.5\com.fnfr.svt.help_26.5.0.xxxxxxxxxxxx\topics
```

完整任務版：

```text
請依照 F:\MyCode\robert-create-codex-skills\docs\itest-help-skill\itest-help-skill-runbook.md
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
- 更新 help data 後要重新套用 `toc.xml`、`index.xml` 與 `contexts.xml`，否則查詢結果會缺少官方 iTest Online Help 章節、index 與 context metadata。
- `index.xml` 與 `contexts.xml` 只能用來幫助找頁、定位或記錄官方 metadata；回答產品行為時仍必須以 help page 文字為證據。
- `ui_scope`、`scope_summary` 與 `mixed_scope_warning` 只能幫助分辨 UI 位置與候選頁，不能單獨證明產品行為。
- 不要把 `Custom Extractor` / `Custom Processor` 與 `Custom Types`、custom session type、custom parsers 或報表客製化混在一起。
- 不要把 `Step Properties` 與 `Analysis Rule Properties` 混在一起。Step Properties 是 Test Case Editor 中 step 層級的設定；Analysis Rule Properties 是 analysis rule 內 extractor、processor 或 action 層級的設定。
- 不要把 context ID 當成官方章節分類。
- 官方 help 的 examples、lists 和 tables 不一定是完整清單。不要把正向範例反推成未列項目不支援，也不要把反向範例反推成未列項目都支援，除非 help 明確說它是完整或排他的規則。
- `probable_category` 是推測分類；回答章節或分類問題時，優先使用 `toc_paths`。
- 子目錄納入後會有同名檔案；搜尋結果與引用要使用 `source_ref` / `relative_path`，不要只依賴 `file_name`。
- clock/time conversion guardrail 不只適用 certificate expiration。只要有日期文字轉秒數、時間比較、時間加減，或 `clock scan` / `clock format`，而且日期在 2038 以後，都要重新驗證。
- 原始 HTML 可以不打包；目前 skill 查的是清理後的 `help_pages.jsonl` 與 `search_index.json`。
- 如果新版本 help 結構大改，先抽樣檢查 title/H1/doc_set 是否仍能正確抽出。
