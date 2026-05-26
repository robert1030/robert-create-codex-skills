---
name: itest-help
description: Use when answering questions about Spirent iTest Automation 25.4 help, including test cases, sessions, commands, actions, QuickCalls, parameters, response maps, topology, reports, preferences, Spirent TestCenter, Spirent Avalanche, CyberFlood, NTAF, iTestRT, and related iTest documentation. Searches a packaged iTest help index and cites source help files.
---

# iTest Help

Use this skill to answer questions about Spirent iTest Automation 25.4 from the packaged help documentation. The skill is self-contained and searches its packaged `references/` data; it does not require the original extracted HTML directory.

## Workflow

1. Search the help index before answering:

   ```powershell
   python scripts/search_help.py "<query>" --top 8 --json
   ```

   The JSON output includes `query_terms`, `unmatched_terms`, `scope_summary`, `mixed_scope_warning`, and `results`. Treat `unmatched_terms` as a warning that the indexed help did not directly cover part of the question.

2. Read the strongest matching page when detail matters:

   ```powershell
   python scripts/search_help.py --show-file "<relative_path_or_source_ref>" --text
   ```

3. Answer from the retrieved help content. Cite source file names such as `quickcalls_arguments_in_quickcall_steps.htm`.

4. If search results are weak or mixed, say that the help index did not find a confident match and list the closest files instead of guessing.

5. If `mixed_scope_warning` appears, do not merge the results into one explanation. Separate the answer by UI location/scope, or rerun the search with `--scope <ui_scope>` after choosing the intended scope.

## Search Data

- `references/help_pages.jsonl`: one cleaned text record per help page.
- `references/search_index.json`: weighted term index for deterministic lookup.
- `references/search_index_summary.json`: index metadata and counts.
- `references/toc_index.json`: official iTest Online Help table-of-contents metadata from `com.fnfr.svt.help/toc.xml`.
- `references/help_index.json`: official iTest Online Help index metadata from `com.fnfr.svt.help/index.xml`.
- `references/contexts_index.json`: official Eclipse help context metadata from `com.fnfr.svt.help/contexts.xml`, including missing or stale topic references.
- `references/interpreter-guide.md`: guardrails for iTest interpreter, Tcl interpreter, and clock questions.
- `references/analysis-rule-wizard-guide.md`: guardrails for Analysis Rule Wizard and analysis rule behavior.
- `references/regression-questions.md`: high-risk questions used to verify answer quality.

The packaged index contains 963 `.htm` / `.html` help pages under `topics/`, including `topics/popups/` and `topics/popups/arules/`.
Source references are original help paths under the logical `topics/` path, such as `topics/quickcalls_arguments_in_quickcall_steps.htm` and `topics/popups/arules/query.html`.
Pages that appear in the official iTest Online Help contents include `toc_paths` and `toc_top_categories`; popup and supplemental pages may have no TOC entry.
Pages referenced by the official help index may include `index_terms` and `index_paths`. Pages referenced by Eclipse help contexts may include `context_ids` and `context_labels`.
These fields are auxiliary metadata for finding and locating pages. They are not page body text and do not prove product behavior by themselves.
Search results also include inferred `ui_scope`, `ui_scope_label`, and `ui_scope_note` values. These are deterministic labels from packaged page metadata to help separate GUI surfaces. They are navigation and answer-organization hints, not product behavior evidence.

## Query Guidance

- Prefer user terms first, then add iTest-specific synonyms.
- For workflow questions, search the task phrase, then inspect one or two top pages.
- For command/action questions, include the command or action name.
- For product-specific questions, include the product name, such as `Spirent TestCenter`, `Avalanche`, `CyberFlood`, or `NTAF`.
- For chapter, category, or navigation questions, use `toc_paths` from search results or inspect `references/toc_index.json`.
- For index-style terms, use `index_terms` / `index_paths` from search results or inspect `references/help_index.json` to find candidate pages.
- For UI help, dialog, wizard, or F1-style context questions, use `context_ids` / `context_labels` from search results or inspect `references/contexts_index.json` to find candidate pages.
- For GUI or properties questions, inspect `scope_summary` first. If the query spans multiple scopes, use `--scope` or read representative pages from each scope before answering.

## GUI Scope Rules

iTest Automation is a GUI-centered test authoring and execution environment. For UI, wizard, editor, property, setting, or "where do I click" answers, name the UI surface before listing options or behavior.

