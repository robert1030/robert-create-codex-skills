---
{
  "chunk_id": "test_reports_view__sorting_reports_in_the_view_576f332038d7a5f0",
  "source_file": "topics/test_reports_view.htm",
  "source_original_path": "topics/test_reports_view.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Test Reports view"
  ],
  "heading_path": [
    "Test Reports view",
    "Test Reports view",
    "Working in the Test Reports view",
    "List of test reports",
    "Sorting reports in the view"
  ],
  "anchor": "1388665",
  "context_ids": [
    "test_reports_view"
  ],
  "index_keywords": [
    "Test Reports view"
  ],
  "index_keyword_paths": [
    "Test Reports view",
    "views > Test Reports view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "576f332038d7a5f0",
  "level": 4
}
---

# Test Reports view > Test Reports view > Working in the Test Reports view > List of test reports > Sorting reports in the view

By default, Velocity iTest lists reports in chronological order. You can click any heading to sort on a property of the report.

- Click the Timestamp heading to sort in chronological or reverse chronological order.

- Click the Test Case heading to sort in alphabetical order or reverse alphabetical order. Within each group of identically-named test cases, reports are sorted by Timestamp.

- Click the Result heading (the first column) to sort in the following order: Pass, Indeterminate, Fail, and Abort. Within each Result group, reports are sorted by Timestamp.

- Click the Report ID heading to sort in numerical order or reverse numerical order.

- Click Topology heading to sort in alphabetical order or reverse alphabetical order. Within each group of identically-named topology names, reports are sorted by Timestamp.

| Timestamp | Date and time that the test case was executed (tests executed today display only the time). |
| --- | --- |
| Test Case | Name of the test case that executed to generate the report. |
| Result | Test execution result: Pass , Fail , Abort , or Indeterminate |
| Report ID | Indicates the ID of the report. |
| Topology | The name of the topoly used in the test case. For example, if you have a master_suite that is running on different topologies, in the test reports view, you will see the master_suite. You may click on each of the test case reports to see the topology used. |
| Host | If you have configured iTest to save test reports to an external database, then this column appears and displays the hostname of the iTest client that generated the report. |
| Group | If you have configured iTest to save test reports to an external database, then this column appears and displays the group name that was configured on the iTest client. |
| Subgroup | If you have configured iTest to save test reports to an external database, then this column appears and displays the subgroup name that was configured on the iTest client. |
