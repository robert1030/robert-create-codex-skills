---
{
  "chunk_id": "field_replacements_4__tcl_4a18b4c8f9e9fc9c",
  "source_file": "topics/field_replacements.4.htm",
  "source_original_path": "topics/field_replacements.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "General format of field replacements"
  ],
  "heading_path": [
    "General format of field replacements",
    "General format of field replacements",
    "Tcl"
  ],
  "anchor": "1120245",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "commands_itest_interpreter.htm#"
  ],
  "images": [],
  "content_hash": "4a18b4c8f9e9fc9c",
  "level": 3
}
---

# General format of field replacements > General format of field replacements > Tcl

In Tcl, the generic format for defining a field replacement is:

[commandName args] or commandName(‘args’) in Python

for example, here is the param command in a field replacement:

Tcl: [param portCount]

Python: [param(‘portCount’)]

Some commands require a single argument, others use a subcommand and multiple arguments. In the example, portCount is the single argument. Subcommands and arguments are separated by spaces.

iTest interpreter commands are fully described in “iTest Commands”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
