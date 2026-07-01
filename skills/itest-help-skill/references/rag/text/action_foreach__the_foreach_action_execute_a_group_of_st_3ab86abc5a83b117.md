---
{
  "chunk_id": "action_foreach__the_foreach_action_execute_a_group_of_st_3ab86abc5a83b117",
  "source_file": "topics/action_foreach.htm",
  "source_original_path": "topics/action_foreach.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "For and ForEach loops",
    "The foreach action: Execute a group of steps in a loop"
  ],
  "heading_path": [
    "The foreach action: Execute a group of steps in a loop",
    "The foreach action: Execute a group of steps in a loop"
  ],
  "anchor": "1518089",
  "context_ids": [
    "action_foreach"
  ],
  "index_keywords": [
    "foreach",
    "foreach loops"
  ],
  "index_keyword_paths": [
    "actions > foreach",
    "foreach loops",
    "loops > foreach"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3ab86abc5a83b117",
  "level": 1
}
---

# The foreach action: Execute a group of steps in a loop > The foreach action: Execute a group of steps in a loop

> **Note:** Note Python supports for loop construct and not ForEach.

A foreach loop performs the steps within the loop for each value in a specified set of values.

The statement in the Description cell (the value of the Command property) of a foreach step follows Tcl foreach syntax and takes an even number of lists and goes through the lists two at a time. The first is a list of variables and the second is the list of values that the variables take on. A foreach loop is composed of all of the steps that are indented under the foreach clause.

Nested loops (if, for, foreach, and while) are supported.
