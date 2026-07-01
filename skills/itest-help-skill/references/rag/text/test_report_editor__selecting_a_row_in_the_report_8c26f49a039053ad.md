---
{
  "chunk_id": "test_report_editor__selecting_a_row_in_the_report_8c26f49a039053ad",
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
    "Selecting a row in the report"
  ],
  "anchor": "1172061",
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
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#"
  ],
  "images": [
    "topics/images/json_exec_report_view.png"
  ],
  "content_hash": "8c26f49a039053ad",
  "level": 3
}
---

# Test Report editor > Test Report editor > Viewing test reports > Selecting a row in the report

If the Response view is open, select a step to display its response. If the Response view is not open, double-click a step to view the response in the view.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

If a step used a field replacement, then the resulting substituted text appears in the report.

For run steps (that run child test cases), you can open the test report for the child test case: Right-click the run step and select Open Test Report.

> **Note:** Note The test report of a master test case is also generated and includes reports of each individual child/slave test cases within it.Whereas, reports generated for a test suite includes individual test case report and not the overall test suite report (unlike master test case report).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/json_exec_report_view.png) <!-- image_chunk: img_7892477c1000c4f7 -->
