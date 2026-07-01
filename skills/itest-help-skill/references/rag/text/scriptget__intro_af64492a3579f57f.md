---
{
  "chunk_id": "scriptget__intro_af64492a3579f57f",
  "source_file": "popups/scriptget.html",
  "source_original_path": "popups/scriptget.html",
  "toc_path": null,
  "heading_path": [
    "scriptget.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_scriptget.html"
  ],
  "images": [
    "images/scriptget.jpg"
  ],
  "content_hash": "af64492a3579f57f",
  "level": 0
}
---

# scriptget.html

scriptGet gets the value of a variable from the specified interpreter and sets the specified iTest interpreter variable to the value. (By default, the command gets the value from the global Tcl interpreter, but you have the option to specify the session with the target interpreter.)

scriptGet takes two arguments: the name of an iTest variable to be set; and something that is substituted by the interpreter. Command substitution happens on both arguments before the interpreter is asked to interpret the second argument.

In this example, t2 is the iTest variable to get the value, and var2 is the Tcl variable whose value will populate t2. The braces around $var2 prevent substitution, causing it to be passed to the specified interpreter as the string "$var2".

For details on arguments and restrictions, see the online help: The scriptGet action.

![screenshot](images/scriptget.jpg) <!-- image_chunk: img_c317ba89524eda5f -->
