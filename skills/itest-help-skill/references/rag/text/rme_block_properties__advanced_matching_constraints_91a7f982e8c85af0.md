---
{
  "chunk_id": "rme_block_properties__advanced_matching_constraints_91a7f982e8c85af0",
  "source_file": "topics/rme_block_properties.htm",
  "source_original_path": "topics/rme_block_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Block Map properties"
  ],
  "heading_path": [
    "Response Map editor: Block Map properties",
    "Response Map editor: Block Map properties",
    "Advanced matching constraints"
  ],
  "anchor": "1178337",
  "context_ids": [
    "rme_block_properties"
  ],
  "index_keywords": [
    "Block Map properties",
    "Response Map editor",
    "block map"
  ],
  "index_keyword_paths": [
    "Block Map properties > Response Map editor",
    "Response Map editor > Block Map properties",
    "properties > block map"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "91a7f982e8c85af0",
  "level": 2
}
---

# Response Map editor: Block Map properties > Response Map editor: Block Map properties > Advanced matching constraints

| Minimum value | This token matches only if the returned value is greater than or equal to: For numeric tokens, the minimum allowed value for the token. See MaxValue. For tokens that can take on any of a set of specified values, see AllowedValues. Note: Use an analysis rule to make Pass / Fail decisions. |
| --- | --- |
| Maximum value | This token matches only if the returned value is less than or equal to: For numeric tokens, the maximum allowed value for the token. See MinValue. Use 0 to represent “any value allowed”. For tokens that can take on any of a set of specified values (text or numeric), see Match only on one of the following values. Note: Use an analysis rule to make Pass / Fail decisions. |
| Match only on one of the following values | (Enter one allowed value on each line) The collection of values that this token can take on. For example, the PortStatus token might take on either of the two values Up or Down. The most common use for the AllowedValues property is for tokens that can take on any of a set of specified values (text or numeric). In the text box, type the allowed values, one per line. When you have finished entering values, press Ctrl-Enter. For tokens that can take on numeric values within a range, see MinValue and MaxValue. Note Use an analysis rule to make Pass / Fail decisions. |
| Note | Use an analysis rule to make Pass / Fail decisions. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
