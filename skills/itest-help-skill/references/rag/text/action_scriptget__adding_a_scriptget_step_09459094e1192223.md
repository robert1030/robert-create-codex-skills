---
{
  "chunk_id": "action_scriptget__adding_a_scriptget_step_09459094e1192223",
  "source_file": "topics/action_scriptget.htm",
  "source_original_path": "topics/action_scriptget.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter)"
  ],
  "heading_path": [
    "The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter)",
    "The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter)",
    "Adding a scriptGet step"
  ],
  "anchor": "1520211",
  "context_ids": [
    "action_scriptget"
  ],
  "index_keywords": [
    "getting",
    "scriptGet",
    "scriptGet action"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > scriptGet",
    "Tcl variable > getting",
    "actions > scriptGet",
    "scriptGet action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "09459094e1192223",
  "level": 3
}
---

# The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter) > The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter) > Adding a scriptGet step

1. Create the step and select an Action of scriptGet. (Do not specify a Session ID.)

1. 2

1. scriptGet takes two arguments in the Description cell. The contents are interpreted as a list, and each element in the list is substituted (unless surrounded by curly braces).

1. 3

1. Optional: Follow this procedure to obtain the value from a selected interpreter other than the Global Tcl interpreter (<itest_var> <expression>):

| itest_variable | Name of the iTest variable to be set (actually any heap query suitable for “set”). If the iTest variable existed before the scriptGet step, then its previous value is lost. This works for all variable types including lists and arrays. |
| --- | --- |
| expression | Expression that will be evaluated by the specified Tcl interpreter. The iTest variable's value will be set to the result. To cause the expression to be treated as a string to be passed to the Tcl interpreter, surround it with { } braces. |

In the Step Properties section, open the EXEC scriptGet properties > scriptGet properties group and specify settings as described here:

| Session containing interpreter (or specify global Tcl interpreter) | Select the Session ID whose interpreter should be used for the scriptGet step. (If you select Global Tcl interpreter, then scriptSet obtains the value from the Global Tcl interpreter.) Default: Global Tcl interpreter |
| --- | --- |
| Store in Global variable | Check the box to store the variable in a global rather than local location. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
