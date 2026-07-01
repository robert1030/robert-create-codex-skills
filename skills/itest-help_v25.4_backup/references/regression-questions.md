# Regression Questions

Use these questions after changing the skill, search index, or guardrails. The expected behavior focuses on answer safety and source coverage, not exact wording.

## Interpreter And Clock

Question: Does iTest `clock scan` support dates after 2038?

Expected behavior:

- Search output should show `2038` as an unmatched term.
- Answer must say the packaged iTest 25.4 help does not document 2038 behavior.
- Answer may cite `topics/command_syntax.htm` and `topics/popups/clock.html` for documented `clock` syntax.
- Answer must not infer Tcl or OS timestamp limits as iTest behavior.

Question: `set target_seconds [clock scan {$target_date}]` returns negative seconds for a future date such as 2049. What should I do?

Expected behavior:

- Answer must distinguish direct iTest interpreter `[clock scan ...]` from using the iTest `tcl` command to call the execution kernel Tcl interpreter.
- Answer should mention the observed large-date risk for direct iTest `[clock scan ...]`.
- Answer should propose testing or using:

  ```tcl
  set target_seconds [tcl "clock scan {$target_date}"]
  ```

- Answer must label this as an observed project guardrail, not an official help statement.
- Cite `topics/command_syntax.htm`, `topics/popups/clock.html`, and `topics/command_tcl.htm`.

Question: For time conversion, timestamp comparison, or time arithmetic around 2041 or 2049, should I use `[clock scan]` or `[tcl "clock scan ..."]`?

Expected behavior:

- Answer should not recommend direct iTest `[clock scan]` alone.
- Answer should explain that `[tcl "clock scan ..."]` executes through the Tcl interpreter via the iTest `tcl` command.
- Answer should warn that the exact target date range should be tested in the user's iTest runtime.

Question: For certificate `notAfter` or expiration dates in 2041 or 2049, should I use `[clock scan]` or `[tcl "clock scan ..."]`?

Expected behavior:

- Answer should treat certificate expiry as one example of the broader time-conversion risk.
- Answer should apply the same large-date guardrail used for general date/time conversion.

Question: What is the difference between iTest `eval`, `scriptEval`, and `tcl`?

Expected behavior:

- Answer distinguishes iTest world and Tcl world.
- Cite `topics/command_syntax.htm`, `topics/action_run.htm`, `topics/action_scripteval.htm`, and `topics/command_tcl.htm`.
- State that `scriptSet` and `scriptGet` bridge variables between worlds.

Question: Are Tcl variables and iTest variables the same?

Expected behavior:

- Answer says they are separate.
- Cite `topics/command_syntax.htm` and, when relevant, `topics/test_cases_exchange_data_between_itest_tcl_variables.htm`.

## Analysis Rule Wizard

Question: In Analysis Rule Wizard, should I right-click Query to enter a query extractor value?

Expected behavior:

- Answer says no for analysis rule query values.
- Cite `topics/arules_extractor_properties.htm`.
- Explain that right-click Query creates a query command such as `[query . up]`, not the intended query value.

Question: Is `$itest_value` safe in asynchronous analysis rules?

Expected behavior:

- Answer says `$itest_value` is a Tcl interpreter variable and is not thread safe.
- Cite `topics/arules_extractor_properties.htm` or `topics/arules_processor_properties.htm`.
- Mention it can be overwritten by another thread in asynchronous steps.

Question: What does Wait for expected response generate?

Expected behavior:

- Cite `topics/awr_wait_for_expected_response.htm`.
- Mention it uses `RepeatStep` and generated When False actions including `DeclareExecutionIssue INFO:{auto_message_wait}` and `RepeatStep max:30 delay:2`.

Question: Does Analysis Rule Wizard hide secret values?

Expected behavior:

- Cite `topics/arw_rule_type_selection_page.htm`.
- State that the Add Rules wizard warning says secret values are not masked on the relevant wizard page.

Question: When answering Analysis Rule Wizard runtime behavior, which pages must be checked?

Expected behavior:

- Answer should include the relevant wizard page plus `topics/arules_extractor_properties.htm` and/or `topics/arules_processor_properties.htm`.

Question: What is the difference between Custom Extractor, Custom Processor, and Custom Types?

Expected behavior:

- Answer must separate the UI scopes instead of treating all "Custom" items as the same setting.
- Custom Extractor should cite `topics/arw_extractor_selection_page.htm` and/or `topics/arules_extractor_properties.htm`.
- Custom Processor should cite `topics/arw_processor_selection_page.htm` and/or `topics/arules_processor_properties.htm`.
- Custom Types should cite `topics/parameters_custom_types.htm`, `topics/tce_custom_type_page.htm`, or `topics/spe_custom_types_page.htm` only when discussing parameter type/value definitions.
- Answer must not imply Custom Types are an Analysis Rule Wizard setting.

Question: Are Step Properties and Analysis Rule Properties the same place in the UI?

Expected behavior:

- Answer must say they are different UI scopes.
- Step Properties should be described as step-level settings in the Test Case Editor or Properties view, citing a `topics/tce_step_properties_*.htm` page or `topics/view_properties.htm`.
- Analysis Rule Properties should be described as rule-level extractor/processor/action settings, citing `topics/arules_extractor_properties.htm`, `topics/arules_processor_properties.htm`, or `topics/arules_global_working_with.htm`.
- Answer must not merge Step Properties options with Analysis Rule Properties options.

Question: Search results for `Custom` or `Properties` span multiple UI scopes. How should the answer be structured?

Expected behavior:

- Answer should use `scope_summary` / `ui_scope` from `search_help.py` to identify the mixed scopes.
- Answer should either separate the response by UI location or refine the search with `--scope`.
- Answer must still verify product behavior in page `text`; `ui_scope` is only an organization hint.
