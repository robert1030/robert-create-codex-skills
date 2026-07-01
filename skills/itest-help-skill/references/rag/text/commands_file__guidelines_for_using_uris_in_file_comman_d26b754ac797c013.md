---
{
  "chunk_id": "commands_file__guidelines_for_using_uris_in_file_comman_d26b754ac797c013",
  "source_file": "topics/commands_file.htm",
  "source_original_path": "topics/commands_file.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "Commands for managing files and directories"
  ],
  "heading_path": [
    "Commands for managing files and directories",
    "Commands for managing files and directories",
    "Guidelines for using URIs in file commands"
  ],
  "anchor": "1810781",
  "context_ids": [
    "commands_file"
  ],
  "index_keywords": [
    "file",
    "file commands"
  ],
  "index_keyword_paths": [
    "commands > file",
    "file commands"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "d26b754ac797c013",
  "level": 2
}
---

# Commands for managing files and directories > Commands for managing files and directories > Guidelines for using URIs in file commands

For all commands in the file group, the following requirements apply:

- The URI argument cannot be a native file path — it must be a URI (for example, project://my_project/myFiles).

- Relative URIs, file URIs, and project URIs are supported (for example, tmp/*.txt, file:/c:/mypath, project://my_project/tmp). Relative URIs are resolved relative to the current test case URI.

- Parent directory references ".." are supported.

- Field replacements are not supported in URIs.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
