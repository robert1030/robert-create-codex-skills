---
{
  "chunk_id": "tse_test_groups_page__type_parameter_assertion_619ce4296b862cfa",
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
    "Type: Parameter assertion"
  ],
  "anchor": "1207021",
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
  "related_links": [],
  "images": [],
  "content_hash": "619ce4296b862cfa",
  "level": 4
}
---

# Configuring a test group: The Test Group page > Configuring a test group: The Test Group page > Editing a test group > Type: Parameter assertion

| Query | Specify the query path to the parameter (its path in the parameter tree). The query returns the value in the $value variable for testing in the assertion that you specify in the Assertion property. |
| --- | --- |
| Assertion | Based on the value returned by the query that you specified in the Query property, specify an expression to evaluate. For example, the assertion $value == 42 tests whether the value returned by the query is equal to 42. |
| On no parameter | Take the specified action when a test case does not include the parameter specified for the Query property: Include: Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: (default) Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| On assertion true | Take the specified action when the filter returns True: Include: (default) Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| On assertion false | Take the specified action when the filter returns False: Include: Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: (default) Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |

1. 5

1. As mentioned earlier: In some cases, you might design the filters so that, after filtering is complete, you also want to include tests that lie outside the filters. In such a case, check After applying all filters, include the test cases that have not yet been included or excluded.

1. 6

1. Now, you will specify whether to execute setup and cleanup test cases.
