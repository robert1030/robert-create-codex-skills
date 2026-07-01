---
{
  "chunk_id": "split__intro_006f8ab0bf37768f",
  "source_file": "popups/split.html",
  "source_original_path": "popups/split.html",
  "toc_path": null,
  "heading_path": [
    "split.html"
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
  "content_hash": "006f8ab0bf37768f",
  "level": 0
}
---

# split.html

[split string ?splitChars?]

The iTest split command splits a string into a proper Tcl list.

The command returns a list created by splitting string at each character that is in the splitChars argument. Each element of the result list will consist of the characters from string that lie between instances of the characters in splitChars. Empty list elements will be generated if string contains adjacent characters in splitChars, or if the first or last character of string is in splitChars. If splitChars is an empty string, then each character of string becomes a separate element of the result list. splitChars defaults to the standard white-space characters.

The iTest split command is compatible with its Tcl counterpart as more fully described at http://www.tcl.tk/man

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
