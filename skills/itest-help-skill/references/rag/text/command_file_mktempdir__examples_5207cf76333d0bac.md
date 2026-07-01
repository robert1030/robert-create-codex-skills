---
{
  "chunk_id": "command_file_mktempdir__examples_5207cf76333d0bac",
  "source_file": "topics/command_file_mktempdir.htm",
  "source_original_path": "topics/command_file_mktempdir.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "file mkTempDir command: Create a unique temporary directory"
  ],
  "heading_path": [
    "file mkTempDir command: Create a unique temporary directory",
    "file mkTempDir command: Create a unique temporary directory",
    "Examples"
  ],
  "anchor": "1755039",
  "context_ids": [
    "command_file_mktempdir"
  ],
  "index_keywords": [
    "creating",
    "creating temporary",
    "file mkTempDir",
    "file mkTempDir command"
  ],
  "index_keyword_paths": [
    "commands > file mkTempDir",
    "directories > creating temporary",
    "file mkTempDir command",
    "folders > creating temporary",
    "temporary directories > creating"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "5207cf76333d0bac",
  "level": 3
}
---

# file mkTempDir command: Create a unique temporary directory > file mkTempDir command: Create a unique temporary directory > Examples

set mydir [file mkTempDir] returns: [tempdirUri]/iTestTempDir_45376/

set mydir [file mkTempDir my] returns: [tempdirUri]/my45377/

set mydir [file mkTempDir my bah] returns: [tempdirUri]/my45378bah/

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
