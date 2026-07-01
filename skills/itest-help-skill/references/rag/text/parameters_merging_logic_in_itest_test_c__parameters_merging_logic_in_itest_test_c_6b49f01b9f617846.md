---
{
  "chunk_id": "parameters_merging_logic_in_itest_test_c__parameters_merging_logic_in_itest_test_c_6b49f01b9f617846",
  "source_file": "topics/parameters_merging_logic_in_itest_test_cases.htm",
  "source_original_path": "topics/parameters_merging_logic_in_itest_test_cases.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Defining and managing parameters",
    "Parameters merging logic in iTest test cases"
  ],
  "heading_path": [
    "Parameters merging logic in iTest test cases",
    "Parameters merging logic in iTest test cases"
  ],
  "anchor": "1627730",
  "context_ids": [
    "parameters_merging_logic_in_itest_test_cases"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "6b49f01b9f617846",
  "level": 1
}
---

# Parameters merging logic in iTest test cases > Parameters merging logic in iTest test cases

The following examples describe the parameters merging logic in iTest test cases:

1. If global parameter file has a parameter param1 with integer value, and test case defines a parameter with the same name, param1 with a string value, the integer value from the global parameter file takes precedence.

1. 2

1. If a source (e.g., testcase1.fftc) defines a parent parameter with child parameter, and a second source (e.g., testcase2.fftc) defines only a parent parameter with the same name, and if you wish to get the value of the parent, the merge results in the value of the child parameter. This is because a parent parameter cannot define values.

1. 3

1. When you call a procedure from a child test case defining its own parameters, from within a parent test case, the parameters from the child test are loaded to the heap memory of the parent test. That is, the children test case parameters remain accumulated in the heap memory.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
