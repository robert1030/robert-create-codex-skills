---
{
  "chunk_id": "sb_qc_definitions_validation_citeria__validation_rules_for_allowedpattern_allo_d38943b4c0efa66b",
  "source_file": "topics/sb_qc_definitions_validation_citeria.htm",
  "source_original_path": "topics/sb_qc_definitions_validation_citeria.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "QuickCall definitions validation criteria"
  ],
  "heading_path": [
    "QuickCall definitions validation criteria",
    "QuickCall definitions validation criteria",
    "Validation rules applied when exporting Quickcall library",
    "Validation rules for allowedPattern, allowedLength, etc., with datatype"
  ],
  "anchor": "1397858",
  "context_ids": [
    "sb_qc_definitions_validation_citeria"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d38943b4c0efa66b",
  "level": 3
}
---

# QuickCall definitions validation criteria > QuickCall definitions validation criteria > Validation rules applied when exporting Quickcall library > Validation rules for allowedPattern, allowedLength, etc., with datatype

The table below lists the properties and the supported datatype. When you use a property that does not match the datatype, a validation conflict occurs and a validation error message displays. For example, using AllowedRange with String (i.e., --datatype=string, allowedRange={3; 5}), displays an error message as follows.

The datatype 'String' does not support the attribute 'AllowedRange'. The supported attributes are AllowedValue, AllowedPattern, AllowedLength, AllowedCount, Marked, isMultiline when exporting a Quickcall library.

| Properties/DataType | string | integer | decimal | boolean | datetime | anyURI |
| --- | --- | --- | --- | --- | --- | --- |
| AllowedValue | x | x | x | x |  | x |
| AllowedPattern | x |  |  |  | x |  |
| AllowedRange |  | x | x |  |  |  |
| AllowedLength | x |  |  |  |  |  |
| AllowedCount | x | x | x | x | x | x |
| Marked | x | x | x |  |  | x |
| isMultiline | x |  |  |  |  |  |
| enablementValue | x | x | x | x | x | x |
