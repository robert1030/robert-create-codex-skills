---
{
  "chunk_id": "action_scriptget__the_scriptget_action_get_the_value_of_a__6c1d69ba5e383c5b",
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
    "The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter)"
  ],
  "anchor": "1600024",
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
  "images": [
    "topics/images/actions_11.1.jpg"
  ],
  "content_hash": "6c1d69ba5e383c5b",
  "level": 1
}
---

# The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter) > The ‘scriptGet’ action: Get the value of a variable (Tcl or a selected interpreter)

scriptGet gets the value of a variable from the specified interpreter and sets the specified iTest interpreter variable to the value. (By default, the command gets the value from the Global Tcl interpreter, but you have the option to specify the session with the target interpreter.)

scriptGet takes two arguments: the name of an iTest variable to be set; and something that is substituted by the Tcl interpreter. Command substitution happens on both arguments before the Tcl interpreter is asked to interpret the second argument.

In this example, t2 is the iTest variable to get the value, and var2 is the Tcl variable whose value will populate t2. The braces around $var2 prevent substitution, causing it to be passed to the Tcl interpreter as the string “$var2“. Notice that we set the Session containing Tcl interpreter property for the step to the session for which we are doing the get.

> **Note:** Note While scriptGet does support getting individual array elements, you cannot use it to move array values between the Tcl interpreter and the iTest interpreter. Instead, use scriptEval.

![screenshot](topics/images/actions_11.1.jpg) <!-- image_chunk: img_5101fa7ef51f641e -->
