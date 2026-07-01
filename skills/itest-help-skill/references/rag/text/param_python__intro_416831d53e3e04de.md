---
{
  "chunk_id": "param_python__intro_416831d53e3e04de",
  "source_file": "popups/param_python.html",
  "source_original_path": "popups/param_python.html",
  "toc_path": null,
  "heading_path": [
    "param_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_param.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [
    "images/cmd_example_python.png"
  ],
  "content_hash": "416831d53e3e04de",
  "level": 0
}
---

# param_python.html

param('parameter_name_or_query', 'default')

The param command inserts the value of a parameter into a test case step or property.

In this example, [param('ping_count')] is a field replacement that is replaced at runtime by the value of the ping_count parameter.

Example: eval count = param('ping_count', 5) #ping_count will have default value eval device = param('device_name') #device_name parameter will be defined in the parameter file command ping -c [count] [device]

Parameters can be defined in the test case, in the testbed, in another test case that loaded as a result of a foreign procedure, or in the session profile associated with the step. To access a parameter defined in the session profile associated with a step, use the profile command.

For details, see the online help: Accessing parameter values: The param command.

Also, see: Field replacements: Substituting values into properties and commands.

![screenshot](images/cmd_example_python.png) <!-- image_chunk: img_ebec6e935d3694f0 -->
