---
{
  "chunk_id": "action_details_view__response_view_8112d64e3ede9f79",
  "source_file": "topics/action_details_view.htm",
  "source_original_path": "topics/action_details_view.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Response view"
  ],
  "heading_path": [
    "Response view",
    "Response view"
  ],
  "anchor": "1261910",
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
  "related_links": [
    "return_value_dialog.htm#1292200",
    "procedures_overview.htm#",
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#"
  ],
  "images": [
    "topics/images/views.01.jpg"
  ],
  "content_hash": "8112d64e3ede9f79",
  "level": 1
}
---

# Response view > Response view

The Response view displays the command and response for the currently selected captured item or test case step. For test case steps, the text is the response received for the step, when it (step) ran in the most recent execution of the test case. (You can select captured items in the Capture view or Capture Report editor. You can select test case steps in the Test Case editor or Test Report editor.)

For the test case, if the JSON response is configured (Procedure Properties > Inputs and Outputs > Response), then the response is available immediately in the Response view and the background is light grey (before running a test case).

Whenever sample JSON response is inserted into the response view (in case no response history exists in the database) the Queries and Structure views are also populated with contents for the response.

For example, in the screen shot below, the response view has been populated with sample JSON (colored grey background) and also populates the response content in Queries and Structure views.

The purpose of the Response View is to make it easier to add analysis rules for test cases. See also Defining a procedure in “Procedures”.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

The Response view makes it easy to review responses and to copy part or all of a response for pasting into other documents. You will also use the Response view while creating analysis rules and while creating and working with response maps and form maps.

![screenshot](topics/images/views.01.jpg) <!-- image_chunk: img_ee47f3e7f547305d -->
