---
name: docs-quality-gen-v1-1
description: Use when producing, updating, synchronizing, or reviewing robert's personal documentation artifacts such as SPEC.md, runbook.md/htm/html, README.md/htm/html, and Word doc/docx files. Enforces format consistency, flow consistency, content consistency, Markdown/HTML sync, Word document quality checks, grade-7 readability, local-environment portability notes, and final delivery review.
---

# Docs Quality Gen

This is robert's personal documentation quality gate. Use it for SPEC, runbook, README, and paired Markdown/HTML documents that robert maintains for handoff, operation, or review.

Version note: v1.1 adds Word `.doc` and `.docx` document quality checks. Word files must meet the same quality bar as Markdown and HTML documents: format consistency, flow consistency, content consistency, readability, portability notes, and honest final delivery.

This skill is not a public documentation standard, not a generic writing assistant, and not a place for project-specific rules such as product help systems or domain manuals.

Do not perform non-document delivery actions such as packaging a skill, installing a skill, syncing to `.codex\skills`, or producing a zip unless the user explicitly asks for that action.

## Supported Files

- `SPEC.md`
- `runbook.md`, `runbook.htm`, `runbook.html`
- `README.md`, `README.htm`, `README.html`
- Paired Markdown and HTML versions of those documents
- Word `.doc` and `.docx` documents

## Workflow

1. Identify the document type: SPEC, runbook, README, Markdown/HTML pair, Word document, review-only, or final delivery check.
2. Read only the matching references:
   - SPEC: `references/spec-rules.md`
   - Runbook: `references/runbook-rules.md`
   - Markdown/HTML sync: `references/markdown-html-sync.md`
   - Word `.doc` or `.docx`: `references/word-doc-quality.md`
   - Handoff or operation docs: `references/readability-grade7.md`
   - Final review: `references/final-review-checklist.md`
   - v1.1 self-validation before packaging or release: `scripts/validate_docs_quality_gen.py`
3. State the success criteria before editing: what will be changed and how it will be verified.
4. Read surrounding context before changing text. Check related sections, callers, cross-links, paired files, and nearby terminology.
5. Make the smallest necessary document edits. Keep examples, observed behavior, and formal requirements clearly separated.
6. After editing, review format consistency, flow consistency, content consistency, Markdown/HTML sync when relevant, Word verification level when relevant, and grade-7 readability when the document is for handoff or operation.
7. In the final reply, state what changed, what was verified, and what was not done.

## Hard Rules

- When editing paired documents, check the synchronized version such as `.md` and `.htm`/`.html`.
- Word `.doc` and `.docx` files must receive the same quality review as Markdown and HTML files. Do not treat a readable export or successful save as enough.
- For Word documents, verify content and structure with document-aware tools when possible, and render to PDF or page images for visual QA when a renderer is available. Use the highest available Word verification level from `references/word-doc-quality.md`. If visual render QA is not available, state that clearly and use content re-read plus structural checks as the fallback.
- Before final delivery, always review flow consistency and content consistency.
- For handoff or operation documents, always run a grade-7 readability pass.
- If a contradiction appears, do not change only one sentence. Check the related paragraphs and matching documents.
- Do not turn one example, one path, or one version number into a permanent rule.
- Mark local paths, user names, drive letters, tool install locations, and version numbers as examples or current-environment facts. Tell readers to replace them on other computers.
- Keep shell syntax and path style consistent with the stated execution environment.
- Before packaging or releasing v1.1 changes, run `python scripts/validate_docs_quality_gen.py` from the skill folder or repository root. When a packaged zip exists, also pass `--package <zip-path>`.
- The final reply must clearly say what changed, what was verified, and what was not done.
