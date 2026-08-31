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

## rag-chunk-generator

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/dist/rag-chunk-generator-v1.3.2.zip
```

用途：將 PDF、DOCX、DOC、HTML、XML、MP4 轉成高細緻度 RAG 切片器。
- AI agent (ex: Codex ): 將zip 放到 /skills/ 內後解壓縮即可,重啟 AI Agent
- AI web Chat: 從 AI web chat add 對應的zip, 在新對話使用
- 版本: v1.3.2 基於酒Ann老師的rag-chunk-generator-v1.2版,個人改良調整後,進版成v1.3.2
- 以PDF為例,如果整個PDF是掃描式圖片內容,需先使用OCR處理過(NAPS2-第一次處理, OCRmyPDF + Tesseract OCR-二次處理,效果比較好, 參考"Windows-把掃描PDF變成可搜尋可複製文字的PDF.md"

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

## joan-skill-conventions(基於酒Ann老師的skill建構基礎-v1.4, 調整Description of skill.md 後的v1.4.1版)
```text
version:1.4.1
目的: 作為建立,升級,檢視,重構 skill 的基本工具, 也能把claude ai (WebGUI)的skill 轉換成相容codex(仍須測試轉換成效)
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/dist/joan-skill-conventions-v1.4.1.zip
在Chatgpt web skill 安裝/上傳整包zip，即可安裝skill
```

文件:
無,叫AI讀zip解釋

## ai-session-handoff (AI Chat / AI Agent) 對話交接摘要 skill
version:1.1.1
目的: 交接對話的上下文脈絡摘要skill + speak-human-tw(整合說人話部分功能來梳理最後輸出)
支援: ChatGPT web Chat/web work; ChatGPT codex; Claude.ai web chat; Claude.ai code-cli

```text
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/dist/ai-session-handoff-v1.1.1.zip
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

## code-audit-fix
version: 無 (應該之後要定義為1.0版)
目的: （程式新建,重購,修改)後,檢查程式碼冗於未用,程式執行效率最佳化,邏輯錯誤,型別錯誤,溢位漏洞,例外錯誤,資安風險,然後修正的skill
支援: Claude.ai ChatWeb / Claude.ai code-cli, ChatGPT codex

```text
skill installer，前往下載 https://github.com/owner/robert-create-codex-skills/dist/code-audit-fix.zip
```

文件：
無,叫AI讀zip解釋

## challenge-claim
version: 0.2.0
目的: 「挑戰這個論點」、「幫我批判思考」、「找出這段分析的漏洞」或提供主張、研究摘要、PDF與決策方案時，用於拆解論證、檢查前提、提出反例並形成可驗證的修正結論
支援: Claude.ai ChatWeb / Claude.ai code-cli, ChatGPT codex

```text
skill installer，前往下載 https://github.com/owner/robert-create-codex-skills/dist/challenge-claim-v0.2.0.zip
```

文件：
無,叫AI讀zip解釋