---
{
  "chunk_id": "scripteval__intro_de0935ac6eefe715",
  "source_file": "popups/scripteval.html",
  "source_original_path": "popups/scripteval.html",
  "toc_path": null,
  "heading_path": [
    "scripteval.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_scripteval.html"
  ],
  "images": [],
  "content_hash": "de0935ac6eefe715",
  "level": 0
}
---

# scripteval.html

The scriptEval action evaluates the Tcl script specified in the Description cell (the value of the Command property) using the global Tcl interpreter.

- For a Tcl Shell session to access Tcl variables, the session must use the global interpreter. In the Tcl Shell session profile, check the Use global Tcl interpreter during execution property.
- The scriptEval action is not supported in rendered scripts.

The response is populated (including structured data) in a way consistent with how a Tcl Shell Command step works (including result, STDOUT, and/or STDERR).

For details and restrictions, see the online help: The scripteval action.
