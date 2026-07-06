# iTest Help Skill Frozen Contract

Version: 26.2.0.

This file records the values that must not drift without an explicit version review.

## Frozen Values

- Skill name: `itest-help-skill`
- Skill folder: `itest-help-skill`
- Help version: `iTest Help 26.2.0`
- Bundled extracted RAG directory: `references/rag`
- Text chunks: `3012`
- Image chunks: `1799`
- Required trigger terms: `itest help`, `itest gui`, `itest tcl`, `itest python`, `itest analysis`
- Required local search script: `scripts/search_itest_help.py`
- Required inspect script: `scripts/inspect_chunk.py`
- Required validation script: `scripts/validate_itest_help_skill.py`
- External fallback rule: if local RAG search has no useful result, use external lookup when available and label those sources as `External source`.

## Change Rule

Do not change these values silently. If the RAG package changes, extract it into `references/rag`, then update `SKILL.md`, `FROZEN.md`, `validate_itest_help_skill.py`, docs, and package verification together.
