# Test Reports > Test reports overview > Test Report editor > Viewing test reports > Selecting a row in the report

If the Response view is open, select a step to display its response. If the Response view is not open, double-click a step to view the response in the view.

On the Response tab/section, the default display format is auto-detected as Text, JSON, or YAML form.

![*](bullet_blue.jpg) <!-- image_ref -->

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

![*](bullet_blue.jpg) <!-- image_ref -->

- iTest automatically detects YAML syntax and format, if response was mapped as YAML.

Response view shows YAML response text (not formatted as pretty-print).

Click Text/JSON/YAML options from the dropdown list on the Response Window to toggle the response view display as JSON Pretty-Print or Text or YAML.

> **Note：** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

![](images/json_exec_report_view.png) <!-- image_ref -->

If a step used a field replacement, then the resulting substituted text appears in the report.

For run steps (that run child test cases), you can open the test report for the child test case: Right-click the run step and select Open Test Report.

> **Note：** Note The test report of a master test case is also generated and includes reports of each individual child/slave test cases within it.Whereas, reports generated for a test suite includes individual test case report and not the overall test suite report (unlike master test case report).
