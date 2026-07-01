---
{
  "chunk_id": "test_cases_action_run_exec__working_with_the_return_result_for_a_run_72810fc3d2567de4",
  "source_file": "topics/test_cases_action_run_exec.htm",
  "source_original_path": "topics/test_cases_action_run_exec.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Running child test cases",
    "Executing a child test case: The ‘run’ action"
  ],
  "heading_path": [
    "Executing a child test case: The ‘run’ action",
    "Executing a child test case: The ‘run’ action",
    "Working with the Return result for a run step"
  ],
  "anchor": "1175268",
  "context_ids": [
    "test_cases_action_run_exec"
  ],
  "index_keywords": [
    "defined",
    "run",
    "run action"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > run",
    "actions > run",
    "child test case > defined",
    "external test case > defined",
    "foreign test case > defined",
    "run action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "72810fc3d2567de4",
  "level": 2
}
---

# Executing a child test case: The ‘run’ action > Executing a child test case: The ‘run’ action > Working with the Return result for a run step

The default expected completion result for a child test case is Pass. If you do not set pass/fail criteria with an analysis rule, then the completion result is Indeterminate and the child test case fails with an Error execution issue with an execution message of: unexpected result "Indeterminate".

To avoid the problem, add an analysis rule that extracts and analyzes the TestResult() query.

In the Response view, right-click the “Indeterminate” part of the Competition Result and select Add Rule > Query > Assert. To verify that it returns with indeterminate result, then your check_run will now pass.
