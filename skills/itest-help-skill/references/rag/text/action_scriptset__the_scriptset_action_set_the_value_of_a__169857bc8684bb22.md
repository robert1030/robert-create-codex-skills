---
{
  "chunk_id": "action_scriptset__the_scriptset_action_set_the_value_of_a__169857bc8684bb22",
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
    "The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter)"
  ],
  "anchor": "1520241",
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
  "images": [
    "topics/images/actions_12.1.jpg"
  ],
  "content_hash": "169857bc8684bb22",
  "level": 1
}
---

# The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter) > The ‘scriptSet’ action: Set the value of a variable (Tcl or a selected interpreter)

The scriptSet action sets the value of a specified variable in the specified interpreter (typically, the Global Tcl interpreter, but you have the option to specify the interpreter). scriptSet works for any kind of variable, including lists, arrays, lists of lists, numbers, and so on. You can specify multiple values.

For example, an analysis rule has extracted a list of values. We have set the value of a iTest interpreter variable called var1 with the list. To pass the list of values into a Tcl interpreter variable called t1 in the Global Tcl interpreter's context, you can use the following scriptSet step. Notice that we disabled substitution for the step by unchecking the For the Command field, perform command, variable, and backslash substitutions property.

> **Note:** Note While scriptSet does support getting individual array elements, you cannot use it to move array values between the Tcl interpreter and the iTest interpreter. Instead, use scriptEval.

![screenshot](topics/images/actions_12.1.jpg) <!-- image_chunk: img_89a655609f9820bd -->
