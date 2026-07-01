---
{
  "chunk_id": "activity_review_test_reports__sorting_reports_in_the_view_cc2e74c27382fe38",
  "source_file": "topics/activity_review_test_reports.htm",
  "source_original_path": "topics/activity_review_test_reports.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Activity View"
  ],
  "heading_path": [
    "Activity View",
    "Activity View",
    "Developing a test case",
    "Reviewing test reports",
    "Sorting reports in the view"
  ],
  "anchor": "1713659",
  "context_ids": [],
  "index_keywords": [
    "Build a topology page",
    "Develop a test case page",
    "Execution view",
    "Manage workspace page",
    "Messages table",
    "Session Profile editor",
    "Work on a test case page",
    "adding session profiles to",
    "analysis rules",
    "defining for devices in topologies",
    "described",
    "editing",
    "examples",
    "find issues in",
    "importing",
    "in analysis rules defined",
    "issues in test reports",
    "preference settings",
    "project set files",
    "projects",
    "psf files",
    "session profiles in topologies",
    "setting criteria"
  ],
  "index_keyword_paths": [
    "Build a topology page",
    "Develop a test case page",
    "Execution view",
    "Manage workspace page",
    "Messages table",
    "Session Profile editor > preference settings",
    "Work on a test case page",
    "adding > session profiles in topologies",
    "analysis rules > described",
    "analysis rules > examples",
    "configuring > session profiles in topologies",
    "devices in topologies > adding session profiles to",
    "editing > session profiles in topologies",
    "editor preferences > Session Profile editor",
    "examples > analysis rules",
    "extractors > in analysis rules defined",
    "find > issues in test reports",
    "importing > project set files",
    "importing > projects",
    "importing > psf files",
    "issues > finding in test reports test reports > find issues in",
    "pass/fail > setting criteria",
    "preference settings > Session Profile editor",
    "processors > in analysis rules defined",
    "project set files > importing",
    "projects > importing",
    "psf files > importing",
    "session profiles > defining for devices in topologies",
    "topologies > adding session profiles to",
    "topologies > editing",
    "validating responses > analysis rules",
    "views > Execution view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "cc2e74c27382fe38",
  "level": 4
}
---

# Activity View > Activity View > Developing a test case > Reviewing test reports > Sorting reports in the view

By default, iTest lists reports in chronological order. You can click any heading to sort on a property of the report. For example, click the Test Case heading to sort in alphabetical order or reverse alphabetical order. Within each group of identically-named test cases, reports are sorted by Timestamp.

- Click the Result heading (the first column) to sort in the following order: Pass, Indeterminate, Fail, and Abort. Within each Result group, reports are sorted by Timestamp.

| Result | Icon representing test execution Result: Pass , Fail , Abort , or Indeterminate |
| --- | --- |
| Timestamp | Date and time that the test case was executed (tests executed today display only the time). |
| Test Case | Name of the test case that executed to generate the report. To display the full URI, select the Show Full Test Case URIs option in the context (right-click) menu, |
| Result | Test execution Result in text form: Pass, Fail, Abort, or Indeterminate |
| Group | Optional. External database only. You specify that the Group value should appear in the list by setting a preference value. If you specify a value, on the Preferences page, then it appears in the Group column on the Review Test Reports activity page and on the Test Reports view. The value acts as a parent to the optional Subgroup value. |
| Subgroup | Optional. External database only. If you specify a value, then it appears in the Subgroup column on the Review Test Reports activity page and on the Test Reports view. The value acts as a child of the optional Group value. |
| Report ID | Unique auto-generated ID for the report. You can search on this value, open the test report using the ID, and access the ID using the info reportId command in a test case step. |
