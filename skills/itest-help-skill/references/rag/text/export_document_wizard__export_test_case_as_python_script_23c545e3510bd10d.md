---
{
  "chunk_id": "export_document_wizard__export_test_case_as_python_script_23c545e3510bd10d",
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
    "Export test case as Python Script"
  ],
  "anchor": "1211349",
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
    "topics/images/export_as_python_script.png",
    "topics/images/export_as_py_source_destination_window.png",
    "topics/images/export_as_py_validate_test_case.png"
  ],
  "content_hash": "23c545e3510bd10d",
  "level": 2
}
---

# Exporting test cases and other iTest documents > Exporting test cases and other iTest documents > Export test case as Python Script

1. In the Project Explorer, right-click the document and click Export. The Export wizard opens.

1. 2

1. On the Select page, select iTest > Export as Python Script. Click Next.

1. 3

1. On the Source and Destination window, select source test case to convert and the location where the generate Python Script will be saved.

- Select test case to be exported: Click Browse. Default location is Workspace. Navigate your workspace or the file system and select the file to be exported as Python Script and click OK.

- Chose location where Python script will be generated: Click Browse. Default location is my_project/scripts and the default name is the test case file name.py. Browse to a location of your choise and click OK.

1. 4

1. Click Next and the Validate Test Case window displays.

- The test case step view displays at the top of the window and a list of validation issue displays at the bottom.

- Each validation issue from the list displays a description and a step id (if any).

- Double-click on the validation issue at the bottom of the window and the corresponding step shown in steps view (if any) displays.

- Right-click this validation issue or a step, to display the Go to Editor menu.

- Click Go to Editor and the corresponding test case opens.

1. 5

1. Click Finish to convert the selected test case to Python.

iTest converts test case to Python irrespective of any validation issues, which you may edit as required.

![screenshot](topics/images/export_as_python_script.png) <!-- image_chunk: img_acc82da4ad9f1046 -->

![screenshot](topics/images/export_as_py_source_destination_window.png) <!-- image_chunk: img_c76019cf792868d5 -->

![screenshot](topics/images/export_as_py_validate_test_case.png) <!-- image_chunk: img_a9778f4248d64350 -->
