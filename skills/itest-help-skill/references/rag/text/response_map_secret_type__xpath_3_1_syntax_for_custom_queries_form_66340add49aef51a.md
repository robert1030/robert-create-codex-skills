---
{
  "chunk_id": "response_map_secret_type__xpath_3_1_syntax_for_custom_queries_form_66340add49aef51a",
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
    "XPath 3.1 syntax for custom queries format"
  ],
  "anchor": "1759990",
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
  "images": [
    "topics/images/rme_queries_custom_syntax_example.png"
  ],
  "content_hash": "66340add49aef51a",
  "level": 3
}
---

# Response Map editor: Queries page > Response Map editor: Queries page > Creating a custom query > XPath 3.1 syntax for custom queries format

XPath 3.1 response maps custom queries follow java.text.MessageFormat. See https://docs.oracle.com/javase/7/docs/api/java/text/MessageFormat.html.

In Xpath 3.1 curly braces are widely used for map and array operations.

The significant difference is that single quotes should be escaped with additional single quotes.

XPath 1.0 syntax: .//*[name() = 'my_node']

XPath 3.1 syntax: .//*[name() = ''my_node'']

{text} in XPath 3.1 syntax may be escaped as follows: '{text} or '{text}'

If you want to wrap an argument value within single quotes, use ''{0}''.

![screenshot](topics/images/rme_queries_custom_syntax_example.png) <!-- image_chunk: img_28f56057eab6d475 -->
