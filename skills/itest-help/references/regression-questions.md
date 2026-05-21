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
