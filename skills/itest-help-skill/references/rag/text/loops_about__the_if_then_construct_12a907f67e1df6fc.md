---
{
  "chunk_id": "loops_about__the_if_then_construct_12a907f67e1df6fc",
  "source_file": "topics/loops_about.htm",
  "source_original_path": "topics/loops_about.htm",
  "toc_path": [
    "iTest Online Help",
    "Controlling execution flow: Loops, If/Then, and Switch",
    "Overview: Loops and flow‑control logic",
    "Overview: Loops and flow‑control logic"
  ],
  "heading_path": [
    "Overview: Loops and flow‑control logic",
    "Overview: Loops and flow‑control logic",
    "The if / then construct"
  ],
  "anchor": "1531495",
  "context_ids": [
    "loops_about"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "for loop > defined",
    "foreach loop > defined",
    "if-then logic > defined",
    "while loop > defined"
  ],
  "related_links": [
    "action_if.htm#1518551"
  ],
  "images": [
    "topics/images/loops.6.jpg",
    "topics/images/if_then_else_example_python.jpg"
  ],
  "content_hash": "12a907f67e1df6fc",
  "level": 2
}
---

# Overview: Loops and flow‑control logic > Overview: Loops and flow‑control logic > The if / then construct

An if step evaluates the expression that appears in the Description cell (the value of the Command property).

Python:

If the expression is True, then continue execution at the immediately following step.

If the expression is False, then continue execution at the associated elseif action. If there is no elseif or elif action, or if the elseif/elif action evaluates to False, then continue execution at the associated else action.

When the steps indented under the else are complete, then continue execution at the immediately following step (that is, after the last step in the if construct).

See The ‘if’ action: Element of an if/then or if-elif-else construct for instructions on creating an if-then-else-elseif construct and a detailed description of how if constructs operate.

![screenshot](topics/images/loops.6.jpg) <!-- image_chunk: img_e0bb335b90cd8357 -->

![screenshot](topics/images/if_then_else_example_python.jpg) <!-- image_chunk: img_b4ff1812f2baf61e -->
