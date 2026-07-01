---
{
  "chunk_id": "action_if__adding_an_if_then_else_elseif_or_if_elif_4111d988ab7ffee9",
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
    "The ‘if’ action: Element of an if/then or if-elif-else construct",
    "Adding an if-then-else-elseif or if-elif-else construct"
  ],
  "anchor": "1534903",
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
  "related_links": [
    "loops_wrap.htm#1106530"
  ],
  "images": [],
  "content_hash": "4111d988ab7ffee9",
  "level": 2
}
---

# The ‘if’ action: Element of an if/then or if-elif-else construct > The ‘if’ action: Element of an if/then or if-elif-else construct > Adding an if-then-else-elseif or if-elif-else construct

See Inserting for, foreach, if, switch, and while constructs into a test case.

Nested loops (if, for, foreach, and while) are supported.

> **Note:** Note You can use field substitutions in the if clause.

else and elseif (elif for Python) steps in an if construct use the Start this step in a new thread and proceed to the next step (asynchronous execution) property of the if step. The asynchronous execution setting of else and elseif/elif steps are ignored.

You can specify multi-line expressions by clicking Advanced for the command property.

Do not define analysis rules for else steps.

You can nest if-then-else or if-elif-else constructs.

> **Note:** If an if step is skipped, then the entire if construct is skipped. However, you can skip individual else and elseif/elif constructs within the if construct.
