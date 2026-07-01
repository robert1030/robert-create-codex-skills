# iTest Help Skill

這份文件說明目前本機建立的 `itest-help-skill`。它是 Codex skill，用來查詢 iTest Help 26.2.0 的 RAG chunk，協助回答 iTest 開發與除錯問題。

## 文件組

- `SPEC.md`：規格與驗收條件。
- `itest-help-skill-runbook.md`：Windows PowerShell 操作流程。
- `itest-help-skill-runbook.htm`：runbook 的 HTML 同步版。

## 目前環境路徑

這些是本機目前使用的路徑。換到其他電腦時，請替換成該環境的實際路徑。

- 工作區 skill：`F:\MyCode\robert-create-codex-skills\skills\itest-help-skill`
- 安裝版 skill：`C:\Users\robert\.codex\skills\itest-help-skill`
- 原始 RAG chunk：`F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help`
- 打包輸出：`F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip`

## 使用方式

在 Codex 中詢問 iTest 問題時，可以明確指定：

```text
使用 $itest-help-skill 查詢 iTest 26.2 help，說明 QuickCall 如何和 topology device 關聯。
```

Skill 會先搜尋封裝在 `references/rag` 的 chunk，再依來源回答。回答應包含來源檔案、TOC 路徑或 heading 路徑。

## 維護方式

- 不要把不同 iTest 版本的 chunk 混入這個 skill。
- 若來源 RAG chunk 重新產生，請重新複製 `references/rag` 並跑驗證。
- 若要支援 iTest 其他版本，建議建立新的 skill 版本或新的 skill 目錄。

## 驗證

在工作區 skill 目錄執行：

```powershell
python C:\Users\robert\.codex\skills\.system\skill-creator\scripts\quick_validate.py F:\MyCode\robert-create-codex-skills\skills\itest-help-skill
python F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\scripts\validate_itest_help_skill.py
python F:\MyCode\robert-create-codex-skills\skills\itest-help-skill\scripts\search_itest_help.py "QuickCall topology" --limit 3
```

## 已知限制

原始轉換報告沒有 blocking issue，但有非阻斷警告，例如 unresolved anchor、broken internal link、missing image reference，以及少數 oversized chunk。這些會影響精準跳轉或檢索粒度，但不代表 help 內容不可用。