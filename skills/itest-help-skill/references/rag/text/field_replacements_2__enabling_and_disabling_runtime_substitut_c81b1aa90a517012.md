---
{
  "chunk_id": "field_replacements_2__enabling_and_disabling_runtime_substitut_c81b1aa90a517012",
  "source_file": "topics/field_replacements.2.htm",
  "source_original_path": "topics/field_replacements.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Where you can use field replacements"
  ],
  "heading_path": [
    "Where you can use field replacements",
    "Where you can use field replacements",
    "Enabling and disabling runtime substitution of field replacements"
  ],
  "anchor": "1336784",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "c81b1aa90a517012",
  "level": 2
}
---

# Where you can use field replacements > Where you can use field replacements > Enabling and disabling runtime substitution of field replacements

To specify whether or not to perform substitution of field replacement text before interpreting the text at runtime, click the icon (the field replacement indicator). The indicator switches among one of the following states:

|  | Perform substitution of all field replacements before interpreting the text |
| --- | --- |
|  | Do not perform substitution of text that has the form of a field replacement |
|  | This indicator appears if you select multiple steps in the Test Case editor and the steps have different settings. |

To specify the substitution setting for multiple steps, select all of the steps (Ctrl-click and Shift-click) and then click the indicator.

Important If the field replacement text includes a character that should not be replaced at runtime, be sure to escape it using the backslash \ character. For example, \$ escapes the $ character.
