---
{
  "chunk_id": "test_report_time_stamp_for_steps__including_system_timestamp_for_individua_76200a93370613e2",
  "source_file": "topics/test_report_time_stamp_for_steps.htm",
  "source_original_path": "topics/test_report_time_stamp_for_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Including system timestamp for individual steps in HTML test reports"
  ],
  "heading_path": [
    "Including system timestamp for individual steps in HTML test reports",
    "Including system timestamp for individual steps in HTML test reports"
  ],
  "anchor": "1466787",
  "context_ids": [
    "test_report_time_stamp_for_steps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "76200a93370613e2",
  "level": 1
}
---

# Including system timestamp for individual steps in HTML test reports > Including system timestamp for individual steps in HTML test reports

By default for each step, HTML-format test reports include the time elapsed since test case execution started. To display, instead, the system timestamp for each executed step, you must edit the item.xslt file to uncomment one section and comment another. Comments begin with <!-- and end with -->. To uncomment a section, delete both sets of characters.

File path: project://resources/reportsXX/test_report_templates/HTML/item.xslt

Sections to comment or uncomment as needed:

<!-- Uncomment to print time elapsed since test case execution started ~~~~~~~~~~~~~~--> (Uncommented by default)

or

<!-- Uncomment to print system time the individual step began ~~~~~~~~~~~~~~~~~~~~~~~-->

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
