---
{
  "chunk_id": "response__intro_e36095d85997faa8",
  "source_file": "popups/response.html",
  "source_original_path": "popups/response.html",
  "toc_path": null,
  "heading_path": [
    "response.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/field_replacement_response.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [],
  "content_hash": "e36095d85997faa8",
  "level": 0
}
---

# response.html

Use the response command to insert the response content stored in the specified variable. (Responses are stored using the Store response in property for a step).

The optional -alwaysList flag is useful when you use the return data as the argument in a foreach statement. See the online help for details.

The optional -group flag and group_number_or_name argument is a regular expression that defines something more specific to extract from the response text.

variable_name Is the name of the variable containing the stored response. If variable_name includes whitespace, it must be surrounded by double-quotes (which will be excluded from the location query before use).

The optional regex argument is a regular expression that defines something more specific to extract from the response text.

For details, see the online help: Using the response command in a field replacement.

Also: Field replacements: Substituting values into properties and commands.
