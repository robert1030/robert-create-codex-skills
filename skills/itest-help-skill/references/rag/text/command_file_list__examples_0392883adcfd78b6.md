---
{
  "chunk_id": "command_file_list__examples_0392883adcfd78b6",
  "source_file": "topics/command_file_list.htm",
  "source_original_path": "topics/command_file_list.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "file list command: List the files in a URI"
  ],
  "heading_path": [
    "file list command: List the files in a URI",
    "file list command: List the files in a URI",
    "Examples"
  ],
  "anchor": "1755008",
  "context_ids": [
    "command_file_list"
  ],
  "index_keywords": [
    "file list",
    "file list command",
    "listing"
  ],
  "index_keyword_paths": [
    "commands > file list",
    "file list command",
    "files > listing"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "0392883adcfd78b6",
  "level": 3
}
---

# file list command: List the files in a URI > file list command: List the files in a URI > Examples

| file list project://my_project/log/*.log | might return: project://my_project/log/file1.log project://my_project/log/file2.log |
| --- | --- |
| file list -r project://my_project/log | ... for the same directory will, in addition, return a list of URIs for all files and sub-directories: project://my_project/log/file1.log project://my_project/log/file2.log project://my_project/log/foo/ project://my_project/log/foo_/file3.log |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
