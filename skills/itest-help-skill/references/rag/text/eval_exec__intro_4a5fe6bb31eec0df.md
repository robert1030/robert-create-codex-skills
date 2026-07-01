---
{
  "chunk_id": "eval_exec__intro_4a5fe6bb31eec0df",
  "source_file": "topics/popups/eval_exec.html",
  "source_original_path": "topics/popups/eval_exec.html",
  "toc_path": null,
  "heading_path": [
    "eval_exec.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_syntax.html",
    "help::/com.fnfr.svt.help/topics/action_eval.html"
  ],
  "images": [],
  "content_hash": "4a5fe6bb31eec0df",
  "level": 0
}
---

# eval_exec.html

The eval action evaluates the statements specified in the Description cell (the value of the Command property). (The statements must use iTest command syntax, as described in Command syntax for test case steps.)

For example, the eval action with a Command of set port 4 sets the value of a local variable named port to the value 4.

- Because eval operates on the whole command text (which can be multi-line), you can execute multiple statements with a single eval statement.
- There is no Session associated with an eval Action.

For details, see the online help: The eval action.
