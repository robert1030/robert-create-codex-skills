---
{
  "chunk_id": "quickcalls_arguments_in_quickcall_steps__about_arguments_in_quickcall_steps_a19ca8bd5cd73533",
  "source_file": "topics/quickcalls_arguments_in_quickcall_steps.htm",
  "source_original_path": "topics/quickcalls_arguments_in_quickcall_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Adding a test case step that executes a QuickCall",
    "About arguments in QuickCall steps"
  ],
  "heading_path": [
    "About arguments in QuickCall steps",
    "About arguments in QuickCall steps"
  ],
  "anchor": "1403617",
  "context_ids": [
    "quickcalls_arguments_in_quickcall_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1533073"
  ],
  "images": [],
  "content_hash": "a19ca8bd5cd73533",
  "level": 1
}
---

# About arguments in QuickCall steps > About arguments in QuickCall steps

A QuickCall has the following content in the Description cell (all items are separated by spaces).

Important Ensure that you select Python or TCL call syntax for procedure calls according to a test case language. Using Python call syntax in TCL test cases (and vice versa) is not supported. See Fixing steps with empty Argument list in Python testcases.

- Optional: Any number of space-separated named arguments in the following format:

-arg_1 value1 -arg_2 value2 -arg_3 value3 ...

You can specify a value dynamically using either a field replacement or $varName

> **Note:** Note All named arguments must appear before all numbered arguments.

- Optional: Any number of values for numbered arguments

To access the value of a numbered argument, use ${arg[<number>]}, for example, ${arg[3]}
