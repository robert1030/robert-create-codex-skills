---
{
  "chunk_id": "lreplace__intro_da83a5ab9577cbb2",
  "source_file": "topics/popups/lreplace.html",
  "source_original_path": "topics/popups/lreplace.html",
  "toc_path": null,
  "heading_path": [
    "lreplace.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/command_syntax.html"
  ],
  "images": [],
  "content_hash": "da83a5ab9577cbb2",
  "level": 0
}
---

# lreplace.html

lreplace list first last ?element element ...?

lreplace returns a new list formed by replacing one or more elements of list with the element arguments. first and last are index values specifying the first and last elements of the range to replace. The index values first and last are interpreted the same as index values for the command string index, supporting simple index arithmetic and indices relative to the end of the list. 0 refers to the first element of the list, and end refers to the last element of the list. If list is empty, then first and last are ignored.

The element arguments specify zero or more new arguments to be added to the list in place of those that were deleted. Each element argument will become a separate element of the list. If no element arguments are specified, then the elements between first and last are simply deleted. If list is empty, any element arguments are added to the end of the list.

The lrange command is compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man

For details on each iTest command, see the online help: Command syntax for test case steps.
