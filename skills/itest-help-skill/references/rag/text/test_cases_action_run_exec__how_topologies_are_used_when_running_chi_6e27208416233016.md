---
{
  "chunk_id": "test_cases_action_run_exec__how_topologies_are_used_when_running_chi_6e27208416233016",
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
    "How topologies are used when running child test cases"
  ],
  "anchor": "1175273",
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
  "content_hash": "6e27208416233016",
  "level": 2
}
---

# Executing a child test case: The ‘run’ action > Executing a child test case: The ‘run’ action > How topologies are used when running child test cases

If a test case calls a procedure in a child test case (a child procedure), then the URI specified in the child test case is not used. Instead, the topologies specified in the calling test case is used.

If an open step in the child procedure refers to a device URI, then the URI will be replaced using the current topology that was loaded at start of execution.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
