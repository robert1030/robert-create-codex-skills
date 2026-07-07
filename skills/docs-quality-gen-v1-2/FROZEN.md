# Frozen Contract

## v1.2｜2026-07-07｜locked

This release keeps the installed skill identity `docs-quality-gen-v1-2` stable and upgrades the internal documentation quality contract to v1.2.

Frozen items：

- Stable skill folder and frontmatter name：`docs-quality-gen-v1-2`.
- Scope：robert's personal SPEC, runbook, README, paired Markdown/HTML, and Word `.doc` or `.docx` documentation quality work.
- Non-scope：public generic documentation standards, project-specific knowledge systems, marketing pages, UI design, and non-document delivery actions unless explicitly requested.
- Required references：`spec-rules.md`, `runbook-rules.md`, `markdown-html-sync.md`, `word-doc-quality.md`, `readability-grade7.md`, and `final-review-checklist.md`.
- Required metadata：`agents/openai.yaml` must describe SPEC, runbook, README, Markdown/HTML, Word DOC/DOCX, consistency, readability, verification level, and final delivery checks.
- Word verification levels：Level 1 content re-read, Level 2 structural check, Level 3 visual render QA, and Level 4 accessibility or document-audit checks.
- Word fallback rule：if visual render QA is unavailable, say so and report content re-read plus structural checks when those were run.
- Markdown/HTML sync rule：paired Markdown and HTML documents must carry the same meaning.
- Portability rule：local paths, user names, drive letters, tool locations, and version numbers must be examples or current-environment facts unless explicitly frozen.
- Final delivery rule：state what changed, what was verified, what was not done, and any unavailable checks or fallbacks.
- Release gate：run `scripts/validate_docs_quality_gen.py` before release, and rerun it with `--package <zip-path>` after packaging.
- Maintenance rule：record validator failures, repeated mistakes, and contract drift in `LESSONS.md`, and convert lessons into validator checks when practical.

## Change Policy

Do not weaken or remove frozen items without explicit user approval. Add new versions or stricter validation instead of silently relaxing the current contract.

Allowed without prior approval when validators pass：

- Clarify wording without changing meaning.
- Add examples that remain labeled as examples.
- Add stricter validator checks.
- Add maintenance lessons.
- Improve reference navigation.

Requires explicit approval：

- Removing a supported file type.
- Weakening Word verification levels or fallback reporting.
- Making Markdown/HTML sync optional for paired documents.
- Removing required references, `FROZEN.md`, `LESSONS.md`, or the self-validator.
- Changing stable skill identity or release packaging expectations.
