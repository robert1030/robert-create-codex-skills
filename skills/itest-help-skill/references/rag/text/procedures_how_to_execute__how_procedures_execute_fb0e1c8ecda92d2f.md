---
{
  "chunk_id": "procedures_how_to_execute__how_procedures_execute_fb0e1c8ecda92d2f",
  "source_file": "topics/procedures_how_to_execute.htm",
  "source_original_path": "topics/procedures_how_to_execute.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "How procedures execute"
  ],
  "heading_path": [
    "How procedures execute",
    "How procedures execute"
  ],
  "anchor": "1518702",
  "context_ids": [
    "procedures_how_to_execute"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "procedures_overview.htm#1278577",
    "procedures_advanced_users_about_procedures.htm#1399200"
  ],
  "images": [],
  "content_hash": "fb0e1c8ecda92d2f",
  "level": 1
}
---

# How procedures execute > How procedures execute

- When a call step or CallProcedure action executes, it calls a procedure. The called procedure becomes the currently executing procedure. Normal execution flow continues in the procedure and, when the procedure exits, the caller again becomes the currently executing procedure.

- The steps in local procedures have the same execution context as the main procedure. (See Local procedures, foreign procedures, and procedure libraries.)

When a call step executes, all steps in the called procedure execute in the same thread (unless steps in the procedure are specified as asynch).

- iTest does not enforce timeout settings for call steps.

- The currently executing procedure waits for all outstanding executing steps and analysis rules to complete before executing a call step or CallProcedure action.

- Sessions span procedural contexts. For example, a CLI session opened in a caller is still active for steps in a called procedure (the Session name must be the same).

- Parameter values are resolved from parameter property settings in the following precedence order: First, the calling test case document, then, the current foreign test case document, and last, the session profile associated with the calling step. See Parameters for details.

- The Procedure column in the Execution view identifies the procedure name associated with each step.

- A called procedure can use a return or write step to populate the response of the calling step. The calling step's analysis rule applies to the result in the normal way.

- In any procedure, the AbortExecution event action terminates the entire test case and sets test result to Abort .

- Pass, Warning, Abort, and Fail settings apply to the overall test result regardless of which procedure declared them.

> **Note:** Note Advanced Users: The default entry point to a test case is the procedure named main. You can rename main, but to ensure that the test case starts properly, change the Entry point setting (on the Test Case editor General page) to the new name.

> **Note:** Tip Invoking a TCL routine

> **Note:** Insert a step that opens a Tcl Shell session. You can execute any TCL commands in that session, including sourcing and executing scripts.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
