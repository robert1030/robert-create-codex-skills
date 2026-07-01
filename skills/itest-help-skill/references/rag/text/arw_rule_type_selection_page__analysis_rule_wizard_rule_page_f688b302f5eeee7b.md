---
{
  "chunk_id": "arw_rule_type_selection_page__analysis_rule_wizard_rule_page_f688b302f5eeee7b",
  "source_file": "topics/arw_rule_type_selection_page.htm",
  "source_original_path": "topics/arw_rule_type_selection_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis Rule Wizard: Rule page"
  ],
  "heading_path": [
    "Analysis Rule Wizard: Rule page",
    "Analysis Rule Wizard: Rule page"
  ],
  "anchor": "1207393",
  "context_ids": [
    "arw_rule_type_selection_page"
  ],
  "index_keywords": [
    "Analysis Rule wizard",
    "Rule page"
  ],
  "index_keyword_paths": [
    "Analysis Rule wizard > Rule page",
    "Rule page > Analysis Rule wizard"
  ],
  "related_links": [
    "param_parameters_type_secret.htm#1554375"
  ],
  "images": [],
  "content_hash": "f688b302f5eeee7b",
  "level": 1
}
---

# Analysis Rule Wizard: Rule page > Analysis Rule Wizard: Rule page

> **Note:** Note When a test case command step uses secret values and you try to add analysis rules, the Add Rules wizard does not mask the secret value and displays the Analysis Rule Wizard: Rule page (See About the Parameter Type ‘Secret’).

Specify the type of analysis rule to apply to the response.

| Validate something in the response | Use this option to determine whether particular text or values appear (or do not appear) in the response text. You will next specify one of the following: The response contains a specified string The response does not contain a specified string Compare the extracted value to a specified value |  | The response contains a specified string |  | The response does not contain a specified string |  | Compare the extracted value to a specified value |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | The response contains a specified string |  |  |  |  |  |  |
|  | The response does not contain a specified string |  |  |  |  |  |  |
|  | Compare the extracted value to a specified value |  |  |  |  |  |  |
| Create a message to display during execution | Use this option to specify an execution issue and associated execution message that should appear in the Execution view, Step Issues view, and Test Report editor as a result of this analysis rule. |  |  |  |  |  |  |
| Store data in a variable or a JSON response value | Use this option to store the returned value in a variable or a JSON response value that you will specify. |  |  |  |  |  |  |
| Wait for an expected response | Use to set up "wait for" logic, which invokes the RepeatStep rule action and displays an INFO level message to indicate that the test case is waiting for a response, so that you don't have to manually insert these action rules. |  |  |  |  |  |  |
| Custom | Configure an analysis rule one step at a time with the wizard's assistance. |  |  |  |  |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
