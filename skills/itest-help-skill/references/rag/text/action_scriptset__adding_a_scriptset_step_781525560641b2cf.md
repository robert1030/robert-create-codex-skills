---
{
  "chunk_id": "action_scriptset__adding_a_scriptset_step_781525560641b2cf",
  "source_file": "topics/action_scriptset.htm",
  "source_original_path": "topics/action_scriptset.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter)"
  ],
  "heading_path": [
    "The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter)",
    "The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter)",
    "Adding a scriptSet step"
  ],
  "anchor": "1520257",
  "context_ids": [
    "action_scriptset"
  ],
  "index_keywords": [
    "scriptSet",
    "scriptSet action"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > scriptSet",
    "actions > scriptSet",
    "scriptSet action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "781525560641b2cf",
  "level": 3
}
---

# The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter) > The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter) > Adding a scriptSet step

1. Create the step and select an Action of scriptSet. (Do not specify a Session ID.)

The command for scriptSet steps is directed at the iTest interpreter. To ensure that iTest commands (like [tcl] or [tclexpr]) will be correctly interpreted, the property that controls field replacements (command substitution) for the step is disabled and dimmed (The For the Command field, perform command, variable, and backslash substitution checkbox is unchecked).

1. 2

1. scriptSet takes two arguments in the Description cell (<itest_var> <value>):

| itest_variable | Name of a Tcl variable in the specified interpreter whose value is to be set. |
| --- | --- |
| value | Value to set. |

1. By default, scriptSet sets the variable value in the Global Tcl interpreter. Follow this procedure to set the value in the interpreter that you specify.

1. 2

1. In the Step Properties section, open the EXEC scriptSet properties > scriptSet properties group.

1. 3

1. Select the interpreter in the Session containing interpreter list. (If you select the default setting of Global Tcl interpreter, then scriptSet sets the value in the Global Tcl interpreter.)

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
