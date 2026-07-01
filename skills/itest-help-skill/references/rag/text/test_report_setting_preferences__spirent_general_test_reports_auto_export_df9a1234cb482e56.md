---
{
  "chunk_id": "test_report_setting_preferences__spirent_general_test_reports_auto_export_df9a1234cb482e56",
  "source_file": "topics/test_report_setting_preferences.htm",
  "source_original_path": "topics/test_report_setting_preferences.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Setting preferences for Test Reports"
  ],
  "heading_path": [
    "Setting preferences for Test Reports",
    "Setting preferences for Test Reports",
    "Spirent > General > Test Reports > Auto-Export Test Reports"
  ],
  "anchor": "1389653",
  "context_ids": [
    "test_report_setting_preferences"
  ],
  "index_keywords": [
    "preference settings",
    "test reports"
  ],
  "index_keyword_paths": [
    "preference settings > test reports",
    "test reports > preference settings"
  ],
  "related_links": [
    "test_report_uses.htm#1391270",
    "test_resport_itest_report_file_formats.htm#1184368",
    "#998406"
  ],
  "images": [
    "topics/images/test_reports_8.1.jpg"
  ],
  "content_hash": "df9a1234cb482e56",
  "level": 2
}
---

# Setting preferences for Test Reports > Setting preferences for Test Reports > Spirent > General > Test Reports > Auto-Export Test Reports

| Export test reports after execution | Select option to ensure that iTest generates a test report document after each test execution. One report is generated for each execution. Report files are named with the test case name and a timestamp. You specify the format of the report documents (HTML, PDF, Text, XML, and/or XML_RAW) using the Formats to generate property. You specify the location to save reports using the Folder for test reports property If not selected, iTest does not automatically generate report documents. Note All other options on this window are grayed and not available for selection In either case, you can manually save any test report as a file as described in Uses for test reports. |  | One report is generated for each execution. |  | Report files are named with the test case name and a timestamp. |  | You specify the format of the report documents (HTML, PDF, Text, XML, and/or XML_RAW) using the Formats to generate property. |  | You specify the location to save reports using the Folder for test reports property | Note | All other options on this window are grayed and not available for selection |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | One report is generated for each execution. |  |  |  |  |  |  |  |  |  |  |
|  | Report files are named with the test case name and a timestamp. |  |  |  |  |  |  |  |  |  |  |
|  | You specify the format of the report documents (HTML, PDF, Text, XML, and/or XML_RAW) using the Formats to generate property. |  |  |  |  |  |  |  |  |  |  |
|  | You specify the location to save reports using the Folder for test reports property |  |  |  |  |  |  |  |  |  |  |
| Note | All other options on this window are grayed and not available for selection |  |  |  |  |  |  |  |  |  |  |
| Export test reports for test cases executed in 'run' steps | Check the box to include test report data for any test case that is executed as the result of a run step in the parent test case. |  |  |  |  |  |  |  |  |  |  |
| Formats to generate | If you checked Export test reports after execution, then specify each document format to generate. You can specify any or all formats (HTML, PDF, Text, XML, XML_RAW). For format information, see Test report file formats. |  |  |  |  |  |  |  |  |  |  |
| Folder for test reports | Specify a directory/path to automatically save the test reports for each testcase. The default folder for test report documents is: project://{project} You may use the following path variables in different combination to define relative or absolute path for automatically exporting and saving the execution reports. Note Path variables are case sensitive. If you include a variable other than the ones lists below, an error displays. Variable {project}: returns the project name Variable {path_in_project}: returns only the testcase path in project (without the project name and the testcase name) Variable {testcase}: returns the testcase name Variable {date}: returns the current day (yyyy-mm-dd) Example 1: Folder for test reports: /home/user/reports/{project}/{date}/ After executing a single test Testcase-01.fftc of projectB iTest saves the report in the specified location as follows: /home/user/reports/projectB/yyyy-MM-dd/B/B_<datetime>.html Example 2a: Executing a master testcase which runs child testcases (Nested TestCases). Folder for test reports: /home/user/reports/ All reports will be saved in: export path + master folder + report name Testcase A.fftc runs B.fftc iTest saves the report in the specified location as follows: Master Report: /home/user/reports/A/A_<datetime>.html Child Report: /home/user/reports/A/B_<datetime>.html Example 2b: Executing a master testcase which runs child testcases (Nested TestCases). Folder for test reports: /home/user/reports/{project}/{date}/ Master report will be saved in: export path(replaced path variables) + master folder + report name Child reports will be saved in: export path(replaced path variables) + master folder + child folder + report name Testcase A.fftc runs B.fftc iTest saves the report in the specified location as follows: Master Report: /home/user/reports/projectA/yyyy-MM-dd/A/A_<datetime>.html Child Reports: /home/user/reports/projectB/yyyy-MM-dd/A/B/B_<datetime>.html See Examples of the iTest GUI and iTestRT scenarios with Project schema and Absolute path:. | Note | Path variables are case sensitive. If you include a variable other than the ones lists below, an error displays. |  | Variable {project}: returns the project name |  | Variable {path_in_project}: returns only the testcase path in project (without the project name and the testcase name) |  | Variable {testcase}: returns the testcase name |  | Variable {date}: returns the current day (yyyy-mm-dd) |
| Note | Path variables are case sensitive. If you include a variable other than the ones lists below, an error displays. |  |  |  |  |  |  |  |  |  |  |
|  | Variable {project}: returns the project name |  |  |  |  |  |  |  |  |  |  |
|  | Variable {path_in_project}: returns only the testcase path in project (without the project name and the testcase name) |  |  |  |  |  |  |  |  |  |  |
|  | Variable {testcase}: returns the testcase name |  |  |  |  |  |  |  |  |  |  |
|  | Variable {date}: returns the current day (yyyy-mm-dd) |  |  |  |  |  |  |  |  |  |  |
|  | Master Report: /home/user/reports/A/A_<datetime>.html |  |  |  |  |  |  |  |  |  |  |
|  | Child Report: /home/user/reports/A/B_<datetime>.html |  |  |  |  |  |  |  |  |  |  |
|  | Test reports for session types that use browsers (Swing and Web) can include thumbnail images of screen snapshots. When the user clicks a thumbnail, the full-size image appears. The full-size image files for reports are saved into the <report subdirectory>/<test_case_name>/<test_case_name>_<timestamt>_images subdirectory. In this example, we executed the test case named web on two different dates, we specified HTML and XML format reports, the test case includes steps that generated snapshot images, and we used the default subfolder names: |  |  |  |  |  |  |  |  |  |  |

![screenshot](topics/images/test_reports_8.1.jpg) <!-- image_chunk: img_6d0403c49200fd00 -->
