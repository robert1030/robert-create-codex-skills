---
{
  "chunk_id": "gget_python__intro_ce7a316b3de2bfd8",
  "source_file": "popups/gget_python.html",
  "source_original_path": "popups/gget_python.html",
  "toc_path": null,
  "heading_path": [
    "gget_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_syntax_python.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [],
  "content_hash": "ce7a316b3de2bfd8",
  "level": 0
}
---

# gget_python.html

gget('variableName', 'defaultValue')

Returns the value of the specified global variable. If the specified variable is not found, then the command returns the default value if specified. Example: gget('varName', param('my_param')) ping -c [gget('ping_count')] 10.155.0.1

To insert a gget command, right-click in the field and then select Insert > Global Variable > Get.

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
