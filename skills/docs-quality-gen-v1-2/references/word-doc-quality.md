# Word Document Quality

## Purpose

Use these rules when producing, updating, or reviewing Word `.doc` and `.docx` documents for robert's personal documentation workflow.

Word files must meet the same quality bar as Markdown and HTML files. A successful save, conversion, or export is not enough.

## Core Rules

- Check format consistency, flow consistency, content consistency, readability, portability notes, and final delivery status.
- Read surrounding context before editing a paragraph, table, heading, list, or front-matter section.
- Preserve the existing document structure unless the user asks for a restructure.
- Keep examples, observed behavior, and formal requirements clearly separated.
- Mark local paths, user names, drive letters, tool locations, and version numbers as examples or current-environment facts.
- If the Word file is paired with Markdown, HTML, PDF, or another source file, check that the paired document carries the same meaning.
- Do not present a converted `.doc` file as equivalent to the original unless the conversion was verified.

## Word-Specific Checks

- Heading levels are ordered and readable.
- Lists use consistent indentation and numbering.
- Tables have clear headers when the table carries structured data.
- Captions, callouts, warnings, and notes are visually distinct enough to scan.
- Code, commands, paths, and inline literals are formatted consistently.
- Page breaks, section breaks, headers, footers, and title pages do not create confusing flow.
- Links, cross-references, and file names match the visible text around them.
- Images, screenshots, and diagrams have enough context for a reader to understand why they are included.

## Verification Levels

Use the strongest available verification level and report the highest level reached. Do not claim a higher level than the local tools support.

- Level 1, content re-read: use a document-aware reader such as `python-docx` for `.docx`, or a verified conversion path for `.doc`.
- Level 2, structural check: inspect headings, tables, lists, links, and required strings.
- Level 3, visual render QA: render to PDF or page images when a renderer such as Word, LibreOffice, or the documents skill render path is available.
- Level 4, accessibility or document-audit checks: run them when the local toolchain provides them.

Level 1 and Level 2 are the minimum fallback for a changed Word document when a document-aware reader is available. If visual render QA is unavailable, say so in the final reply. Then report the fallback checks that were run, such as content re-read and structural inspection.

## Failure Boundaries

- Do not silently skip visual QA when layout matters.
- Do not claim a `.doc` file was safely edited if it was only converted and not checked.
- Do not overwrite a Word file that may be open or locked unless the write succeeds. If a lock is likely, create a revised copy first and replace the original only after the lock clears.
- Do not mix Windows, WSL, and Linux path styles in commands or examples.
