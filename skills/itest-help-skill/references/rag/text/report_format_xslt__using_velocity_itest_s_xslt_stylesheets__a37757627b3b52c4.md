---
{
  "chunk_id": "report_format_xslt__using_velocity_itest_s_xslt_stylesheets__a37757627b3b52c4",
  "source_file": "topics/report_format_xslt.htm",
  "source_original_path": "topics/report_format_xslt.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Sharing Test Reports",
    "Using Velocity iTest's XSLT stylesheets to format reports"
  ],
  "heading_path": [
    "Using Velocity iTest's XSLT stylesheets to format reports",
    "Using Velocity iTest's XSLT stylesheets to format reports"
  ],
  "anchor": "1169506",
  "context_ids": [
    "report_format_xslt"
  ],
  "index_keywords": [
    "formatting reports",
    "formatting using XSLT stylesheets"
  ],
  "index_keyword_paths": [
    "XSLT stylesheets > formatting reports",
    "reports > formatting using XSLT stylesheets"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "a37757627b3b52c4",
  "level": 1
}
---

# Using Velocity iTest's XSLT stylesheets to format reports > Using Velocity iTest's XSLT stylesheets to format reports

Velocity iTest uses the Java XML transformer and XSLT stylesheets to transform Velocity iTest XML documents to various document types. XML_RAW, Text, PDF, and HTML styles are supported for test reports, capture reports, and test cases.

Additional XML styles are provided for test reports.

You can export test reports in a format that matches a published schema. This ensures that any tools that you create to extract the test report data will work with future versions of Velocity iTest.

- The “XML” choice produces a Velocity iTest XML test report file that adheres to the schema in resources/reports<highestNumber>/test_report_templates/XML/test_report.xsd

- The “XML Raw” choice is the Velocity iTest 3.1 full report format.

The stylesheets are located in the workspace under the resources project. The project must be open for the transformations to work. They are created the first time you try to export a document.
