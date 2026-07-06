# CyberFlood Session > Creating CyberFlood Session Profile in iTest > 第1段

> **Note：** Note The CyberFlood session requires a license.

In iTest, open a session, select CyberFlood, and specify the required parameter values:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- URL: The CloudStress application URL, for example: https://ac-cf-controller.spirenteng.com/api/V2/

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Authentication: Leave blank.

All other settings can be left with their defaults.

![](images/cyberFlood_session.1.jpg) <!-- image_ref -->

Click Start and the session window displays with session commands.

![](images/cf_session_commandsList.png) <!-- image_ref -->

Choose the Authentication session command to authenticate to CyberFlood. Enter email and password for CyberFlood account associated with the test, click Run, and verify that an access token is returned in the response window.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

![*](bullet_blue.jpg) <!-- image_ref -->

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

![*](bullet_blue.jpg) <!-- image_ref -->

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note：** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

.

![](images/cf_session_commands.png) <!-- image_ref -->

Run a sequence of session commands to accomplish your tasks. For example, to run an existing test, the following sequence would follow:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- ListTests (to get the test id of the existing test)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- StartTest (invoking the test to run)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- ListHttpOpenConnectionsTests (to verify number of open HTTP connections)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- ListHttpConnectionsPerSecondTests (to verify HTTP connections)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->
