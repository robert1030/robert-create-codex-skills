# Claude Skill 與 Codex Skill 格式差異對照表

轉換遇到不確定的地方，先查這份表；房規知識本身（九條房規＋三種模式）不受這份表影響，只有外殼結構受影響。

## 總表

| 項目 | Claude Skill | Codex Skill |
|---|---|---|
| 觸發機制 | 只靠 `SKILL.md` 的 `name`／`description` 語意比對，隱性觸發 | 一樣靠 `description` 語意比對隱性觸發，另外支援使用者明確打 `$skill-name` 點名呼叫 |
| UI 中繼資料 | 不需要 | 需要 `agents/openai.yaml`：`display_name`／`short_description`（二十五至六十四字）／`default_prompt`（必須含 `$skill-name`） |
| 資料夾規則 | 沒有嚴格限制 | 資料夾名稱必須和 `name` 完全一致；`name` 只能小寫字母、數字、連字號，六十四字以內，不可開頭結尾連字號或連續連字號 |
| `scripts`／`references`／`assets` 分工 | 三層定義：可執行、載入內文、輸出用資源 | 定義完全相同，檔案結構不用重整 |
| frontmatter 允許欄位 | `name`／`description` | `name`／`description`／`license`／`allowed-tools`／`metadata`，其餘一律進 `agents/openai.yaml` |
| `description` 上限 | 沒有明確字數上限 | 一千零二十四字，超過會被 `quick_validate.py` 擋下 |
| 驗證工具 | 自寫的 `validate_punct.py`、`sync_validator.py` | 多一層平台附帶的 `quick_validate.py`（檢查 frontmatter 格式）、`init_skill.py`（鷹架用） |
| 執行環境 | 固定 Ubuntu 沙箱容器 | 通常在使用者本機或設定過的環境，作業系統／套件管理工具不固定 |
| 隱性觸發開關 | 沒有這個概念，永遠隱性觸發 | `policy.allow_implicit_invocation`，預設 `true`；設 `false` 就只能靠 `$skill-name` 明確呼叫 |

## 五步驟轉換流程（本 skill 的轉換器依此實作）

1. **結構補件**：新增 `agents/openai.yaml`（`display_name`／`short_description`／`default_prompt`）。
2. **frontmatter 對齊**：確認 `name`／`description` 是唯一觸發依據，補齊所有情境，檢查字數上限與命名規則。
3. **語意與用語轉換**：移除「另一個 Claude 實例」等指涉，改中性用語；`skill-creator` 的內部連結從 Claude 版指向 Codex 版。
4. **環境相依重寫**：`bootstrap` 改偵測式安裝，不假設固定 Ubuntu 沙箱、不寫死 `--break-system-packages`。
5. **命名與驗證**：資料夾名稱與 `name` 一致；跑 `quick_validate.py` 確認格式沒問題。

## 不用動的部分

九條房規本身、三種模式、滿意度確認迴圈、多格式交付、`validate_punct.py`、`canonical-snippets.md` 這些都是純知識內容，語言模型無關，整段照搬即可。
