---
{
  "chunk_id": "quickcalls_arguments_in_quickcall_steps__example_67898c5f803a4b20",
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
    "About arguments in QuickCall steps",
    "Example:"
  ],
  "anchor": "1403625",
  "context_ids": [
    "quickcalls_arguments_in_quickcall_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1533073"
  ],
  "images": [
    "topics/images/quickcalls_2.01.jpg"
  ],
  "content_hash": "67898c5f803a4b20",
  "level": 4
}
---

# About arguments in QuickCall steps > About arguments in QuickCall steps > Example:

This example call to the ExercisePorts QuickCall includes two named arguments and one numbered argument. Here is the form of the call:

<QuickCallName> -slot slotNumber -port portNumber numberOfRepetitions

Here is the actual QuickCall step: The value of the port argument is determined dynamically by the return value of a param command.The numbered argument has the value 75.

Ensure that you select Python or TCL call syntax for procedure calls according to the test case language. Using Python call syntax in TCL test cases (and vice versa) is not supported. See Fixing steps with empty Argument list in Python testcases.

![screenshot](topics/images/quickcalls_2.01.jpg) <!-- image_chunk: img_8893194729daa514 -->
