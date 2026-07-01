---
{
  "chunk_id": "test_cases_action_run_exec__executing_a_child_test_case_the_run_acti_9260a1c2969d355f",
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
    "Executing a child test case: The ‘run’ action"
  ],
  "anchor": "1714621",
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
  "related_links": [
    "procedures_overview.htm#",
    "favorites_view.htm#1170095"
  ],
  "images": [
    "topics/images/test_cases_4.2.jpg",
    "topics/images/test_cases_2.3.jpg"
  ],
  "content_hash": "9260a1c2969d355f",
  "level": 1
}
---

# Executing a child test case: The ‘run’ action > Executing a child test case: The ‘run’ action

A run step executes the specified test case (the child test case — sometimes called a foreign or an external test case, from within a master test case) and optionally passes parameter values. The response for a run step is configurable.

- You cannot use the run action to execute a procedure — instead, use a call step or CallProcedure action as described in “Procedures”.

- You can run child test cases without loading topologies for the parent main procedure.

- The child test case occurs within the current process context.

- The run step response can include a table of all child test case executions (either the test case that was executed directly by the run or the test cases that were executed indirectly when run was executed inside one of the child test cases, and so on).



Shortcut: To add a ‘run’ step

While editing a test case, right-click the child test case in the Favorites view and select Insert step to run this test case. The run step is added after the selected step in the parent/master test case. See Using the Favorites view to add steps to a test case.



To add a ‘run’ step

1. Create a step with an Action of run.

1. 2

1. In the Description cell, specify the URI of the test case to run: Click to open a dialog box that allows you to select a test case either:

- From the list of test cases in the current workspace

- From another location on the file system (typically a test case in an itar file)

1. 3

1. In the Step Properties section, open the EXEC run Properties > Run properties group.

1. 4

1. Set property values as follows:

| Test case timeout | Specify the maximum time in seconds that the test case is allowed to execute. If test duration exceeds the specified limit, then the test case is aborted and marked Fail. The default value of 0.0 indicates no time limit — the test case will “never” time out. |
| --- | --- |
| Expected completion result | Specify the result that you expect for the child test case. This property enables you to ensure that the overall test result reflects your preference. For example, if the child test case is a negative test, then, you would expect it to return a Fail result to indicate that the test successfully performed the test. In this case, you should set Expected completion result to Fail. If the child returns a Fail result, then, for the parent test case, the run step passes. |

1. 5

1. Response format: Specify the format of the response to the run step. “Unexpected results” means any value other than the value that you specified for the Expected completion result property. Example response formats:

![screenshot](topics/images/test_cases_4.2.jpg) <!-- image_chunk: img_342cc1a4892ed029 -->

![screenshot](topics/images/test_cases_2.3.jpg) <!-- image_chunk: img_8dfb0495cfddb72c -->
