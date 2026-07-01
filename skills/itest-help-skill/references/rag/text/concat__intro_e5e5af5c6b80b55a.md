---
{
  "chunk_id": "concat__intro_e5e5af5c6b80b55a",
  "source_file": "topics/popups/concat.html",
  "source_original_path": "topics/popups/concat.html",
  "toc_path": null,
  "heading_path": [
    "concat.html"
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
  "content_hash": "e5e5af5c6b80b55a",
  "level": 0
}
---

# concat.html

concat ?arg arg ...?

Joins each of its arguments together with spaces after trimming leading and trailing white-space from each of them. If all the arguments are lists, this has the same effect as concatenating them into a single list. It permits any number of arguments; if no args are supplied, the result is an empty string.

To insert a concat command, right-click in the field and then select Insert > Special Actions > Concatenate Strings.

The iTest concat command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
