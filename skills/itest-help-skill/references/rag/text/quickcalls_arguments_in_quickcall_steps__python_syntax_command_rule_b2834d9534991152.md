---
{
  "chunk_id": "quickcalls_arguments_in_quickcall_steps__python_syntax_command_rule_b2834d9534991152",
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
    "Python Syntax Command Rule"
  ],
  "anchor": "1542289",
  "context_ids": [
    "quickcalls_arguments_in_quickcall_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/quickcalls_3.02.jpg"
  ],
  "content_hash": "b2834d9534991152",
  "level": 4
}
---

# About arguments in QuickCall steps > About arguments in QuickCall steps > Python Syntax Command Rule

When using Python syntax Call or QuickCall command, ensure that you do not use Python keywords as argument names of the called procedure or QuickCall (example, for, if, in, pass, or, and, etc.,).

If you use any Python keyword as argument names, iTest does not parse the command as Python syntax on the TestCase Editor and displays a warning message. In addition, at runtime, iTest parses the arguments incorrectly. Below is an example of invalid QuickCall.

> **Note:** Note iTest does not parse the command above in Python as the second argument has the name 'pass', which is a reserved keyword in Python.

![screenshot](topics/images/quickcalls_3.02.jpg) <!-- image_chunk: img_0939313be87a59b5 -->
