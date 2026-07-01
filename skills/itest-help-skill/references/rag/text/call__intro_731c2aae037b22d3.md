---
{
  "chunk_id": "call__intro_731c2aae037b22d3",
  "source_file": "popups/call.html",
  "source_original_path": "popups/call.html",
  "toc_path": null,
  "heading_path": [
    "call.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_call.html",
    "help::/com.fnfr.svt.help/topics/action_write.html"
  ],
  "images": [],
  "content_hash": "731c2aae037b22d3",
  "level": 0
}
---

# call.html

The call action transfers execution from the current procedure (the caller) to the first step in a different procedure (the called procedure).

- The call action can pass arguments to procedures.
- When the called procedure exits, execution returns to the caller.
- Procedures can call procedures in a nested fashion.
- call creates an executed step in test reports. The step contains any response data, and the calling step's analysis rule applies in the normal way to the returned data.

Important: Because the call action alters the flow of execution, it is deferred (not executed) until execution completes for all preceding steps.

A call action has the following content in the Description cell (all items are separated by spaces):

- The procedure name
- Optional: Any number of named arguments in the format -namedArg_1 value
- Optional: Any number of values for un-named arguments

For example:

call procedureName slot slotNumber port porttNumber numberOfRepetitions

call ExercisePorts -slot 3 -port 4 75

For details, see the online help: The call action.

Also, see the help for the write action.
