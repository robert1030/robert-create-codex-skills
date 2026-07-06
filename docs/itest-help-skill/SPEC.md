# itest-help-skill SPEC

本文是 `itest-help-skill` 的交付契約。它說明 skill 必須支援什麼、資料來源是什麼、以及如何驗證。

## Scope

`itest-help-skill` 必須協助查詢 Spirent iTest Help 26.2.0。它支援下列主題：

- iTest Help 使用方式。
- iTest GUI。
- iTest Tcl interpreter commands。
- iTest Python interpreter commands。
- iTest Analysis 與 Analysis Rules。
- Test cases、sessions、commands、actions、QuickCalls、response maps、topology、reports、preferences、Spirent TestCenter、Spirent Avalanche、CyberFlood、NTAF、iTestRT。

## Source Contract

目前環境的來源例子如下。其他電腦請替換成實際路徑。

- RAG chunk source: `F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help_ragchunk.zip`
- Original help source: `F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106\itest-help_26.2.0.zip`
- Skill folder: `F:\MyCode\robert-create-codex-skills\skills\itest-help-skill`
- Bundled extracted RAG directory inside the skill: `references/rag`

The skill package must be self-contained. It must not require the original help zip or source RAG zip at answer time.

## Frozen Values

These values are current-version facts for 26.2.0 and are checked by `scripts/validate_itest_help_skill.py`.

- Skill name: `itest-help-skill`
- Internal version: `26.2.0`
- Text chunks: `3012`
- Image chunks: `1799`
- Chunk manifest rows: `3012`
- Required trigger terms: `itest help`, `itest gui`, `itest tcl`, `itest python`, `itest analysis`

## Required Behavior

- Search bundled local RAG chunks before using other sources.
- Cite local evidence with `chunk_id` and `source_original_path`.
- Use `toc_path` and `heading_path` to judge whether a result matches the question.
- Do not invent GUI paths, command syntax, API behavior, or product support claims.
- If local RAG search has no useful result, use external lookup when available.
- Label non-bundled evidence as `External source`.
- If external lookup is not available, state that limitation and do not guess.

## Required Files

The skill must include:

- `SKILL.md`
- `agents/openai.yaml`
- `FROZEN.md`
- `references/rag/manifest.md`
- `references/rag/validation_report.md`
- `references/rag/chunk_manifest.jsonl`
- `references/rag/index_manifest.jsonl`
- `references/rag/text/*.md`
- `references/rag/images/*.md`
- `scripts/search_itest_help.py`
- `scripts/inspect_chunk.py`
- `scripts/validate_itest_help_skill.py`

## Verification

The build is acceptable only when these checks pass:

- `python -m py_compile` passes for all scripts.
- `python scripts/validate_itest_help_skill.py` passes.
- Codex `quick_validate.py` reports `Skill is valid!`.
- Local smoke tests return at least one result for `itest help`, `itest gui`, `itest tcl`, `itest python`, and `itest analysis`.
- The package zip contains top-level folder `itest-help-skill/` and includes `SKILL.md`.

## Known Limits

The bundled RAG report lists non-blocking limits such as oversized chunks, unknown image classification, and broken internal links from the source help. These limits must be disclosed when they affect an answer. They are not automatic blockers if local search and source citation still work.
