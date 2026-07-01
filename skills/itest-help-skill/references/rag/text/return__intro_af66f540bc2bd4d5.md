---
{
  "chunk_id": "return__intro_af66f540bc2bd4d5",
  "source_file": "popups/return.html",
  "source_original_path": "popups/return.html",
  "toc_path": null,
  "heading_path": [
    "return.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_return.html"
  ],
  "images": [],
  "content_hash": "af66f540bc2bd4d5",
  "level": 0
}
---

# return.html

A return step stops executing the current procedure and returns execution from the current procedure to the caller.

This means to either continue processing the procedure whose call step (or CallProcedure action) caused the procedure to start, or end test case execution if the procedure was the initial entry point. Any threads started by the procedure continue.

- You can return a value for the procedure. The text specified for the specified in the Description cell (the value of the Command property) of the return step is appended to the response of the call step. The text string can contain field replacements (for example, [response var_name]).
- The Start this step in a new thread and proceed to the next step (asynchronous execution) property on a return step is ignored.
- Steps nested inside return steps are never executed.

Tip: You can use a return step in the main procedure to exit a test case. Because you do not typically want to return every time the test case runs, you'll probably include the return step within an if construct.

For details, see the online help: The return action.

Also, see the help for the related write action.
