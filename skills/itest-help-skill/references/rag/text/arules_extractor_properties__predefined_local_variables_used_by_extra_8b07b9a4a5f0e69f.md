---
{
  "chunk_id": "arules_extractor_properties__predefined_local_variables_used_by_extra_8b07b9a4a5f0e69f",
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
    "Predefined local variables used by extractors"
  ],
  "anchor": "1176761",
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
  "content_hash": "8b07b9a4a5f0e69f",
  "level": 2
}
---

# Analysis rules: Properties of the extractor > Analysis rules: Properties of the extractor > Predefined local variables used by extractors

iTest populates predefined local variables while processing an analysis rule:

- $value is an iTest interpreter variable that stores the data that is extracted by the extractor. $value is created in the heap.

- For the contains extractor (string comparisons), $value is either 1 (True, the string matches) or 0 (zero, False)

- For the regex extractor, $value is the extracted value

- For the queries extractor, $value is the result of the query

- $itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_value is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_value can be overwritten by another thread.

- $index is an iTest interpreter variable. When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, you would use a value's index to chart each extracted value on a separate line or series.

- $itest_index is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_index is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_index can be overwritten by another thread.
