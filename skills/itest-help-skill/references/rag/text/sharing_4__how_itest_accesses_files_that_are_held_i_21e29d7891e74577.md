---
{
  "chunk_id": "sharing_4__how_itest_accesses_files_that_are_held_i_21e29d7891e74577",
  "source_file": "topics/sharing.4.htm",
  "source_original_path": "topics/sharing.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Sharing iTest Resources",
    "Accessing iTest files that are held in iTar files"
  ],
  "heading_path": [
    "Accessing iTest files that are held in iTar files",
    "Accessing iTest files that are held in iTar files",
    "How iTest accesses files that are held in iTar files"
  ],
  "anchor": "1121318",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "21e29d7891e74577",
  "level": 2
}
---

# Accessing iTest files that are held in iTar files > Accessing iTest files that are held in iTar files > How iTest accesses files that are held in iTar files

If iTest looks for a file in the current workspace and does not find it, then iTest.exe will look in following places for files that are held in iTar files, in the following order:

- In any directory (or file) that is referenced using an --itar command-line option when eclipse/iTest is started

- In a iTar directory immediately under the workspace root

- In any directory (or file) referenced using an ITAR_PATH environment variable.

To enable this capability, define an ITAR_PATH environment variable for the path. The ITAR_PATH environment variable uses the same conventions as the CLASSPATH environment variable (delimiters, quotes for paths that include spaces, and so on).

> **Note:** Note The path that you specify for ITAR_PATH cannot contain the path separator character.Linux: Paths cannot contain ":"

> **Note:** Windows: Paths cannot contain ";"
