---
{
  "chunk_id": "tgen_cmds_harness__parameters_e7e8c68414415f8b",
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
    "av_delete",
    "Parameters"
  ],
  "anchor": "1305961",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "e7e8c68414415f8b",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_delete > Parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | string | The object handle that identifies the object to be deleted. |
| DDNPath | string | A dotted path name sequence that begins with an object handle, followed by one or more object relation names. The path must identify a valid sequence of objects in your data model hierarchy. Avalanche Automation deletes the object identified by the last name in the sequence. Use index values to identify one of a set of children of the same type. Index values are assigned in the order of creation. An unqualified type name (a name with no index value) indicates the first child object of that type for the parent. |
