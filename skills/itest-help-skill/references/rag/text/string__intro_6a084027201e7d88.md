---
{
  "chunk_id": "string__intro_6a084027201e7d88",
  "source_file": "popups/string.html",
  "source_original_path": "popups/string.html",
  "toc_path": null,
  "heading_path": [
    "string.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_syntax.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [],
  "content_hash": "6a084027201e7d88",
  "level": 0
}
---

# string.html

string option ?arg arg ...?

The iTest string command performs string operations as specified by option.

In addition to the standard string options, the iTest interpreter supports the [string concat arg arg ...] command which concatenates the string representations of all of the arguments into a single string. If all of the arguments are lists, this has the same effect as concatenating them into a single list. The command permits any number of arguments; if no arguments are supplied, the result is an empty string.

The iTest string command is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man with the following limitations:

[string match args] supports only * and ? glob pattern sequences and does not support [chars] and \x.

[string replace] does not accept Tcl's end.

[string trim $attrs , ] is not supported.

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
