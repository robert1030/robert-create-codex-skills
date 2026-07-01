---
{
  "chunk_id": "command_file_move__response_71155003b924c1a8",
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
    "Response"
  ],
  "anchor": "1755084",
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
  "related_links": [],
  "images": [],
  "content_hash": "71155003b924c1a8",
  "level": 3
}
---

# file move command: Move or rename files to a destination URI > file move command: Move or rename files to a destination URI > Response

Returns the number of files moved.

Returned count is 0 when empty directories are moved or renamed.

Returned count is limited to 5000 to ensure reasonable performance after a large directory has been moved or renamed. This does not limit the number of files moved.
