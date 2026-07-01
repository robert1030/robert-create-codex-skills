---
{
  "chunk_id": "action_run__about_the_itest_interpreter_and_the_tcl__8888f3d4c8e2765b",
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
    "About the iTest interpreter and the Tcl interpreters"
  ],
  "anchor": "1809404",
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
  "related_links": [],
  "images": [],
  "content_hash": "8888f3d4c8e2765b",
  "level": 2
}
---

# The ‘eval’ action: Evaluate an iTest interpreter command > The ‘eval’ action: Evaluate an iTest interpreter command > About the iTest interpreter and the Tcl interpreters



Actions that operate in the iTest environment: eval, set, get

The iTest interpreter performs tasks that are useful in the iTest environment. We designed the syntax to be very much like Tcl so that the commands would be easier to understand. You can use iTest interpreter commands to perform a variety of tasks; some commands set a variable value (set), get a variable value (get), perform mathematical operations (math.abs), return information about iTest (info), or access the response to an earlier step (response).

Some iTest interpreter commands have Tcl counterparts and some do not. For example, you can use set i 0 (which uses the same syntax as Tcl) to assign the value 0 to the variable i. You can then use i as a local variable in your test case with the value $i.

You can use the iTest eval action to evaluate the iTest commands (actually, statements) that are specified in the Description cell.
