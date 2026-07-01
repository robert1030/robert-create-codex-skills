---
{
  "chunk_id": "trt_customize__customizing_the_standard_html_test_repor_0169a76b3658aa50",
  "source_file": "topics/trt_customize.htm",
  "source_original_path": "topics/trt_customize.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Customizing the Standard HTML test report template"
  ],
  "heading_path": [
    "Customizing the Standard HTML test report template",
    "Customizing the Standard HTML test report template"
  ],
  "anchor": "1534213",
  "context_ids": [
    "trt_customize"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tr_customize.htm#1169470"
  ],
  "images": [
    "topics/images/trt_folderStructure.png"
  ],
  "content_hash": "0169a76b3658aa50",
  "level": 1
}
---

# Customizing the Standard HTML test report template > Customizing the Standard HTML test report template

You can customize the iTest HTML+JSON reports, personalize the content, include your branding, and select what should be included in the report. The resulting test report template can be chosen when exporting the test report in iTest. You may also distribute the template to your co-workers to ensure that everyone uses the standard report template (You may also use the customized template to generate reports in Velocity Core)..

To create/modify a custom template follow these steps.

1. In Project Explorer, browse to the /resources/reports24/test_report_templates/

1. 2

1. Copy the folder with the template to be modified (e.g., HTML+JSON folder) to the same directory: /test_report_templates/

1. 3

1. Rename the copy of the template folder to create a new custom template (e.g., CUSTOM HTML).

> **Note:** Note Report name is inherited from folder name.

1. 4

1. Modify the .ftl inside the template folder.

To use a custom logo, add your custom image to the CUSTOM HTML folder and rename the image you added as customImage.png.

> **Note:** Note The name customImage.png is the default/fixed name and iTest uses this image name as the custom logo to generate/print the custom report.

1. 5

1. Modify report content as in Customizing the content of a test report.

1. 6

1. Now, whenever you save a test report by clicking Save Test Report As, CUSTOM HTML appears as an option in the Format drop-down list. Select CUSTOM HTML, and, the resulting report displays as per your template.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/trt_folderStructure.png) <!-- image_chunk: img_43ba891af0f9ccf4 -->
