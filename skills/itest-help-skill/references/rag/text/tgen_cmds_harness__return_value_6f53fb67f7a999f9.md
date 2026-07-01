---
{
  "chunk_id": "tgen_cmds_harness__return_value_6f53fb67f7a999f9",
  "source_file": "topics/tgen_cmds_harness.htm",
  "source_original_path": "topics/tgen_cmds_harness.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Avalanche API Commands"
  ],
  "heading_path": [
    "Avalanche API Commands",
    "Avalanche API Commands",
    "av_get",
    "Return Value"
  ],
  "anchor": "1306039",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "6f53fb67f7a999f9",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_get > Return Value

When you retrieve one or more attributes, av_get returns a string containing a single attribute value or a set of name-value pairs. If you do not specify any attributes, the get function can return either a single attribute value or a list of name-value pairs.

When the get function returns a list of name-value pairs, Avalanche Automation returns a single string containing the list. Each attribute name and its value is separated by a space, and the name-value pairs are also separated by a space:

attr1 value1 attr2 value2 ..attrN valueN

When you specify a relation name, the get function returns one or more handles.

Errors are raised as exceptions, encoded as string values that describe the error condition.
