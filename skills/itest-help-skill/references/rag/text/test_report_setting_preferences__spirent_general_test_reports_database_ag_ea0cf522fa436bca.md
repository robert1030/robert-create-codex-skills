---
{
  "chunk_id": "test_report_setting_preferences__spirent_general_test_reports_database_ag_ea0cf522fa436bca",
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
    "Spirent > General > Test Reports > Database Aging"
  ],
  "anchor": "1389678",
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
  "related_links": [],
  "images": [],
  "content_hash": "ea0cf522fa436bca",
  "level": 2
}
---

# Setting preferences for Test Reports > Setting preferences for Test Reports > Spirent > General > Test Reports > Database Aging

To ensure that the database of test reports does not become too large, you can specify that old reports should be deleted when they reach a particular “age”.

| Enable Automatic Test Report Aging | Select to ensure that the database of test report older than the specified age is automatically deleted. |
| --- | --- |
| Delete reports older than | Note This setting applies only to the default iTest “standalone” database within your workspace. When a test report exceeds the specified age in days, it is deleted. Default: 30 Note A report will be deleted only after the current execution of the test case is completed and the next execution of the same test case starts. For a recursive test case (a test case that includes a run step that executes itself), the test reports are never deleted. Exit and restart iTest to apply a new setting. |
| Note | This setting applies only to the default iTest “standalone” database within your workspace. |
| Note | A report will be deleted only after the current execution of the test case is completed and the next execution of the same test case starts. For a recursive test case (a test case that includes a run step that executes itself), the test reports are never deleted. |
| Age Now | Click Age Now to immediately invoke a database report aging process using the Delete reports older than value above. |
