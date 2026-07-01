---
{
  "chunk_id": "export_document_wizard__export_test_case_to_robot_library_d52a90a8f43be65d",
  "source_file": "topics/export_document_wizard.htm",
  "source_original_path": "topics/export_document_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Exporting test cases and other iTest documents"
  ],
  "heading_path": [
    "Exporting test cases and other iTest documents",
    "Exporting test cases and other iTest documents",
    "Export test case to Robot library"
  ],
  "anchor": "1218623",
  "context_ids": [
    "export_document_wizard"
  ],
  "index_keywords": [
    "iTest documents as HTML XML or text",
    "saving as HTML",
    "saving as HTML XML or text",
    "saving iTest docs as",
    "saving test cases as",
    "saving test reports as"
  ],
  "index_keyword_paths": [
    "HTML > saving iTest docs as",
    "HTML > saving test cases as",
    "HTML > saving test reports as",
    "XML > saving iTest docs as",
    "XML > saving test cases as",
    "XML > saving test reports as",
    "documents > saving as HTML XML or text",
    "exporting > iTest documents as HTML XML or text",
    "iTest documents > saving as HTML XML or text",
    "saving > iTest documents as HTML XML or text",
    "test cases > saving as HTML",
    "text > saving iTest docs as",
    "text > saving test cases as",
    "text > saving test reports as"
  ],
  "related_links": [],
  "images": [
    "topics/images/export_to_robot_library.png",
    "topics/images/export_robot_source_destination.png",
    "topics/images/exported_QC_to_robot.png"
  ],
  "content_hash": "d52a90a8f43be65d",
  "level": 2
}
---

# Exporting test cases and other iTest documents > Exporting test cases and other iTest documents > Export test case to Robot library

1. In the Project explorer, right-click the document and click Export. The Export wizard opens.

1. 2

1. On the Select page, select iTest > Export to Robot library. Click Next.

1. 3

1. On the Source and Destination window, select source QuickCall to convert and the location where the generate Python Script will be saved.

- Select test case to be exported: Click Browse. Default location is Workspace. Navigate your workspace or the file system and select the file to be exported as Python Script and click OK.

You may select only one QuickCall at a time and export to Robot Keyword file.

- Chose location where robot library will be generated: Click Browse. Default location is file://C:/Users/user-01/ and the default name is the QuickCall file name.py. Browse to a location of your choice and click OK.

- Include iTest common library: Indicates whether the iTest common keyword file should be generated to the robot library file folder. This option is selected by default.

When selected: The export wizard will include the iTest common keyword file—iTestCommon.py, in the robot library file folder.

This file is a support file required to use iTest exported Robot Keyword file in Robot script and execute in an external environment. You cannot execute QuickCall library without this file.

When not selected: The export wizard will not generate the iTest common keyword file—iTestCommon.py.

1. 4

1. Click Finish to convert the selected QuickCall to Robot framework file or click Cancel to discard the export operation.

iTest generates a Python file, example: library_<quickcall>.py, which a robot framework user can import it to robot test case.

If you had selected to Include iTest common library, iTest will generate an additional python file—iTestcommon.py. See the example below.

If the file exists, iTest displays a dialog asking you to confirm whether you wish to overwrite the existing file or change file name.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/export_to_robot_library.png) <!-- image_chunk: img_e0f8873d095c20a5 -->

![screenshot](topics/images/export_robot_source_destination.png) <!-- image_chunk: img_d539f7d82931d22c -->

![screenshot](topics/images/exported_QC_to_robot.png) <!-- image_chunk: img_b7ea27d32a06ee06 -->
