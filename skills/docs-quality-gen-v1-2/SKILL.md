---
name: docs-quality-gen-v1-2
description: Use when producing, updating, synchronizing, or reviewing robert's personal documentation artifacts such as SPEC.md, runbook.md/htm/html, README.md/htm/html, and Word doc/docx files. Enforces format consistency, flow consistency, content consistency, Markdown/HTML sync, Word document quality checks, grade-7 readability, local-environment portability notes, and final delivery review.
---

# Docs Quality Gen

This is robert's personal documentation quality gate. Use it for SPEC, runbook, README, and paired Markdown/HTML documents that robert maintains for handoff, operation, or review.

Version note: v1.2 strengthens the v1.1 Word checks with explicit workflow gates, frozen contract handling, release validation, maintenance lessons, and final-delivery house rules. Word files still meet the same quality bar as Markdown and HTML documents: format consistency, flow consistency, content consistency, readability, portability notes, and honest final delivery.

This skill is not a public documentation standard, not a generic writing assistant, and not a place for project-specific rules such as product help systems or domain manuals.

Do not perform non-document delivery actions such as packaging a skill, installing a skill, syncing to `.codex\skills`, or producing a zip unless the user explicitly asks for that action.

## Execution Priority

1. Protect the v1.2 contract first. Do not weaken `FROZEN.md`, required references, validator behavior, Word verification levels, Markdown/HTML sync rules, or final delivery wording without explicit user approval.
2. Define success criteria before editing. Name the files, expected sync relationships, validation commands, Word verification level, and known limits.
3. Read the surrounding document context before changing text. Include paired Markdown/HTML files, related SPEC/runbook/README sections, and source notes when they exist.
4. Make surgical edits. Do not rewrite a whole document when a scoped correction is enough, unless stale contract drift affects the full document.
5. Run the relevant gates before delivery. At minimum run `scripts/validate_docs_quality_gen.py` when editing or releasing this skill, and run the matching document checks for the user artifact.
6. Report honestly. Say what changed, what was verified, what was not run, and which fallback was used when Word visual QA or independent acceptance is unavailable.

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
   - v1.2 self-validation before packaging or release: `scripts/validate_docs_quality_gen.py`
   - Contract and maintenance context when changing this skill: `FROZEN.md` and `LESSONS.md`
3. State the success criteria before editing: what will be changed and how it will be verified.
4. Read surrounding context before changing text. Check related sections, callers, cross-links, paired files, and nearby terminology.
5. Make the smallest necessary document edits. Keep examples, observed behavior, and formal requirements clearly separated.
6. After editing, review format consistency, flow consistency, content consistency, Markdown/HTML sync when relevant, Word verification level when relevant, and grade-7 readability when the document is for handoff or operation.
7. If the document is paired or mirrored, search key terms in every paired file before final delivery.
8. If the work changes this skill, run the self-validator before packaging, then validate the package with `--package`.
9. In the final reply, state what changed, what was verified, what was not done, and any remaining risk.

## House Rules

1. **Contract rules are frozen once released.** Keep stable skill identity, supported file types, Word verification levels, Markdown/HTML sync requirements, final delivery wording, and validator behavior in `FROZEN.md`.
2. **Validation is a delivery gate.** Do not call the skill release verified unless the self-validator and package validation pass. For user documents, do not claim checks that were not run.
3. **Paired documents move together.** When Markdown and HTML represent the same README or runbook, update both or clearly state that one side was not changed.
4. **Word quality is not file-open quality.** A `.doc` or `.docx` file is not verified merely because it opens, saves, or converts. Report the highest verification level reached.
5. **Examples are not requirements.** Local paths, user names, drive letters, tool locations, and version numbers must be labeled as current-environment examples unless they are truly part of the contract.
6. **Readability must not weaken accuracy.** Grade-7 readability means a clear main line, not removing important limits or technical truth.
7. **No project rules inside the generic gate.** Keep project-specific knowledge, such as iTest help behavior, in the project skill or project docs.
8. **Three repeated failures stop the loop.** After three failures of the same validation category, stop editing and report the validator, output, attempts, likely cause, and recommended decision.
9. **Acceptance must be evidence-based.** Prefer executable validators and document re-read. If independent review is unavailable, label the result as local best-effort acceptance.

## Contract And Maintenance

- `FROZEN.md` records the v1.2 release contract and the change policy.
- `LESSONS.md` records validation failures, contract drift, and repair lessons. Convert lessons into validator checks when practical.
- `scripts/validate_docs_quality_gen.py` is the self-validation gate for this skill and packaged zips.
- `agents/openai.yaml` must stay aligned with this skill: compact display text, relevant default prompt, and document-quality scope.

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
- Before packaging or releasing v1.2 changes, run `python scripts/validate_docs_quality_gen.py` from the skill folder or repository root. When a packaged zip exists, also pass `--package <zip-path>`.
- Before changing this skill's contract, read `FROZEN.md` and preserve or intentionally version frozen items.
- After a validator catches a real issue, append a concise lesson to `LESSONS.md` and add a validator check when practical.
- The final reply must clearly say what changed, what was verified, and what was not done.
