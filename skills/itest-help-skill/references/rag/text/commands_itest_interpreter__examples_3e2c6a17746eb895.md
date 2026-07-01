---
{
  "chunk_id": "commands_itest_interpreter__examples_3e2c6a17746eb895",
  "source_file": "topics/commands_itest_interpreter.htm",
  "source_original_path": "topics/commands_itest_interpreter.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "iTest interpreter commands"
  ],
  "heading_path": [
    "iTest interpreter commands",
    "iTest interpreter commands",
    "Examples"
  ],
  "anchor": "1684640",
  "context_ids": [
    "commands_itest_interpreter"
  ],
  "index_keywords": [
    "iTest",
    "iTest commands",
    "inserting into test case steps",
    "inserting variables and parameters into"
  ],
  "index_keyword_paths": [
    "iTest > command syntax > command syntax > iTest",
    "parameters > inserting into test case steps",
    "steps > inserting variables and parameters into",
    "syntax > iTest commands",
    "variables > inserting into test case steps"
  ],
  "related_links": [
    "field_replacements_tasks.htm#"
  ],
  "images": [
    "topics/images/commands.1.jpg",
    "topics/images/commands.2.jpg",
    "topics/images/commands.3.jpg"
  ],
  "content_hash": "3e2c6a17746eb895",
  "level": 2
}
---

# iTest interpreter commands > iTest interpreter commands > Examples

In this example eval step, a set command sets the value of the port_count variable.

The param command returns the value of a parameter. In this example, the param command in the command step is placed inside a field replacement. At runtime, before the step is interpreted, iTest substitutes the returned value for the field replacement (in this example, iTest substitutes the value of the parameter named ping_count). So, if the parameter had the value 9, then the step would execute as ping -c 9 dut37. (Field replacements are described in “Field Replacements”.)

Python

![screenshot](topics/images/commands.1.jpg) <!-- image_chunk: img_f71c0844bd4cbd9b -->

![screenshot](topics/images/commands.2.jpg) <!-- image_chunk: img_d40bdae3a54d53f7 -->

![screenshot](topics/images/commands.3.jpg) <!-- image_chunk: img_1bf572d0f80d5707 -->
