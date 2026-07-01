---
{
  "chunk_id": "test_cases_exchange_data_between_itest_t__exchanging_data_between_itest_variables__0254f5760455860d",
  "source_file": "topics/test_cases_exchange_data_between_itest_tcl_variables.htm",
  "source_original_path": "topics/test_cases_exchange_data_between_itest_tcl_variables.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Test suites: Organizing tests for group execution",
    "Exchanging data between iTest variables and Tcl variables"
  ],
  "heading_path": [
    "Exchanging data between iTest variables and Tcl variables",
    "Exchanging data between iTest variables and Tcl variables"
  ],
  "anchor": "1730643",
  "context_ids": [
    "test_cases_exchange_data_between_itest_tcl_variables"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "action_scriptget.htm#1600024",
    "action_scriptset.htm#1520241"
  ],
  "images": [],
  "content_hash": "0254f5760455860d",
  "level": 1
}
---

# Exchanging data between iTest variables and Tcl variables > Exchanging data between iTest variables and Tcl variables

Use the scriptGet and scriptSet commands to exchange data.

iTest supports both Tcl sessions and a default/global Tcl interpreter, so you must specify the Tcl environment/interpreter using the Session containing interpreter (or specify global Tcl interpreter) property. (The property appears in the Step Properties section, EXEC scriptGet Properties and EXEC scriptGet Properties.)

- To save an EXEC (eval) value named evalVar to a Tcl variable named tclVar, use a scriptSet step with the following text in the Description cell: tclVar $evalVar

- To save a Tcl value to an EXEC (eval) variable, use a scriptSet step with the following text in the Description cell: evalVar {$tclVar}

For more detail, see The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter) and The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
