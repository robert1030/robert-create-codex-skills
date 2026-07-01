---
{
  "chunk_id": "sb_using_new_cs_type__using_extended_custom_session_5354d0fc39d04b3f",
  "source_file": "topics/sb_using_new_cs_type.htm",
  "source_original_path": "topics/sb_using_new_cs_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "Using the new custom session type"
  ],
  "heading_path": [
    "Using the new custom session type",
    "Using the new custom session type",
    "Using extended custom session"
  ],
  "anchor": "1341589",
  "context_ids": [
    "sb_using_new_cs_type"
  ],
  "index_keywords": [
    "using console based custom session type",
    "using new custom session type"
  ],
  "index_keyword_paths": [
    "session builder > using console based custom session type",
    "session builder > using new custom session type"
  ],
  "related_links": [
    "sb_creating_a_cs_type.htm#1381030",
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#",
    "sb_verify_cs_type.htm#1334595"
  ],
  "images": [
    "topics/images/03-open-custom-sessiontype.png",
    "topics/images/03-a-start-custom-session-Extends.png",
    "topics/images/04-customize-session-commands.png",
    "topics/images/04-customize-session-commands-text.png",
    "topics/images/06-execute-test-case.png"
  ],
  "content_hash": "5354d0fc39d04b3f",
  "level": 2
}
---

# Using the new custom session type > Using the new custom session type > Using extended custom session

These steps describe opening the new custom session you built (Building a new Session type), executing the session and customizing the session commands.

Step 1

Create a new session profile

Create a new session profile, notice that the new session type listed (e.g., Custom_session).

Save and Start session

Click Method: POST (for example) to display the native commands. Select the required command and execute the base/native command (click the Green arrow).

On the top of the window a Session Command button appears. Click the down-arrow to view the list of commands and click Session Command to open the Customize Sessions Command window.

Filter the list and get to the required command (e.g., queryToken). Enter the details and click Run.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

> **Note:** Note You may also fill in the parameters or enter the Command Text.

Click Restore Defaults to restore to the default values of command properties.

The illustration below shows execution (when you click Run) of the customized queryToken command and it’s response.

Important The customized command parameters gets saved automatically when they are run.

Executed Session Commands

All session commands executed, are captured in the Capture View as illustrated. You execute/replay these capture commands.

See also topic Verify the customized session type to see how the custom session type are used.

![screenshot](topics/images/03-open-custom-sessiontype.png) <!-- image_chunk: img_088f4cde07287548 -->

![screenshot](topics/images/03-a-start-custom-session-Extends.png) <!-- image_chunk: img_f96f1eccbcf9d830 -->

![screenshot](topics/images/04-customize-session-commands.png) <!-- image_chunk: img_a237383c5c4d9137 -->

![screenshot](topics/images/04-customize-session-commands-text.png) <!-- image_chunk: img_79fd69226af11795 -->

![screenshot](topics/images/06-execute-test-case.png) <!-- image_chunk: img_a7c3430b0c152df1 -->
