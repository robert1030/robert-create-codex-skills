---
{
  "chunk_id": "response_map_secret_type__creating_a_custom_query_a1190e5fb02db3d7",
  "source_file": "topics/response_map_secret_type.htm",
  "source_original_path": "topics/response_map_secret_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Queries page"
  ],
  "heading_path": [
    "Response Map editor: Queries page",
    "Response Map editor: Queries page",
    "Creating a custom query"
  ],
  "anchor": "1106213",
  "context_ids": [
    "response_map_secret_type",
    "rme_queries_page"
  ],
  "index_keywords": [
    "Queries page",
    "Response Map editor",
    "custom definitions",
    "in response maps",
    "queries"
  ],
  "index_keyword_paths": [
    "Queries page > Response Map editor",
    "Response Map editor > Queries page",
    "queries > custom definitions",
    "queries > in response maps",
    "response maps > queries"
  ],
  "related_links": [
    "#1735972"
  ],
  "images": [
    "topics/images/rme_queries_custom.png",
    "topics/images/response_mapping_3.2.jpg"
  ],
  "content_hash": "a1190e5fb02db3d7",
  "level": 2
}
---

# Response Map editor: Queries page > Response Map editor: Queries page > Creating a custom query

1. Select the query in the list. Click Make Custom

1. 2

1. The query is added to the Custom Queries section: The name appears in the Queries list, the name is added to the Query name box, and the XPath is added to the Query format box.

1. 3

1. Edit the values as needed:

Custom queries

| Query name | Specify a name for the custom query. |
| --- | --- |
| Query format | Specify an XPath expression with optional argument substitution using zero-based argument numbers in the format {0} {1} {2} For example, assume that there is one argument that is the ifIndex: count(mapped/yaml/document/*) |
| Description | Type text that will help coworkers understand the use of the query. |
| Secret | Select Hide the values in views and reports to hide the custom queries defined as Secret. To see how the Secret type appears on the Response, Structure, and Query views, see Response Map Editor: Secret Type. To see how this secret type is applied in REST interactive sessions, see Apply Custom Response Maps to interactive REST session responses, “REST sessions”. |
|  | To see how the Secret type appears on the Response, Structure, and Query views, see Response Map Editor: Secret Type. |
|  | To see how this secret type is applied in REST interactive sessions, see Apply Custom Response Maps to interactive REST session responses, “REST sessions”. |

1. 4

1. If appropriate, click Add to add arguments and specify property settings as needed:

Arguments

| Argument name | Specify a name for the argument. |
| --- | --- |

Optional advanced properties

| Default value | Optional. Type a default value. Later when a test case that uses the query is loaded for execution or paused, you can change the value in the Data view. |
| --- | --- |
| Values query | Optional. Provide an XPath query that finds all possible values for the argument within the structure data. iTest shows all possible cases in the Queries view. This means that users can right-click the blue boxes in the Response view to add a query-based analysis rule. (Most auto-generated queries make use of this technology). You can try the query out by pasting it into the Structure view and clicking Evaluate. When the query returns the values you expect, copy/paste it back into the Values query property box. |
| Interpret as | Optional. Specify how to interpret the Values query setting. DontInterpret: Ignore the Values query setting. There will be one value for the argument supplied by the Default Value property. SampleValues: Values for the argument will be the values of the nodes returned by the Values query. ItemCount: When the Values query returns a list, then you can specify ItemCount to so that the values for the argument will be 1, 2, 3, … up to count of items returned by the query. For example, use this setting to get the count of rows in a table. SampleNodeNames: Values for the argument will be the names of the nodes returned by the Values query. |

![screenshot](topics/images/rme_queries_custom.png) <!-- image_chunk: img_263eb03d21b87e50 -->

![inline_icon](topics/images/response_mapping_3.2.jpg) <!-- image_chunk: img_378e67886742c9fc -->
