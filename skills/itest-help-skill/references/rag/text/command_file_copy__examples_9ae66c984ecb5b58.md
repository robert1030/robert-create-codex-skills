---
{
  "chunk_id": "command_file_copy__examples_9ae66c984ecb5b58",
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
    "Examples"
  ],
  "anchor": "1754920",
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
  "related_links": [],
  "images": [],
  "content_hash": "9ae66c984ecb5b58",
  "level": 3
}
---

# file copy command: Copying files to a destination URI > file copy command: Copying files to a destination URI > Examples

| file copy -r tmp save | Copies directory 'tmp' (relative to test case URI) and its contents to a new relative directory 'save' |
| --- | --- |
| file copy tmp/my.log file:/c:/logfiles/new.log | Copies my.log file to new.log |
| file copy ../my.log [file pathToUri [info homeDir]] | Copies my.log file from parent directory to user's home directory |
| file copy -y project://my_project/*.log save | Copies all log files to 'save' directory relative to test case URI |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
