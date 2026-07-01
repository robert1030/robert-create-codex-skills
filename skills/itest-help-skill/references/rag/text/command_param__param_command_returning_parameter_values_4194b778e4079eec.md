---
{
  "chunk_id": "command_param__param_command_returning_parameter_values_4194b778e4079eec",
  "source_file": "topics/command_param.htm",
  "source_original_path": "topics/command_param.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "param command: Returning parameter values"
  ],
  "heading_path": [
    "param command: Returning parameter values",
    "param command: Returning parameter values"
  ],
  "anchor": "1679166",
  "context_ids": [
    "command_param"
  ],
  "index_keywords": [
    "accessing",
    "param",
    "param field replacement",
    "using in steps"
  ],
  "index_keyword_paths": [
    "field replacements > param",
    "param field replacement",
    "parameters > accessing",
    "parameters > using in steps"
  ],
  "related_links": [
    "field_replacements_tasks.htm#"
  ],
  "images": [
    "topics/images/commands_3.1.jpg",
    "topics/images/command_example_python.png"
  ],
  "content_hash": "4194b778e4079eec",
  "level": 1
}
---

# param command: Returning parameter values > param command: Returning parameter values

Returns the value of a parameter (typically for insertion into a command or property).

In this example, the param command in the command step is inside a field replacement that is replaced just before the step executes. The command is replaced with the value of the parameter named ping_count. So, if the parameter had the value 9, then the step would execute as ping -c 9 dut37. (Field replacements are described in “Field Replacements”.)

Python:

![screenshot](topics/images/commands_3.1.jpg) <!-- image_chunk: img_44b95d6cfbefd370 -->

![screenshot](topics/images/command_example_python.png) <!-- image_chunk: img_e7606acc24158191 -->
