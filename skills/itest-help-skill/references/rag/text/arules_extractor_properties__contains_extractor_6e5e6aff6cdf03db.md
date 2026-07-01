---
{
  "chunk_id": "arules_extractor_properties__contains_extractor_6e5e6aff6cdf03db",
  "source_file": "topics/arules_extractor_properties.htm",
  "source_original_path": "topics/arules_extractor_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis rules: Properties of the extractor"
  ],
  "heading_path": [
    "Analysis rules: Properties of the extractor",
    "Analysis rules: Properties of the extractor",
    "Contains extractor"
  ],
  "anchor": "1176775",
  "context_ids": [
    "arules_extractor_properties"
  ],
  "index_keywords": [
    "$index",
    "$itest_index",
    "$itest_value",
    "$value",
    "ExecutionDuration extractor",
    "None extractor",
    "analysis rules",
    "contains extractor",
    "extractor properties",
    "in analysis rules",
    "predefined",
    "predefined variable",
    "predefined variables",
    "query extractor",
    "regex extractor",
    "temporary data tag",
    "{assertion}",
    "{values}",
    "{value}"
  ],
  "index_keyword_paths": [
    "$index > predefined variables",
    "$itest_index > predefined variable",
    "$itest_value > predefined variables",
    "$value > predefined variable",
    "ExecutionDuration extractor",
    "Extract using property > in analysis rules",
    "None extractor",
    "analysis rules > extractor properties",
    "assertion > temporary data tag",
    "contains extractor",
    "extractor properties > analysis rules",
    "extractors > ExecutionDuration extractor",
    "extractors > None extractor",
    "extractors > contains extractor",
    "extractors > query extractor",
    "extractors > regex extractor",
    "predefined variables > $index",
    "predefined variables > $itest_index",
    "predefined variables > $itest_value",
    "predefined variables > $value",
    "query extractor",
    "regex extractor",
    "temporary data tag > {assertion}",
    "temporary data tag > {values}",
    "temporary data tag > {value}",
    "value > temporary data tag",
    "values > temporary data tag",
    "variables > predefined"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "6e5e6aff6cdf03db",
  "level": 2
}
---

# Analysis rules: Properties of the extractor > Analysis rules: Properties of the extractor > Contains extractor

The contains extractor returns the value 1 (True) if the specified string appears in the response and returns 0 (False) if the specified string does not appear in the response.

For Global rules, the Extract using cell displays contains.

For Global rules, the What to extract cell displays the text that is being searched on.

| Contains | Specify the alphanumeric text that you wish to find or not to find in the response text. |
| --- | --- |
| Match type | Specify how to interpret the text in the Contains property. Case-Insensitive: The case of the text in the response is not important. Case-Sensitive: The case of the text in the response is important. You must specify the exact text for the Contains property and then specify Wildcard. Regular expression: Interpret the text in the Contains property as a regular expression. Wildcard: This setting indicates that the text in the Contains property includes the * wildcard character. |
