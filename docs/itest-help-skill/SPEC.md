# iTest Help Skill SPEC

中文閱讀方式：這份文件是規格，負責說明 `itest-help` 必須做到什麼。實際要輸入哪些指令，請看 runbook。

This document defines the expected behavior, data boundaries, and acceptance criteria for the `itest-help` Codex skill. It is a product and data contract, not an operational runbook. Use the runbook for commands and update steps.

## Purpose（目的）

中文說明：這段說明這個 skill 的目的。它要用打包好的 iTest help 資料回答問題，回答時要指出資料來源。

`itest-help` answers questions about Spirent iTest Automation help documentation from a packaged, self-contained search index.

The skill must ground answers in retrieved help content and cite logical source references such as `topics/quickcalls_arguments_in_quickcall_steps.htm`.

## Scope（資料範圍）

中文說明：這段規定哪些 help HTML 會放進 skill，哪些暫時不放。若以後要加入更多資料，必須重新檢查數量、同名檔案與搜尋品質。

Current indexed source scope:

- Include `topics/**/*.htm`
- Include `topics/**/*.html`
- Include short popup help pages under `topics/popups/`
- Include analysis-rule popup help pages under `topics/popups/arules/`

Current out-of-scope source material:

- HTML files outside the `topics/` directory in the original help plugin
- Non-HTML assets from the help plugin, unless needed by a future search or citation design

Expanding scope outside `topics/` requires a separate inventory review, duplicate-path review, and search-quality verification.

## Data Model（資料格式）

中文說明：這段規定每一頁 help 存進索引時要保留哪些欄位。重點是每一頁都要有穩定路徑，不能依賴某台電腦的本機路徑。

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

Search results may include deterministic UI-scope hints inferred from packaged page metadata:

- `ui_scope`: stable scope key used by `search_help.py`
- `ui_scope_label`: human-readable scope label
- `ui_scope_note`: short note about how to use the scope
- `scope_summary`: grouped scope counts in a search response
- `mixed_scope_warning`: warning that a query spans multiple UI or product scopes

UI-scope hints are answer-organization metadata. They help separate GUI surfaces such as Step Properties, Analysis Rule Properties, Custom Extractor, Custom Processor, Custom Types, and custom session type pages. They are not official iTest taxonomy and must not replace page text as evidence for product behavior.

Each indexed help page should preserve official iTest Online Help table-of-contents context when the page appears in `com.fnfr.svt.help/toc.xml`:

- `toc_entries`: one or more official TOC entries for the page
- `toc_paths`: breadcrumb strings such as `iTest Online Help > Field Replacements > ...`
- `toc_top_categories`: official top-level TOC labels
- `toc_primary_path`: first TOC breadcrumb, used for display

TOC metadata is authoritative for help navigation context. It does not replace page text as evidence for product behavior. Popup and supplemental pages may have no TOC entry.

Each indexed help page should preserve official iTest Online Help index metadata when the page appears in `com.fnfr.svt.help/index.xml`:

- `index_entries`: one or more official help index entries for the page
- `index_terms`: deduplicated keyword terms from the help index
- `index_paths`: breadcrumb strings from nested index keywords

Each indexed help page should preserve Eclipse help context metadata when the page appears in `com.fnfr.svt.help/contexts.xml`:

- `context_entries`: one or more context mappings for the page
- `context_ids`: Eclipse help context IDs
- `context_labels`: labels attached to context topic references

Index and context metadata are auxiliary metadata. They help find candidate pages and identify official context links, but they must not be inserted into `text` and must not replace page text as evidence for product behavior. Context IDs are not official iTest chapter categories.

## Search Behavior（搜尋規則）

中文說明：這段規定搜尋工具要怎麼找資料。搜尋只能根據索引裡真的有的文字，不可以因為 AI 覺得像，就當成 help 文件已經證明。

Search must be deterministic and lexical. It is not semantic search and must not infer iTest behavior beyond retrieved help content.

Search results must expose logical sources through `source_ref`. User-facing answers should cite `source_ref` or the source file name when context is unambiguous.

Search results should expose official TOC context when available. User-facing answers may include `toc_primary_path` to identify where a page appears in iTest Online Help.

Search may use official help index and context metadata as low-weight ranking signals. These signals must not outweigh page text, title, H1, headings, or official TOC context. A match that exists only in `index_terms`, `index_paths`, `context_ids`, or `context_labels` is a page-location signal, not product-behavior evidence.

