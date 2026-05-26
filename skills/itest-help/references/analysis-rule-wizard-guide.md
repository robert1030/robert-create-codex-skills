# Analysis Rule Wizard Guide

Use this guide as a guardrail when answering questions about Analysis Rule Wizard, Quick Analysis Rule, analysis rule extractors/processors, and response-map query behavior.

## Required Source Pages

For general Analysis Rule Wizard questions, inspect:

- `topics/add_analysis_rule_wizard.htm`: overview, start locations, wizard pages, and generated rule relationship.
- `topics/arw_rule_type_selection_page.htm`: rule type choices and secret value warning.
- `topics/arw_select_step_page.htm`: step selection behavior.
- `topics/arw_validation_type_selection_page.htm`: validation choices.
- `topics/arw_select_from_response_page.htm`: extractor choices shown in the wizard.
- `topics/arw_comparison_page.htm`: comparison settings.
- `topics/arw_store_variable_page.htm`: storing data in variables or response values.
- `topics/arw_processor_selection_page.htm`: processor choices and mapping to Perform values.
- `topics/arw_assertion_page.htm`: When True / When False actions and predefined variables.
- `topics/arw_message_page.htm`: execution message behavior.
- `topics/arw_finish_page.htm`: summary page and generated settings.

For implementation details and limitations, also inspect:

- `topics/arules_extractor_properties.htm`: extractor properties, query extractor behavior, predefined variables, and query entry warning.
- `topics/arules_processor_properties.htm`: processor properties, multiple-match behavior, not-thread-safe Tcl variables, deferred flow-control actions, RepeatStep, Store, writeFile, and messages.
- `topics/arules_working_with.htm`: adding rules, wizard entry points, and limitations.
- `topics/awr_wait_for_expected_response.htm`: Wait for expected response behavior and generated RepeatStep defaults.

## Boundary Rules

- The wizard creates ordinary analysis rules. Generated rules operate like rules created by hand or by Quick Analysis Rule.
- The wizard UI page labels do not fully define runtime behavior. Runtime details often live in extractor and processor property pages.
- For query extractor answers, do not rely only on the Extract page. Check `topics/arules_extractor_properties.htm`.
- For action/result behavior, do not rely only on the Actions page. Check `topics/arules_processor_properties.htm`.
- Keep Analysis Rule Wizard pages separate from Analysis Rule Properties pages. Wizard pages describe what the user selects while creating a rule. Properties pages describe the resulting extractor, processor, action, and runtime behavior.
- Keep Analysis Rule Properties separate from Step Properties. Step Properties are step-level settings in the Test Case Editor or Properties view; Analysis Rule Properties are rule-level settings inside local or global analysis rules.
- Keep `Custom Extractor` / `Custom Processor` separate from `Custom Types`, `custom session type`, custom parsers, and report customization. These are different UI surfaces even though they share the word "Custom".

## Known Limitations And Traps

- In analysis rules, do not use right-click `Query` to enter a query value. The help says this creates a query command such as `[query . up]`, not the intended query value such as `up`.
- `$value` and `$index` are iTest interpreter variables populated during analysis rule processing.
- `$itest_value` and `$itest_index` are Tcl interpreter variables and are not thread safe. They can be overwritten by another thread when analysis rules run in asynchronous steps.
- Some extractors return multiple values. Check the multiple-match behavior before claiming a single result.
- Wait for expected response generates repeat logic using `RepeatStep`; the documented generated When False actions include `DeclareExecutionIssue INFO:{auto_message_wait}` and `RepeatStep max:30 delay:2`.
- The Add Rules wizard can display secret values unmasked in relevant wizard pages.
- Flow-control actions in analysis rules can be deferred until other actions for the step are complete.

## High-Risk Answering Rules

- When a user asks "what should I click" or "what does the wizard create", answer from wizard pages and mention the generated property/rule mapping.
- When a user asks "what happens during execution", answer from extractor/processor property pages, not only wizard pages.
- When a user reports UI behavior that differs from a generic wizard explanation, search for limitations using terms such as `right-click`, `not thread safe`, `multiple matches`, `secret`, `RepeatStep`, `When True`, and `When False`.
- If retrieved pages disagree or cover different layers, state the layer explicitly: wizard UI, generated analysis rule, Step Properties, Analysis Rule Properties, extractor property, processor property, action property, or execution behavior.
