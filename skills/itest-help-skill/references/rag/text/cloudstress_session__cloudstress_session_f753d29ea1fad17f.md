---
{
  "chunk_id": "cloudstress_session__cloudstress_session_f753d29ea1fad17f",
  "source_file": "topics/cloudstress_session.htm",
  "source_original_path": "topics/cloudstress_session.htm",
  "toc_path": [
    "iTest Online Help",
    "CloudStress Session",
    "CloudStress Session"
  ],
  "heading_path": [
    "CloudStress Session",
    "CloudStress Session"
  ],
  "anchor": "1279396",
  "context_ids": [
    "cloudstress_session"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#"
  ],
  "images": [
    "topics/images/cloudstress_session.1.jpg",
    "topics/images/cloudstress_session.2.jpg",
    "topics/images/cs_queryBearerToken.png",
    "topics/images/cs_test_case_steps.png",
    "topics/images/cs_pencil_icon.png"
  ],
  "content_hash": "f753d29ea1fad17f",
  "level": 1
}
---

# CloudStress Session > CloudStress Session

In iTest, open a session, select CloudStress, and specify the required parameter values:

- URL: The CloudStress application VM URL, for example: http://cloudstress-app-1.spirent.com/api.

- Authentication: Leave blank—Temeva credentials are supplied using QueryBearerToken once the session is open.

All other settings can be left with their defaults, except for Proxy, which may be required if reaching Temeva and the CloudStress application via a proxy server.

> **Note:** Note The CloudStress session requires a license.

Click Start and the session window displays with session commands.

Choose the QueryBearerToken session command to authenticate to Temeva. Enter user credentials for the Temava account associated with the test, click Run, and verify that an access token is returned in the response window.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

Run a sequence of session commands to accomplish your tasks. For example, to run an existing test, the following sequence would follow:

- ListTests (to get the test id of the existing test)

- StartTest (invoking the test to run)

- GetTestStatus (to verify the test has started and ultimately stopped)

- GenerateReportDocumentByTestId (to download a test report in PDF, DOCX, or XLSX format)

- GetReport (to access specific report data elements in JSON format)

The input argument value in Step properties mirror the Steps Description column.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/cloudstress_session.1.jpg) <!-- image_chunk: img_27dbc483dd837b54 -->

![screenshot](topics/images/cloudstress_session.2.jpg) <!-- image_chunk: img_883313ef7db06884 -->

![screenshot](topics/images/cs_queryBearerToken.png) <!-- image_chunk: img_f743651d8082d731 -->

![screenshot](topics/images/cs_test_case_steps.png) <!-- image_chunk: img_afd246adc443e542 -->

![screenshot](topics/images/cs_pencil_icon.png) <!-- image_chunk: img_ac19581bc79ebf85 -->
