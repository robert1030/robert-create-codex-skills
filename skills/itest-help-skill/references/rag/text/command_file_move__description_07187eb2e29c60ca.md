---
{
  "chunk_id": "command_file_move__description_07187eb2e29c60ca",
  "source_file": "topics/command_file_move.htm",
  "source_original_path": "topics/command_file_move.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "file move command: Move or rename files to a destination URI"
  ],
  "heading_path": [
    "file move command: Move or rename files to a destination URI",
    "file move command: Move or rename files to a destination URI",
    "Description"
  ],
  "anchor": "1755068",
  "context_ids": [
    "command_file_move"
  ],
  "index_keywords": [
    "file move",
    "file move command",
    "moving files",
    "moving or renaming",
    "renaming files"
  ],
  "index_keyword_paths": [
    "commands > file move",
    "file move command",
    "files > moving or renaming",
    "moving files",
    "renaming files"
  ],
  "related_links": [
    "commands_file.htm#1810781"
  ],
  "images": [],
  "content_hash": "07187eb2e29c60ca",
  "level": 3
}
---

# file move command: Move or rename files to a destination URI > file move command: Move or rename files to a destination URI > Description

See Guidelines for using URIs in file commands.

You can use the * wildcard character in the sourceURI but not in destinationURI

- sourceURI must be for an existing folder or files; an error occurs if the source does not exist.

- If sourceURI is a directory name, then destinationURI is interpreted as a directory name.

- If sourceURI is a filename, then:

- If there is no directory with that name, sourceURI is interpreted as a filename (equivalent to rename)

- If there is an existing directory with that name, the new file is created (with the source filename) in the destination directory

- If multiple source files are specified (by using the * wildcard character in the last segment of sourceURI), then the destination is interpreted as a directory.

- Use the * wildcard in URI to represent directories or subdirectories.

- If needed, the destination directory and appropriate parent folders are created.
