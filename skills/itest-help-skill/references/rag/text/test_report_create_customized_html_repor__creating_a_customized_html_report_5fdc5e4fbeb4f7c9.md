---
{
  "chunk_id": "test_report_create_customized_html_repor__creating_a_customized_html_report_5fdc5e4fbeb4f7c9",
  "source_file": "topics/test_report_create_customized_html_report.htm",
  "source_original_path": "topics/test_report_create_customized_html_report.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Creating a Customized HTML Report"
  ],
  "heading_path": [
    "Creating a Customized HTML Report",
    "Creating a Customized HTML Report"
  ],
  "anchor": "1534791",
  "context_ids": [
    "test_report_create_customized_html_report"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "report_format_xslt.htm#1169506"
  ],
  "images": [],
  "content_hash": "5fdc5e4fbeb4f7c9",
  "level": 1
}
---

# Creating a Customized HTML Report > Creating a Customized HTML Report

You may download the default template provided by iTest, customize it as required using the provided template data model Velocity Portfolio Report Data Model (on Spirent Knowledgebase) and upload the custom template. You may also upload custom images as the logo to be used with your custom template.

Important You must be logged into Spirent Knowledge base to access Velocity Portfolio Report Data Model (on Spirent Knowledgebase).

To create/modify a custom template follow these steps.

1. In Project Explorer, browse to the /resources/reports25/test_report_templates/

1. 2

1. Copy the folder with the template to be modified (e.g., HTML folder) to the same directory: /test_report_templates/

1. 3

1. Rename the copy of the template folder to create a new custom template (e.g., CUSTOM HTML).

> **Note:** Note Report name is inherited from folder name.

1. 4

1. Modify the .ftl inside the template folder as per the instructions in Velocity Portfolio Report Data Model (on Spirent Knowledgebase).

To use a custom logo, add your custom image to the CUSTOM HTML folder and rename the image you added as customImage.png.

> **Note:** Note The name customImage.png is the default/fixed name and iTest uses this image name as the custom logo to generate/print the custom report.

1. 5

1. Modify report content as in Velocity Portfolio Report Data Model (on Spirent Knowledgebase).

Now, whenever you save a test report by clicking Save Test Report As, CUSTOM HTML appears as an option in the Format drop-down list. Select CUSTOM HTML, and, the resulting report displays as per your template.

For advanced XSLT options, see Using Velocity iTest's XSLT stylesheets to format reports.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
