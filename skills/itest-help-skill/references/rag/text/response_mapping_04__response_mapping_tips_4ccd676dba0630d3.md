---
{
  "chunk_id": "response_mapping_04__response_mapping_tips_4ccd676dba0630d3",
  "source_file": "topics/response_mapping.04.htm",
  "source_original_path": "topics/response_mapping.04.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response mapping tips"
  ],
  "heading_path": [
    "Response mapping tips",
    "Response mapping tips"
  ],
  "anchor": "1133490",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "specify_memory.htm#1162850"
  ],
  "images": [],
  "content_hash": "4ccd676dba0630d3",
  "level": 1
}
---

# Response mapping tips > Response mapping tips

- If you need to return only a small number of values from a response, it is probably faster and easier to add individual queries rather than creating a response map. You can do that from the Response view, the Queries view, or the Structure view. In the view, select the value, right-click it, and then select Add Rule.

- Once you create a response map, you can access it quickly from a test case by right-clicking the appropriate step and then selecting Open Response Map.

- For ease of maintenance and understanding, you typically name a response map with the text of the command that results in the response (for example, name the response map for the show interfaces command show_interfaces).

- For very large responses, allocate more memory to iTest. See Specifying how much memory to allocate to iTest.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
