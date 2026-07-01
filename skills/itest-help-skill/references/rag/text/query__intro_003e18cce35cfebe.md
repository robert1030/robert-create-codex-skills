---
{
  "chunk_id": "query__intro_003e18cce35cfebe",
  "source_file": "popups/query.html",
  "source_original_path": "popups/query.html",
  "toc_path": null,
  "heading_path": [
    "query.html"
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
  "content_hash": "003e18cce35cfebe",
  "level": 0
}
---

# query.html

Use the query command to insert the result of a query into a command or property.

varName is a variable that stores the response content. (Responses are stored using the Store response in property for a step). You can use "." to indicate the response for the current step.

mapperQuery is a mapping query that will be applied to the structured data in that response object. Either an XPath query or a query from a response map, as defined in the response map for the step. If query includes whitespace, it must be surrounded by double-quotes.

The optional -alwaysList flag causes a single extracted value to be stored in a list with a single element, rather than in a scalar string. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single extracted value can contain whitespace. When you use the -alwaysList flag, a foreach statement that iterates over the stored variable will loop once for the match (rather than once for each word in the match).

For details, see the online help: Inserting the results of a query

Here's a tip for the quickest way to insert a field replacement for a query command applied to a stored response
