---
{
  "chunk_id": "events_overview_page__events_fe830bdf8c6ce199",
  "source_file": "topics/events_overview_page.htm",
  "source_original_path": "topics/events_overview_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Events: Taking Action when a Particular Event Occurs During Execution",
    "Events"
  ],
  "heading_path": [
    "Events",
    "Events"
  ],
  "anchor": "1174101",
  "context_ids": [
    "events_overview_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "fe830bdf8c6ce199",
  "level": 1
}
---

# Events > Events

You can add considerable power to a test case by specifying that, whenever a particular event occurs during execution, iTest should perform a certain action. For example, you can configure that when a step times out (an OnStepTimeout event occurs), iTest should perform the following two actions:

- Perform a DeclareExecutionIssue action: Issue an execution issue with a severity level of Error with associated execution message text “Step has timed out.”

- Perform a FailTest action: Set the test result to Fail and continue to execute.
