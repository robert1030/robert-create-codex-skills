---
{
  "chunk_id": "tce_inserting_captured_steps__inserting_captured_steps_into_an_existin_a8bc80cf511dbc20",
  "source_file": "topics/tce_inserting_captured_steps.htm",
  "source_original_path": "topics/tce_inserting_captured_steps.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Overview: Creating a test case",
    "Inserting captured steps into an existing test case"
  ],
  "heading_path": [
    "Inserting captured steps into an existing test case",
    "Inserting captured steps into an existing test case"
  ],
  "anchor": "1861380",
  "context_ids": [
    "tce_inserting_captured_steps"
  ],
  "index_keywords": [
    "inserting captured steps into",
    "inserting into an existing test case",
    "tips for inserting into an existing test case"
  ],
  "index_keyword_paths": [
    "captured steps > inserting into an existing test case",
    "steps > tips for inserting into an existing test case",
    "test cases > inserting captured steps into"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "a8bc80cf511dbc20",
  "level": 1
}
---

# Inserting captured steps into an existing test case > Inserting captured steps into an existing test case

Here's a fast way to add steps that iTest captured during an interactive session:

1. 1

1. In the test case, set a breakpoint where you want to start adding steps.

1. 2

1. Execute the test case.

1. 3

1. When execution stops at the breakpoint, select the current session window (if it is CLI, it will be stopped at a prompt).

1. 4

1. Enter any commands that you want to add at this point.

1. 5

1. In the Execution view, click to complete execution.

1. 6

1. In the Capture view, select the last session. Click to save it as a new procedure.

> **Note:** Note When you convert manual steps into test case steps, iTest uses the combination of Session name from the session profile and the unique session number for the day (for example, myDUT5) to create the Session ID that appears in the Session cell in the Test Case editor.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
