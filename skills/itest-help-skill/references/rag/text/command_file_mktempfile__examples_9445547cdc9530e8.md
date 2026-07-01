---
{
  "chunk_id": "command_file_mktempfile__examples_9445547cdc9530e8",
  "source_file": "topics/command_file_mktempfile.htm",
  "source_original_path": "topics/command_file_mktempfile.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "file mkTempFile command: Create a unique temporary file"
  ],
  "heading_path": [
    "file mkTempFile command: Create a unique temporary file",
    "file mkTempFile command: Create a unique temporary file",
    "Examples"
  ],
  "anchor": "1755058",
  "context_ids": [
    "command_file_mktempfile"
  ],
  "index_keywords": [
    "creating",
    "creating temporary",
    "file mkTempFile",
    "file mkTempFile command"
  ],
  "index_keyword_paths": [
    "commands > file mkTempFile",
    "file mkTempFile command",
    "files > creating temporary",
    "temporary files > creating"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "9445547cdc9530e8",
  "level": 3
}
---

# file mkTempFile command: Create a unique temporary file > file mkTempFile command: Create a unique temporary file > Examples

set myfile [file mkTempFile] returns: [tempdirUri]/iTestTempFile_38343.tmp

set myfile [file mkTempFile my] returns: [tempdirUri]/my38344.tmp

set myfile [file mkTempFile my .log] returns: [tempdirUri]/iTestTempFile_38345.log

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
