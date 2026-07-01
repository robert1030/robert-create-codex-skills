---
{
  "chunk_id": "query_python__intro_9f8bd9060fcc6429",
  "source_file": "popups/query_python.html",
  "source_original_path": "popups/query_python.html",
  "toc_path": null,
  "heading_path": [
    "query_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/field_replacement_query.html",
    "help::/com.fnfr.svt.help/topics/insert_query_on_stored_response_dialog.html"
  ],
  "images": [],
  "content_hash": "9f8bd9060fcc6429",
  "level": 0
}
---

# query_python.html

Use the query command to insert the result of a query into a command or property.

The query command takes two arguments, the first is the location of the stored response. It is either an XPATH query to the location of the stored response on the heap, or a ".", to mean the response for the current step.

variable_name is a variable that stores the response content. The query command takes two arguments, the first is the location of the stored response. It is either an XPATH query to the location of the stored response on the heap, or a ".", to mean the response for the current step.

mapper_query is the query that is performed on the stored response, whose result is returned by the command.

alwaysList is an optional flag that causes a single extracted value to be stored in a list with a single element, rather than in a scalar string. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single extracted value can contain whitespace.

Example:

eval print("some: thing") Stores the response in a variable named "response". query('response', 'some()', alwaysList=False) Do not check the option Store only the text of the response, in Step Properties > Other Post-processing.

For details, see the online help: Inserting the results of a query

Here's a tip for the quickest way to insert a field replacement for a query command applied to a stored response
