---
{
  "chunk_id": "scan__intro_57ee475c9b0f17f3",
  "source_file": "topics/popups/scan.html",
  "source_original_path": "topics/popups/scan.html",
  "toc_path": null,
  "heading_path": [
    "scan.html"
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
  "content_hash": "57ee475c9b0f17f3",
  "level": 0
}
---

# scan.html

[scan string format ?varName varName ...?]

The scan command parses substrings from an input string in a fashion similar to the ANSI C sscanf procedure.

The command returns a count of the number of conversions performed, or -1 if the end of the input string is reached before any conversions have been performed. string gives the input to be parsed and format indicates how to parse it, using % conversion specifiers as in sscanf. Each varName gives the name of a variable; when a substring is scanned from string that matches a conversion specifier, the substring is assigned to the corresponding variable. If no varName variables are specified, then scan works in an inline manner, returning the data that would otherwise be stored in the variables as a list. In the inline case, an empty string is returned when the end of the input string is reached before any conversions have been performed.

The iTest scan command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
