---
{
  "chunk_id": "action_else__the_else_action_element_of_an_if_then_or_daa45e7d0c97806b",
  "source_file": "topics/action_else.htm",
  "source_original_path": "topics/action_else.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "If / then / else logic",
    "The ‘else’ action: Element of an if/then or if-else-elif construct"
  ],
  "heading_path": [
    "The ‘else’ action: Element of an if/then or if-else-elif construct",
    "The ‘else’ action: Element of an if/then or if-else-elif construct"
  ],
  "anchor": "1530733",
  "context_ids": [
    "action_else"
  ],
  "index_keywords": [
    "Element of an if/then or if-else-elif construct” on page 325",
    "Element of an if/then/if-else-elif construct” on page 325",
    "else",
    "else action",
    "if-then-else"
  ],
  "index_keyword_paths": [
    "actions > else",
    "else action",
    "if-then-else",
    "“The ‘if’ action > Element of an if/then or if-else-elif construct” on page 325",
    "“The ‘if’ action > Element of an if/then/if-else-elif construct” on page 325"
  ],
  "related_links": [
    "action_if.htm#1518551"
  ],
  "images": [
    "topics/images/loops_8.1.jpg",
    "topics/images/loops_2.2.jpg"
  ],
  "content_hash": "daa45e7d0c97806b",
  "level": 1
}
---

# The ‘else’ action: Element of an if/then or if-else-elif construct > The ‘else’ action: Element of an if/then or if-else-elif construct

> **Note:** Note Python uses the if-elif-else construct and not the if/then construct. The ‘if’ action: Element of an if/then or if-elif-else construct.

An optional EXEC else step is a part of an if-then-else-elseif construct in Tcl and if-elif-else construct in Python.

An else step is similar to elseif/elif, but it must come last in the sequence of steps associated with the if construct. See The ‘if’ action: Element of an if/then or if-elif-else construct for full details.

If the assertion associated with the else is True, then its nested steps will be executed as long as no previous associated if or elseif has been actioned.

![screenshot](topics/images/loops_8.1.jpg) <!-- image_chunk: img_cc3fea66a1e14b27 -->

![screenshot](topics/images/loops_2.2.jpg) <!-- image_chunk: img_bacae7d71e8990d7 -->
