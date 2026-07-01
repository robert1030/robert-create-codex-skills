---
{
  "chunk_id": "action_while__execution_9f91432c8e99384b",
  "source_file": "topics/action_while.htm",
  "source_original_path": "topics/action_while.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "While loops",
    "The while action: Repeat the steps in a ‘while’ loop"
  ],
  "heading_path": [
    "The while action: Repeat the steps in a ‘while’ loop",
    "The while action: Repeat the steps in a ‘while’ loop",
    "Execution"
  ],
  "anchor": "1518329",
  "context_ids": [
    "action_while"
  ],
  "index_keywords": [
    "while",
    "while loops"
  ],
  "index_keyword_paths": [
    "actions > while",
    "loops > while",
    "while loops"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "9f91432c8e99384b",
  "level": 3
}
---

# The while action: Repeat the steps in a ‘while’ loop > The while action: Repeat the steps in a ‘while’ loop > Execution

The following process continues until the assertion is false, or the step's timeout (if any) fires, or until execution times out or is canceled:

1. Evaluate the Tcl expression that appears in the Command field. (You can change the example $i < 5 ( i < 5 in Python) expression to meet your need.)

> **Tip:** Tip Use a field replacement to set the comparison value dynamically. The example uses a field replacement that evaluates a parameter named portCount.

1. 2

1. If the expression is True, then execute all steps in the while construct.

> **Note:** Note Typically, one of the steps changes a value that affects the condition — this is what enables the truth of the condition to change. In the example, the EXEC eval incr port step changes the value.

1. 3

1. Return to the while step and evaluate the expression.

If expression is True, then repeat execution.

If the expression is False, then skip to the step after the while construct.
