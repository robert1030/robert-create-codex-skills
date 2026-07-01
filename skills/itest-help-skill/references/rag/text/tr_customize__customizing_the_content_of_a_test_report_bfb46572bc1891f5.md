---
{
  "chunk_id": "tr_customize__customizing_the_content_of_a_test_report_bfb46572bc1891f5",
  "source_file": "topics/tr_customize.htm",
  "source_original_path": "topics/tr_customize.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Customizing the content of a test report"
  ],
  "heading_path": [
    "Customizing the content of a test report",
    "Customizing the content of a test report"
  ],
  "anchor": "1169470",
  "context_ids": [
    "tr_customize"
  ],
  "index_keywords": [
    "customizing",
    "test reports"
  ],
  "index_keyword_paths": [
    "customizing > test reports",
    "test reports > customizing"
  ],
  "related_links": [],
  "images": [
    "topics/images/trt_folderStructure.png"
  ],
  "content_hash": "bfb46572bc1891f5",
  "level": 1
}
---

# Customizing the content of a test report > Customizing the content of a test report

You can omit any section from an exported test report document by deleting its associated stylesheet from the resources project. The test_report_templates folder has a subfolder representing each file type that you can save:

For example, to save only the Summary portion of HTML reports:

1. 1

1. First, make a copy of the HTML folder (to a folder named my_custom, for example).

1. 2

1. In your folder, delete all of the xslt files in the HTML folder, except summary.xslt.

1. 3

1. Now, whenever you save a test report by clicking Save Test Report As, my_custom appears as an option in the Format drop-down list. Select my_custom, and, in the resulting report, only the Summary section of the report will be included.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/trt_folderStructure.png) <!-- image_chunk: img_43ba891af0f9ccf4 -->
