---
name: itest-help-skill
description: Use when answering questions about Spirent iTest Automation 26.2.0 help, including GUI workflows, test cases, sessions, commands, actions, QuickCalls, parameters, response maps, topology, reports, preferences, Spirent TestCenter, Spirent Avalanche, CyberFlood, NTAF, iTestRT, Tcl, Python, and related iTest documentation. Searches the packaged iTest 26.2 help RAG chunks, cites source help files, and avoids guessing when the help data does not contain enough evidence.
---

# iTest Help Skill

Version note: this skill is bound to iTest Help 26.2.0 RAG chunks. Treat the packaged source as a frozen knowledge source. If the help version or chunking contract changes, create a new version or clearly update the source contract before packaging.

## Purpose

Use this skill to answer iTest development and troubleshooting questions from the packaged iTest 26.2.0 help data. Favor evidence from the RAG chunks over memory.

Typical requests include questions about test cases, sessions, commands, actions, QuickCalls, parameters, response maps, topology, reports, preferences, Spirent TestCenter, Spirent Avalanche, CyberFlood, NTAF, iTestRT, Tcl, and Python in iTest.

## Required Workflow

1. Search before answering. Run `python scripts/search_itest_help.py "<query>" --limit 8` from this skill folder.
2. Read the strongest matching chunks listed by the script. Use `python scripts/inspect_chunk.py <chunk-id-or-image-id>` when the exact chunk body is needed.
3. Prefer text chunks. Read image chunks only when the user asks about screenshots, dialogs, icons, or when a text chunk points to an image.
4. Cite evidence in the answer with `source_file`, `toc_path`, and `heading_path` when available.
5. If OCR text is used, state that OCR is not manually verified.
6. If results are weak or conflicting, say what was found and what remains uncertain. Do not invent iTest behavior.

## Search Guidance

Use narrow terms first, then broaden:

- For commands: search the command name plus `syntax`, `parameters`, or `return value`.
- For actions: search the action name plus `action`, `example`, or `properties`.
- For response maps: search `response map`, parser type, XPath, table map, block map, or token name.
- For sessions: search the session type plus `session profile`, `terminal`, `capture`, or `replay`.
- For GUI workflows: search the dialog, view, editor, wizard, or preference page name.

When multiple chunks match, prefer chunks with heading or index keyword matches over body-only matches. When a large reference chunk is returned, inspect nearby headings inside the chunk before answering.

## Packaged Data

The RAG source lives under `references/rag/`:

- `manifest.md` summarizes conversion and known warnings.
- `validation_report.md` lists validation results.
- `chunk_manifest.jsonl` maps chunk IDs to metadata.
- `index_manifest.jsonl` maps help index keywords to topics.
- `text/` contains text chunk Markdown files.
- `images/` contains image chunk Markdown files with OCR where available.

Known source warnings are non-blocking. They include some unresolved anchors, broken internal links, missing image references, and oversized chunks. Treat these as retrieval caveats, not as proof that the answer is wrong.

## Boundaries

This skill does not run iTest, validate live device behavior, or guarantee that a workflow applies to versions other than iTest 26.2.0. If the user asks about another version, answer from 26.2.0 only when useful and label it as version-specific.
