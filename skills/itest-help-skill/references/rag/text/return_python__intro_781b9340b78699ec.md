---
{
  "chunk_id": "return_python__intro_781b9340b78699ec",
  "source_file": "popups/return_python.html",
  "source_original_path": "popups/return_python.html",
  "toc_path": null,
  "heading_path": [
    "return_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_return.html"
  ],
  "images": [],
  "content_hash": "781b9340b78699ec",
  "level": 0
}
---

# return_python.html

A return step stops executing the current procedure and returns execution from the current procedure to the caller.

This means to either continue processing the procedure whose call step caused the procedure to start, or end test case execution if the procedure was the initial entry point. Any threads started by the procedure continue.

- You can return a value for the procedure. The text specified for the specified in the Description cell (the value of the Command property) of the return step is appended to the response of the call step).
- Steps nested inside return steps are never executed.

Tip: You can use a return step in the main procedure to exit a test case. Because you do not typically want to return every time the test case runs, you will probably include the return step within an if construct.

For details, see the online help: The return action.

Also, see the help for the related write action.
