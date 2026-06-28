# docs-quality-gen SPEC

中文閱讀方式：這份文件是規格，負責說明 `docs-quality-gen` 必須做到什麼。實際操作流程請看 `runbook.md` 或 `runbook.htm`。

This document defines the expected behavior, boundaries, and acceptance criteria for robert's personal `docs-quality-gen` Codex skill. It is a document quality contract, not an operation runbook.

## Purpose（目的）

中文說明：`docs-quality-gen` 是 robert 個人的文件品質 gate。它用來產生、同步、檢查 SPEC、runbook、README、成對的 Markdown/HTML 文件，以及 Word `.doc` 和 `.docx` 文件。v1.1 加入 Word 文件品質檢查。

`docs-quality-gen` must help Codex produce, update, synchronize, and review robert's personal documentation artifacts with these goals:

- Format consistency
- Flow consistency
- Content consistency
- Markdown and HTML synchronization
- Word `.doc` and `.docx` document quality checks
- Grade-7 readability for handoff or operation documents
- Clear separation between examples, observed behavior, and formal requirements
- Honest final delivery notes

## Scope（範圍）

中文說明：這段定義 v1.1 支援哪些文件。這不是公開通用文件標準，也不是泛用寫作助手。

In v1.1, the skill applies to these documentation artifacts:

- `SPEC.md`
- `runbook.md`
- `runbook.htm`
- `runbook.html`
- `README.md`
- `README.htm`
- `README.html`
- Paired Markdown and HTML versions of those files
- Word `.doc` and `.docx` documents

The skill is for robert's personal documentation workflow. It must not present itself as a public documentation standard or generic writing assistant.

Word files must meet the same quality bar as Markdown and HTML files. This includes format consistency, flow consistency, content consistency, readability, portability notes, and honest final delivery notes.

## Out of Scope（非範圍）

中文說明：這些項目不屬於 v1.1。除非使用者明確要求，skill 不應主動做文件以外的交付動作。

The v1.1 skill must not define rules for:

- Project-specific knowledge, such as iTest help rules
- Full HTML visual design, brand design, interactive UI, or marketing-page layout
- General public documentation style guides
- Non-document delivery actions, such as packaging a skill, installing a skill, syncing into `.codex\skills`, or producing a zip

If the user explicitly asks for a non-document delivery action, Codex may perform that action by using the proper skill or tool. That exception must not change the default responsibility of `docs-quality-gen`.

## Required Skill Structure（必要結構）

中文說明：這段規定 skill 本體要有哪些主要檔案。`agents/openai.yaml` 可存在作為 Codex UI metadata，但品質規則主體應在 `SKILL.md` 與 `references/`。

The skill folder must be named:

```text
docs-quality-gen
```

The required skill entry file is:

```text
docs-quality-gen/SKILL.md
```

The v1.1 reference files are:

```text
docs-quality-gen/references/spec-rules.md
docs-quality-gen/references/runbook-rules.md
docs-quality-gen/references/markdown-html-sync.md
docs-quality-gen/references/word-doc-quality.md
docs-quality-gen/references/readability-grade7.md
docs-quality-gen/references/final-review-checklist.md
docs-quality-gen/scripts/validate_docs_quality_gen.py
```

`SKILL.md` must stay concise and act as the entry point. Detailed rules should live in the matching reference file so Codex only loads the context needed for the current task.

## Required Workflow（必要流程）

中文說明：這段是 skill 的行為契約。Codex 使用此 skill 時，應先判斷文件類型，再讀對應 reference，最後做交付前 review。

When the skill is used, Codex must follow this workflow:

1. Identify the document type: SPEC, runbook, README, Markdown/HTML pair, Word document, review-only, or final delivery check.
2. Read the matching reference files.
3. State success criteria before editing.
4. Read surrounding context before changing text.
5. Make the smallest necessary document edits.
6. Separate examples, observed behavior, and formal requirements.
7. Review format consistency, flow consistency, content consistency, sync status, Word document quality when relevant, and readability after editing.
8. In the final reply, state what changed, what was verified, and what was not done.

