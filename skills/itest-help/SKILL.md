---
name: itest-help
description: Use when answering questions about Spirent iTest Automation 25.4 help, including GUI workflows, test cases, sessions, commands, actions, QuickCalls, parameters, response maps, topology, reports, preferences, Spirent TestCenter, Spirent Avalanche, CyberFlood, NTAF, iTestRT, and related iTest documentation. Searches a packaged help index, separates GUI scopes, and cites source help files.
---

# iTest Help

Use this skill to answer questions about Spirent iTest Automation 25.4 from the packaged help documentation. The skill is self-contained and searches its packaged `references/` data; it does not require the original extracted HTML directory.

## Workflow

1. Search the help index before answering:

   ```powershell
   python scripts/search_help.py "<query>" --top 8 --json
   ```

2. Inspect the search output before deciding how to answer:
   - Treat `unmatched_terms` as a warning that the indexed help did not directly cover part of the question.
   - Use `scope_summary`, `surface_summary`, `ui_scope`, `ui_surface`, and `ui_location` to separate GUI surfaces.
   - Use `match_sources`, `match_source_summary`, `has_page_text_match`, `metadata_only_match`, `metadata_exact_match`, and `evidence_note` to distinguish page-text evidence from navigation metadata.
   - Treat `property_poc` as a small structured hint for documented property sections/rows only. It does not replace reading page text.

3. Read the strongest matching page when detail matters:

   ```powershell
   python scripts/search_help.py --show-file "<relative_path_or_source_ref>" --text
   ```

4. Answer from retrieved help page text. Cite source file names such as `topics/quickcalls_arguments_in_quickcall_steps.htm`.

5. If search results are weak, mixed, or metadata-heavy, say so and either list the closest files or rerun with `--scope <ui_scope>`.

## Packaged References

- `references/help_pages.jsonl`: cleaned page text for 963 `.htm` / `.html` help pages under logical `topics/` paths.
- `references/search_index.json`: weighted deterministic term index.
- `references/search_rules.json`: data-driven boosts for high-risk phrases and scope-sensitive candidate pages.
- `references/property_index.jsonl`: small POC index for documented property sections/rows.
- `references/toc_index.json`: official iTest Online Help table-of-contents metadata.
- `references/help_index.json`: official help index metadata.
- `references/contexts_index.json`: official Eclipse help context metadata.
- `references/interpreter-guide.md`: guardrails for iTest interpreter, Tcl interpreter, and clock questions.
- `references/analysis-rule-wizard-guide.md`: guardrails for Analysis Rule Wizard and analysis rule behavior.
- `references/regression-questions.md`: high-risk questions used to verify answer quality.

TOC, index, and context fields are useful for locating candidate pages and explaining navigation. They are not page body text and do not prove product behavior by themselves.

## Query Guidance

- Prefer the user's terms first, then add iTest-specific synonyms.
- For workflow questions, search the task phrase, then inspect one or two top pages.
- For command/action questions, include the command or action name.
- For product-specific questions, include the product name, such as `Spirent TestCenter`, `Avalanche`, `CyberFlood`, or `NTAF`.
- For chapter, index, or F1/context questions, use TOC/index/context metadata only to locate candidate pages; verify behavior in page text.
- For GUI or properties questions, inspect scope and surface summaries first. If results span multiple surfaces, separate the answer by location or refine with `--scope`.

## Evidence Rules

