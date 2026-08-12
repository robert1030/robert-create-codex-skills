# robert-create-codex-skills

這個 repo 保存 Robert 個人使用的 Codex skills、文件與可移植 zip。

## skill-packager

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/skills/skill-packager
```

文件：

- `docs/skill-packager/README.html`
- `docs/skill-packager/SPEC.html`

## itest-help-skill

```text
AI Chatweb: https://github.com/owner/robert-create-codex-skills/dist/itest-help-v1.3.5-chatweb.zip
AI Agent:  https://github.com/owner/robert-create-codex-skills/dist/itest-help-v1.3.5-runtime.zip
```

- 安裝提示：'itest-help-dist-manifest.md'
- 目前知識庫基礎版本：iTest v26.2.0。
- AI agent (ex: Codex or claude agent): 參考itest-help-dist-manifest.md, 將zip 放到 /skills/ 內後解壓縮即可,重啟 AI Agent
- AI web Chat: 參考itest-help-dist-manifest.md, 從 AI web chat add 對應的chatweb.zip, 在新對話使用
- 版本: v1.3.5
文件:
無,叫AI讀zip解釋

## multiformat-rag-chunker-v1.2.3

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/dist/multiformat-rag-chunker-v1.2.3.zip
```

用途：將 PDF、DOCX、DOC、HTML、含嵌入圖片的 HTML、XML、CSV、Markdown、MP4、JPG／JPEG、PNG、HEIC／HEIF 轉成高細緻度 RAG Markdown 切片，支援英文文件為主。
- AI agent (ex: Codex ): 將zip 放到 /skills/ 內後解壓縮即可,重啟 AI Agent
- AI web Chat: 從 AI web chat add 對應的zip, 在新對話使用
- 目前主要支援ChatGPT chat web 和 ChatGPT codex Agent, claude 仍未同步建構

文件:
無,叫AI讀zip解釋

## docs-quality-gen-v1-2

Robert 個人文件品質 gate。

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/dist/docs-quality-gen-v1-2.zip
```

文件：

- `docs/docs-quality-gen-v1-1/README.html`
- `docs/docs-quality-gen-v1-1/runbook.htm`
- `docs/docs-quality-gen-v1-1/SPEC.md`

## joan-skill-conventions-v1.2.1 (基於酒Ann老師的skill建構基礎,調整修改後的v1.2.1版本)

version:1.2.1
目的: 作為建立,升級,檢視,重構 skill 的基本工具
AI Chat 安裝 Claude.ai Chat Web -> customize -> skill 安裝/上傳整包zip，即可安裝skill
AI agent 安裝 joan-skill-conventions-v1.2.1.zip -> /.claude/skills/ 解壓縮, 重啟AI Agent

```text
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/claude-skills/dists/joan-skill-conventions-v1.2.1.zip
```

文件:
無,叫AI讀zip解釋

## gpt-skill-conventions (基於酒Ann老師的skill建構基礎,轉換的gpt-skill-conventions-v1.2.2)
```text
version:1.2.2
目的: 作為建立,升級,檢視,重構 skill 的基本工具, 也能把claude ai (WebGUI)的skill 轉換成相容codex(仍須測試轉換成效)
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/dist/gpt-skill-conventions-v1.2.2.zip
在Chatgpt web skill 安裝/上傳整包zip，即可安裝skill
```

文件:
無,叫AI讀zip解釋

## ai-session-handoff (AI Chat / AI Agent) 對話交接摘要 skill
version:1.0.1
目的: 交接對話的上下文脈絡摘要skill
支援: ChatGPT web Chat/web work; ChatGPT codex; Claude.ai web chat; Claude.ai code-cli

```text
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/dist/ai-session-handoff-v1.0.1.zip
在Chatgpt/Claude.ai web skill 安裝/上傳整包zip，即可安裝skill
```

文件:
無,叫AI讀zip解釋

## gpt-operate-discipline-v1.1.2
version:1.1.2
目的: ChatGPT ChatWeb / WorkWeb; ChatGPT Codex 的資料查詢後,輸出結果或報告前, 資料分析驗證規範 skill
支援: ChatGPT web Chat/web work; ChatGPT codex

```text
skill installer，前往下載 https://github.com/owner/robert-create-codex-skills/dist/gpt-operate-discipline-v1.1.2.zip
```

文件：
無,叫AI讀zip解釋

## operate-discipline-v1.1
version:1.1
目的: Claude.ai ChatWeb / Claude.ai code-cli 的資料查詢後,輸出結果或報告前, 資料分析驗證規範 skill
支援: Claude.ai ChatWeb / Claude.ai code-cli

```text
skill installer，前往下載 https://github.com/owner/robert-create-codex-skills/claude-skills/dists/operate-discipline-v1.1.zip
```

文件：
無,叫AI讀zip解釋