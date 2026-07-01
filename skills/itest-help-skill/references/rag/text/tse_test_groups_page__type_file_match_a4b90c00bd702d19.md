---
{
  "chunk_id": "tse_test_groups_page__type_file_match_a4b90c00bd702d19",
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
    "Type: File match"
  ],
  "anchor": "1206637",
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
  "content_hash": "a4b90c00bd702d19",
  "level": 4
}
---

# Configuring a test group: The Test Group page > Configuring a test group: The Test Group page > Editing a test group > Type: File match

While you created the test suite document using the wizard, if you checked the Filter files based upon matching criteria option, then the values in this table are already filled in.

> **Note:** Note All test cases starting with “_” (the _setup and _cleanup test cases) are excluded from the test case filtering process.

| Pattern | Type the text that should be used as the basis for filtering test cases. For example, you might specify a Pattern of *regression* to add only tests with the text “regression” in the filename. |
| --- | --- |
| Match type | Wildcard: The filename must match the text specified for the Pattern property. Regular Expression: Interpret the text specified for the Pattern property as a regular expression when comparing the filename to the Pattern. Strict: The filename must exactly match the text specified for the Pattern property. |
| On match | Take the specified action when a test case’s filename matches the pattern: Include: (default) Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| On no match | Take the specified action when a test case’s filename does not match the pattern: Include: Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: (default) Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| Root folder | Browse to the folder that contains the tests that the filter should be applied to. |
| Allow subfolders | Check the box to search subfolders when applying filters. Default: Checked |
