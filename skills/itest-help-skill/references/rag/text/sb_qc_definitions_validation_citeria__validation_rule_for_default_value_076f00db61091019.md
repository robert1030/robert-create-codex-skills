---
{
  "chunk_id": "sb_qc_definitions_validation_citeria__validation_rule_for_default_value_076f00db61091019",
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
    "Validation rule for default value"
  ],
  "anchor": "1397816",
  "context_ids": [
    "sb_qc_definitions_validation_citeria"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "076f00db61091019",
  "level": 3
}
---

# QuickCall definitions validation criteria > QuickCall definitions validation criteria > Validation rules applied when exporting Quickcall library > Validation rule for default value

In iTest Quickcall, the default value of argument can be specified in the parameter default value. When the default value is specified and the custom session command property declaration is defined, the validation criteria will be used to validate any conflict. The table below shows the validation criteria and the error message displayed.

| Validation criteria | Example | Error Message |
| --- | --- | --- |
| The defaultValue does not match the datatype | dataType=integer, defaultValue=abc | "The value '%s' does not match the data-type %s. " |
| The defaultValue does not match the allowedValue | allowedValue=1|2, defaultValue=a | "The defaultValue '%s' is not in the allowedValue list \"%s\". " |
| The defaultValue does not match the allowedRange | allowedRange={2;4}, defaultValue=5 | "The defaultValue '%s' does not match the allowedRange \"%s\". " |
| The defaultValue does not match the allowedLength | allowedLength={2;4}, defaultValue=abcde | "The defaultValue '%s' does not match the allowedLength \"%s\". " |
| The defaultValue does not match the allowedPattern | allowedPattern=\\d+, defaultValue=abcde | "The defaultValue '%s' does not match the pattern \"%s\". " |
