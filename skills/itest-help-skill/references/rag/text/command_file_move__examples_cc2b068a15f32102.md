---
{
  "chunk_id": "command_file_move__examples_cc2b068a15f32102",
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
    "Examples"
  ],
  "anchor": "1755107",
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
  "content_hash": "cc2b068a15f32102",
  "level": 3
}
---

# file move command: Move or rename files to a destination URI > file move command: Move or rename files to a destination URI > Examples

| file copy -r tmp save | Copies directory 'tmp' (relative to test case URI) and its contents to a new relative directory 'save' |
| --- | --- |
| file copy tmp/my.log file:/c:/logfiles/new.log | Copies my.log file to new.log |
| file copy ../my.log [file pathToUri [info homeDir]] | Copies my.log file from parent directory to user's home directory |
| file copy -y project://my_project/*.log save | Copies all log files to 'save' directory relative to test case URI |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
