---
{
  "chunk_id": "action_call__about_arguments_in_procedure_calls_087211398c880426",
  "source_file": "topics/action_call.htm",
  "source_original_path": "topics/action_call.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "The ‘call’ action: Calling a procedure"
  ],
  "heading_path": [
    "The ‘call’ action: Calling a procedure",
    "The ‘call’ action: Calling a procedure",
    "About arguments in procedure calls"
  ],
  "anchor": "1384995",
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
    "quickcalls_arguments_in_quickcall_steps.htm#1530955",
    "quickcalls_arguments_in_quickcall_steps.htm#1533073"
  ],
  "images": [],
  "content_hash": "087211398c880426",
  "level": 2
}
---

# The ‘call’ action: Calling a procedure > The ‘call’ action: Calling a procedure > About arguments in procedure calls

A call action has the following content in the Description cell (all items are separated by spaces).

- The procedure name (you can specify the name dynamically using either a variable or a field replacement)

- Optional: Any number of space-separated named arguments in the following format:

(Tcl): -arg_1 value1 -arg_2 value2 -arg_3 value3 ...

(Python): (arg_1 = value1, arg_2 = value2, arg_3 = value3)

Important Ensure that you select Python or TCL call syntax for procedure calls according to the test case language. Using Python call syntax in TCL test cases (and vice versa) is not supported. See also Fixing QuickCall steps with empty description in Python TestCases and Fixing steps with empty Argument list in Python testcases.

You can specify a value dynamically using either a field replacement or $varName

> **Note:** Note All named arguments must appear before all numbered arguments.

- Optional: Any number of values for numbered arguments

To access the value of a numbered argument, use as follows.

Tcl: ${arg[<number>]}, for example, ${arg[3]}

Python: [arg(<number>)], for example, [arg(3)]
