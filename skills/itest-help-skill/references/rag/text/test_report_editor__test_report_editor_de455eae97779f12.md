---
{
  "chunk_id": "test_report_editor__test_report_editor_de455eae97779f12",
  "source_file": "topics/test_report_editor.htm",
  "source_original_path": "topics/test_report_editor.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Test Report editor"
  ],
  "heading_path": [
    "Test Report editor",
    "Test Report editor"
  ],
  "anchor": "1174232",
  "context_ids": [
    "test_report_editor"
  ],
  "index_keywords": [
    "Go To Next Issue button",
    "Go To Previous Issue button",
    "Test Report editor",
    "child test case",
    "defined",
    "find issues in",
    "issues in test reports",
    "master test case",
    "test reports"
  ],
  "index_keyword_paths": [
    "Go To Next Issue button",
    "Go To Previous Issue button",
    "Indeterminate result > defined",
    "Test Report editor",
    "editors > Test Report editor",
    "find > issues in test reports",
    "issues > finding in test reports test reports > find issues in",
    "result > Indeterminate > defined",
    "test reports",
    "test reports > child test case",
    "test reports > master test case"
  ],
  "related_links": [
    "executing_tests_preferences_execution.htm#1155279",
    "test_report_setting_preferences.htm#1331474"
  ],
  "images": [
    "topics/images/test_reports.01.jpg"
  ],
  "content_hash": "de455eae97779f12",
  "level": 1
}
---

# Test Report editor > Test Report editor

By default, the Test Report editor displays the report as soon as execution ends. For older test reports, double-click the report in the Test Reports view to open the report in the Test Report editor.

In the report, the steps are organized into a hierarchy matching the procedures and steps that were executed. To make it easier for you to troubleshoot execution, the report looks very much like the Test case editor: a grid of steps and analysis rules with events occurring during execution nested under step row.

- While working on a test case in the Test Case editor, the fastest way to view a recent test report is to click in the toolbar. Click to open the most recent report in the Test Report editor. Click the arrow to display the list of the five most recent reports and then select a report to open it.

- The Test Report editor displays only executed steps, skipped steps are not included.

- You can click and to open and close procedures, QuickCalls, analysis rules, and nested step constructs in the report.

- To set a preference for displaying or not displaying test reports when execution ends, see Setting preferences for execution.

- You can specify a preference for how long to store test reports in Velocity iTest’s built-in database (that is, when to start discarding old reports). See Setting preferences for Test Reports.

- To make it easy to distinguish between a test report and its associated test case, the background color for test reports is blue by default. For instructions on configuring a different background color, see Setting preferences for Test Reports.

- To ensure best execution speed, Velocity iTest saves test report data only while the session is not actively communicating. As a result, there may be a delay in displaying the report after execution ends. You can specify the maximum wait. See Setting preferences for Test Reports.

![inline_icon](topics/images/test_reports.01.jpg) <!-- image_chunk: img_16b64640d7d8dfda -->
