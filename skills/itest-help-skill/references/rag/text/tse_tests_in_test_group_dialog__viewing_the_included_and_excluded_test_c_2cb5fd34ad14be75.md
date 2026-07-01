---
{
  "chunk_id": "tse_tests_in_test_group_dialog__viewing_the_included_and_excluded_test_c_2cb5fd34ad14be75",
  "source_file": "topics/tse_tests_in_test_group_dialog.htm",
  "source_original_path": "topics/tse_tests_in_test_group_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Suites",
    "Reviewing the tests that are members of a test suite or of a test group"
  ],
  "heading_path": [
    "Reviewing the tests that are members of a test suite or of a test group",
    "Reviewing the tests that are members of a test suite or of a test group",
    "Viewing the test cases in a test suite or test group",
    "Viewing the included and excluded test cases in a test group"
  ],
  "anchor": "1202344",
  "context_ids": [
    "tse_tests_in_test_group_dialog",
    "tse_tests_in_test_suite_dialog"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tse_test_groups_page.htm#1196514",
    "test_suites.3.htm#1303166",
    "tse_test_groups_page.htm#1304133"
  ],
  "images": [
    "topics/images/test_suites_4.2.jpg"
  ],
  "content_hash": "2cb5fd34ad14be75",
  "level": 3
}
---

# Reviewing the tests that are members of a test suite or of a test group > Reviewing the tests that are members of a test suite or of a test group > Viewing the test cases in a test suite or test group > Viewing the included and excluded test cases in a test group

On the Test Group page in the Test Suite editor, click Show Tests. The Tests in Test Group dialog box displays the list of all tests that will execute when the test group runs.

- On the Included Tests tab, member test cases appear in the order in which they will be executed. The order is determined by the Sorting setting that you made on the test group’s page in the Test Suite editor (as described in Sorting properties: Specify the order of execution).

- To display the setup and cleanup test cases in the list (also in execution order), check the Show setup/cleanup tests check box. You can specify two levels of setup/cleanup:

- Setup/cleanup before/after executing the test cases in a folder and/or before/after executing each test case. See Configuring setup and cleanup test cases for folders.

- Global setup and Global cleanup before/after executing all of the test cases in a group. See Global Setup / Cleanup properties).

- The Excluded Tests tab lists the tests in the root folder that were excluded from the group for the reason displayed in the Reason cell.

![screenshot](topics/images/test_suites_4.2.jpg) <!-- image_chunk: img_308c3989ce274b3c -->
