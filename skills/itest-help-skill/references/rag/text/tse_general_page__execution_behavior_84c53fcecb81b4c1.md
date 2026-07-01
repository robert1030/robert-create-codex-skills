---
{
  "chunk_id": "tse_general_page__execution_behavior_84c53fcecb81b4c1",
  "source_file": "topics/tse_general_page.htm",
  "source_original_path": "topics/tse_general_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Suites",
    "Configuring a test suite: The General page of the Test Suite editor"
  ],
  "heading_path": [
    "Configuring a test suite: The General page of the Test Suite editor",
    "Configuring a test suite: The General page of the Test Suite editor",
    "Execution Behavior"
  ],
  "anchor": "1199389",
  "context_ids": [
    "tse_general_page"
  ],
  "index_keywords": [
    "Test Suite editor",
    "defining"
  ],
  "index_keyword_paths": [
    "Test Suite editor",
    "editors > Test Suite editor",
    "test suites > defining"
  ],
  "related_links": [
    "test_suites.3.htm#1303166",
    "tse_test_groups_page.htm#1202096"
  ],
  "images": [
    "topics/images/test_suites.2.jpg"
  ],
  "content_hash": "84c53fcecb81b4c1",
  "level": 4
}
---

# Configuring a test suite: The General page of the Test Suite editor > Configuring a test suite: The General page of the Test Suite editor > Execution Behavior

| On setup test or cleanup test failure | Specify the action to take when any setup or cleanup test fails for any reason while the test suite is running. Stop the test suite: iTest aborts setup or cleanup test execution and stops running the suite. Stop the test group: iTest aborts setup or cleanup test execution and stops running the group. The next group in the suite then begins running. Continue: iTest aborts setup or cleanup test execution and executes the next test (either in the current group or in the next group — whichever test is next). Note You can make use of special setup and cleanup test cases for test suites. See Configuring setup and cleanup test cases for folders. | Note | You can make use of special setup and cleanup test cases for test suites. See Configuring setup and cleanup test cases for folders. |
| --- | --- | --- | --- |
| Note | You can make use of special setup and cleanup test cases for test suites. See Configuring setup and cleanup test cases for folders. |  |  |
| Estimated execution time | This estimate is for how long it will take for the suite to run is obtained by summing the estimated execution time for each test cases in the test suite. The value for each test case is taken from the Estimated execution time property as specified on the Test Case editor General page for the test case. |  |  |
| Impose execution time limit | Optional. To ensure that the test suite does not exceed a particular run time, check the box and specify the maximum time allowed for the suite to finish its run. If a test is executing when the limit is reached, then iTest aborts test execution and stops running the suite. The Test case result is set to Aborted. The default setting of 00:00 mans that there is no time limit. |  |  |
| Impose maximum test failures | Optional. Specify the number of test case failures that you will allow to occur. If the limit is exceeded, then iTest aborts test execution and stops running the suite. |  |  |
| Impose maximum contiguous test failures | Optional. Specify the number of test case failures that you will allow to occur in a row (that is, one after the other with no successful executions between). If the limit is exceeded, then iTest aborts test execution and stops running the suite. |  |  |
| Tests can be in multiple groups | Check the box to allow any test that passes a filter to become a member of any test group. As a result, a test case might execute multiple times per test suite run — one time in each test group in which it is a member. Uncheck the box (default) to ensure that a particular test case can be a member only of the first test group for which it passes a filter. As a result the test case will execute only once per test suite run. Note All test cases starting with "_" (the _setup and _cleanup test cases) are excluded from the test case filtering process. | Note | All test cases starting with "_" (the _setup and _cleanup test cases) are excluded from the test case filtering process. |
| Note | All test cases starting with "_" (the _setup and _cleanup test cases) are excluded from the test case filtering process. |  |  |

1. 3

1. You will now add as many test groups as are needed to define the test suite. Typically, you define a test group for each set of criteria that determine whether to execute or not execute a particular test case when the test suite runs. That is, you will define filters that determine which test cases from all specified folders should run.

To create a new test group and add it to the test suite, click Add . On the Test Group dialog box, supply a name for the test group and click OK. iTest adds the group to the Test Groups list.

1. 4

1. In the Test Groups list, double-click a group to configure its properties. We discuss adding and configuring a test group in Configuring a test group: The Test Group page.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/test_suites.2.jpg) <!-- image_chunk: img_5e1806dd1bc52fb7 -->
