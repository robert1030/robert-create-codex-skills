# Final Review Checklist

## Purpose

Use this checklist before final delivery of robert's personal documentation changes.

## 1. Format Consistency

- Heading levels are reasonable.
- List style is consistent.
- Code block language labels are correct when used.
- Markdown and HTML versions match when both exist.
- Word documents use consistent headings, lists, tables, captions, code formatting, page breaks, headers, and footers.

## 2. Flow Consistency

- Step order is reasonable.
- Prerequisites appear before dependent steps.
- File names, paths, and version numbers are consistent.
- Default outputs match verification commands.
- Commands can run in the stated environment.
- Shell syntax and path format are consistent.

## 3. Content Consistency

- Definitions do not conflict across the document.
- SPEC, runbook, and README do not contradict each other when they cover the same topic.
- Word documents do not contradict paired Markdown, HTML, PDF, or source notes when those files exist.
- Examples, observed results, and formal requirements are clearly separated.
- Local-environment assumptions are not written as universal facts.
- Local examples include replacement notes or portable alternatives where useful.

## 4. Readability

- The opening explains the document purpose.
- Technical terms are explained when needed.
- High-risk sections include plain-language reminders.
- A grade-7 reader can follow the main line.

## 5. Honest Delivery

- Check the frozen contract before changing released skill behavior.
- Update `LESSONS.md` when a validator failure, contract drift, or repeated documentation mistake shaped the fix.
- Run release validation with `scripts/validate_docs_quality_gen.py` before packaging this skill, and run it again with `--package <zip-path>` after packaging.
- State which files changed.
- State what was verified.
- For Word documents, state the highest verification level reached and whether content re-read, structural checks, visual render QA, and accessibility or document-audit checks were run.
- State what was not done.
- Say clearly when tests, packaging, or synchronization were not run.
- Say clearly when Word visual render QA was not available and name the fallback checks used instead.
