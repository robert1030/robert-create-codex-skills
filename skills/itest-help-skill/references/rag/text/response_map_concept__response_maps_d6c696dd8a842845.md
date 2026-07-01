---
{
  "chunk_id": "response_map_concept__response_maps_d6c696dd8a842845",
  "source_file": "topics/response_map_concept.htm",
  "source_original_path": "topics/response_map_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response maps"
  ],
  "heading_path": [
    "Response maps",
    "Response maps"
  ],
  "anchor": "1179277",
  "context_ids": [
    "response_map_concept"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d6c696dd8a842845",
  "level": 1
}
---

# Response maps > Response maps

A text response from a session is either structured or unstructured. If a response is structured, it contains a native format that identifies the data in the response. Examples of structured responses are HTML, XML, TL-1, JSON, YAML, etc. – all formats that use tags and formatting to identify data. iTest natively identifies structured responses and can easily create accurate iTest queries for the data located within structured responses.

Unstructured responses are text responses with no parsing format. There is no native formatting that identifies the location of data in the response. These are the most common type of responses you will see in iTest. For example, a response table may look neat and orderly to us humans and therefore seem to be structured. Because it is purely a text file with tabs or spaces to improve its appearance and has no XML structure, however, it is not a structured response and no computer program can generated guaranteed queries to return particular items of data from the response. (iTest can do a pretty good job of guessing, however!)

You can think of a response map as a template that you define to bring structure to an unstructured response. The template specifically identifies the data within the response with queries that can return particular values from the response. When a response map is applied to a response, you will see each item of data in color (in the Response view) that matches the queries defined in the response map.

Typically, you use a response map to return the data that you are interested in from the response to a step in a test case.
