---
{
  "chunk_id": "add_test_suite_wizard__creating_a_test_suite_the_test_suite_wiz_c1be7c3cd3699276",
  "source_file": "topics/add_test_suite_wizard.htm",
  "source_original_path": "topics/add_test_suite_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Suites",
    "Creating a test suite: The Test Suite wizard"
  ],
  "heading_path": [
    "Creating a test suite: The Test Suite wizard",
    "Creating a test suite: The Test Suite wizard"
  ],
  "anchor": "1303091",
  "context_ids": [
    "add_test_suite_wizard"
  ],
  "index_keywords": [
    "Test Suite wizard"
  ],
  "index_keyword_paths": [
    "Test Suite wizard"
  ],
  "related_links": [],
  "images": [
    "topics/images/test_suites_2.1.jpg"
  ],
  "content_hash": "c1be7c3cd3699276",
  "level": 1
}
---

# Creating a test suite: The Test Suite wizard > Creating a test suite: The Test Suite wizard

The Test Suite wizard helps you to quickly create a new test suite.

1. Create the test suite document: Click New and select Test Suite and then click Next.

1. 2

1. On the New Test Suite page of the Test Suite wizard, specify the following properties and then click OK.

| Container | Path to the new test suite file. Default: /my_project/test_suites |
| --- | --- |
| File name | Provide a name for the test suite that you are creating. This is the name that will appear in the Project Explorer and Favorites view. |

1. 3

1. On the Root Folder page, specify the following properties and then click OK.

| Group root folder | Browse to the folder that contains the tests that you want to include in the test suite. |
| --- | --- |
| Filter files based upon matching criteria | To add test cases to the suite on the basis of filename, check the box. On the next wizard page, you will specify a filename filter so that only the test cases in the Group root folder whose filenames match the filter you specify are added to the test suite, then click Next. For example, you might specify a filter Pattern of *regression* to add only tests with the text “regression” in the filename. To add test cases to the suite on a basis other than filename, do not check the box and then click Finish. Note If you choose not to check the box, but later want to apply a filter in defining a test group, you later can apply a filter in the Test Suite editor. The editor enables you to define other types of filters: File match (default): The Pattern is compared with the names of the files in the specified subfolder. Match with the filename. You can use the * wildcard character. Description match: Match text in the Description property string for the test case. Owner match: Match text in the Owner property string for the test case (typically, a person’s name). Parameter match: Specify a parameter setting Include or exclude test cases with a matching parameter setting. (for example, testType=stress). Parameter assertion: Specify a <paramName = value> assertion. Include or exclude test cases for which the assertion is true. |
| Note | If you choose not to check the box, but later want to apply a filter in defining a test group, you later can apply a filter in the Test Suite editor. The editor enables you to define other types of filters: |
|  | File match (default): The Pattern is compared with the names of the files in the specified subfolder. Match with the filename. You can use the * wildcard character. |
|  | Description match: Match text in the Description property string for the test case. |
|  | Owner match: Match text in the Owner property string for the test case (typically, a person’s name). |
|  | Parameter match: Specify a parameter setting Include or exclude test cases with a matching parameter setting. (for example, testType=stress). |
|  | Parameter assertion: Specify a <paramName = value> assertion. Include or exclude test cases for which the assertion is true. |

1. 4

1. If you checked the Filter files based upon matching criteria option, then the wizard opens the Configure Filter page. Specify the settings as described in the table and then click Finish.

> **Note:** Note All test cases starting with "_" (the _setup and _cleanup test cases) are excluded from the test case filtering process.

| Pattern | Type the text that should be used as the basis for filtering test cases. For example, you might specify a Pattern of *regression* to add only tests with the text “regression” in the filename. |
| --- | --- |
| Match type | Strict: The filename must exactly match the text specified for the Pattern. Regular Expression: Interpret the text specified for the Pattern as a regular expression when comparing the filename to the Pattern. Wildcard: (default) The filename must match the text specified for the Pattern. |
| On match | Take the specified action when a test case’s filename matches the pattern: Include: (default) Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| On no match | Take the specified action when a test case’s filename does not match the pattern: Include: Include the matching test in the group. Exclude: Exclude the matching test from the group. Do not change: (default) Do not include or exclude the test case. Instead, consider the test again when applying the next filter in the list of filters. |
| Root folder | Browse to the folder that contains the tests that the filter should be applied to. |
| Allow subfolders | Check the box to search subfolders when applying filters, Default: Checked |

The wizard saves the new test suite document (.ffts filename extension) and then opens it in the Test Suite editor.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/test_suites_2.1.jpg) <!-- image_chunk: img_f5913d5db7a32e60 -->
