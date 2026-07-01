---
{
  "chunk_id": "itestrt_commands__test_report_options_da152f85d5e72852",
  "source_file": "topics/itestrt_commands.htm",
  "source_original_path": "topics/itestrt_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "iTestRT command reference"
  ],
  "heading_path": [
    "iTestRT command reference",
    "iTestRT command reference",
    "Test Report options"
  ],
  "anchor": "1227693",
  "context_ids": [
    "itestrt_commands"
  ],
  "index_keywords": [
    "command reference",
    "iTestRT",
    "iTestRT command reference"
  ],
  "index_keyword_paths": [
    "command reference > iTestRT",
    "iTest Runtime > iTestRT command reference",
    "iTestRT > command reference"
  ],
  "related_links": [
    "json_preferences_pretty_print.htm#1335837",
    "json_editor_overview.htm#"
  ],
  "images": [],
  "content_hash": "da152f85d5e72852",
  "level": 2
}
---

# iTestRT command reference > iTestRT command reference > Test Report options

The report options enable you to control how test reports are generated. The long forms of option names begin with: com.fnfr.itest.testreport.optionModule

On the test report’s Response section, iTest displays response format as JSON or Text form (as auto-detected).

- If JSON syntax is detected, iTest displays text formatted as JSON pretty-print.

Only text indentation is applied (to HTML, HTML/JSON, PDF, and customized reports) and not the text color.

- If JSON format is not detected, the data will be displayed as TEXT and will interpret/present the data accordingly.

> **Note:** Note When iTest auto-detects JSON format, or select the JSON option to display the content, the pretty print format is assigned as per your settings (see Setting preferences for JSON Pretty Print in “JSON Editor”).

| --report URI | Generate test report at the specified URI. Note If a command includes multiple instances of the of the --report option, then only the last instance is used. The following substitutions are supported in the text of the URI: {tcfilename}, {datetime}, {date}, {time}, {tcpath} (test case path) {jobfilename}, {jobstart} Note You must append an appropriate file extension to the end of the replacement text, for example, {tcfilename}.html {tcfilename}.xml {tcfilename}.xml_raw {tcfilename}.txt The report format will be determined by the specified file extension and iTest supports 5 types of format: HTML, Text, XML, XML_Raw and PDF. The file extension supported is predefined in file extension.txt with appropriate text (html, xml, xml_raw, or txt) and located in test_report_templates/format_name/. If the extension appended does not match any predefined format, HTML format will be used, the file name with extension are kept as provided, and any existing XSLT stylesheet is applied. In addition, the test report may be compressed when publishing to the Quality Center server. Note For Microsoft Windows 7: You must run the CLI as “Administrator' to use the --report option to store the report in a folder. (If not, then an “Access Denied” error occurs) Example --report project://my_project/stressTests/{tcfilename}{datetime}.html Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> | Note | If a command includes multiple instances of the of the --report option, then only the last instance is used. | Note | You must append an appropriate file extension to the end of the replacement text, for example, {tcfilename}.html {tcfilename}.xml {tcfilename}.xml_raw {tcfilename}.txt | Note | For Microsoft Windows 7: You must run the CLI as “Administrator' to use the --report option to store the report in a folder. (If not, then an “Access Denied” error occurs) | Note | Use a single slash character after “file:” in the URI. For example: |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note | If a command includes multiple instances of the of the --report option, then only the last instance is used. |  |  |  |  |  |  |  |  |
| Note | You must append an appropriate file extension to the end of the replacement text, for example, {tcfilename}.html {tcfilename}.xml {tcfilename}.xml_raw {tcfilename}.txt |  |  |  |  |  |  |  |  |
| Note | For Microsoft Windows 7: You must run the CLI as “Administrator' to use the --report option to store the report in a folder. (If not, then an “Access Denied” error occurs) |  |  |  |  |  |  |  |  |
| Note | Use a single slash character after “file:” in the URI. For example: |  |  |  |  |  |  |  |  |
| --quiet | Suppress output from test report generation. Note Not used in conjunction with the --comparereports option. | Note | Not used in conjunction with the --comparereports option. |  |  |  |  |  |  |
| Note | Not used in conjunction with the --comparereports option. |  |  |  |  |  |  |  |  |
| --format URI | Specifies the templates to use to format HTML, PDF, TEXT, XML, or XML_RAW reports. If you use this option, then you do not need to export the resources project to an itar file. To use the option: 1. Copy the reportsXX/test_report_templates/<format_name> folder from your resources project into a local folder. 2. Specify the URI of the new folder using the --format option. Example Copy project://resources/reportsXX/test_report_templates/HTML to C:\templates\my_templates You may copy the custom templates and specifiy the URI during execution. 2. Now, when executing iTestrRT, use--format file:/C:/templates/my_templates Note Use a single slash character after “file:” in the URI. For example: file:/C:/Workspace/my_project/<folder>/<filename>.<extension> | 1. | Copy the reportsXX/test_report_templates/<format_name> folder from your resources project into a local folder. | 2. | Specify the URI of the new folder using the --format option. |  | Copy project://resources/reportsXX/test_report_templates/HTML to C:\templates\my_templates | 2. | Now, when executing iTestrRT, use--format file:/C:/templates/my_templates |
| 1. | Copy the reportsXX/test_report_templates/<format_name> folder from your resources project into a local folder. |  |  |  |  |  |  |  |  |
| 2. | Specify the URI of the new folder using the --format option. |  |  |  |  |  |  |  |  |
|  | Copy project://resources/reportsXX/test_report_templates/HTML to C:\templates\my_templates |  |  |  |  |  |  |  |  |
| 2. | Now, when executing iTestrRT, use--format file:/C:/templates/my_templates |  |  |  |  |  |  |  |  |
| Note | Use a single slash character after “file:” in the URI. For example: |  |  |  |  |  |  |  |  |
| --report URI ?format | Generate test report at the specified URI in the specified format. Example: --report file://C:/?XML_Raw The format output will be xml and the report name will be testcasename+time stamp.xml. --report file://C:/abc?XML_Raw The format output will be xml and the report name will be abc.testnumber.xml. Note The report format will be determined by the specified file extension and iTest supports 5 types of format: HTML, Text, XML, XML_Raw and PDF. The file extension supported is predefined in file extension.txt with appropriate text (html, xml, xml_raw, or txt) and located in test_report_templates/format_name/. If the extension appended does not match any predefined format, HTML format will be used, the file name with extension are kept as provided, and any existing XSLT stylesheet is applied. In addition, the test report may be compressed when publishing to the Quality Center server. iTestRT auto-detects JSON response data, and if the response is valid JSON, iTest formats the response as JSON prettiy print. Note The above applies to both test case and test suite. | Note |  | Note |  |  |  |  |  |
| Note |  |  |  |  |  |  |  |  |  |
| Note |  |  |  |  |  |  |  |  |  |
| --chartcolor <ChartColor> | Specify the color palette to be used to generate charts. if no chart color is specified, the color palette iTest is used by defaul. You can use the itestrt --help to list the available color pallette: Chart Color Options: --chartcolor <chartColor> Specify color for chart's series <iTest, Beach,Bermuda, Fall, gentleman, marine, Party, Playground, Vacation, Velocity> Example usage: --itar file://D://workspace/ChartColor/ --test project://my_project/test_cases/new_chart_testCase.fftc --licenseServer 100.100.10.1 --report file://D:/workspace/ChartColor/result --chartcolor iTest |  |  |  |  |  |  |  |  |
