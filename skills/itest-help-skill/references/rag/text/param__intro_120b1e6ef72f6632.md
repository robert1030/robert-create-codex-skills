---
{
  "chunk_id": "param__intro_120b1e6ef72f6632",
  "source_file": "popups/param.html",
  "source_original_path": "popups/param.html",
  "toc_path": null,
  "heading_path": [
    "param.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/field_replacement_param.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [
    "images/insert_parameter_step2.jpg"
  ],
  "content_hash": "120b1e6ef72f6632",
  "level": 0
}
---

# param.html

The param command inserts the value of a parameter into a test case step or property.

In this example, [param ping_count] is a field replacement that is replaced at runtime by the value of the ping_count parameter.

Parameters can be defined in the test case, in the testbed, in another test case that loaded as a result of a foreign procedure, or in the session profile associated with the step. To access a parameter defined in the session profile associated with a step, use the profile command.

For details, see the online help: Accessing parameter values: The param command.

Also, see: Field replacements: Substituting values into properties and commands.

![screenshot](images/insert_parameter_step2.jpg) <!-- image_chunk: img_770c3138e54b54ca -->