- Always distinguish at least these scopes when they appear in search results:
  - Analysis Rule Wizard pages, such as `Custom Extractor` or `Processor` wizard pages.
  - Analysis rule extractor/processor/action properties, such as `Extract using`, `Perform`, `When True`, `When False`, `Processor Properties`, `Action Properties`, or `Analysis Rule Properties`.
  - Step Properties sections in the Test Case Editor or Properties view.
  - Parameter Custom Types pages.
  - Session Builder custom session type pages.
  - Response Map editor/query/parser pages.
- Do not mix `Custom Extractor` / `Custom Processor` with `Custom Types`, `custom session type`, custom parsers, report customization, or perspective customization. If the user only says "Custom", explain that the help contains multiple unrelated Custom surfaces and ask or separate them by source.
- Do not mix `Step Properties` with `Analysis Rule Properties`. Step Properties are step-level settings for the selected test case step. Analysis Rule Properties are rule-level extractor/processor/action settings inside an analysis rule or global analysis rule.
- When an answer mentions a configurable option, state where it appears, for example: `Test Case Editor > Step Properties section > General properties group`, or `Analysis rule > Extractor Properties > Query`.
- When the same word is used in multiple places, such as `Action`, `Command`, `Query`, `Custom`, `Properties`, or `Message`, identify the owner object: step, action step, analysis rule extractor, analysis rule processor, response map, parameter type, session profile, or session builder.
- If only one layer is documented, say that the retrieved help documents that layer only. Do not imply the same setting exists in another UI layer.
- Use `ui_scope` only to organize the answer and choose pages. Confirm behavior in the retrieved page `text`.

## Answering Rules

- Keep answers grounded in the help page text and mention uncertainty when pages disagree.
- Include the relevant source file name in the answer.
- When useful, include the official iTest Online Help TOC path from `toc_paths` to identify the chapter context.
- For GUI answers, include the relevant UI scope or location before the behavior details.
- Prefer official TOC metadata over `probable_category`; `probable_category` is a heuristic fallback.
- Use `help_index.json` and `contexts_index.json` only to find candidate pages, identify UI/context links, or explain navigation metadata.
- Do not use `index_terms`, `index_paths`, `context_ids`, or `context_labels` alone as evidence for product behavior. Verify behavior in the retrieved help page `text`.
- Do not treat context IDs as official chapter categories.
- Treat official examples, lists, and tables as evidence only for what they explicitly state.
- Do not infer inverse, opposite, or exhaustive behavior from examples, positive lists, negative lists, or tables unless the help page explicitly says the list is complete, exclusive, required, unsupported, always true, or never true.
- If the help gives only positive examples, say the help documents those examples but does not prove that unlisted cases are unsupported.
- If the help gives only negative examples or unsupported cases, say the help documents those limits but does not prove that every unlisted case is supported.
- Do not claim behavior that was not found in the indexed help.
- Use Traditional Chinese when replying to this user unless they ask otherwise.

## High-Risk Topics

Before answering these topics, read the relevant guardrail file and inspect the required source pages listed there:

- For iTest interpreter, Tcl interpreter, `eval`, `scriptEval`, `scriptSet`, `scriptGet`, `tcl`, `tclexpr`, `clock`, time conversion, epoch seconds, timestamp comparison, time arithmetic, clock scan/format, large future dates, 2038-style questions, 2041, 2049, certificate expiry, `notAfter`, or expiration dates, read `references/interpreter-guide.md`.
- For Analysis Rule Wizard, Quick Analysis Rule, Custom Extractor, Custom Processor, Custom Process, Analysis Rule Properties, Processor Properties, Extractor Properties, Action Properties, query extractor, extractor/processor behavior, `When True`, `When False`, `RepeatStep`, thread/asynchronous behavior, `$value`, `$itest_value`, `$index`, `$itest_index`, or secret values, read `references/analysis-rule-wizard-guide.md`.

If a high-risk query has unmatched terms, explicitly say which requested detail was not found in the packaged help. For example, if `2038` is unmatched, do not infer post-2038 clock behavior from Tcl or operating-system knowledge.

For direct iTest `[clock scan ...]` used in time conversion, epoch-second conversion, timestamp comparison, time arithmetic, clock formatting/scanning, or large future-date handling, apply the observed large-date guardrail in `references/interpreter-guide.md`: distinguish direct iTest interpreter clock handling from `[tcl "clock scan ..."]`, and label the workaround as observed behavior rather than official help text. Certificate expiration and `notAfter` handling are examples of this broader risk, not the only case.
