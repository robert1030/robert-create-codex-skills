---
{
  "chunk_id": "capture_command_concept__commands_in_test_cases_c7296eaf62f50c2c",
  "source_file": "topics/capture_command_concept.htm",
  "source_original_path": "topics/capture_command_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Commands"
  ],
  "heading_path": [
    "Commands",
    "Commands",
    "Commands in test cases"
  ],
  "anchor": "1131808",
  "context_ids": [
    "capture_command_concept"
  ],
  "index_keywords": [
    "CLI commands",
    "defined"
  ],
  "index_keyword_paths": [
    "CLI commands",
    "CLI sessions > defined",
    "commands > defined",
    "terminal-based sessions > defined"
  ],
  "related_links": [],
  "images": [
    "topics/images/capture_tasks_2.3.jpg"
  ],
  "content_hash": "c7296eaf62f50c2c",
  "level": 2
}
---

# Commands > Commands > Commands in test cases

For CLI sessions, when you are working in the Test Case editor, you define a command by selecting an Action of type command, and then providing the text of the command in the Command property (or the Description cell) for the step.

There are only two Actions that are specific to CLI steps in a test case (the other actions in the list appear for all session types):

command: A command action submits a command to the session.

break: A break action is special. It sends a break character (typically Ctrl-C, configurable in the session profile)

There is one Action that is specific to traffic generator session types: configure

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/capture_tasks_2.3.jpg) <!-- image_chunk: img_12072e1c101ae2eb -->
