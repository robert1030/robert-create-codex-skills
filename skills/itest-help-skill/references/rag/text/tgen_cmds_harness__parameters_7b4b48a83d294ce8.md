---
{
  "chunk_id": "tgen_cmds_harness__parameters_7b4b48a83d294ce8",
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
    "av_create",
    "Parameters"
  ],
  "anchor": "1305904",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "7b4b48a83d294ce8",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_create > Parameters

| Name | Type | Description |
| --- | --- | --- |
| handle | handle | Specifies the handle of the parent for the newly created object. |
| relationName or objectTypeName | string | The name of the relation from the parent to the created object, or the name of the object’s type. |
| DDNPath |  | A dotted path name sequence that begins with an object handle, followed by one or more object type names. The path must identify a valid sequence of objects in the data model hierarchy. Avalanche Automation returns data for the object identified by the last name in the sequence. Use index values to identify one of a set of children of the same type. Index values are assigned in the order of creation. An unqualified type name (a name with no index value) indicates the first child object of that type for the parent. |
| DANpath |  | A dotted path name beginning with a sequence of one or more object types, and ending with an attribute name. Avalanche Automation combines the objectHandle (or the directDescendantPath) with the descendantAttributePath to resolve the attribute reference. |
| attr/value |  | The attr portion of the pair is the name of the attribute to be modified. The value portion specifies the new value. You can specify one or more attr/value pairs in a single function call. The attribute name and value must be separated by a space; each name-value pair in a sequence must be separated by a space. |
