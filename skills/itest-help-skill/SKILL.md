---
name: itest-help-skill
description: Use when answering questions about Spirent iTest Help 26.2.0, including iTest help, iTest GUI, iTest Tcl, iTest Python, iTest analysis, test cases, sessions, commands, actions, QuickCalls, response maps, topology, reports, preferences, Spirent TestCenter, Spirent Avalanche, CyberFlood, NTAF, and iTestRT. Search the bundled iTest Help RAG chunks first, cite chunk IDs and source paths, and if local search has no useful result, use external lookup and label those sources as external.
---

# iTest Help Skill

Version: 26.2.0.

Use this skill to answer questions from the packaged Spirent iTest Help 26.2.0 RAG chunks. Trigger examples include `itest help`, `itest gui`, `itest tcl`, `itest python`, and `itest analysis`.

## Required Workflow

1. Restate the user question as a compact search query.
2. Run local search first:

```powershell
python scripts/search_itest_help.py "<query>"
```

3. Read the top results. Prefer chunks whose `source_original_path`, `toc_path`, `heading_path`, and preview match the user question.
4. If one chunk is important, inspect it directly:

```powershell
python scripts/inspect_chunk.py <chunk_id>
```

5. Answer with evidence. Cite local results as `chunk_id` plus `source_original_path`.
6. If local search has no useful result, perform an external lookup when tools are available. Clearly label every non-bundled source as `External source`. Do not mix external facts into local-help facts without labeling them.
7. If neither local search nor external lookup is available, say what was searched and that the answer could not be verified.

## Source Priority

1. Bundled extracted RAG chunks in `references/rag`.
2. Local metadata in `manifest.md`, `validation_report.md`, `chunk_manifest.jsonl`, and `index_manifest.jsonl` inside `references/rag`.
3. External sources only after local search fails or is clearly insufficient.

## Evidence Rules

- Prefer direct local citations from `chunk_id`, `source_original_path`, `toc_path`, and `heading_path`.
- Use exact feature names from the help chunks when they matter, such as QuickCall, Response Map, Analysis, Tcl, Python, Session, Action, and Test Case.
- Keep uncertain statements marked as uncertain.
- Do not invent GUI menu paths, Tcl APIs, Python APIs, command syntax, or product support claims.
- When using external lookup, label the source line as `External source` and include the URL or source name when available.

## Local Tools

- `scripts/search_itest_help.py`: deterministic local search over bundled extracted RAG text chunks and metadata.
- `scripts/inspect_chunk.py`: print one text or image chunk by ID.
- `scripts/validate_itest_help_skill.py`: validate the skill contract, bundled extracted RAG directory, expected chunk counts, and required trigger terms.

## Capability Boundary

This skill answers from the iTest Help 26.2.0 RAG package. It is not a license checker, not a live product support channel, and not proof that a feature exists in versions other than 26.2.0. For version-specific or live vendor status questions, search local help first, then use external lookup and label the result as external.

## iTest Help Skill House Rule

If `itest-help-skill` cannot find a useful answer in the bundled local RAG chunks, it must try external lookup when available and must mark that material as `External source`. If external lookup is unavailable, it must report that limitation instead of guessing.
