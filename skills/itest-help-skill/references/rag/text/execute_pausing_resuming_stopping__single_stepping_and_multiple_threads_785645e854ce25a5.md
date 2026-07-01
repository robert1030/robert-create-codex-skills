---
{
  "chunk_id": "execute_pausing_resuming_stopping__single_stepping_and_multiple_threads_785645e854ce25a5",
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
    "Single-stepping and multiple threads"
  ],
  "anchor": "1112753",
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
  "content_hash": "785645e854ce25a5",
  "level": 2
}
---

# Debugging: Executing procedures, Pausing, stopping, and single-stepping > Debugging: Executing procedures, Pausing, stopping, and single-stepping > Single-stepping and multiple threads

Single-step execution has unique behaviors when multiple threads are running. One thread is always designated as the “foreground thread,” and is highlighted in the Threads view. Each click of Execute One Step moves the procedure through the foreground thread one step at a time. For more details, see the Threads view.

> **Note:** Note When you click Execute One Step, the procedure pauses at the completion of each step in the foreground thread exactly as if it had reached a breakpoint. Other threads then pause on completion of their respective executing steps. If any other thread reaches a breakpoint, then that thread becomes the foreground thread from that point on.

Because of this behavior, We recommend that you use the Threads view to keep track of the foreground thread whenever you are single-stepping through a procedure with multiple threads.
