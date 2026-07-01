---
{
  "chunk_id": "command_file_copy__description_09d16768af5d5e14",
  "source_file": "topics/command_file_copy.htm",
  "source_original_path": "topics/command_file_copy.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "file copy command: Copying files to a destination URI"
  ],
  "heading_path": [
    "file copy command: Copying files to a destination URI",
    "file copy command: Copying files to a destination URI",
    "Description"
  ],
  "anchor": "1754883",
  "context_ids": [
    "command_file_copy"
  ],
  "index_keywords": [
    "copying",
    "copying files",
    "file copy",
    "file copy command"
  ],
  "index_keyword_paths": [
    "commands > file copy",
    "copying files",
    "file copy command",
    "files > copying"
  ],
  "related_links": [
    "commands_file.htm#1810781"
  ],
  "images": [],
  "content_hash": "09d16768af5d5e14",
  "level": 3
}
---

# file copy command: Copying files to a destination URI > file copy command: Copying files to a destination URI > Description

See Guidelines for using URIs in file commands.

- You can use the * wildcard character in sourceURI but not in destinationURI

- If sourceURI is a directory name, then destinationURI is interpreted as a directory name.

- If sourceURI is a filename, then:

- If there is no directory with that name, sourceURI is interpreted as a filename

- If there is an existing directory with that name, the new file is created (with the source filename) in the destination directory

- If multiple source files are specified (by using the * wildcard in the last segment of the URI), then the destination is interpreted as a directory.

- You can use the * wildcard to represent subdirectories.

- If needed, the destination directory and appropriate parent folders are created.
