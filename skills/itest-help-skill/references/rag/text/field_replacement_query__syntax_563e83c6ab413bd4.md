---
{
  "chunk_id": "field_replacement_query__syntax_563e83c6ab413bd4",
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
    "Syntax"
  ],
  "anchor": "1839912",
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
  "related_links": [],
  "images": [],
  "content_hash": "563e83c6ab413bd4",
  "level": 2
}
---

# query command: Inserting the results of a query > query command: Inserting the results of a query > Syntax

Tcl: query ?-alwayslist? varName mapperQuery

Python: query('variable_name', 'mapper_query', alwayslist=False)

| Tcl | Python | Description |
| --- | --- | --- |
| varName | variable_name | Variable that stores the response content. (Responses are stored using the Store response in property for a step). You can use “.” to indicate the response for the current step. |
| mapperQuery | mapper_query | Mapping query that will be applied to the structured data in that response object. Either an XPath query or a query from a response map, as defined in the response map for the step. If query includes whitespace, it must be surrounded by double-quotes. |
| -alwaysList | alwayslist | The optional -alwaysList flag causes a single extracted value to be stored in a list with a single element, rather than in a scalar string. (A response with zero values or multiple values is always stored in a list.) This setting is important when you're using the response as the argument to a foreach statement and a single extracted value can contain whitespace. When you use the -alwaysList flag, a foreach statement that iterates over the stored variable will loop once for the match (rather than once for each word in the match). |

Mapper queries support field substitutions, but some queries may also contain special interpreter characters. So you may need to “escape” these special characters. For example,

- Tcl: query myResponse inputPktsByPort("$portName")

- Python: query('myResponse','inputPktsByPort("'+portName+'")')

In this case, $portName or portName will first be substituted to become, for example, FastEthernet1/0/1.

> **Note:** Note You must place double-quotes around portName because the query engine is XPATH, which requires strings around its arguments.

For a more complicated query:

Tcl: table/row[1]/fieldB

Python: query("myResponse", "table/row[1]/fieldB")

In this case, the square brackets will not be appropriate for interpreter substitution, use:

[query myResponse table/row[1]/fieldB]
