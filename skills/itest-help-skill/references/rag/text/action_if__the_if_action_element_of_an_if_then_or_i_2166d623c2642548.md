---
{
  "chunk_id": "action_if__the_if_action_element_of_an_if_then_or_i_2166d623c2642548",
  "source_file": "topics/action_if.htm",
  "source_original_path": "topics/action_if.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "If / then / else logic",
    "The ‘if’ action: Element of an if/then or if-elif-else construct"
  ],
  "heading_path": [
    "The ‘if’ action: Element of an if/then or if-elif-else construct",
    "The ‘if’ action: Element of an if/then or if-elif-else construct"
  ],
  "anchor": "1518551",
  "context_ids": [
    "action_if"
  ],
  "index_keywords": [
    "if",
    "if loops",
    "if-then",
    "if-then-else-elseif"
  ],
  "index_keyword_paths": [
    "actions > if",
    "actions > if-then",
    "actions > if-then-else-elseif",
    "if loops",
    "if-then",
    "loops > if-then-else-elseif"
  ],
  "related_links": [],
  "images": [
    "topics/images/loops_6.1.jpg",
    "topics/images/if_then_else_example_python.jpg"
  ],
  "content_hash": "2166d623c2642548",
  "level": 1
}
---

# The ‘if’ action: Element of an if/then or if-elif-else construct > The ‘if’ action: Element of an if/then or if-elif-else construct

An if step evaluates the expression that appears in the Description cell (the value of the Command property).

Tcl example:

Python example:

If the expression is True, then continue execution at the immediately following step.

If the expression is False, then continue execution at the associated elseif action (elif action for Python). If there is no elseif/elif action, or if the elseif/elif action evaluates to False, then continue execution at the associated else action.

When the steps indented under the else are complete, then continue execution at the immediately following step (that is, after the last step in the if construct).

![screenshot](topics/images/loops_6.1.jpg) <!-- image_chunk: img_237e9116b3339951 -->

![screenshot](topics/images/if_then_else_example_python.jpg) <!-- image_chunk: img_b4ff1812f2baf61e -->
