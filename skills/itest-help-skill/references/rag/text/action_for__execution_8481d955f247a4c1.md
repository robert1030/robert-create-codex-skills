---
{
  "chunk_id": "action_for__execution_8481d955f247a4c1",
  "source_file": "topics/action_for.htm",
  "source_original_path": "topics/action_for.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "For and ForEach loops",
    "The for action: Execute a group of steps in a loop"
  ],
  "heading_path": [
    "The for action: Execute a group of steps in a loop",
    "The for action: Execute a group of steps in a loop",
    "Execution"
  ],
  "anchor": "1661125",
  "context_ids": [
    "action_for"
  ],
  "index_keywords": [
    "for",
    "for action",
    "for loops"
  ],
  "index_keyword_paths": [
    "actions > for",
    "for action",
    "for loops",
    "loops > for"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "8481d955f247a4c1",
  "level": 3
}
---

# The for action: Execute a group of steps in a loop > The for action: Execute a group of steps in a loop > Execution

The for loop in the example follows this logic:

1. Evaluate (execute) set i 0 (i = 10 in Python) one time upon entering the loop. This clause initializes the value that controls the loop. The default initial value of i is 0, but you can replace 0 with any value.

1. 2

1. Evaluate the expression i < 10. (You can replace 10 with any value greater than the initial value of i.)

If True, then continue execution at the next step.

If False, then exit the loop by executing the step after for construct.

> **Tip:** Tip Use a field replacement to set the comparison value dynamically.

1. 3

1. Evaluate incr i in Tcl or i+=1 in Python after the last step in the for construct. The clause increments the value used to control the loop. (Use a negative value to decrement.)

1. 4

1. Repeat steps 2 and 3 until $i < 10 in Tcl or 1 < 10 in Python is False.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