When multiple pages share the same `file_name`, lookup by file name alone must not silently choose one page. The tool must report ambiguity and require `relative_path` or `source_ref`, for example `topics/popups/query.html`.

Weak or mixed search results must be described as weak or mixed instead of being treated as authoritative.

For GUI, wizard, editor, property, setting, or "where do I click" questions, search results should expose UI-scope information. If `mixed_scope_warning` appears, the answer must separate the relevant UI locations or refine the search with `--scope`.

The scope filter is a search aid. A filtered search must still cite retrieved help page text for product behavior.

## Evidence Boundaries（證據邊界）

中文說明：這段規定回答時不能把官方範例、清單或表格過度解讀。官方 help 有寫到的內容可以引用；沒有直接寫到的反向結論或完整性結論，不能自動推論。

Retrieved help examples, lists, and tables are evidence only for what they explicitly state.

The skill must not infer inverse, opposite, or exhaustive behavior from examples, positive lists, negative lists, or tables unless the help page explicitly says the list is complete, exclusive, required, unsupported, always true, or never true.

If a help page gives only positive examples, the answer must not claim that unlisted cases are unsupported. If a help page gives only negative examples or unsupported cases, the answer must not claim that every unlisted case is supported.

When an answer combines multiple documented facts into a recommended workflow, it must separate official help statements from the derived recommendation. For example, it may say that the help documents a regex extractor and a store processor, but it must not claim that a combined multi-output workflow is officially guaranteed unless the help directly says so.

The skill must not let UI-scope metadata prove behavior. For example, `ui_scope=analysis_rule_processor_properties` can help choose pages, but the answer must still read the page `text` before describing processor or action behavior.

## Guardrail Behavior（高風險提醒規則）

中文說明：這段規定高風險問題要多一層提醒。若某些規則是專案實際觀察到的行為，不是官方 help 明文寫的，就必須清楚標示。

Guardrails document known high-risk interpretation rules that are not fully represented by lexical search ranking alone. They may include local observed behavior, but any such behavior must be clearly labeled as observed rather than official help text.

The `interpreter-guide.md` guardrail must cover iTest interpreter vs Tcl interpreter boundaries. It must also cover time conversion risks for direct iTest interpreter clock usage.

For direct iTest `[clock scan ...]` used in date/time string conversion, epoch-second conversion, timestamp comparison, time arithmetic, clock scanning/formatting, or large future-date handling, the skill must treat dates around or beyond 2038 as high risk. This applies generally and is not limited to certificate expiration or `notAfter` handling.

The 25.4 baseline includes an observed project guardrail: direct iTest interpreter `[clock scan ...]` can work for near-term dates but has produced incorrect negative seconds for larger future dates such as 2041 or 2049. The preferred workaround to consider is using the iTest `tcl` command to invoke the execution kernel Tcl interpreter, for example `[tcl "clock scan {$target_date}"]`.

This observed clock behavior is a guardrail for answer quality. It is not represented as an official Spirent help statement unless a future help version documents it.

## Portability Requirements（可攜性要求）

中文說明：這段規定 skill 打包後要能搬到別台電腦。包好的資料不能留下 `F:\MyCode`、使用者名稱或原始 help plugin 的絕對路徑。

The packaged skill must be self-contained. It must not require the original extracted help plugin directory.

Packaged references must not contain machine-specific absolute paths, such as Windows drive paths, user profile paths, or workspace-specific source directories.

References to original help content must use logical source paths:

```text
topics/<relative_path>
```

Eclipse help URIs or original plugin references should be normalized to logical `topics/...` paths when included in packaged data.

Version runbooks may define environment-specific validation patterns. Those patterns are examples for a known build environment, not universal SPEC requirements.

## Packaging Requirements（打包要求）

中文說明：這段規定 zip 裡面應該長什麼樣子。zip 檔名可以改，但 zip 裡最上層資料夾一定要叫 `itest-help/`。

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
  scripts/apply_toc_metadata.py
  references/help_pages.jsonl
  references/search_index.json
  references/search_index_summary.json
  references/toc_index.json
  references/help_index.json
  references/contexts_index.json
  references/interpreter-guide.md
  references/analysis-rule-wizard-guide.md
  references/regression-questions.md
