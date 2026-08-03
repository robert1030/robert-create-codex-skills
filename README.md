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

- 安裝提示：'itest-help-dist-manifest.md'
- 目前基礎版本：iTest v26.2。
- AI agent (ex: Codex or claude agent): 參考itest-help-dist-manifest.md, 將zip 放到 /skills/ 內後解壓縮即可,重啟 AI Agent
- AI web Chat: 參考itest-help-dist-manifest.md, 從 AI web chat add 對應的chatweb.zip, 在新對話使用

文件:
無,叫AI讀zip解釋

## multiformat-rag-chunker-v1.2.1.zip

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/skills/multiformat-rag-chunker-v1.2.1
```

用途：將 PDF、DOCX、DOC、HTML、含嵌入圖片的 HTML、XML、CSV、Markdown、MP4、JPG／JPEG、PNG、HEIC／HEIF 轉成高細緻度 RAG Markdown 切片，支援英文文件為主。
- AI agent (ex: Codex ): 將zip 放到 /skills/ 內後解壓縮即可,重啟 AI Agent
- AI web Chat: 從 AI web chat add 對應的zip, 在新對話使用
- 目前主要支援ChatGPT chat web 和 ChatGPT codex Agent, claude 仍未同步建構

文件:
無,叫AI讀zip解釋

## docs-quality-gen-v1-1

Robert 個人文件品質 gate。

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/skills/docs-quality-gen-v1-1
```

文件：

- `docs/docs-quality-gen-v1-1/README.html`
- `docs/docs-quality-gen-v1-1/runbook.htm`
- `docs/docs-quality-gen-v1-1/SPEC.md`

## joan-skill-conventions-v1.2.1 (基於酒Ann老師的skill建構基礎,調整修改後的v1.2.1版本)
claude-skills\dists\joan-skill-conventions-v1.2.1.zip

```text
version:1.2.1
目的: 作為建立,升級,檢視,重構 skill 的基本工具
AI Chat 安裝 Claude.ai Chat Web -> customize -> skill 安裝/上傳整包zip，即可安裝skill
AI agent 安裝 joan-skill-conventions-v1.2.1.zip -> /.claude/skills/ 解壓縮, 重啟AI Agent
```

文件:
無,叫AI讀zip解釋

## gpt-skill-conventions (基於酒Ann老師的skill建構基礎,轉換的gpt-skill-conventions-v1.2.2)
```text
version:1.2.2
目的: 作為建立,升級,檢視,重構 skill 的基本工具, 也能把claude ai (WebGUI)的skill 轉換成相容codex(仍須測試轉換成效)
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/gpt-skill-conventions-v1.2.2.zip
在Chatgpt web skill 安裝/上傳整包zip，即可安裝skill
```

文件:
無,叫AI讀zip解釋

## session-handoff (AI Chat / AI Agent) 對話交接摘要 skill
- gpt-session-handoff-v1.2 -> ChatGPT Chat & Codex
- claude-skills\dists\session-handoff-v1.2-claude.zip -> Claude.ai Chat & Claude agent
文件:
無,叫AI讀zip解釋