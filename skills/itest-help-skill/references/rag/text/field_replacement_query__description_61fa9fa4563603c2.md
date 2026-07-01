---
{
  "chunk_id": "field_replacement_query__description_61fa9fa4563603c2",
  "source_file": "topics/field_replacement_query.htm",
  "source_original_path": "topics/field_replacement_query.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "Commands that are commonly used in field replacements",
    "query command: Inserting the results of a query"
  ],
  "heading_path": [
    "query command: Inserting the results of a query",
    "query command: Inserting the results of a query",
    "Description"
  ],
  "anchor": "1697207",
  "context_ids": [
    "field_replacement_query"
  ],
  "index_keywords": [
    "in field replacements",
    "mapping queries in",
    "query",
    "query field replacement"
  ],
  "index_keyword_paths": [
    "field replacements > mapping queries in",
    "field replacements > query",
    "mapping queries > in field replacements",
    "queries > in field replacements",
    "query field replacement"
  ],
  "related_links": [
    "preferences_response_map.htm#1318143"
  ],
  "images": [],
  "content_hash": "61fa9fa4563603c2",
  "level": 2
}
---

# query command: Inserting the results of a query > query command: Inserting the results of a query > Description

Returns the result of the query — a number, a string, or a list of strings. In the case of a list of strings, if an element is empty or contains whitespace, then it will be surrounded by { } (in Tcl) or [ ] (in Python) characters automatically. Otherwise, the list of strings is just returned as a concatenation of the elements, separated by whitespace.

If “.” is used for the location, then this is a special case and treated as pointing to the response to the current step. It is only valid for fields that are used after the step's execution is complete (typically in analysis rules).

If the node identified by query is not a response object (as identified by a corresponding attribute on that node), then iTest declares an error in the test report and on the Execution view.

> **Tip:** Tip You can set preferences for queries. See Setting preferences for response mapping.
