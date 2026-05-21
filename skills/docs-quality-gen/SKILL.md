---
name: docs-quality-gen
description: Use when producing, updating, synchronizing, or reviewing robert's personal documentation artifacts such as SPEC.md, runbook.md/htm/html, and README.md/htm/html. Enforces format consistency, flow consistency, content consistency, Markdown/HTML sync, grade-7 readability, local-environment portability notes, and final delivery review. Word doc/docx is out of scope for v1.
---

# Docs Quality Gen

This is robert's personal documentation quality gate. Use it for SPEC, runbook, README, and paired Markdown/HTML documents that robert maintains for handoff, operation, or review.

This skill is not a public documentation standard, not a generic writing assistant, and not a place for project-specific rules such as product help systems or domain manuals. For v1, Word `.doc` and `.docx` files are out of scope.

Do not perform non-document delivery actions such as packaging a skill, installing a skill, syncing to `.codex\skills`, or producing a zip unless the user explicitly asks for that action.

## Supported Files

- `SPEC.md`
- `runbook.md`, `runbook.htm`, `runbook.html`
- `README.md`, `README.htm`, `README.html`
- Paired Markdown and HTML versions of those documents

## Workflow

1. Identify the document type: SPEC, runbook, README, Markdown/HTML pair, review-only, or final delivery check.
2. Read only the matching references:
   - SPEC: `references/spec-rules.md`
   - Runbook: `references/runbook-rules.md`
   - Markdown/HTML sync: `references/markdown-html-sync.md`
   - Handoff or operation docs: `references/readability-grade7.md`
   - Final review: `references/final-review-checklist.md`
3. State the success criteria before editing: what will be changed and how it will be verified.
4. Read surrounding context before changing text. Check related sections, callers, cross-links, paired files, and nearby terminology.
5. Make the smallest necessary document edits. Keep examples, observed behavior, and formal requirements clearly separated.
6. After editing, review format consistency, flow consistency, content consistency, Markdown/HTML sync when relevant, and grade-7 readability when the document is for handoff or operation.
7. In the final reply, state what changed, what was verified, and what was not done.

## Hard Rules

- When editing paired documents, check the synchronized version such as `.md` and `.htm`/`.html`.
- Before final delivery, always review flow consistency and content consistency.
- For handoff or operation documents, always run a grade-7 readability pass.
- If a contradiction appears, do not change only one sentence. Check the related paragraphs and matching documents.
- Do not turn one example, one path, or one version number into a permanent rule.
- Mark local paths, user names, drive letters, tool install locations, and version numbers as examples or current-environment facts. Tell readers to replace them on other computers.
- Keep shell syntax and path style consistent with the stated execution environment.
- The final reply must clearly say what changed, what was verified, and what was not done.
