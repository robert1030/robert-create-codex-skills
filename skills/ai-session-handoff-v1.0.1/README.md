# ai-session-handoff

版本 1.0.1。把當前 session 壓縮成一份下一個 AI session 可直接接手的交接文件。

本檔只講安裝、執行與驗證。**行為規格一律以 `SKILL.md` 與 `references/` 為準**，本檔不重複規則，也不是 runtime 規格。

## 這包裡有什麼

| 路徑 | 內容 |
| --- | --- |
| `SKILL.md` | runtime 主檔：六步流程、九節骨架、硬規則、條件式參考 |
| `references/output-contract.md` | 九節 inclusion criteria、模板、交付形式 |
| `references/platform-capabilities.md` | 能力偵測、三種輸出分支、降級階梯 |
| `references/encoding-policy.md` | UTF-8、BOM、CP950、換行與各 shell 差異 |
| `references/redaction-policy.md` | 敏感資訊判定與寫法 |
| `references/examples.md` | 最小可用範例與五組情境範例索引 |
| `schemas/handoff.schema.json` | 交接文件的結構化契約 |
| `scripts/` | 驗證器、能力偵測、遮蔽與編碼工具 |
| `tests/` | 回歸測試與五組 golden fixtures |
| `FROZEN.md` | 凍結契約帳本 |
| `agents/openai.yaml` | ChatGPT Web 與 Codex 的 metadata adapter |

## 安裝

**Claude Code 或 Claude.ai**：把整個 `ai-session-handoff/` 目錄放進 skills 目錄（Claude Code 常見位置為使用者家目錄下的 `.claude/skills/`），或直接上傳本包的 zip。安裝後即為 model-invoked，說「交接 session」「handoff」「context 快滿了要換新對話」都會觸發。

**ChatGPT Codex 或 ChatGPT Web**：同樣放進該宿主的 skills 目錄，`agents/openai.yaml` 提供顯示名稱、圖示與預設提示，並允許隱式觸發。

**想改成只由手動呼叫**：在 `SKILL.md` 的 frontmatter 加一行 `disable-model-invocation: true`。這會讓 skill 不再佔用每回合的 context，但也不會自動觸發，需要自己輸入名稱。取捨在於：交接最常見的觸發時機是 context 快滿，而這件事通常由 agent 先察覺，改成手動呼叫等於放棄這個分支。

## 使用

直接說出需求即可，例如：

- 交接這個 session，下一個 session 要接著把封裝流程做完。
- context 快滿了，幫我 handoff 到新對話。
- 讓另一個 agent 接手這份工作。

可選參數（沒給就採安全預設，不會中斷流程）：下一個 session 的用途、下一步焦點、目標 agent 或平台、詳細程度、是否寫檔、輸出路徑。

## 驗證指令

以下 `<python>` 代表當前環境可用的直譯器（Linux 常為 `python3`，Windows 依 PEP 397 常為 `py` 或 `python`）。Windows 繁體中文環境請先設定 `PYTHONUTF8=1`，設定方式見 `references/encoding-policy.md`。

```text
<python> tests/run_all.py                       全部回歸測試
<python> scripts/validate_skill.py .            套件級驗證
<python> scripts/validate_handoff.py <草稿路徑>  交接文件驗證
<python> scripts/validate_punct.py <草稿路徑>    全形標點與禁破折號
<python> scripts/check_encoding.py .            編碼與換行
<python> scripts/detect_capabilities.py         能力偵測結果（JSON）
```

全部只用 Python 標準函式庫，離線可跑，無需安裝任何套件。支援 Python 3.8 以上。

## 授權

MIT，見 `LICENSE`。
