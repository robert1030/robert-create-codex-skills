---
{
  "chunk_id": "tr_comparison_editor__working_in_the_test_report_comparison_ed_593927acb0618007",
  "source_file": "topics/tr_comparison_editor.htm",
  "source_original_path": "topics/tr_comparison_editor.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Comparing (“diffing”) two test reports"
  ],
  "heading_path": [
    "Comparing (“diffing”) two test reports",
    "Comparing (“diffing”) two test reports",
    "Working in the Test Report Comparison editor"
  ],
  "anchor": "1466854",
  "context_ids": [
    "tr_comparison_editor"
  ],
  "index_keywords": [
    "Go To Next Issue button",
    "Go To Previous Issue button",
    "Test Report Comparison",
    "Test Report Comparison editor",
    "comparing",
    "test reports"
  ],
  "index_keyword_paths": [
    "Go To Next Issue button",
    "Go To Previous Issue button",
    "Test Report Comparison editor",
    "comparing > test reports",
    "editors > Test Report Comparison",
    "test reports > comparing"
  ],
  "related_links": [
    "#1442912"
  ],
  "images": [
    "topics/images/test_reports_3.03.jpg"
  ],
  "content_hash": "593927acb0618007",
  "level": 2
}
---

# Comparing (“diffing”) two test reports > Comparing (“diffing”) two test reports > Working in the Test Report Comparison editor

The editor has the following pages:

- Comparison page:

- The Summary section displays identifying information about the two test reports. The older of the two reports is the “Reference” report and the newer report is the “Target”.

- The Executed Steps Comparison section displays a diff icon for steps that differ between the reference report and the target report. Steps can differ in the following ways:

- Text: If the step does not have a response map associated with it, then Velocity iTest compares the text of the response (for example, the target report includes a line that does not appear in the reference report).

- Query: If the step has a response map associated with it, then Velocity iTest compares the queries. This type of comparison is very helpful in identifying subtle differences between software releases (for example, it can ignore unimportant diffs like timestamp and focus only on items that are identified with a query in the response map). For details, see Examining queries for differences.

- Execution flow: If the two executions diverge (for example, an if step took the True path in the first execution and the False path in the second) then the comparison stops at the point of divergence.

- Response view: When you select a diff step, the Response view displays the reference response on the left and the target response on the right, separated by the | character. The Response view highlights the lines in the response that differ between the reference report and the target report.

- Queries view: When you select a diff step that has a response map associated with it, the Queries view identifies differences using the diff icon . For details, see Examining queries for differences.

- Execution view: The Execution view displays the list of differences marked by the diff icon . Double-click a difference to select the corresponding difference on the Comparison page of the Test Report Comparison editor.

- Reference page: Displays the standard test report for the reference execution of the test case

- Target page: Displays the standard test report for the target execution of the test case

![screenshot](topics/images/test_reports_3.03.jpg) <!-- image_chunk: img_feeb384c97440f68 -->
