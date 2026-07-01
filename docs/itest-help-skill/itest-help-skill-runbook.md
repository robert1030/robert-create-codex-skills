# iTest Help Skill Runbook

這份 runbook 說明如何建立、驗證、安裝與打包目前的 `itest-help-skill`。本流程以 iTest Help 26.2.0 RAG chunk 為來源。

## 目標

產出一個可安裝到 Codex 的本機 skill：

```text
itest-help-skill/
  SKILL.md
  agents/openai.yaml
  FROZEN.md
  scripts/search_itest_help.py
  scripts/inspect_chunk.py
  scripts/validate_itest_help_skill.py
  references/rag/
```

重要原則：

- skill 必須自足，不依賴原始 RAG chunk 來源資料夾。
- zip 內部頂層資料夾必須是 `itest-help-skill/`。
- 解壓或安裝後必須是 `.codex/skills/itest-help-skill/SKILL.md`。
- `SKILL.md` frontmatter 的 `name` 必須是 `itest-help-skill`。
- 不要把其他 iTest 版本的 chunk 混入這個 skill。

## 執行環境

這份 runbook 使用 Windows PowerShell 路徑。下列路徑是目前本機環境事實。換到其他電腦時，請替換成該環境的實際路徑。

```text
工作區 skill：F:\MyCode\robert-create-codex-skills\skills\itest-help-skill
安裝版 skill：C:\Users\robert\.codex\skills\itest-help-skill
文件資料夾：F:\MyCode\robert-create-codex-skills\docs\itest-help-skill
打包輸出：F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip
原始 RAG chunk：F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help
```

不要把 Windows 路徑直接當成 Linux、WSL 或 Ubuntu 指令使用。

## Step 1: 檢查來源 RAG chunk

目的：確認來源資料是 iTest Help 26.2.0 的 RAG chunk，且轉換報告沒有 blocking issue。

```powershell
Get-Content "F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help\manifest.md" -TotalCount 80
Get-Content "F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help\validation_report.md" -TotalCount 80
```

預期結果：

- text chunk 數量是 `2891`。
- image chunk 數量是 `1221`。
- blocking issues 是 `0`。

## Step 2: 建立或更新工作區 skill

目的：建立 Codex skill 外殼，並把 RAG chunk 放入 `references/rag`。

工作區 skill 應位於：

```text
F:\MyCode\robert-create-codex-skills\skills\itest-help-skill
```

必要檔案：

```text
SKILL.md
agents/openai.yaml
FROZEN.md
scripts/search_itest_help.py
scripts/inspect_chunk.py
scripts/validate_itest_help_skill.py
references/rag/manifest.md
references/rag/validation_report.md
references/rag/chunk_manifest.jsonl
references/rag/index_manifest.jsonl
references/rag/inventory.json
references/rag/text/
references/rag/images/
```

注意：複製 `references/rag` 時，複製的是 RAG 內容，不是把整個原始來源資料夾變成巢狀資料夾。

## Step 3: 驗證工作區 skill

目的：確認 skill 外殼、資料契約與搜尋功能可用。

```powershell
python "C:\Users\robert\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill"
python "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\scripts\validate_itest_help_skill.py"
python "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\scripts\search_itest_help.py" "QuickCall topology" --limit 3
python "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\scripts\search_itest_help.py" "response map XPath" --limit 3
python "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\scripts\search_itest_help.py" "Spirent TestCenter command reference" --limit 3
```

預期結果：

- `quick_validate.py` 顯示 `Skill is valid!`。
- `validate_itest_help_skill.py` 顯示 `text_chunks=2891 image_chunks=1221`。
- 三個搜尋命令都有相關結果。

## Step 4: 安裝到本機 Codex Skills

目的：讓 Codex 可以用 `$itest-help-skill` 觸發這個 skill。

如果目標資料夾不存在，複製工作區 skill：

```powershell
$source = "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill"
$target = "C:\Users\robert\.codex\skills\itest-help-skill"
Copy-Item -Path $source -Destination $target -Recurse
```

如果目標資料夾已存在，先確認內容是否可覆蓋。不要把資料夾複製成下面這種錯誤結構：

```text
C:\Users\robert\.codex\skills\itest-help-skill\itest-help-skill\SKILL.md
```

正確結果必須是：

```text
C:\Users\robert\.codex\skills\itest-help-skill\SKILL.md
```

## Step 5: 驗證安裝版

目的：確認 Codex user skills 目錄中的安裝版也能查詢。

```powershell
python "C:\Users\robert\.codex\skills\.system\skill-creator\scripts\quick_validate.py" "C:\Users\robert\.codex\skills\itest-help-skill"
python "C:\Users\robert\.codex\skills\itest-help-skill\scripts\validate_itest_help_skill.py"
python "C:\Users\robert\.codex\skills\itest-help-skill\scripts\search_itest_help.py" "Spirent TestCenter command reference" --limit 2
```

不要只驗證工作區版就打包或宣稱安裝完成。

## Step 6: 打包

目的：建立可搬移的 zip。

```powershell
New-Item -ItemType Directory -Force -Path "F:\MyCode\robert-create-codex-skills\dist" | Out-Null
python "C:\Users\robert\.codex\skills\skill-packager\scripts\package_skill.py" `
  "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill" `
  "F:\MyCode\robert-create-codex-skills\dist"
```

預期輸出：

```text
F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip
```

## Step 7: 驗證 zip

目的：確認 zip 頂層資料夾與必要檔案正確。

```powershell
python -c "import zipfile, pathlib; p=pathlib.Path(r'F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip'); z=zipfile.ZipFile(p); names=z.namelist(); print('entries', len(names)); print('has_skill_md', 'itest-help-skill/SKILL.md' in names); print('top_levels', sorted(set(n.split('/')[0] for n in names))[:5])"
```

預期結果：

- `has_skill_md True`
- top-level folder 是 `itest-help-skill`

## Step 8: 使用方式

在 Codex 中明確指定 skill：

```text
使用 $itest-help-skill 查詢 iTest 26.2 help，說明 QuickCall 如何和 topology device 關聯。
```

回答應根據搜尋到的 chunks，並引用 `source_file`、`toc_path` 或 `heading_path`。

## 常見風險

- 不要把其他 iTest 版本的 chunk 混進 `references/rag`。
- 不要只改 zip 檔名，卻改壞 zip 內部頂層資料夾。
- 不要把 OCR 文字當成人工校對過的內容。
- 不要把原始 RAG 來源路徑寫成跨機器都必須存在的要求。
- 不要用舊的搜尋架構檢查這個 skill；目前使用的是 `search_itest_help.py` 與 `chunk_manifest.jsonl`。