---
{
  "chunk_id": "action_elseif__substitutions_in_the_command_property_te_70d8b4e4e944688b",
  "source_file": "topics/action_elseif.htm",
  "source_original_path": "topics/action_elseif.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "If / then / else logic",
    "The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct"
  ],
  "heading_path": [
    "The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct",
    "The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-elseconstruct",
    "Substitutions in the Command property text"
  ],
  "anchor": "1519047",
  "context_ids": [
    "action_elseif"
  ],
  "index_keywords": [
    "Element of an if/then or if-else-elif construct” on page 325",
    "elseif or elif",
    "elseif or elif action"
  ],
  "index_keyword_paths": [
    "actions > elseif or elif",
    "elseif or elif action",
    "“The ‘if’ action > Element of an if/then or if-else-elif construct” on page 325"
  ],
  "related_links": [
    "action_if.htm#1518551",
    "action_continue.htm#1532852",
    "action_break_loop.htm#1532697"
  ],
  "images": [],
  "content_hash": "70d8b4e4e944688b",
  "level": 2
}
---

# The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct > The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-elseconstruct > Substitutions in the Command property text

The command of the if construct is directed at the iTest interpreter. To ensure that iTest commands like [tcl ] or [tclexpr ] will be correctly interpreted, the text in the Description cell (actually, the text for the Command property) is interpreted as literal text.

The property that controls field replacements (command substitution) for the step is disabled and dimmed (the For the Command field, perform command, variable, and backslash substitution checkbox is unchecked).

As a result, the text is not processed for the following substitution types before the step is executed (substitution occurs during execution):

Command field replacements (char, expr, param, query, and response)

Variables

Backslash characters used to escape special characters

See The ‘if’ action: Element of an if/then or if-elif-else construct, The ‘continue’ action: Interrupt a loop iteration, and The ‘break’ action: Break out of a loop.

> **Note:** Note Switch logic does not apply to Python test cases

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
