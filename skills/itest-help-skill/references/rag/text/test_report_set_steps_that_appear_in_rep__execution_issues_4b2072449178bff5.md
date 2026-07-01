---
{
  "chunk_id": "test_report_set_steps_that_appear_in_rep__execution_issues_4b2072449178bff5",
  "source_file": "topics/test_report_set_steps_that_appear_in_report.htm",
  "source_original_path": "topics/test_report_set_steps_that_appear_in_report.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Reports",
    "Test reports overview",
    "Controlling which executed steps appear in test reports"
  ],
  "heading_path": [
    "Controlling which executed steps appear in test reports",
    "Controlling which executed steps appear in test reports",
    "Execution issues"
  ],
  "anchor": "1466773",
  "context_ids": [
    "test_report_set_steps_that_appear_in_report"
  ],
  "index_keywords": [
    "Selective step reporting",
    "improving",
    "improving performance",
    "not reporting"
  ],
  "index_keyword_paths": [
    "Selective step reporting",
    "improving performance",
    "performance > improving",
    "steps > not reporting"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "4b2072449178bff5",
  "level": 2
}
---

# Controlling which executed steps appear in test reports > Controlling which executed steps appear in test reports > Execution issues

If a child step of any step that is configured not to appear in reports has an execution issue, then, in the list of execution messages in the Execution view, the issue’s icon appears next to the message for its nearest ancestor. The step index for the issue is associated with the child step that had the issue, so you can double-click the issue to open the Test Case editor to the child step that had the issue.



To specify that a step should not appear in test reports

1. In the Test Report editor, select the step or steps.

1. 2

1. In the General properties group, uncheck Include this step and its children in test reports.



To override the “no-report” setting: To specify that all steps should appear in test reports, regardless of the settings for the individual steps

You might want to include all steps in test reports, even though individual steps might be configured not to appear. Follow this procedure:

1. 1

1. Click Window > Preferences.

1. 2

1. On the Preferences page, in the Spirent group, navigate to General > Execution.

1. 3

1. Check Include all steps in test reports (ignore the setting for the step).



To override the “no-report” setting in iTestRT

iTestRT uses Boolean arguments to specify that all steps should appear in test reports, regardless of the settings for the individual steps:

iTestRT: --reportallsteps

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
