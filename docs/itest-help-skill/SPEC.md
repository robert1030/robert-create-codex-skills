# iTest Help Skill SPEC

This document defines the expected behavior, data boundaries, and acceptance criteria for the `itest-help` Codex skill. It is a product and data contract, not an operational runbook. Use the runbook for commands and update steps.

## Purpose

`itest-help` answers questions about Spirent iTest Automation help documentation from a packaged, self-contained search index.

The skill must ground answers in retrieved help content and cite logical source references such as `topics/quickcalls_arguments_in_quickcall_steps.htm`.

## Scope

Current indexed source scope:

- Include `topics/**/*.htm`
- Include `topics/**/*.html`
- Include short popup help pages under `topics/popups/`
- Include analysis-rule popup help pages under `topics/popups/arules/`

Current out-of-scope source material:

- HTML files outside the `topics/` directory in the original help plugin
- Non-HTML assets from the help plugin, unless needed by a future search or citation design

Expanding scope outside `topics/` requires a separate inventory review, duplicate-path review, and search-quality verification.

## Data Model

Each indexed help page must preserve stable identity fields:

- `relative_path`: path relative to `topics/`, using forward slashes
- `source_ref`: logical source path in the form `topics/<relative_path>`
- `file_name`: base file name, retained for display and compatibility

Each indexed help page must include searchable content:

- `text`: cleaned plain text extracted from the HTML
- `text_length`: length of cleaned text
- `links`: normalized links that do not depend on local absolute paths

Each indexed help page may include best-effort metadata:

- `title`
- `h1`
- `headings`
- `doc_set`
- `probable_category`
- `classification_basis`

Best-effort metadata is not authoritative. Popup pages may have empty `title` or `h1` while still containing valid searchable text.

## Search Behavior

Search must be deterministic and lexical. It is not semantic search and must not infer iTest behavior beyond retrieved help content.

Search results must expose logical sources through `source_ref`. User-facing answers should cite `source_ref` or the source file name when context is unambiguous.

When multiple pages share the same `file_name`, lookup by file name alone must not silently choose one page. The tool must report ambiguity and require `relative_path` or `source_ref`, for example `topics/popups/query.html`.

Weak or mixed search results must be described as weak or mixed instead of being treated as authoritative.

## Portability Requirements

The packaged skill must be self-contained. It must not require the original extracted help plugin directory.

Packaged references must not contain machine-specific absolute paths, such as Windows drive paths, user profile paths, or workspace-specific source directories.

References to original help content must use logical source paths:

```text
topics/<relative_path>
```

Eclipse help URIs or original plugin references should be normalized to logical `topics/...` paths when included in packaged data.

Version runbooks may define environment-specific validation patterns. Those patterns are examples for a known build environment, not universal SPEC requirements.

## Packaging Requirements

The skill name must remain:

```yaml
name: itest-help
```

The installable folder must be named:

```text
itest-help
```

Zip file names may be versioned, but the zip contents must preserve `itest-help/` as the top-level folder:

```text
itest-help/
  SKILL.md
  agents/openai.yaml
  scripts/search_help.py
  references/help_pages.jsonl
  references/search_index.json
  references/search_index_summary.json
```

## Verification Criteria

A generated package is acceptable only if:

- Inventory count equals `help_pages.jsonl` line count.
- `search_index_summary.json` document count equals `help_pages.jsonl` line count.
- Packaged references contain no machine-specific absolute source paths.
- Sample searches return relevant pages for common topics such as parameters, QuickCalls, response maps, and query commands.
- A duplicate file-name lookup reports ambiguity instead of choosing an arbitrary page.
- A lookup using `source_ref` or `relative_path` can show a specific popup page.
- Zip extraction preserves the required `itest-help/` top-level folder.

## Version Baselines

iTest 25.4 baseline:

```text
topics                  761
topics/popups           166
topics/popups/arules     36
total                   963
```

The `963` count is a 25.4 baseline fact, not a permanent requirement. New iTest versions must be counted from their own source tree.

## Known Risks

Popup pages often have empty `title` and `h1`, so title completeness alone is not a valid failure signal.

Short popup pages can rank highly for single-term queries. Search-quality checks must confirm that popup hits improve recall without hiding primary help pages.

Subdirectories can contain files with the same base name. `relative_path` and `source_ref` are required for stable identity.

The current scope excludes HTML outside `topics/`. That does not prove excluded files are irrelevant; it only means they are outside the current accepted data boundary.

Generated categories are heuristic and should not be treated as official Spirent taxonomy.
