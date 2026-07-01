---
{
  "chunk_id": "test_report_editor__columns_in_the_report_06eec91ef3efdce4",
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
    "Test Report editor",
    "Viewing test reports",
    "Columns in the report"
  ],
  "anchor": "1357116",
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
    "action_message.htm#1696651",
    "action_concept.htm#",
    "test_report_setting_preferences.htm#1331474"
  ],
  "images": [
    "topics/images/test_reports.24.jpg"
  ],
  "content_hash": "06eec91ef3efdce4",
  "level": 3
}
---

# Test Report editor > Test Report editor > Viewing test reports > Columns in the report

| Icon (execution issue) | Test reports display icons that represent execution issues that are generated during execution. Each issue can have an associated execution message. Hover over the icon to read the execution message associated with the execution issue. Execution issues and their associated execution messages appear in the Step Issues view and Execution view. Each message has a Severity associated as described below. Information OK (this severity is listed as “pass” in test reports that have been saved in HTML, PDF, Text, XML, and XML_RAW formats) Warning Error (this severity is listed as “fail” in test reports that have been saved in HTML, PDF, Text, XML, and XML_RAW formats) Some execution issues are built-in (for example, Execution started, Executions completed). Others are defined by the test case developer (for example, “Test command message”—see The ‘message’ action: Add a severity type and message type in “Actions”). |
| --- | --- |
| [first column] | Step index numbers appear in the first column. Notice that, due to changes to execution flow (for example, due to a loop), the numbers may differ from the Step ID numbers in the test case. You can set a preference to display or hide the index numbers. See Setting preferences for Test Reports. |
| Action | Specifies the action executed in the step. |
| Session | Identifies the session in which the step was executed. In procedures with more than one session, this will help you match the step to its session. |
| Description | The Description column identifies the action, analysis rule, or event and provides detailed information about the executed step, such as the command executed or the session profile used for an open step. |
| Step | Identifies the executed step by procedure name and step ID number using procedureName:stepNumber format. |
| Timestamp | Date and time of execution for the step. |
| Duration | Time for completion (including analysis) for the step. |
| Thread | Identifies the thread in which the step executed. |

![screenshot](topics/images/test_reports.24.jpg) <!-- image_chunk: img_d90e69cdb8acf85b -->
