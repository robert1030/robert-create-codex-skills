---
{
  "chunk_id": "loops_wrap__inserting_for_foreach_if_switch_and_whil_b08aa8c1ef84831e",
  "source_file": "topics/loops_wrap.htm",
  "source_original_path": "topics/loops_wrap.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Overview: Loops and flow‑control logic",
    "Inserting for, foreach, if, switch, and while constructs into a test case"
  ],
  "heading_path": [
    "Inserting for, foreach, if, switch, and while constructs into a test case",
    "Inserting for, foreach, if, switch, and while constructs into a test case"
  ],
  "anchor": "1106530",
  "context_ids": [
    "loops_wrap"
  ],
  "index_keywords": [
    "Wrap In",
    "adding to test cases",
    "loops to test cases",
    "wrapping steps inside loops"
  ],
  "index_keyword_paths": [
    "Wrap In",
    "adding > loops to test cases",
    "for loops > adding to test cases",
    "foreach loops > adding to test cases",
    "if-else statements > adding to test cases",
    "loops > adding to test cases",
    "wrapping steps inside loops"
  ],
  "related_links": [
    "action_for.htm#1518031",
    "action_foreach.htm#1518089",
    "action_while.htm#1518303",
    "action_if.htm#1518551",
    "action_switch.htm#1602914"
  ],
  "images": [],
  "content_hash": "b08aa8c1ef84831e",
  "level": 1
}
---

# Inserting for, foreach, if, switch, and while constructs into a test case > Inserting for, foreach, if, switch, and while constructs into a test case

> **Note:** Note Python supports only for, if, and while loop constructs.

The easiest way to add program control logic is to follow this procedure:

1. Create the steps that should appear within the construct (the steps must be a contiguous group).

1. 2

1. Select all the steps (use Shift-click).

1. 3

1. Right-click, and then select Wrap in the type of construct (for example, while statement).

(Alternatively, use the Alt-Shift-w keyboard shortcut)

1. 4

1. iTest adds the appropriate control step (if, for, foreach, switch, or while) and then indents the selected steps to indicate that they are included in the construct.

- If statements wrap the selected steps in a then step and include an else step after the selected steps. You have the option to add an elseif step if needed.

- Switch statements wrap the selected steps in a case step and include a default step after the selected steps.

1. 5

1. Now edit the control step as described in the appropriate section (for example, to set the number of repetitions in the for loop).

The for action: Execute a group of steps in a loop

The foreach action: Execute a group of steps in a loop (Tcl only)

The while action: Repeat the steps in a ‘while’ loop

The ‘if’ action: Element of an if/then or if-elif-else construct

The ‘switch’ action: Control execution flow based on the value of a variable or expression (Tcl) (Tcl only).

> **Note:** Note Python supports for loop construct and not ForEach.

The for action: Execute a group of steps in a loop

The foreach action: Execute a group of steps in a loop

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
