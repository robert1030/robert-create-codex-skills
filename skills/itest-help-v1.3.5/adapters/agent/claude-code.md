# Claude Code 與 Claude CLI Adapter

本檔只補 Claude Code 與 Claude CLI 的安裝位置、執行路徑與已知限制，基礎流程請先讀 [instructions.md](instructions.md)

## 安裝

使用 `runtime` profile，解壓到下列其中一處：

```text
個人層級（所有專案可用）：~/.claude/skills/itest-help/
專案層級（只在該專案可用）：<專案>/.claude/skills/itest-help/
```

Windows 的個人層級路徑是 `%USERPROFILE%\.claude\skills\itest-help\`。

**目錄名必須是 `itest-help`**。Claude Code 的個人與專案 skill 以目錄名決定叫用指令，改名會讓 `/itest-help` 失效，frontmatter 的 `name` 對這兩種 skill 只是顯示標籤。

安裝後 `SKILL.md` 應位於 `~/.claude/skills/itest-help/SKILL.md`。Claude Code 會在目前 session 內偵測到新檔案，但若 `~/.claude/skills/` 這個上層目錄是 session 開始後才建立的，需要重開 Claude Code。

## 不要把 full profile 解壓到這裡

`full` profile 含 `knowledge/rag/`，其中 1,136 個檔案路徑安裝到使用者家目錄下的 skill 目錄後會超過 Windows 的 260 字元路徑上限，最長達 304 字元。未啟用 `LongPathsEnabled` 的 Windows 會解壓失敗或靜默截斷，Windows 內建的檔案總管解壓縮即使啟用該設定也可能失敗。

要跑完整 provenance 鏈驗證時，把 `full` profile 解壓到短路徑，例如 `D:\itest-verify\itest-help\`，再執行：

```text
python scripts/validate_itest_help.py --profile full D:\itest-verify\itest-help
```

## 執行檢索

Claude Code 會把 `${CLAUDE_SKILL_DIR}` 展開為本 skill 的安裝目錄。工作目錄是使用者的專案目錄，不是 skill 目錄，所以命令列一律帶 `${CLAUDE_SKILL_DIR}`：

```bash
python3 "${CLAUDE_SKILL_DIR}/scripts/search_itest_help.py" "<query>" --limit 5
python3 "${CLAUDE_SKILL_DIR}/scripts/inspect_chunk.py" "<chunk-id>"
```

**Windows 一律用 `py -3`**，退而求其次用 `python`，其餘不變：

```bash
py -3 "${CLAUDE_SKILL_DIR}/scripts/search_itest_help.py" "<query>" --limit 5
```

**不要在 Windows 上用 `python3`。** Windows 預設會在 `%LOCALAPPDATA%\Microsoft\WindowsApps\` 放一個同名的 Microsoft Store 空殼程式，它存在於 PATH、可被執行，但退出碼 49 且不輸出任何內容。這種失敗看起來像檢索沒有結果，實際上腳本根本沒被執行，很容易被誤判成知識庫查不到而錯誤降級。本機實測：

```text
py -3 -V      → Python 3.12.10，退出碼 0
python -V     → Python 3.12.10，退出碼 0
python3 -V    → 無輸出，退出碼 49
```

`${CLAUDE_SKILL_DIR}` 的展開需要 Claude Code v2.1.129 以上。版本較舊時，把它換成 skill 的絕對路徑。檢索腳本以 `__file__` 定位索引，所以只要腳本路徑正確，從任何工作目錄執行結果都一樣。

## 減少權限提示（選用）

本 skill 的 `SKILL.md` frontmatter 只放 `name` 與 `description`，刻意不加 `allowed-tools`，以維持對 ChatGPT Codex CLI 與 Codex Desktop 的相容性。若要免去每次檢索的權限提示，在 `~/.claude/settings.json` 自行加入允許規則，不要改 `SKILL.md`：

```json
{
  "permissions": {
    "allow": [
      "Bash(python3 //*/.claude/skills/itest-help/scripts/search_itest_help.py:*)",
      "Bash(python //*/.claude/skills/itest-help/scripts/search_itest_help.py:*)",
      "Bash(python3 //*/.claude/skills/itest-help/scripts/inspect_chunk.py:*)",
      "Bash(python //*/.claude/skills/itest-help/scripts/inspect_chunk.py:*)"
    ]
  }
}
```

這是使用者環境設定，不是 skill 契約的一部分。不加也能正常運作，只是每次會問一次。

## 外部官方查證

Claude Code 具備 WebSearch 與 WebFetch。仍然只有在本地知識庫不足、版本不符、內容衝突或使用者明確要求更新資訊時才呼叫，並依 [../../core/external-research-policy.md](../../core/external-research-policy.md) 列出 `【外部查證聲明】`。工具被停用或無網路時，依 [error-handling.md](error-handling.md) 回報 `tool_unavailable` 或 `network_unavailable`，不得改用模型記憶。

## 已知限制

- `runtime` profile 不含 `knowledge/rag/`，本地無法重跑完整來源鏈比對。可宣稱的只有 `python3 "${CLAUDE_SKILL_DIR}/scripts/validate_itest_help.py" --profile runtime` 的凍結雜湊比對通過。
- 本 adapter 描述的安裝方式屬個人或專案層級。放在 `~/.claude/skills/` 的個人 skill 不會出現在雲端 routine 的遠端 session 中。
