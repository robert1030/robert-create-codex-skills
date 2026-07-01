---
{
  "chunk_id": "field_replacements_6__variable_substitutions_030cca45df63eb55",
  "source_file": "topics/field_replacements.6.htm",
  "source_original_path": "topics/field_replacements.6.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Guidelines for using field replacements"
  ],
  "heading_path": [
    "Guidelines for using field replacements",
    "Guidelines for using field replacements",
    "Variable substitutions"
  ],
  "anchor": "1397450",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "commands_built_in_local_variables.htm#1705062"
  ],
  "images": [],
  "content_hash": "030cca45df63eb55",
  "level": 2
}
---

# Guidelines for using field replacements > Guidelines for using field replacements > Variable substitutions

Variable substitutions are performed as follows:

| Tcl | Python |
| --- | --- |
| On any string Starting with $ (for example, $j) | Any string: j (non-session commands) and [j] (session commands) |
| For variable names with spaces, use ${variable name} | Does not support spaces in variable names. |
| port${i}count: If the variable i has value 10, then this is replaced by port10count | For variable namesport[i]count. If the variable i has value 10, then this is replaced by nameport10count |
| The $ character is escaped by a single backslash \ | Backslash is not required in Python. |

iTest includes some useful pre-defined Tcl variables. See Tcl interpreter local variables.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
