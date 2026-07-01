---
{
  "chunk_id": "tse_test_groups_page__type_owner_match_56fdd37c6928ec29",
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
    "Type: Owner match"
  ],
  "anchor": "1206974",
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
  "content_hash": "56fdd37c6928ec29",
  "level": 4
}
---

# Configuring a test group: The Test Group page > Configuring a test group: The Test Group page > Editing a test group > Type: Owner match

| Pattern | Type the text that should be used as the basis for filtering test cases. For example, you might specify a Pattern of *Yujie* (with a Match type of Wildcard) to add only tests with the text “Yujie” in the Owner property text string. |
| --- | --- |
| Match type | Wildcard: The Description property text string must match the text specified for the Pattern property. Regular Expression: Interpret the text specified for the Pattern property as a regular expression when comparing the Owner property text string to the Pattern. Strict: The Owner property text string must exactly match the text specified for the Pattern property. |
| On match | Take the specified action when a test case’s Owner property text string matches the pattern: Include: (default) Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| On no match | Take the specified action when a test case’s Owner property text string does not match the pattern: Include: Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: (default) Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
