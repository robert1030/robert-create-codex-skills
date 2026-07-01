---
{
  "chunk_id": "response_python__intro_54dacaa7a4bc97b0",
  "source_file": "popups/response_python.html",
  "source_original_path": "popups/response_python.html",
  "toc_path": null,
  "heading_path": [
    "response_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_response.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [],
  "content_hash": "54dacaa7a4bc97b0",
  "level": 0
}
---

# response_python.html

response('variable_name', 'regex') #alwayslist=True, group='number_or_name'

Use the response command to insert the response content stored in the specified variable. (Responses are stored using the Store response in property for a step).

alwaysList: The optional flag is useful when you use the return data as the argument in a for statement. See the online help for details.

group: The optional flag and group='number_or_name' argument is a regular expression that defines something more specific to extract from the response text.

variable_Name Is the name of the variable containing the stored response. If varName includes whitespace, it must be surrounded by double-quotes (which will be excluded from the location query before use).

regex: The optional argument is a regular expression that defines something more specific to extract from the response text.

Example:

eval print("This string will be stored in a variable"), stores the response in a variable named "output" eval response("output")

Note: In Step Properties > Other Post-processing > Store Response, do not check the option Store only the text of the response.

For details, see the online help: Using the response command in a field replacement.

Also: Field replacements: Substituting values into properties and commands.
