---
{
  "chunk_id": "test_report_overview__how_test_reports_are_stored_c061a247409bfb25",
  "source_file": "topics/test_report_overview.htm",
  "source_original_path": "topics/test_report_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Test reports overview"
  ],
  "heading_path": [
    "Test reports overview",
    "Test reports overview",
    "How test reports are stored"
  ],
  "anchor": "1418876",
  "context_ids": [
    "test_report_overview"
  ],
  "index_keywords": [
    "test reports",
    "test reports, debug mode"
  ],
  "index_keyword_paths": [
    "test reports",
    "test reports, debug mode"
  ],
  "related_links": [
    "test_report_setting_preferences.htm#1331474"
  ],
  "images": [],
  "content_hash": "c061a247409bfb25",
  "level": 2
}
---

# Test reports overview > Test reports overview > How test reports are stored

In test automation solutions, test scripts often generate very large test report files. For ease of reference, and performance reasons, Velocity iTest stores test reports in a database. While Velocity iTest executes a test case, it places execution information into records in an embedded database in your workspace (or optionally into a separate database that you specify). A test report in the database is not a specific file; rather it is a series of records in a database. The .report directory contains files that implement the default database.

> **Note:** Note The manual steps captured during debug mode are highlighted in green to indicate manual commands and separate them from the test scripts.

You may also configure Velocity iTest to automatically save reports in separate folders specified by you when the test execution completes. See Setting preferences for Test Reports.

In addition, to make it easier to share report data, you can configure Velocity iTest to save test reports to an external database rather than to the default database within your workspace.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
