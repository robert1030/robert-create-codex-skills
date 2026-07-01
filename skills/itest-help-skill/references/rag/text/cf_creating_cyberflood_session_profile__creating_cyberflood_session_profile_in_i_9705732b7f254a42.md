---
{
  "chunk_id": "cf_creating_cyberflood_session_profile__creating_cyberflood_session_profile_in_i_9705732b7f254a42",
  "source_file": "topics/cf_creating_cyberflood_session_profile.htm",
  "source_original_path": "topics/cf_creating_cyberflood_session_profile.htm",
  "toc_path": [
    "iTest Online Help",
    "CyberFlood Session",
    "Creating CyberFlood Session Profile in iTest"
  ],
  "heading_path": [
    "Creating CyberFlood Session Profile in iTest",
    "Creating CyberFlood Session Profile in iTest"
  ],
  "anchor": "1279396",
  "context_ids": [
    "cf_creating_cyberflood_session_profile"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#"
  ],
  "images": [
    "topics/images/cyberFlood_session.1.jpg",
    "topics/images/cf_session_commandsList.png",
    "topics/images/cf_session_commands.png"
  ],
  "content_hash": "9705732b7f254a42",
  "level": 1
}
---

# Creating CyberFlood Session Profile in iTest > Creating CyberFlood Session Profile in iTest

> **Note:** Note The CyberFlood session requires a license.

In iTest, open a session, select CyberFlood, and specify the required parameter values:

- URL: The CloudStress application URL, for example: https://ac-cf-controller.spirenteng.com/api/V2/

- Authentication: Leave blank.

All other settings can be left with their defaults.

Click Start and the session window displays with session commands.

Choose the Authentication session command to authenticate to CyberFlood. Enter email and password for CyberFlood account associated with the test, click Run, and verify that an access token is returned in the response window.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

.

Run a sequence of session commands to accomplish your tasks. For example, to run an existing test, the following sequence would follow:

- ListTests (to get the test id of the existing test)

- StartTest (invoking the test to run)

- ListHttpOpenConnectionsTests (to verify number of open HTTP connections)

- ListHttpConnectionsPerSecondTests (to verify HTTP connections)

- GetTestResult (to verify the test has started and ultimately stopped)

![screenshot](topics/images/cyberFlood_session.1.jpg) <!-- image_chunk: img_0cc8af88a160271d -->

![screenshot](topics/images/cf_session_commandsList.png) <!-- image_chunk: img_d692fcff7d520b70 -->

![screenshot](topics/images/cf_session_commands.png) <!-- image_chunk: img_815473c86ebce2f0 -->