- Keep answers grounded in retrieved help page text and mention uncertainty when pages disagree.
- Include the relevant source file name in the answer.
- Prefer official TOC metadata over `probable_category`; `probable_category` is a heuristic fallback.
- Do not use `index_terms`, `index_paths`, `context_ids`, or `context_labels` alone as evidence for product behavior.
- Do not treat context IDs as official chapter categories.
- Use `ui_scope`, `ui_surface`, `ui_location`, `scope_summary`, and `surface_summary` only to organize answers and choose pages. Confirm behavior in retrieved page `text`.
- Use `property_poc` only as a POC hint for documented property sections/rows from help page text. Do not treat it as a complete property index.
- Treat official examples, lists, and tables as evidence only for what they explicitly state. Do not infer inverse, opposite, or exhaustive behavior unless the help explicitly says complete, exclusive, required, unsupported, always, or never.
- If a page gives only positive examples, say the help documents those examples but does not prove unlisted cases are unsupported. If it gives only negative examples or unsupported cases, say it documents those limits but does not prove every unlisted case is supported.
- Do not claim behavior that was not found in the indexed help.
- Use Traditional Chinese when replying to this user unless they ask otherwise.

## GUI Scope Rules

iTest Automation is a GUI-centered test authoring and execution environment. For UI, wizard, editor, property, setting, or "where do I click" answers, name the UI surface before listing options or behavior.

- Do not merge different uses of the same label. In particular, keep these surfaces separate when they appear:
  - Analysis Rule Wizard pages, such as `Custom Extractor` or `Processor` wizard pages.
  - Analysis rule extractor/processor/action properties, such as `Extract using`, `Perform`, `When True`, `When False`, `Processor Properties`, `Action Properties`, or `Analysis Rule Properties`.
  - Step Properties sections in the Test Case Editor or Properties view.
  - Parameter Custom Types pages.
  - Session Builder custom session type pages.
  - Response Map editor/query/parser pages.
- Do not mix `Custom Extractor` / `Custom Processor` with `Custom Types`, `custom session type`, custom parsers, report customization, or perspective customization.
- Do not mix `Step Properties` with `Analysis Rule Properties`. Step Properties are step-level settings for the selected test case step. Analysis Rule Properties are rule-level extractor/processor/action settings inside an analysis rule or global analysis rule.
- When an answer mentions a configurable option, state where it appears, for example: `Test Case Editor > Step Properties section > General properties group`, or `Analysis rule > Extractor Properties > Query`.
- When the same word is used in multiple places, such as `Action`, `Command`, `Query`, `Custom`, `Properties`, or `Message`, identify the owner object: step, action step, analysis rule extractor, analysis rule processor, response map, parameter type, session profile, or session builder.
- If only one layer is documented, say that the retrieved help documents that layer only. Do not imply the same setting exists in another UI layer.

## High-Risk Topics

Before answering these topics, read the relevant guardrail file and inspect the required source pages listed there:

- For iTest interpreter, Tcl interpreter, `eval`, `scriptEval`, `scriptSet`, `scriptGet`, `tcl`, `tclexpr`, `clock`, time conversion, epoch seconds, timestamp comparison, time arithmetic, clock scan/format, large future dates, 2038-style questions, 2041, 2049, certificate expiry, `notAfter`, or expiration dates, read `references/interpreter-guide.md`.
- For Analysis Rule Wizard, Quick Analysis Rule, Custom Extractor, Custom Processor, Custom Process, Analysis Rule Properties, Processor Properties, Extractor Properties, Action Properties, query extractor, extractor/processor behavior, `When True`, `When False`, `RepeatStep`, thread/asynchronous behavior, `$value`, `$itest_value`, `$index`, `$itest_index`, or secret values, read `references/analysis-rule-wizard-guide.md`.

If a high-risk query has unmatched terms, explicitly say which requested detail was not found in the packaged help. For example, if `2038` is unmatched, do not infer post-2038 clock behavior from Tcl or operating-system knowledge.

For direct iTest `[clock scan ...]` used in time conversion, epoch-second conversion, timestamp comparison, time arithmetic, clock formatting/scanning, or large future-date handling, apply the observed large-date guardrail in `references/interpreter-guide.md`: distinguish direct iTest interpreter clock handling from `[tcl "clock scan ..."]`, and label the workaround as observed behavior rather than official help text. Certificate expiration and `notAfter` handling are examples of this broader risk, not the only case.
