---
{
  "chunk_id": "response_map_secret_type__example_custom_query_8f074c87a8a804bf",
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
    "Creating a custom query",
    "XPath 3.1 syntax for custom queries format",
    "Example custom query:"
  ],
  "anchor": "1760731",
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
  "related_links": [],
  "images": [],
  "content_hash": "8f074c87a8a804bf",
  "level": 4
}
---

# Response Map editor: Queries page > Response Map editor: Queries page > Creating a custom query > XPath 3.1 syntax for custom queries format > Example custom query:

| mapped/yaml/document/*[local-name() = ''{0}'' and text() = '''{ curly brace text }'''] |
| --- |

If the query has a single argument with value my_node, the following XPath will be produced:

| mapped/yaml/document/*[local-name() = 'my_node' and text() = '{ curly brace text }'] |
| --- |

> **Note:** Note Single curly brace ({) may be escaped by enclosing within a single quote.
