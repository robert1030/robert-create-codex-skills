---
{
  "chunk_id": "rm_chaining__making_use_of_existing_response_map_libr_a924c8cf11cec195",
  "source_file": "topics/rm_chaining.htm",
  "source_original_path": "topics/rm_chaining.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Making use of existing response map libraries: Chaining response maps"
  ],
  "heading_path": [
    "Making use of existing response map libraries: Chaining response maps",
    "Making use of existing response map libraries: Chaining response maps"
  ],
  "anchor": "1139163",
  "context_ids": [
    "rm_chaining"
  ],
  "index_keywords": [
    "chaining",
    "chaining response maps",
    "reusing"
  ],
  "index_keyword_paths": [
    "chaining response maps",
    "response map libraries > chaining",
    "response map libraries > reusing",
    "response maps > chaining"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "a924c8cf11cec195",
  "level": 1
}
---

# Making use of existing response map libraries: Chaining response maps > Making use of existing response map libraries: Chaining response maps

The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other specified libraries.

Response map chaining is helpful when:

- You do not have write-permission to modify the response maps in the corporate library, but need to provide alternative response maps for a step to try before (and in addition to) the response maps in the corporate library.

- You have sets of commands for device families and the specific devices (for example, one set for IOS and one for all 3K-series devices).

> **Note:** Note A custom parser is applicable only in the map in which it is used. Custom parsers are not imported from chained maps.
