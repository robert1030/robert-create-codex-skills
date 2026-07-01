---
{
  "chunk_id": "action_run__the_run_action_execute_the_specified_tes_1984a9db36734ba5",
  "source_file": "topics/action_run.htm",
  "source_original_path": "topics/action_run.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘eval’ action: Evaluate an iTest interpreter command"
  ],
  "heading_path": [
    "The ‘eval’ action: Evaluate an iTest interpreter command",
    "The ‘eval’ action: Evaluate an iTest interpreter command",
    "The ‘run’ action: Execute the specified test case"
  ],
  "anchor": "1692659",
  "context_ids": [
    "action_eval",
    "action_run"
  ],
  "index_keywords": [
    "action",
    "eval",
    "evaluating in steps",
    "in steps"
  ],
  "index_keyword_paths": [
    "actions > eval",
    "eval > action",
    "evaluating expressions > in steps",
    "expressions > evaluating in steps"
  ],
  "related_links": [
    "test_cases_action_run_exec.htm#1714621"
  ],
  "images": [],
  "content_hash": "1984a9db36734ba5",
  "level": 2
}
---

# The ‘eval’ action: Evaluate an iTest interpreter command > The ‘eval’ action: Evaluate an iTest interpreter command > The ‘run’ action: Execute the specified test case

A run step executes the specified test case (the child test case — sometimes called a foreign or an external test case) and optionally passes parameter values.

See Executing a child test case: The ‘run’ action.

> **Note:** Note If a call step in a child test case B (begun by a run step in a grandparent test case A) calls grandchild test case C: The called test case C will use the shared session from test case A in its open step if the Session ID in C is same as the Session ID in A. If you do not want to use the shared session, then change the Session ID in C to be different from the Session ID in A.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
