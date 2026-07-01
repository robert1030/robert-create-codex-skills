---
{
  "chunk_id": "response_mapping_02__a_response_map_returns_data_from_a_respo_e92d32e6ef170378",
  "source_file": "topics/response_mapping.02.htm",
  "source_original_path": "topics/response_mapping.02.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Why create a response map?"
  ],
  "heading_path": [
    "Why create a response map?",
    "Why create a response map?",
    "A response map returns data from a response for analysis or for other uses"
  ],
  "anchor": "1426176",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/response_view_blue_text.png"
  ],
  "content_hash": "e92d32e6ef170378",
  "level": 2
}
---

# Why create a response map? > Why create a response map? > A response map returns data from a response for analysis or for other uses

When you create a response map, you create queries that can reliably return particular values from any response to the particular command (based on the structured sample response that you used to create the response map). As a result, when you later execute a test case, an analysis rule for a step can use a query defined in the map to return values from a response and can then evaluate the response to determine pass/fail for the test case or to perform other tasks.

In this example response, the matches to queries (defined in the response map) are in color on a white background— your visual cue that the mapper has done its work and returned all matches to defined queries. The values in quotes are available for you to work with using analysis rules.

iTest automatically maps queries for keys at the root level of a JSON object response. There is no need to create auto-mapping queries for nested keys.

So, a response map is a more-or-less complete structuring of a response so that any value of any of the data fields of interest can be returned for use by the test case developer. A map is a general-purpose tool that you can reuse in different test cases for different testing / analysis purposes.

The process of response mapping has two main purposes:

- Parsing an unstructured response and returning the interesting data into a structured version of the response.

- Providing meaningful queries to mine the data in that structured portion of the response. The process of mapping is performed either by built-in mappers for some session types (Web, SNMP, TL1, JSON, all of the traffic generator session types) or by passing a text response (for example, from Telnet or SSH) through a response map.

![screenshot](topics/images/response_view_blue_text.png) <!-- image_chunk: img_5955ed7182b536cb -->
