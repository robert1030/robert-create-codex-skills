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

2. Read the strongest matching page when detail matters:

   ```powershell
   python scripts/search_help.py --show-file "<relative_path_or_source_ref>" --text
   ```

3. Answer from the retrieved help content. Cite source file names such as `quickcalls_arguments_in_quickcall_steps.htm`.

4. If search results are weak or mixed, say that the help index did not find a confident match and list the closest files instead of guessing.

## Search Data

- `references/help_pages.jsonl`: one cleaned text record per help page.
- `references/search_index.json`: weighted term index for deterministic lookup.
- `references/search_index_summary.json`: index metadata and counts.

The packaged index contains 963 `.htm` / `.html` help pages under `topics/`, including `topics/popups/` and `topics/popups/arules/`.
Source references are original help paths under the logical `topics/` path, such as `topics/quickcalls_arguments_in_quickcall_steps.htm` and `topics/popups/arules/query.html`.

## Query Guidance

- Prefer user terms first, then add iTest-specific synonyms.
- For workflow questions, search the task phrase, then inspect one or two top pages.
- For command/action questions, include the command or action name.
- For product-specific questions, include the product name, such as `Spirent TestCenter`, `Avalanche`, `CyberFlood`, or `NTAF`.

## Answering Rules

- Keep answers grounded in the help page text and mention uncertainty when pages disagree.
- Include the relevant source file name in the answer.
- Do not claim behavior that was not found in the indexed help.
- Use Traditional Chinese when replying to this user unless they ask otherwise.
