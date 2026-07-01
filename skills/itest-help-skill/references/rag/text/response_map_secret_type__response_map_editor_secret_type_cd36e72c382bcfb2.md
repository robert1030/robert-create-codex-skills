---
{
  "chunk_id": "response_map_secret_type__response_map_editor_secret_type_cd36e72c382bcfb2",
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
    "Response Map Editor: Secret Type"
  ],
  "anchor": "1735972",
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
    "topics/images/response_view_secret.png"
  ],
  "content_hash": "cd36e72c382bcfb2",
  "level": 4
}
---

# Response Map editor: Queries page > Response Map editor: Queries page > Creating a custom query > XPath 3.1 syntax for custom queries format > Response Map Editor: Secret Type

The Response map editor designates specific keys as secret types and their values appear masked in the Response, Queries, and Structure views.

When secrets are specified in a response map, iTest will change some or all of the contents of a step's response (masking the secret values). Therefore, when mapping a response with one or more secrets, you should update the samples in the response map editor with the updated response. This will ensure that other mappings can be applied to the masked response.

> **Note:** Note When the JSON response is mapped with a response map file contains secret values and is masked, the response will not be treated as a valid JSON anymore and will be shown as text response (no highlighting and formatting).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/response_view_secret.png) <!-- image_chunk: img_2183d95888778a61 -->