```

## Verification Criteria（驗收條件）

中文說明：這段是驗收清單。做完或更新 skill 後，要用這些條件確認資料數量、搜尋結果、可攜性與高風險提醒都正常。

A generated package is acceptable only if:

- Inventory count equals `help_pages.jsonl` line count.
- `search_index_summary.json` document count equals `help_pages.jsonl` line count.
- `toc_index.json` is packaged and reports the official iTest Online Help root label.
- TOC-referenced pages include `toc_paths`; pages not present in TOC remain searchable by `source_ref`.
- `help_index.json` is packaged and reports official help index reference counts.
- `contexts_index.json` is packaged and reports context counts, contexts without topics, and missing or stale topic references.
- Pages referenced by `index.xml` include `index_terms` and `index_paths`.
- Pages referenced by `contexts.xml` include `context_ids` and `context_labels`.
- Packaged references contain no machine-specific absolute source paths.
- Sample searches return relevant pages for common topics such as parameters, QuickCalls, response maps, and query commands.
- Chapter searches, such as `Field Replacements`, return pages with matching official TOC paths.
- High-risk searches expose query terms that were not found in the indexed help. Missing terms are warning signals only; they must not be treated as evidence that the help supports those terms.
- High-risk guardrail references are packaged and readable.
- Example/list/table boundary checks confirm that the answer does not infer unsupported inverse, opposite, or exhaustive behavior from official examples.
- GUI-scope searches expose `scope_summary` and `ui_scope` values for relevant results.
- Mixed GUI or properties searches, such as `Custom Extractor Custom Process` and `Step Properties Analysis Rule Properties`, produce `mixed_scope_warning`.
- Scope-filtered searches using `--scope` return only results from the requested UI scope.
- Answer guardrails distinguish Step Properties from Analysis Rule Properties and distinguish Custom Extractor / Custom Processor from Custom Types or custom session type pages.
- Time conversion regression checks cover general post-2038 date/time conversion, not only certificate expiration examples.
- A duplicate file-name lookup reports ambiguity instead of choosing an arbitrary page.
- A lookup using `source_ref` or `relative_path` can show a specific popup page.
- Zip extraction preserves the required `itest-help/` top-level folder.

## Version Baselines（版本基準）

中文說明：這段記錄 iTest 25.4 的實際數量，方便下次比較。這不是永遠固定的數字，新版本要重新統計。

iTest 25.4 baseline:

```text
topics                  761
topics/popups           166
topics/popups/arules     36
total                   963
toc top-level labels     76
toc href entries        749
index topic refs       1901
index source refs       444
index keyword paths    1671
contexts                645
context topic refs      656
context source refs     620
context stale refs        1
contexts without topic    3
```

The `963`, `76`, `749`, `1901`, `444`, `1671`, `645`, `656`, `620`, `1`, and `3` counts are 25.4 baseline facts, not permanent requirements. New iTest versions must be counted from their own source tree, `toc.xml`, `index.xml`, and `contexts.xml`.

## Known Risks（已知風險）

中文說明：這段列出容易誤判的地方。看到這些狀況時，不要直接當成錯誤，要先用抽樣或搜尋結果確認。

Popup pages often have empty `title` and `h1`, so title completeness alone is not a valid failure signal.

Short popup pages can rank highly for single-term queries. Search-quality checks must confirm that popup hits improve recall without hiding primary help pages.

Subdirectories can contain files with the same base name. `relative_path` and `source_ref` are required for stable identity.

The current scope excludes HTML outside `topics/`. That does not prove excluded files are irrelevant; it only means they are outside the current accepted data boundary.

Generated categories are heuristic and should not be treated as official Spirent taxonomy.

Official TOC metadata covers pages linked from `toc.xml`. Popup pages and some supplemental pages can be valid searchable help content even when they have no TOC path.

Official index metadata can contain duplicate topic references and printed-page wording. Search-quality checks must confirm that index metadata improves recall without allowing index keywords to answer product-behavior questions by themselves.

Official context metadata can contain context IDs without topic references and stale topic references. These must be recorded in `contexts_index.json` and treated as metadata-quality findings, not as extracted help pages.

Official examples, lists, and tables can be partial. A page that lists supported examples does not automatically prove that unlisted items are unsupported. A page that lists unsupported cases does not automatically prove that every unlisted case is supported.

Some UI terms are reused across unrelated product areas. `Custom`, `Properties`, `Action`, `Command`, `Query`, and `Message` must be tied back to the owning UI surface before answering.

UI-scope labels are deterministic helper classifications from the packaged metadata. They are useful for answer structure, but they are not official Spirent categories.
