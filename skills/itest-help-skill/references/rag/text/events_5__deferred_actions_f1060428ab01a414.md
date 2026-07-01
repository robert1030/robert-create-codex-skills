---
{
  "chunk_id": "events_5__deferred_actions_f1060428ab01a414",
  "source_file": "topics/events.5.htm",
  "source_original_path": "topics/events.5.htm",
  "toc_path": [
    "iTest Online Help",
    "Events: Taking Action when a Particular Event Occurs During Execution",
    "Deferred actions"
  ],
  "heading_path": [
    "Deferred actions",
    "Deferred actions"
  ],
  "anchor": "1251139",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "actions_on_events.htm#1206889"
  ],
  "images": [],
  "content_hash": "f1060428ab01a414",
  "level": 1
}
---

# Deferred actions > Deferred actions

Because some actions alter the flow of execution, they are deferred (not executed) until all other actions for the step are executed. This is true even if the action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after an AbortExecution action, the AbortExecution action does not execute until the FailTest action is finished executing. The following actions are deferred and are fully described in the table in Actions on events: Definitions:

AbortExecution

Break

CallProcedure

Continue

ExitExecution

ExitProcedure

Goto [Deprecated. We strongly recommend that you not use this action.]

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
