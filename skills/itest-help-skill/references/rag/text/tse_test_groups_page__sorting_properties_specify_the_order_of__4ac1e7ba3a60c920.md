---
{
  "chunk_id": "tse_test_groups_page__sorting_properties_specify_the_order_of__4ac1e7ba3a60c920",
  "source_file": "topics/tse_test_groups_page.htm",
  "source_original_path": "topics/tse_test_groups_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Suites",
    "Configuring a test group: The Test Group page"
  ],
  "heading_path": [
    "Configuring a test group: The Test Group page",
    "Configuring a test group: The Test Group page",
    "Editing a test group",
    "Sorting properties: Specify the order of execution"
  ],
  "anchor": "1196514",
  "context_ids": [
    "tse_test_groups_page"
  ],
  "index_keywords": [
    "Test Group page",
    "configuring",
    "configuring for test group",
    "execution order"
  ],
  "index_keyword_paths": [
    "Description match > configuring for test group",
    "File match > configuring for test group",
    "Owner match > configuring for test group",
    "Parameter assertion > configuring for test group",
    "Parameter match > configuring for test group",
    "Test Group page",
    "test groups > configuring",
    "test groups > execution order",
    "test suites > configuring",
    "test suites > execution order"
  ],
  "related_links": [
    "test_suites.3.htm#1303166"
  ],
  "images": [],
  "content_hash": "4ac1e7ba3a60c920",
  "level": 3
}
---

# Configuring a test group: The Test Group page > Configuring a test group: The Test Group page > Editing a test group > Sorting properties: Specify the order of execution

Specify one of the following methods of determining the order in which the test cases should execute:

| Sort by directory tree position | Order the test cases for execution in the order they are listed in the root folder. If you specify this sorting option, then you can further specify whether to run setup or cleanup test cases, as follows: |
| --- | --- |
| These options are applied only when you select Sort by directory tree position | Run setup/cleanup tests per folder |
| Run setup/cleanup tests per test | Check the box to execute the _setup_each and _cleanup_each test cases for each test case that is included in the test group. See Configuring setup and cleanup test cases for folders. Default: Checked |
| Sort by test case parameter value | Order the test cases for execution in the order of the value returned for the specified parameter. |
|  | Parameter query |
|  | Sort order |
| Sort randomly | Order the test cases for execution in random order. |
|  | Use a random generator seed |
