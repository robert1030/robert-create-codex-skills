---
{
  "chunk_id": "action_return__the_return_action_returning_execution_fr_1b81fada12648b04",
  "source_file": "topics/action_return.htm",
  "source_original_path": "topics/action_return.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "The ‘return’ action: Returning execution from the current procedure"
  ],
  "heading_path": [
    "The ‘return’ action: Returning execution from the current procedure",
    "The ‘return’ action: Returning execution from the current procedure"
  ],
  "anchor": "1385020",
  "context_ids": [
    "action_return"
  ],
  "index_keywords": [
    "return",
    "return action",
    "returning from",
    "returning from procedures"
  ],
  "index_keyword_paths": [
    "actions > return",
    "procedures > returning from",
    "return action",
    "returning from procedures"
  ],
  "related_links": [
    "action_write.htm#1385240",
    "action_write.htm#1385033"
  ],
  "images": [],
  "content_hash": "1b81fada12648b04",
  "level": 1
}
---

# The ‘return’ action: Returning execution from the current procedure > The ‘return’ action: Returning execution from the current procedure

A return step stops executing the current procedure and returns execution from the current procedure to the caller. This means either continue processing the procedure or QuickCall whose call step (or CallProcedure action) caused the procedure to start, or end test case execution if the procedure was the initial entry point. Any threads started by the procedure or QuickCall continue.

- The return action does not return a response. To return a value for a procedure, the text specified in the Description cell (the value of the Command property) of the return step is appended to the response of the call step. The text string can contain field replacements (for example, [response var_name]). See Tips on using ‘write’ and ‘return’ steps to prepare useful response data for called procedures.

The Start this step in a new thread and proceed to the next step (asynchronous execution) property on a return step is ignored.

- Steps nested inside return steps are never executed.

- Contrast return with write. See The ‘write’ action: Adding text into the response of a call step.

> **Tip:** Tip You can use a return step in the main procedure to exit a test case. Because you do not typically want to return every time the test case runs, you'll probably include the return step within an if construct.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
