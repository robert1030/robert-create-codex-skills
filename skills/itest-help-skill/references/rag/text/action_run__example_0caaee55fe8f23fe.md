---
{
  "chunk_id": "action_run__example_0caaee55fe8f23fe",
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
    "Example:"
  ],
  "anchor": "1515992",
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
    "test_cases.04.htm#1861511"
  ],
  "images": [
    "topics/images/actions_6.1.jpg",
    "topics/images/actions_3.2.jpg"
  ],
  "content_hash": "0caaee55fe8f23fe",
  "level": 2
}
---

# The ‘eval’ action: Evaluate an iTest interpreter command > The ‘eval’ action: Evaluate an iTest interpreter command > Example:

This eval step sets the value of a local variable.

Tcl example:

Python examaple:

> **Note:** Note Using an eval action directs the statement to the iTest interpreter, which does not support all Tcl commands (and supports iTest commands that are not supported by Tcl). Typically, you should use an EXEC eval action. In cases where you need to use a Tcl command that does not exist in the iTest interpreter, however, use scriptEval. See iTest interpreter commands in steps.

![screenshot](topics/images/actions_6.1.jpg) <!-- image_chunk: img_43518fbe2e5b1547 -->

![screenshot](topics/images/actions_3.2.jpg) <!-- image_chunk: img_1c77249d482add61 -->
