---
{
  "chunk_id": "tse_test_groups_page__editing_a_test_group_244a027b7a341f35",
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
    "Editing a test group"
  ],
  "anchor": "1197167",
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
    "#1206212"
  ],
  "images": [],
  "content_hash": "244a027b7a341f35",
  "level": 2
}
---

# Configuring a test group: The Test Group page > Configuring a test group: The Test Group page > Editing a test group

1. You got to this page by double-clicking the test group in the Test Groups list on the General page of the Test Suite editor.

1. 2

1. Specify the Group root folder — the folder that includes the test cases that should be in the test group (depending on the filters you design, some test cases in the folder will not be included in the group).

> **Note:** Note While creating the test suite document using the wizard, if you checked the Filter files based upon matching criteria option, then this value is filled in.

1. 3

1. In the Selection Filters section, click Add to add a filter and then specify the following properties for the new filter:

| Name | Specify a meaningful name for the filter. For example, deleteLogMsgs or includeOnlyPortStatus |
| --- | --- |
| Type | While you created the test suite document using the wizard, if you checked the Filter files based upon matching criteria option, then the Type is set to File match, and you can continue at Step 4. Specify how to interpret the pattern that you specify for the Pattern property: File match (default): The Pattern is compared with the names of the files in the folder. Match with the filename. You can use the * wildcard character. Note All test cases starting with "_" (the _setup and _cleanup test cases) are excluded from the test case filtering process. Description match: Match text in the Description property string for the test case. Owner match: Match text in the Owner property string for the test case (typically, a person’s name). Parameter match: Specify a parameter setting Include or exclude test cases with a matching parameter setting. (for example, testType=stress). Parameter assertion: Specify a <paramName = value> assertion. Include or exclude test cases for which the assertion is true. |
|  | File match (default): The Pattern is compared with the names of the files in the folder. Match with the filename. You can use the * wildcard character. |
| Note | All test cases starting with "_" (the _setup and _cleanup test cases) are excluded from the test case filtering process. |
|  | Description match: Match text in the Description property string for the test case. |
|  | Owner match: Match text in the Owner property string for the test case (typically, a person’s name). |
|  | Parameter match: Specify a parameter setting Include or exclude test cases with a matching parameter setting. (for example, testType=stress). |
|  | Parameter assertion: Specify a <paramName = value> assertion. Include or exclude test cases for which the assertion is true. |
