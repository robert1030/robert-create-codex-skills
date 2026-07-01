---
{
  "chunk_id": "regsub__intro_04566a4c2bb7cf1b",
  "source_file": "popups/regsub.html",
  "source_original_path": "popups/regsub.html",
  "toc_path": null,
  "heading_path": [
    "regsub.html"
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
  "content_hash": "04566a4c2bb7cf1b",
  "level": 0
}
---

# regsub.html

The regsub command performs substitutions based on regular expression pattern matching.

The command matches the regular expression regExp against string, and either copies string to the variable whose name is given by varName or returns string if varName is not present.

The syntax of Java regexps patterns is described at http://java.sun.com/javase/6/docs/api/java/util/regex/Pattern.html

The iTest regsub command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
