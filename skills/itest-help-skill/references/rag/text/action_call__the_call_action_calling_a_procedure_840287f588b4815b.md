---
{
  "chunk_id": "action_call__the_call_action_calling_a_procedure_840287f588b4815b",
  "source_file": "topics/action_call.htm",
  "source_original_path": "topics/action_call.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "The ‘call’ action: Calling a procedure"
  ],
  "heading_path": [
    "The ‘call’ action: Calling a procedure",
    "The ‘call’ action: Calling a procedure"
  ],
  "anchor": "1384965",
  "context_ids": [
    "action_call"
  ],
  "index_keywords": [
    "call",
    "call action",
    "calling",
    "calling procedures"
  ],
  "index_keyword_paths": [
    "actions > call",
    "call action",
    "calling procedures",
    "procedures > calling"
  ],
  "related_links": [
    "#1384995",
    "action_write.htm#1385033",
    "procedure_calling.htm#1291793",
    "return_value_dialog.htm#1292200",
    "procedures_how_to_execute.htm#1518702"
  ],
  "images": [],
  "content_hash": "840287f588b4815b",
  "level": 1
}
---

# The ‘call’ action: Calling a procedure > The ‘call’ action: Calling a procedure

The EXEC call action transfers execution from the current procedure (the caller) to the first step in a different procedure (the called procedure).

- The call action can pass arguments to procedures. Named arguments are listed first in -arg1 arg1Value -arg2 arg2Value (Tcl) or (arg_1 = value1, arg_2 = value2, arg_3 = value3) (Python) format, followed by the values of numbered arguments in order. See About arguments in procedure calls.

> **Note:** Note When editing a test case, if you enable the "Perform command, variable, and backslash substitution” behavior on a call step (by clicking the checkbox in the step property), iTest displays a warning message as follows and requires you to acknowledge what you are doing.

Call steps already perform command, variable, and backslash substitutions. Enabling this may result in unexpected double substitution and should be avoided in most cases. However, to call a procedure with arguments through substitution, this option would need to be enabled.

- When the called procedure exits, execution returns to the caller

- Procedures can call procedures in a nested fashion

- call creates an executed step in test reports. The step contains any response data, and the calling step's analysis rule applies in the normal way to the returned data.

> **Tip:** Tip A write step adds text into the response of a call step. In a called procedure, you can use write steps to include response text from multiple steps in the called procedure (as a multi-line string). The text that appears in the Description cell of the write step is appended to the response. See The ‘write’ action: Adding text into the response of a call step for details.

> **Note:** Note If a call step in a child test case B (begun by a run step in a grandparent test case A) calls grandchild test case C: The called test case C will use the shared session from test case A in its open step if the Session ID in C is same as the Session ID in A. If you do not want to use the shared session, then change the Session ID in C to be different from the Session ID in A.



To call a procedure (Adding a ‘call’ step)

See Calling a procedure in a test case step or in a property setting



To define a procedure

See Defining a procedure.



How procedures execute

See How procedures execute
