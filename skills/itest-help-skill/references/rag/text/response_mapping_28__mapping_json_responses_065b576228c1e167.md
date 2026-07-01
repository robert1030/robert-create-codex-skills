---
{
  "chunk_id": "response_mapping_28__mapping_json_responses_065b576228c1e167",
  "source_file": "topics/response_mapping.28.htm",
  "source_original_path": "topics/response_mapping.28.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Mapping JSON responses"
  ],
  "heading_path": [
    "Mapping JSON responses",
    "Mapping JSON responses"
  ],
  "anchor": "1611384",
  "context_ids": [],
  "index_keywords": [
    "JSON",
    "JSON responses",
    "mapping responses"
  ],
  "index_keyword_paths": [
    "JSON > mapping responses",
    "mapping > JSON responses",
    "response mapping > JSON"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "065b576228c1e167",
  "level": 1
}
---

# Mapping JSON responses > Mapping JSON responses

iTest understands JSON structured data, maps a JSON response without requiring a response map. The structured data root for JSON responses is: mapped/Json/

A simple JSON object {name:"value1"} is structured: mapped/Json/name

A simple JSON array ["value1", "value2"] is structured: mapped/Json/item[]

The iTest JSON mapper is more tolerant than the JSON specification.

> **Note:** Note ​Empty ("") JSON object name will be replaced with the special word, "iTestEmptyXmlKeyName" in structured response.

- An extra comma (,) may appear just before the closing bracket.

- The null value will be inserted when there is, (comma) elision.

- Strings may be quoted with ' (single quote).

- Strings are not required to be quoted under these conditions.

If they do not:

- begin with a quote or single quote, do not contain leading or trailing spaces

- contain any of these characters: { } [ ] / \ : , = ; #

- look like numbers and if they are not the reserved words true, false, or null.

- Values can be separated by ; (semicolon) as well as by a , (comma).

- Numbers may have the 0- (octal) or 0x- (hex) prefix.

- Comments written in the slash-slash, slash-star, and hash conventions are ignored.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
