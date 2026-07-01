---
{
  "chunk_id": "action_details_view__viewing_the_latest_response_view_7eef8c3e4b97d92a",
  "source_file": "topics/action_details_view.htm",
  "source_original_path": "topics/action_details_view.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Response view"
  ],
  "heading_path": [
    "Response view",
    "Response view",
    "Viewing the latest response view"
  ],
  "anchor": "1588970",
  "context_ids": [
    "action_details_view"
  ],
  "index_keywords": [
    "Response view",
    "adding from Response view"
  ],
  "index_keyword_paths": [
    "Response view",
    "form maps > adding from Response view",
    "response maps > adding from Response view",
    "views > Response view"
  ],
  "related_links": [],
  "images": [
    "topics/images/response_view_preferences.png"
  ],
  "content_hash": "7eef8c3e4b97d92a",
  "level": 2
}
---

# Response view > Response view > Viewing the latest response view

iTest populates the response view from the most recent test report resulting from the test case execution.

For example, if you accidently run the QuickCall libraries and then run the test case that calls that QuickCall library, the QuickCall command step response of the test case displays empty with the probable causes. See below.

This is because iTest is reads from the most recent test report generated from the QuickCall library execution. To display the correct response from the Test Case execution, Righ-click and select the option to show the most recent response regardless of the test report name.

You may also delete the QuickCall test report, and then click on a step in the QuickCall library, the response view shows the expected response from the test case execution.

> **Note:** Note A QuickCall procedure with JSON Response, inserted in a Test Case populates the Response View with the JSON response from the called procedure and the Response View background is light grey before running a test case.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/response_view_preferences.png) <!-- image_chunk: img_67ea2992a7baae04 -->
