# Adapter 對照表

先依執行型態選一份基礎 adapter，再依實際平台加讀一份平台 adapter。兩層都要讀。

| 執行平台 | 基礎 adapter | 平台 adapter | 建議 profile |
| --- | --- | --- | --- |
| Claude Code | [agent/instructions.md](agent/instructions.md) | [agent/claude-code.md](agent/claude-code.md) | `runtime` |
| Claude CLI | [agent/instructions.md](agent/instructions.md) | [agent/claude-code.md](agent/claude-code.md) | `runtime` |
| Claude Chat Web，走 Skills 上傳 | [chat-web/instructions.md](chat-web/instructions.md) | [chat-web/claude-ai-skill.md](chat-web/claude-ai-skill.md) | `chatweb` |
| Claude Chat Web，走 Project 知識庫 | [chat-web/instructions.md](chat-web/instructions.md) | [chat-web/knowledge-configuration.md](chat-web/knowledge-configuration.md) | 取 `runtime` 內的 `knowledge/chat-web-knowledge.md` |
| ChatGPT Codex CLI | [agent/instructions.md](agent/instructions.md) | 無，用基礎 adapter 即可 | `runtime` |
| ChatGPT Codex Desktop | [agent/instructions.md](agent/instructions.md) | 無，用基礎 adapter 即可 | `runtime` |
| ChatGPT Chat Web，走 Personal Skills 上傳 | [chat-web/instructions.md](chat-web/instructions.md) | [chat-web/chatgpt-skill.md](chat-web/chatgpt-skill.md) | `chatweb` |
| ChatGPT Chat Web，無 Skills 存取權，或 ChatGPT 工作 | [chat-web/instructions.md](chat-web/instructions.md) | [chat-web/knowledge-configuration.md](chat-web/knowledge-configuration.md) | 取 `runtime` 內的 `knowledge/chat-web-knowledge.md` |

平台 adapter 只補「這個平台怎麼執行、有什麼硬性限制」。檢索政策、來源優先順序、引用格式、版本規則與不確定性降級一律由 [../core/](../core/) 決定，平台 adapter 不得覆寫。

各平台的實際能力與已驗證狀態見 [../docs/platform-matrix.md](../docs/platform-matrix.md)
