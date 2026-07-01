---
{
  "chunk_id": "action_scripteval__moving_array_variables_from_the_tcl_shel_d8bf2ca8d21b4b15",
  "source_file": "topics/action_scripteval.htm",
  "source_original_path": "topics/action_scripteval.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘scriptEval’ action: Evaluate a Tcl command"
  ],
  "heading_path": [
    "The ‘scriptEval’ action: Evaluate a Tcl command",
    "The ‘scriptEval’ action: Evaluate a Tcl command",
    "Moving array variables from the Tcl shell into iTest"
  ],
  "anchor": "1600013",
  "context_ids": [
    "action_scripteval"
  ],
  "index_keywords": [
    "evaluating",
    "evaluating Tcl commands",
    "scriptEval",
    "scriptEval action"
  ],
  "index_keyword_paths": [
    "Tcl commands > evaluating",
    "actions > scriptEval",
    "evaluating Tcl commands",
    "scriptEval action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "d8bf2ca8d21b4b15",
  "level": 2
}
---

# The ‘scriptEval’ action: Evaluate a Tcl command > The ‘scriptEval’ action: Evaluate a Tcl command > Moving array variables from the Tcl shell into iTest

To move an array variable tcl_variable in the Tcl shell into the iTest variable itest_variable to determine the value of tcl_variable, use the following steps to return an array list:

scriptEval array set tcl_variable {apple orange mango banana}

scriptGet itest_variable {[array get tcl_variable]}

puts $itest_variable

To access the array elements using eval in iTest, use:

scriptGet itest_variable {[array get tcl_variable]}

eval array set me $itest_variable

puts $me(apple)

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
