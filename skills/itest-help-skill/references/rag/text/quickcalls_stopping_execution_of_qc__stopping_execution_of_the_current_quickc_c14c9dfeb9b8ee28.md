---
{
  "chunk_id": "quickcalls_stopping_execution_of_qc__stopping_execution_of_the_current_quickc_c14c9dfeb9b8ee28",
  "source_file": "topics/quickcalls_stopping_execution_of_qc.htm",
  "source_original_path": "topics/quickcalls_stopping_execution_of_qc.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Adding a test case step that executes a QuickCall",
    "Stopping execution of the current QuickCall: The ‘return’ action"
  ],
  "heading_path": [
    "Stopping execution of the current QuickCall: The ‘return’ action",
    "Stopping execution of the current QuickCall: The ‘return’ action"
  ],
  "anchor": "1405664",
  "context_ids": [
    "quickcalls_stopping_execution_of_qc"
  ],
  "index_keywords": [
    "action",
    "exiting",
    "exiting QuickCalls",
    "return"
  ],
  "index_keyword_paths": [
    "QuickCalls > exiting",
    "actions > return",
    "exiting QuickCalls",
    "return > action"
  ],
  "related_links": [
    "action_return.htm#1385020"
  ],
  "images": [],
  "content_hash": "c14c9dfeb9b8ee28",
  "level": 1
}
---

# Stopping execution of the current QuickCall: The ‘return’ action > Stopping execution of the current QuickCall: The ‘return’ action

An return step inside the definition of a QuickCall immediately stops executing the current QuickCall and continues execution after the step that called the QuickCall. Any threads started by the QuickCall continue.

An appropriate execution message appears in the Execution view, in the Step Issues view, and in test reports.

A typical use is to place the return step in an if-then construct that branches based on the response from a session.

The return action has no configurable properties. See The ‘return’ action: Returning execution from the current procedure.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
