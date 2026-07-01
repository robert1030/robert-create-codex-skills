---
{
  "chunk_id": "breakpoints_view__breakpoints_and_multiple_threads_0b6f1678851b75ac",
  "source_file": "topics/breakpoints_view.htm",
  "source_original_path": "topics/breakpoints_view.htm",
  "toc_path": [
    "iTest Online Help",
    "Debugging Test Cases",
    "Breakpoints view"
  ],
  "heading_path": [
    "Breakpoints view",
    "Breakpoints view",
    "Breakpoints and multiple threads"
  ],
  "anchor": "1119129",
  "context_ids": [
    "breakpoints_view"
  ],
  "index_keywords": [
    "Breakpoints view"
  ],
  "index_keyword_paths": [
    "Breakpoints view",
    "views > Breakpoints view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "0b6f1678851b75ac",
  "level": 2
}
---

# Breakpoints view > Breakpoints view > Breakpoints and multiple threads

Remember that common situations such as asynchronous steps or calls to foreign procedures initiate new threads. If a procedure is running multiple threads, then when any thread reaches a breakpoint, all threads pause upon completion of the executing step in each thread.

For more details on thread behavior, see the Threads view.

> **Note:** Note iTest ignores breakpoints on skipped steps — the steps are skipped without pausing execution.
