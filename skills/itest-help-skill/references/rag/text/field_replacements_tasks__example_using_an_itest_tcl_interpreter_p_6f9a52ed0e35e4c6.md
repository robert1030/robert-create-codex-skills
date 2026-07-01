---
{
  "chunk_id": "field_replacements_tasks__example_using_an_itest_tcl_interpreter_p_6f9a52ed0e35e4c6",
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
    "Example: Using an iTest Tcl interpreter ‘param’ command in a field replacement"
  ],
  "anchor": "1336311",
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
    "topics/images/field_replacements.1.jpg"
  ],
  "content_hash": "6f9a52ed0e35e4c6",
  "level": 2
}
---

# Field replacements: Substituting values into properties and commands > Field replacements: Substituting values into properties and commands > Example: Using an iTest Tcl interpreter ‘param’ command in a field replacement

1. The text strings [param PortType] and [param SubIndex] appear in the following step:

The [param PortType] syntax means “Before running this step, replace all of the text in this field with the value of the PortType parameter”. (We will describe the syntax in a moment.)

1. 2

1. The test case has the following parameter settings:

PortType = FASTETHERNET

SubIndex = 0

1. 3

1. At runtime, step preprocessing replaces the fields. As a result, iTest issues the following command:

show interfaces FASTETHERNET 1/0indicator

![screenshot](topics/images/field_replacements.1.jpg) <!-- image_chunk: img_925d7fae566a927a -->
