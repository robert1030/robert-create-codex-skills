---
{
  "chunk_id": "action_break_loop__the_break_action_break_out_of_a_loop_4b418885c0e3bf5f",
  "source_file": "topics/action_break_loop.htm",
  "source_original_path": "topics/action_break_loop.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Loop control actions",
    "The ‘break’ action: Break out of a loop"
  ],
  "heading_path": [
    "The ‘break’ action: Break out of a loop",
    "The ‘break’ action: Break out of a loop"
  ],
  "anchor": "1532697",
  "context_ids": [
    "action_break_loop"
  ],
  "index_keywords": [
    "break",
    "breaking out of",
    "breaking out of loops"
  ],
  "index_keyword_paths": [
    "actions > break",
    "actions > breaking out of loops",
    "break action > breaking out of loops",
    "breaking out of loops",
    "loops > breaking out of"
  ],
  "related_links": [
    "action_break.htm#1592856"
  ],
  "images": [
    "topics/images/loops_5.1.jpg"
  ],
  "content_hash": "4b418885c0e3bf5f",
  "level": 1
}
---

# The ‘break’ action: Break out of a loop > The ‘break’ action: Break out of a loop

There are two distinct kinds of break action:

- Break CLI session execution (marked #1 in the example): The break that appears in the first group of actions sends the break character for CLI sessions (typically Ctrl+C). See The break action: Send the break character.

- Break out of a loop (marked #2 in the example): The break that appears in the list of EXEC actions breaks out of a for, foreach (in Tcl), or while loop. Use this break action to stop executing a loop and continue executing at the step after the loop.

- The Start this step in a new thread and proceed to the next step (asynchronous execution) property on a break step is ignored.

- Steps nested inside a break step are never used.

![screenshot](topics/images/loops_5.1.jpg) <!-- image_chunk: img_893f7091aafe8737 -->
