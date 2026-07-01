---
{
  "chunk_id": "field_replacements_6__guidelines_for_using_field_replacements_b290e1815114fa17",
  "source_file": "topics/field_replacements.6.htm",
  "source_original_path": "topics/field_replacements.6.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Guidelines for using field replacements"
  ],
  "heading_path": [
    "Guidelines for using field replacements",
    "Guidelines for using field replacements"
  ],
  "anchor": "1170038",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "b290e1815114fa17",
  "level": 1
}
---

# Guidelines for using field replacements > Guidelines for using field replacements

- If the first separator [ is present, but the second separator ] is not, then iTest generates an error.

- To include the character [ as text within a command (that is, not as the initial characters of a field replacement), type \[

- Whenever a single one of the characters \ or [ appears in text, it results in an error and an Execution Message is displayed in the Execution view and in the test report.

- Field replacements can appear anywhere in the text.

- Field replacements support nesting. The innermost replacement is processed first, followed in succession by each more outward replacement. Use the syntax shown here:

[command_2 [command_1:value_1] argument_2]

For example:

[param [param portIndex] State]
