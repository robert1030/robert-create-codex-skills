---
{
  "chunk_id": "field_replacements_tasks__example_using_an_itest_python_interprete_fd41a2ec42a3ce7a",
  "source_file": "topics/field_replacements_tasks.htm",
  "source_original_path": "topics/field_replacements_tasks.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Field replacements: Substituting values into properties and commands"
  ],
  "heading_path": [
    "Field replacements: Substituting values into properties and commands",
    "Field replacements: Substituting values into properties and commands",
    "Example: Using an iTest Python interpreter command in a field replacement"
  ],
  "anchor": "1386214",
  "context_ids": [
    "field_replacements_tasks"
  ],
  "index_keywords": [
    "defined",
    "field substitution",
    "guidelines",
    "runtime field replacement",
    "substituting values at runtime",
    "syntax"
  ],
  "index_keyword_paths": [
    "field replacements > defined",
    "field replacements > guidelines",
    "field replacements > syntax",
    "field substitution",
    "runtime field replacement",
    "substituting values at runtime"
  ],
  "related_links": [],
  "images": [
    "topics/images/field_replacements.2.jpg"
  ],
  "content_hash": "fd41a2ec42a3ce7a",
  "level": 2
}
---

# Field replacements: Substituting values into properties and commands > Field replacements: Substituting values into properties and commands > Example: Using an iTest Python interpreter command in a field replacement

1. The text strings [param(‘PortType’)] and [param(‘SubIndex’)] appear in the following step:

The [param(‘PortType’)] syntax means “Before running this step, replace all of the text in this field with the value of the PortType parameter”

1. 2

1. At runtime, step preprocessing replaces the fields. As a result, iTest issues the following command displaying the type of values, ins:

PortType = FASTETHERNET

SubIndex = 0

1. 3

1. At runtime, step preprocessing replaces the fields. As a result, iTest issues the following command:

show interfaces FASTETHERNET 1/0indicator

![screenshot](topics/images/field_replacements.2.jpg) <!-- image_chunk: img_e48f28a01ec6137e -->
