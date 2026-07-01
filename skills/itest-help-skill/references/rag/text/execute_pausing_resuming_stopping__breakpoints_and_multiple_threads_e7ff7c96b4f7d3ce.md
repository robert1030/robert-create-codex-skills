---
{
  "chunk_id": "execute_pausing_resuming_stopping__breakpoints_and_multiple_threads_e7ff7c96b4f7d3ce",
  "source_file": "topics/execute_pausing_resuming_stopping.htm",
  "source_original_path": "topics/execute_pausing_resuming_stopping.htm",
  "toc_path": [
    "iTest Online Help",
    "Debugging Test Cases",
    "Debugging: Executing procedures, Pausing, stopping, and single-stepping"
  ],
  "heading_path": [
    "Debugging: Executing procedures, Pausing, stopping, and single-stepping",
    "Debugging: Executing procedures, Pausing, stopping, and single-stepping",
    "Breakpoints and multiple threads"
  ],
  "anchor": "1194150",
  "context_ids": [
    "execute_pausing_resuming_stopping"
  ],
  "index_keywords": [
    "executing while paused",
    "pausing execution",
    "pausing stopping single-stepping debugging",
    "pausing stopping single-stepping executing procedures",
    "resuming execution",
    "single-stepping",
    "stopping execution"
  ],
  "index_keyword_paths": [
    "debugging > pausing stopping single-stepping executing procedures",
    "execution > pausing stopping single-stepping debugging",
    "pausing execution",
    "procedures > executing while paused",
    "resuming execution",
    "single-stepping",
    "stopping execution"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "e7ff7c96b4f7d3ce",
  "level": 2
}
---

# Debugging: Executing procedures, Pausing, stopping, and single-stepping > Debugging: Executing procedures, Pausing, stopping, and single-stepping > Breakpoints and multiple threads

Remember that common situations such as asynchronous steps or calls to foreign procedures initiate new threads. If a procedure is running multiple threads, then when any thread reaches a breakpoint, all threads pause upon completion of the executing step in each thread.

For more details on thread behavior, see the Threads view.

> **Note:** Note iTest ignores breakpoints on skipped steps — the steps are skipped without pausing execution.
