---
{
  "chunk_id": "sb_qc_definitions_validation_citeria__validation_rules_for_allowedrange_allowe_bc9b8b1becf16119",
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
    "Validation rules for AllowedRange, AllowedLength, AllowedCount:"
  ],
  "anchor": "1403653",
  "context_ids": [
    "sb_qc_definitions_validation_citeria"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "bc9b8b1becf16119",
  "level": 3
}
---

# QuickCall definitions validation criteria > QuickCall definitions validation criteria > Validation rules applied when exporting Quickcall library > Validation rules for AllowedRange, AllowedLength, AllowedCount:

The properties of AllowedRange, AllowedLength, and AllowedCount must be defined with the correct systax and structure as follows:

Format/Syntax: {min;max} or {;max} or {min;}

If an inconsistent minimum or maximum values are used, validation criteria/rule displays an error message, as the validation does not meet the defined rules:

Invalid allowed %s: %s. It should be allowed%s={min_value;max_value} or allowed%s={min_value; } or allowed%s={ ;max_value}.

For example, --datatype=integer, allowedrange={5;3}, displays an error message as follows:

Invalid allowed range: {5;3}. It should be allowedRange={min_value;max_value} or allowedRange={min_value; } or allowedRange={ ;max_value}.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
