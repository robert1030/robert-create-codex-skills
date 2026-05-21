# Markdown HTML Sync

## Purpose

Use these rules when a Markdown document and an HTML document represent the same README or runbook.

## Core Rules

- If `.md` is the source, the HTML file must carry the same meaning.
- HTML is not a free rewrite of the Markdown source.
- Add, remove, or change warnings in both files.
- Keep paths, file names, version numbers, lists, and commands aligned.
- HTML may use `<code>`, `<pre><code>`, and `<strong>` for formatting, but the meaning must not change.
- After editing, search key terms to confirm both files were updated.

## Checks

- Confirm the same path appears in both files.
- Confirm the same zip name appears in both files.
- Confirm the same warning appears in both files.
- Confirm required lists in Markdown also exist in HTML.
- Confirm HTML did not miss paragraphs added to Markdown.
- Confirm HTML does not keep old paths, old file names, or old version numbers.
