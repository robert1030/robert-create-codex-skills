---
{
  "chunk_id": "action_continue__the_continue_action_interrupt_a_loop_ite_76d45ef4b44a8788",
  "source_file": "topics/action_continue.htm",
  "source_original_path": "topics/action_continue.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Loop control actions",
    "The ‘continue’ action: Interrupt a loop iteration"
  ],
  "heading_path": [
    "The ‘continue’ action: Interrupt a loop iteration",
    "The ‘continue’ action: Interrupt a loop iteration"
  ],
  "anchor": "1532852",
  "context_ids": [
    "action_continue"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "action_if.htm#1518551",
    "action_then.htm#1662011",
    "action_else.htm#1530733",
    "action_elseif.htm#1519025"
  ],
  "images": [],
  "content_hash": "76d45ef4b44a8788",
  "level": 1
}
---

# The ‘continue’ action: Interrupt a loop iteration > The ‘continue’ action: Interrupt a loop iteration

The continue action causes the current script to be aborted out to the innermost containing for, foreach, or while loop command. The loop then continues with the next iteration of the loop.

> **Note:** Note Python does not use foreach construct in a loop.

Use the continue action when you want to execute particular steps for some iterations of the loop, but not for other iterations.

- The Start this step in a new thread and proceed to the next step property (asynchronous execution) on a continue step is ignored.

- Steps nested inside a continue step are never used.

The ‘if’ action: Element of an if/then or if-elif-else construct

The ‘then’ action: Element of an if/then construct (Tcl)

The ‘else’ action: Element of an if/then or if-else-elif construct

The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
