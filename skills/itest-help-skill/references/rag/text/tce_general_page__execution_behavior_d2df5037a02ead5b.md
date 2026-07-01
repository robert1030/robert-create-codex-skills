---
{
  "chunk_id": "tce_general_page__execution_behavior_d2df5037a02ead5b",
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
    "Execution Behavior"
  ],
  "anchor": "1965477",
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
  "related_links": [
    "preferences.04.htm#1253281",
    "preferences_itest.htm#",
    "action_comment.htm#1654076"
  ],
  "images": [],
  "content_hash": "d2df5037a02ead5b",
  "level": 2
}
---

# Test Case editor: General page > Test Case editor: General page > Execution Behavior

| Language | Language: Select the language that will be used to create the session profile. You may use the default language displayed (as set in Preferences: Spirent > General > General preference settings, Chapter , “Configuring iTest Preferences”) or select a different language from the list. |
| --- | --- |
| Xpath version | Indicates the XPath version used. iTest uses XPath queries to extract data from the Test Case Steps responses. Default: 3.1 Option: 3.1, 1.0 (XPath 1.0 engine provides backward compatibility) |
| Entry point | The first procedure to execute when you execute the test case. Typically, main. All procedures defined in the test case are listed. |
| Generate an execution message for each comment step that is executed | Check the box to cause steps with an Action of comment to display execution messages in both the Execution view and test report. See The ‘comment’ action: Add a comment to a test case. Default: unchecked |
| Force all variables to be global | Warning This option is not recommended for new iTest test cases. It is intended for use with imported FanfareSVT test cases to ensure proper operation (all FanfareSVT variables are global). Check the box to cause all variables (local or global) to be treated as global. Warning When using this option, take care with procedure arguments, especially unnamed procedure arguments, as these will all appear in the same global namespace and can therefore cause problems with nested procedure calls. Default: unchecked |
| Warning |  |
| Warning |  |
| Discard session profile parameters when sessions close | Check the box to ensure that parameter values are removed from memory when the current session finishes. We strongly recommend that you leave the box checked. Default: checked |
| Execution time limit | Specify the time limit for the overall test case. iTest stops the test case if it exceeds the limit. hh:mm:ss format |
| Default step timeout | Specify the maximum time limit for any step in the test case. iTest stops the test case if it exceeds the limit. hh:mm:ss format |
| Estimated execution time | This value represents iTest's best estimate of how long it will take to execute the test case. The value is updated after each uninterrupted execution. The value is not updated when the test case is executed by an EXEC run step or a test suite. The value is used in two ways: On the Execution view during execution, to determine the progress on the Time remaining progress bar For use by test case scheduling applications You have the option to edit this value as needed. For a test case that has never been executed, the default value is 00:00:00. |
|  | On the Execution view during execution, to determine the progress on the Time remaining progress bar |
|  | For use by test case scheduling applications |
| Update “Estimated execution time” value after execution | Check the box to cause iTest to update the estimate when execution ends. The algorithm is (0.7*<current value>) + (0.3*<duration of latest execution>). The Estimated execution time value is not modified if: The user cancels execution The test case is executed by an EXEC run step or a test suite Test result is Fail or Abort Execution speed setting is not "fastest possible" Default: Checked |
|  | The user cancels execution |
|  | The test case is executed by an EXEC run step or a test suite |
|  | Test result is Fail or Abort |
|  | Execution speed setting is not "fastest possible" |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
