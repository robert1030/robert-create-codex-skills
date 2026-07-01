---
{
  "chunk_id": "array__intro_94cd5fb235af95d8",
  "source_file": "popups/array.html",
  "source_original_path": "popups/array.html",
  "toc_path": null,
  "heading_path": [
    "array.html"
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
  "content_hash": "94cd5fb235af95d8",
  "level": 0
}
---

# array.html

array ?-g? subcommand arrayName ?arg arg ...?

Performs the specified operation on the existing array variable given by arrayName. The optional -g argument indicates a global array.

For array commands that use the optional pattern, only the * and ? wildcard characters are supported. The [chars] and \x options are not supported. The following subcommands are supported:

compare array1 array2 exists arrayName get arrayName ?pattern? names arrayName ?pattern? set arrayName list size arrayName unset arrayName ?pattern?

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
