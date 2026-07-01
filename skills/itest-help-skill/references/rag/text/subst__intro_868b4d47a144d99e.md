---
{
  "chunk_id": "subst__intro_868b4d47a144d99e",
  "source_file": "topics/popups/subst.html",
  "source_original_path": "topics/popups/subst.html",
  "toc_path": null,
  "heading_path": [
    "subst.html"
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
  "content_hash": "868b4d47a144d99e",
  "level": 0
}
---

# subst.html

subst string

Performs backslash, command, and variable substitutions on the string argument. The substitutions are performed in exactly the same way as for Tcl commands. As a result, the string argument is actually substituted twice; once by the Tcl parser in the usual fashion for Tcl commands, and again by the subst command.

Limitation: No additional arguments are allowed. The command is otherwise compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man

For details on using this and other iTest interpreter commands, see the online help: Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
