---
{
  "chunk_id": "if_python__intro_c57603268958596f",
  "source_file": "popups/if_python.html",
  "source_original_path": "popups/if_python.html",
  "toc_path": null,
  "heading_path": [
    "if_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/wrap.html",
    "help::/com.fnfr.svt.help/topics/action_if.html"
  ],
  "images": [
    "images/if_elif_else_example_python.jpg"
  ],
  "content_hash": "c57603268958596f",
  "level": 0
}
---

# if_python.html

An if step evaluates the expression that appears in the Description cell (the value of the Command property).

- If the expression is True, then continue execution at the immediately following step.
- If the expression is False, then continue execution at the associated elif action. If there is no elif action, or if the elif action evaluates to False, then continue execution at the associated else action.
- When the steps indented under the else are complete, then continue execution at the immediately following step (that is, after the last step in the if construct).

Nested loops (if, for, and while) are supported.

Note: A legal contiguous sequence of if, elif, and else steps will have one if step, followed by zero or more elif steps followed by zero or one else step. Any other sequence is illegal. No other types of steps within the scope can be interleaved in these sequences.

See the online help for tips on adding if constructs and help on the if action.

![screenshot](images/if_elif_else_example_python.jpg) <!-- image_chunk: img_6cd42e49bd35123c -->
