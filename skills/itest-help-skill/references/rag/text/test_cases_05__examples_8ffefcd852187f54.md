---
{
  "chunk_id": "test_cases_05__examples_8ffefcd852187f54",
  "source_file": "topics/test_cases.05.htm",
  "source_original_path": "topics/test_cases.05.htm",
  "toc_path": null,
  "heading_path": [
    "iTest interpreter commands in steps",
    "iTest interpreter commands in steps",
    "Examples"
  ],
  "anchor": "1714167",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "field_replacements_tasks.htm#",
    "commands_itest_interpreter.htm#",
    "procedures_overview.htm#"
  ],
  "images": [
    "topics/images/test_cases_4.1.jpg",
    "topics/images/test_cases_3.2.jpg"
  ],
  "content_hash": "8ffefcd852187f54",
  "level": 2
}
---

# iTest interpreter commands in steps > iTest interpreter commands in steps > Examples

In this example eval step, a set command sets the value of the port_count variable.

The param command returns the value of a parameter. In this example, the param command in the command step is placed inside a field replacement. At runtime, before the step is interpreted, iTest substitutes the returned value for the field replacement (in this example, iTest substitutes the value of the parameter named ping_count). So, if the parameter had the value 9, then the step executes as ping -c 9 dut37. (Field replacements are described in “Field Replacements”.)

For full descriptions of iTest commands, see “iTest Commands”.

You can use a call step or CallProcedure action to execute a local or foreign procedure. See “Procedures”.

Create a test case and add other test cases that may be run from within this test case. The test case that contains other test cases is referred to as a Master test case and the included test cases are referred to as slave or child test cases.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/test_cases_4.1.jpg) <!-- image_chunk: img_c88d863399406b76 -->

![screenshot](topics/images/test_cases_3.2.jpg) <!-- image_chunk: img_ada760a7f28e0d15 -->
