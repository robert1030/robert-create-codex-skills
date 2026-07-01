---
{
  "chunk_id": "tgen_cmds_harness__parameters_d5a5cd1ebf6efab2",
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
    "Parameters"
  ],
  "anchor": "1306050",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d5a5cd1ebf6efab2",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_get > Parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | handle | Identifies the object from which data will be retrieved. |
| attributeName | string | Identifies an attribute for the specified object. |
| DDNPath |  | A dotted path name sequence that begins with an object handle, followed by one or more relation names. The path must identify a valid sequence of relations in your data model hierarchy. Avalanche Automation returns data for the object identified by the last name in the sequence. Use index values to identify one of a set of children of the same type. Index values are assigned in the order of creation. An unqualified type name (a name with no index value) indicates the first child object of that type for the parent. |
| DANPath |  | A dotted path name beginning with a sequence of one or more relation names, and ending with an attribute name. Avalanche Automation combines the handle (or the DDNPath) with the DANPath to resolve the attribute reference. |
| relationName |  | Specifies name of the relation that should be retrieved from the target object. |
