---
{
  "chunk_id": "tce_general_page__test_suite_reporting_5bc92ec2b97f5cf3",
  "source_file": "topics/tce_general_page.htm",
  "source_original_path": "topics/tce_general_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "General page on the Test Case Editor",
    "Test Case editor: General page"
  ],
  "heading_path": [
    "Test Case editor: General page",
    "Test Case editor: General page",
    "Test Suite Reporting"
  ],
  "anchor": "1962983",
  "context_ids": [
    "tce_general_page"
  ],
  "index_keywords": [
    "General page",
    "Test Case editor",
    "messaging out",
    "run command responses",
    "specifying",
    "summary reports",
    "summary responses",
    "test suites"
  ],
  "index_keyword_paths": [
    "General page > Test Case editor",
    "Test Case editor > General page",
    "comments > messaging out",
    "run command responses",
    "summary reports",
    "summary responses",
    "test suites",
    "testbeds > specifying"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "5bc92ec2b97f5cf3",
  "level": 2
}
---

# Test Case editor: General page > Test Case editor: General page > Test Suite Reporting

This group of properties configures reporting for test cases that are parent test cases that execute child test cases using EXEC.run steps. A test case that is made up of only run steps is called a test suite.

Because the default settings result in normal reporting for test cases that are not test suites, you do not have to change any of these settings for test cases that do not run other test cases. By default, the response to an EXEC summarize step includes the results only of the individual child test cases but not the test suites that executed them. This avoids double-counting of successes or failures.

You can specify the following reporting settings:

| Include test cases executed by this test case (via EXEC run) | If this test case runs child test cases (it contains one or more EXEC run steps), you might want either to suppress reporting on the results of the children or to include each child's results in EXEC summarize steps. Check the box to include the results of child test cases in the response to summarize steps. Uncheck the box to not include the results of child test cases in the response to summarize steps. Default: Checked |
| --- | --- |
| Include this test case in response to summarize steps | This setting applies if this test case will execute as a child test case. Specify whether to or not to display the results of this test case in the response to a summarize step in its parent test case. Yes: Display the results of this test case in the response to a summarize step No: Do not display the results of this test case in the response to a summarize step Auto: If this test case does not run child test cases (it contains no EXEC run steps), then display the results of this test case If this test case runs child test cases (it contains one or more EXEC run steps), then do not display the results of this test case For the Auto setting, the response to a summarize step will include the results only of children and not of the intermediate parent test cases (this avoids double reporting). Default: Auto |
|  | If this test case does not run child test cases (it contains no EXEC run steps), then display the results of this test case |
|  | If this test case runs child test cases (it contains one or more EXEC run steps), then do not display the results of this test case |
| Include execution issues in response to summarize steps | This setting applies if this test case will execute as a child test case. Specify whether or not to display execution messages for this test case in the response to a summarize step in its parent test case. Yes: Display execution messages for this test case in the response to a summarize step. No: Do not display execution messages for this test case in the responses to a summarize step. Auto: If this test case does not execute child test cases (it contains no EXEC run steps), then include this test case's execution messages If this test case has one or more child test cases (it contains one or more EXEC run steps), then do not include this test case's execution messages. For the Auto setting, the response to a summarize step will show only a list of the child tests and their results, and not the intermediate parent test cases and results (this avoids double reporting). Default: Auto |
|  | If this test case does not execute child test cases (it contains no EXEC run steps), then include this test case's execution messages |
|  | If this test case has one or more child test cases (it contains one or more EXEC run steps), then do not include this test case's execution messages. |
