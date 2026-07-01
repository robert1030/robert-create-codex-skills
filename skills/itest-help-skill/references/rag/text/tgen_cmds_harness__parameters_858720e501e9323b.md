---
{
  "chunk_id": "tgen_cmds_harness__parameters_858720e501e9323b",
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
    "av_config",
    "Parameters"
  ],
  "anchor": "1305796",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "858720e501e9323b",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_config > Parameters

| Name | Type | Description |
| --- | --- | --- |
| objectHandle | handle | Data model object/node handle |
| attrName value | name/value pair | An attribute name/value pair. The attr portion of the pair is the name of the attribute to be modified. The value portion specifies the new value. You can specify one or more attrName/value pairs in a single function call. The attribute name and value must be separated by a space; each attrName/value pair in a sequence must also be separated by a space. |
| DANPath | string | A dotted path name that begins with a sequence of one or more object types, and ending with an attribute name. Avalanche Automation combines the objectHandle (or the directDescendantPath) with the descendantAttributePath to resolve the attribute reference. |
| DDNPath | string | A dotted path name sequence that begins with an object handle, followed by one or more object type names. The path must identify a valid sequence of objects in the data model hierarchy. Avalanche Automation returns data for the object identified by the last name in the sequence. Use index values to identify one of a set of children of the same type. Index values are assigned in the order of creation. An unqualified type name (a name with no index value) indicates the first child object of that type for the parent. |
