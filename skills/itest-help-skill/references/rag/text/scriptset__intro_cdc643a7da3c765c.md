---
{
  "chunk_id": "scriptset__intro_cdc643a7da3c765c",
  "source_file": "topics/popups/scriptset.html",
  "source_original_path": "topics/popups/scriptset.html",
  "toc_path": null,
  "heading_path": [
    "scriptset.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_scriptset.html"
  ],
  "images": [],
  "content_hash": "cdc643a7da3c765c",
  "level": 0
}
---

# scriptset.html

The scriptSet action sets the value of a specified variable in the specified interpreter (typically, the global Tcl interpreter, but you have the option to specify the interpreter). scriptSet works for any kind of variable, including lists, arrays, lists of lists, numbers, and so on. You can specify multiple values.

For example, an analysis rule has extracted a list of values. We have set the value of an iTest interpreter variable called var1 with the list. To pass the list of values into an interpreter variable called t1 in the global Tcl interpreter's context, you can use the following scriptSet step:

For details on arguments and restrictions, see the online help: The scriptSet action.
