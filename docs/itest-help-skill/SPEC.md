# iTest Help Skill SPEC

中文閱讀方式：這份文件是規格，負責說明 `itest-help-skill` 必須做到什麼。實際操作步驟請看 runbook。

This document defines the expected behavior, data boundaries, and acceptance criteria for the `itest-help-skill` Codex skill. It is a product and data contract, not an operational runbook.

## Purpose（目的）

`itest-help-skill` answers questions about Spirent iTest Automation 26.2.0 help documentation from packaged RAG chunks.

The skill must ground answers in retrieved help content. Answers should cite source metadata such as `source_file`, `toc_path`, and `heading_path` when available.

## Source Contract（來源契約）

This skill is bound to iTest Help 26.2.0.

Current source facts:

- Original RAG folder in this environment: `F:\MyCode\Java\iTest26.2\com.fnfr.svt.help_26.2.0.202603260106_RAG\itest-help`
- Packaged skill data folder: `references/rag`
- Skill name and folder name: `itest-help-skill`
- Packaged zip: `itest-help-skill.zip`

The original source path is a current local environment fact, not a portable requirement. On another computer, use that computer's actual source path.

Do not mix chunks from another iTest help version into this skill. If the help version changes, create a new skill version or update this source contract and rerun validation.

## Scope（資料範圍）

The packaged data must include the RAG output files created from iTest Help 26.2.0:

- `references/rag/manifest.md`
- `references/rag/validation_report.md`
- `references/rag/chunk_manifest.jsonl`
- `references/rag/index_manifest.jsonl`
- `references/rag/inventory.json`
- `references/rag/text/*.md`
- `references/rag/images/*.md`

The expected chunk counts for this 26.2.0 package are:

- Text chunks: `2891`
- Image chunks: `1221`
- Total chunk manifest records: `4112`

These counts are current 26.2.0 baseline facts. They are not universal iTest requirements.

## Data Model（資料格式）

Text chunk records must expose enough metadata for evidence-based answers:

- `kind`
- `chunk_id`
- `source_file`
- `source_original_path`
- `toc_path`
- `heading_path`
- `anchor`
- `context_ids`
- `index_keywords`
- `index_keyword_paths`
- `related_links`
- `images`
- `content_hash`
- `char_count`

Image chunk records must expose enough metadata to identify screenshots and OCR caveats:

- `kind`
- `image_chunk_id`
- `image_path`
- `category`
- `dimensions`
- `ocr_status`
- `has_ocr_text`
- `referenced_by`
- `usage_count`

Chunk Markdown files must keep their JSON front matter and body together. Search and inspection scripts may read the files directly from `references/rag`.

## Search Behavior（搜尋規則）

The skill must use deterministic local search before answering. The current search entrypoint is:

```powershell
python scripts\search_itest_help.py "<query>" --limit 8
```

Search should prefer evidence in this order:

1. Heading, TOC, index keyword, and context matches.
2. Text body matches.
3. Image OCR matches only when images are relevant or explicitly requested.

The search script must not create product behavior that is absent from the help chunks. It may rank and summarize candidate chunks only.

The inspection entrypoint is:

```powershell
python scripts\inspect_chunk.py <chunk-id-or-image-id>
```

## Evidence Boundaries（證據邊界）

Answers must distinguish product behavior from navigation metadata.

- Use `source_file`, `toc_path`, and `heading_path` to show where evidence came from.
- Treat OCR as unverified unless manually checked.
- Treat broken links, unresolved anchors, and oversized chunks as retrieval caveats.
- If the retrieved chunks do not support an answer, say what was found and what remains uncertain.
- Do not claim behavior for iTest versions other than 26.2.0 unless the answer clearly labels the source as 26.2.0-specific.

## Portability Requirements（可攜性要求）

The installed skill must work from its own folder after being copied to a Codex user skills directory.

Portable package requirements:

- `SKILL.md` exists at the skill folder root.
- `agents/openai.yaml` exists and its default prompt names `$itest-help-skill`.
- `references/rag` exists inside the skill.
- Search scripts use paths relative to the skill folder, not hard-coded local source paths.
- The package may document current local paths, but runtime scripts must not require the original RAG folder.

## Packaging Requirements（打包要求）

The skill folder name and frontmatter name must remain:

```yaml
name: itest-help-skill
```

The installable folder must be named:

```text
itest-help-skill
```

The zip contents must preserve `itest-help-skill/` as the top-level folder:

```text
itest-help-skill/
  SKILL.md
  agents/openai.yaml
  FROZEN.md
  scripts/search_itest_help.py
  scripts/inspect_chunk.py
  scripts/validate_itest_help_skill.py
  references/rag/chunk_manifest.jsonl
  references/rag/index_manifest.jsonl
  references/rag/text/
  references/rag/images/
```

## Verification Criteria（驗收條件）

A generated package is acceptable only if these checks pass:

- Codex skill validation passes with `quick_validate.py`.
- `scripts/validate_itest_help_skill.py` reports `text_chunks=2891` and `image_chunks=1221`.
- Every manifest record points to an existing Markdown chunk file.
- Sample searches return relevant chunks for QuickCall, response map XPath, and Spirent TestCenter command reference topics.
- The installed copy under the Codex user skills directory passes the same validation checks as the workspace copy.
- The zip has one top-level folder named `itest-help-skill` and includes `SKILL.md`.

Current verification commands for this Windows environment are listed in the runbook.

## Known Risks（已知風險）

The source conversion report has no blocking issue, but it lists non-blocking warnings:

- Some TOC href targets are missing.
- Some context href or anchor references are unresolved.
- Some index anchors are unresolved while topic-level mapping still works.
- Some internal links are broken in the original help content.
- Some image references are missing.
- One duplicate chunk hash group exists.
- Some chunks are oversized.

These issues affect navigation precision or retrieval granularity. They do not by themselves make the package invalid.