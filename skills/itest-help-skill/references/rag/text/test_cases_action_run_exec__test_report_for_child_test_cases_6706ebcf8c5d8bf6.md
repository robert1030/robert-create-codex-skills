---
{
  "chunk_id": "test_cases_action_run_exec__test_report_for_child_test_cases_6706ebcf8c5d8bf6",
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
    "Test report for child test cases"
  ],
  "anchor": "1714714",
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
  "content_hash": "6706ebcf8c5d8bf6",
  "level": 3
}
---

# Executing a child test case: The ‘run’ action > Executing a child test case: The ‘run’ action > Test report for child test cases

While the child test case executes, its output is displayed in the Console view. However, the test case produces its own test report and the resulting execution messages are written into the response of the run step. The execution messages do not become a part of the parent test case.

The overall test case result (Pass/Fail/Abort/Indeterminate) is used to declare a single Pass/Fail execution issue in the parent test case. The Indeterminate result causes a Fail declaration on the parent test case.
