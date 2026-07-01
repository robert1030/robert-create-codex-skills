---
{
  "chunk_id": "sharing_4__executing_test_cases_that_are_held_in_it_15d874713b17d4a3",
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
    "Executing test cases that are held in iTar files"
  ],
  "anchor": "1102537",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "15d874713b17d4a3",
  "level": 2
}
---

# Accessing iTest files that are held in iTar files > Accessing iTest files that are held in iTar files > Executing test cases that are held in iTar files

iTest looks for files in iTar files in the following order:

- If a run step refers to the URI project://com.fnfr.project2/icmp_echo_verify.fftc, then iTest will look for a project named com.fnfr.project2 in the workspace.

- If found, then it will look in the project for icmp_echo_verify.fftc.

- Otherwise, it will look in the <workspaceName>/iTar directory for a file named com.fnfr.project2.itar. It will look in the iTar for icmp_echo_verify.fftc. If found, it will be used.

- Otherwise, it will look in all the directories in ITAR_PATH for a file named com.fnfr.project2.itar. It will look in the iTar for icmp_echo_verify.fftc

> **Note:** Note Once iTest finds a matching project source, no additional sources will be searched, even if that first source does not contain the path or file requested.
