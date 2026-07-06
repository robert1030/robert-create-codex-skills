# itest-help-skill Runbook

這份 runbook 說明如何在 Windows PowerShell 建置、驗證、打包 `itest-help-skill`。本文中的磁碟路徑是目前環境例子；在其他電腦請替換成實際路徑。

## 1. Prerequisites

Purpose: 確認來源檔與工具存在。

Current environment paths:

- Workspace: `F:\MyCode\robert-create-codex-skills`
- Skill folder: `F:\MyCode\robert-create-codex-skills\skills\itest-help-skill`
- RAG zip: `F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help_ragchunk.zip`
- Original help zip: `F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106\itest-help_26.2.0.zip`
- Bundled extracted RAG inside skill: `F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\references\rag`
- Package output folder: `F:\MyCode\robert-create-codex-skills\dist`

Verify:

```powershell
Get-Item -LiteralPath "F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help_ragchunk.zip"
Get-Item -LiteralPath "F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106\itest-help_26.2.0.zip"
```

Expected result: both files exist.

## 2. Clean Old Workspace Copy

Purpose: 避免舊版 `itest-help-skill` 檔案混入新包。

Warning: 只刪除確認位於 workspace 內的 `itest-help-skill` 目標，不要刪除整個 `skills`、`docs` 或 `dist`。

```powershell
$root = "F:\MyCode\robert-create-codex-skills"
Remove-Item -LiteralPath "$root\skills\itest-help-skill" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath "$root\docs\itest-help-skill" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -LiteralPath "$root\dist\itest-help-skill.zip" -Force -ErrorAction SilentlyContinue
```

Expected result: old workspace copy is gone.

## 3. Validate the Skill

Purpose: 確認 skill 結構與 RAG 契約符合 26.2.0。

```powershell
Set-Location "F:\MyCode\robert-create-codex-skills\skills\itest-help-skill"
python -m py_compile ".\scripts\search_itest_help.py" ".\scripts\inspect_chunk.py" ".\scripts\validate_itest_help_skill.py"
python ".\scripts\validate_itest_help_skill.py"
python "C:\Users\robert\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

Expected result:

- Python compile has no output and exits with code `0`.
- `validate_itest_help_skill.py` prints `Validation passed.`
- `quick_validate.py` prints `Skill is valid!`

## 4. Run Smoke Searches

Purpose: 確認使用者要求的五組觸發查詢都有本地 RAG 命中。

```powershell
python ".\scripts\search_itest_help.py" "itest help" --limit 2
python ".\scripts\search_itest_help.py" "itest gui" --limit 2
python ".\scripts\search_itest_help.py" "itest tcl" --limit 2
python ".\scripts\search_itest_help.py" "itest python" --limit 2
python ".\scripts\search_itest_help.py" "itest analysis" --limit 2
```

Expected result: each command prints at least one result with `chunk_id` and `source_original_path`.

## 5. Package the Skill

Purpose: 產出可移動、可安裝的 zip。

```powershell
Set-Location "F:\MyCode\robert-create-codex-skills"
python "C:\Users\robert\.codex\skills\skill-packager\scripts\package_skill.py" ".\skills\itest-help-skill" ".\dist"
```

Expected result: `F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip` exists.

## 6. Verify the Zip

Purpose: 確認 zip 沒有多包一層資料夾，也沒有漏掉 `SKILL.md`。

```powershell
Add-Type -AssemblyName System.IO.Compression.FileSystem
$zip = [System.IO.Compression.ZipFile]::OpenRead("F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip")
try {
  ($zip.Entries | Select-Object -First 10 FullName)
  ($zip.Entries.FullName -contains "itest-help-skill/SKILL.md")
  ($zip.Entries.FullName -contains "itest-help-skill/references/rag/chunk_manifest.jsonl")
} finally {
  $zip.Dispose()
}
```

Expected result: entries start with `itest-help-skill/`, and both final checks return `True`.

## 7. Answering Rule

When using the skill, search the local RAG first. If no useful local result exists, use external lookup when tools are available and label those facts as `External source`. If external lookup is not available, say so clearly.
