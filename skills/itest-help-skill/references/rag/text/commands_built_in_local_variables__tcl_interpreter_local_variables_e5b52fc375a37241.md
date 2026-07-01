---
{
  "chunk_id": "commands_built_in_local_variables__tcl_interpreter_local_variables_e5b52fc375a37241",
  "source_file": "topics/commands_built_in_local_variables.htm",
  "source_original_path": "topics/commands_built_in_local_variables.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "Tcl interpreter local variables"
  ],
  "heading_path": [
    "Tcl interpreter local variables",
    "Tcl interpreter local variables"
  ],
  "anchor": "1705062",
  "context_ids": [
    "commands_built_in_local_variables"
  ],
  "index_keywords": [
    "built-in local",
    "built-in variables"
  ],
  "index_keyword_paths": [
    "iTest interpreter > built-in variables",
    "variables > built-in local"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "e5b52fc375a37241",
  "level": 1
}
---

# Tcl interpreter local variables > Tcl interpreter local variables

- $value is a iTest interpreter variable that stores the data that is returned by the extractor. $value is created in the heap.

- For the contains extractor (string comparisons), $value is either 1 (True, the string matches) or 0 (zero, False)

- For the regex extractor, $value is the extracted value

- For the queries extractor, $value is the result of the query

$itest_value is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_value is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_value can be overwritten by another thread.

> **Note:** Note To make use of $itest_value, you must have executed a scriptEval step at least once in the test case.

- $index is a iTest interpreter variable. When the extractor extracts multiple items and the processor is invoked for each item, then $index holds the index of each value. For example, use a value's index to chart each extracted value on a separate line or series.

$itest_index is a Tcl interpreter variable that stores the data that is extracted by the extractor. $itest_index is not thread safe. Because only one instance of the Tcl interpreter is used, if you use an analysis rule in asynchronous steps, then $itest_index can be overwritten by another thread.

> **Note:** Note To make use of $itest_index, you must have executed a scriptEval step at least once in the test case.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
