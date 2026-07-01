---
{
  "chunk_id": "test_cases_step_delaying__delaying_the_start_of_step_execution_70b12d53e0f04ab1",
  "source_file": "topics/test_cases_step_delaying.htm",
  "source_original_path": "topics/test_cases_step_delaying.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Test suites: Organizing tests for group execution",
    "Delaying the start of step execution"
  ],
  "heading_path": [
    "Delaying the start of step execution",
    "Delaying the start of step execution"
  ],
  "anchor": "1714472",
  "context_ids": [
    "test_cases_step_delaying"
  ],
  "index_keywords": [
    "delaying start of",
    "delaying steps"
  ],
  "index_keyword_paths": [
    "delaying steps",
    "execution > delaying steps",
    "steps > delaying start of"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "70b12d53e0f04ab1",
  "level": 1
}
---

# Delaying the start of step execution > Delaying the start of step execution

In some cases, you need to delay the start of a step. For example, the step should wait for a device to reboot or should wait for sufficient debug output when there is no prompt upon completion. In this example, we'll delay the start of a step by 25 seconds:

1. 1

1. Select the step before the step that should be delayed.

1. 2

1. In the Step Properties section, click Timing > Start.

1. 3

1. Set Normal to 25.

1. 4

1. Set Fast to 25. (The Fast setting must be equal to or less than the Normal setting.)

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
