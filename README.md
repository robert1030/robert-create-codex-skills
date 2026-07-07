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

Codex 安裝提示：

```text
$skill-installer install https://github.com/owner/robert-create-codex-skills/skills/itest-help-skill
```

目前基礎版本：iTest v26.2。

文件：

- `docs/itest-help-skill/itest-help-skill-runbook.htm`
- `docs/itest-help-skill/SPEC.md`

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

## codex-skill-conventions (基於酒Ann老師的skill建構基礎,轉換的codex-skill-conventions-v1-6-1)
```text
version:1.6.1
限制: codex使用，SKILL.md內容定義，chatgpt和cdoex 結構不一樣，不能混用，
目的: 作為建立,升級,檢視,重構 skill 的基本工具, 也能把claude ai (WebGUI)的skill 轉換成相容codex(仍須測試成效)
$skill-installer install https://github.com/owner/robert-create-codex-skills/skills/codex-skill-conventions
或解壓縮zip後,整包,放到.codex/skills/內 -> /使用者家目錄/.codex/skills/codex-skill-conventions
```

文件:
無,叫AI讀

## gpt-skill-conventions (基於酒Ann老師的skill建構基礎,轉換的gpt-skill-conventions-v1-6-1)
```text
version:1.6.1
限制: Chatgpt(web)使用，SKILL.md 內容定義，chatgpt和cdoex 結構不一樣，不能混用，
目的: 作為建立,升級,檢視,重構 skill 的基本工具, 也能把claude ai (WebGUI)的skill 轉換成相容codex(仍須測試轉換成效)
skill installer，前往下載 https://github.com/robert1030/robert-create-codex-skills/gpt-skill-conventions-v1-6-1.zip
在Chatgpt web skill 安裝/上傳整包zip，即可安裝skill
```

文件:
無,叫AI讀zip解釋