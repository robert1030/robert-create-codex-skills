---
{
  "chunk_id": "command_file_list__notes_on_usage_90354269cff9bf9c",
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
    "Notes on usage"
  ],
  "anchor": "1754989",
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
  "content_hash": "90354269cff9bf9c",
  "level": 3
}
---

# file list command: List the files in a URI > file list command: List the files in a URI > Notes on usage

If the URI is a directory, then all files in the directory are listed.

If the -r argument is used, then the contents of all subdirectories are also listed (this behavior is similar to "ls -R dir in a Linux command shell).

If the directory name is matched with a wildcard (for example, file list temp*), then each matching directory URI is also listed along with its contents.

If the URI is for a filename then the filename is listed. For example file list $dir/*.log lists all log files in directory $dir and file list *.fftc lists all test cases in the same folder as the current test case.

A test case can iterate over the list and use [file isFile URI] or [file isDirectory URI] to help parse the list (provided the -p argument is not used).

If the list URI argument is relative, then a list of project URIs is returned (for example, project://my_project/test_cases/temp/... for relative temp URI).

If the URI argument is for the OS file system, then a list of file URIs is returned (for example, file:/c:/myfiles/...).