## Markdown and HTML Sync Requirements（Markdown/HTML 同步要求）

中文說明：如果 Markdown 和 HTML 是同一份 runbook 或 README 的兩種版本，內容意思必須同步。HTML 不能變成另一份自由改寫版。

When a Markdown file and an HTML file represent the same document:

- The Markdown file may be treated as the source when no other source is stated.
- The HTML file must preserve the same meaning.
- Warnings, paths, file names, version numbers, command examples, and required lists must match.
- HTML may use semantic tags such as `<code>`, `<pre><code>`, and `<strong>`, but it must not change the document meaning.
- After edits, Codex must search key terms or compare sections to confirm both versions were updated.

## Word Document Quality Requirements（Word 文件品質要求）

中文說明：v1.1 支援 Word `.doc` 和 `.docx` 文件品質檢查。Word 文件的標準要和 Markdown、HTML 一樣，不能只確認檔案可開啟或可儲存。

For Word `.doc` and `.docx` documents, quality checks must include:

- Format consistency for headings, lists, tables, captions, code, page breaks, headers, and footers
- Flow consistency for prerequisites, step order, section order, and cross-references
- Content consistency with paired Markdown, HTML, PDF, source notes, or previous versions when those exist
- Grade-7 readability when the document is for handoff or operation
- Portability notes for local paths, user names, drive letters, tool locations, and version numbers
- Honest final delivery notes that say which Word checks were run

Word verification should use the strongest available level and report the highest level reached:

- Level 1, content re-read with a document-aware reader when possible
- Level 2, structural inspection of headings, tables, lists, links, and required strings
- Level 3, visual render QA to PDF or page images when a renderer is available
- Level 4, accessibility or document-audit checks when the local toolchain provides them

If visual render QA is unavailable, the final reply must say so and name the fallback checks that were used.

## Portability Requirements（可攜性要求）

中文說明：本機路徑可以當例子，但不能寫成所有電腦都適用。文件應提醒讀者依自己的環境替換。

The skill must not treat local paths, user names, drive letters, tool install locations, or version numbers as universal facts.

Current-environment examples may be documented, such as:

```text
C:\Users\robert\.codex\skills\docs-quality-gen
F:\MyCode\robert-create-codex-skills\docs\docs-quality-gen
```

These paths are examples from the current Windows environment. On another computer, replace them with the actual user profile, drive letter, workspace path, and skill location.

Ubuntu examples should use placeholders or native paths such as:

```text
<workspace>/robert-create-codex-skills/docs/docs-quality-gen
```

For WSL only, the current Windows `F:` drive may appear as:

```text
/mnt/f/MyCode/robert-create-codex-skills/docs/docs-quality-gen
```

The `/mnt/f/...` path is a WSL example, not a native Linux requirement.

## Acceptance Criteria（驗收條件）

中文說明：符合這些條件，才算 `docs-quality-gen` 文件品質 gate 的 v1.1 行為可接受。

The skill is acceptable when:

- `SKILL.md` explains the purpose, supported file types, v1.1 exclusions, basic workflow, and hard rules.
- Each v1.1 reference file exists and has a single clear responsibility.
- SPEC rules do not become runbook steps.
- Runbook rules describe step-by-step operation quality.
- Markdown/HTML sync rules require paired files to carry the same meaning.
- Word document quality rules require explicit verification levels, content, structure, visual render QA when available, and honest fallback reporting when render QA is not available.
- Grade-7 readability rules improve clarity without reducing technical correctness.
- Final review rules require format, flow, content, readability, and honest delivery checks.
- `scripts/validate_docs_quality_gen.py` passes before packaging or release.
- Word `.doc` and `.docx` behavior is included for v1.1 document quality checks.
- iTest or other project-specific knowledge is not included.
- The skill remains robert's personal documentation quality gate, not a public generic standard.
