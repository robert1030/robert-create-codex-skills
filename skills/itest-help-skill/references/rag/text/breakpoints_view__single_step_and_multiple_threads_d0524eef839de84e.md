---
{
  "chunk_id": "breakpoints_view__single_step_and_multiple_threads_d0524eef839de84e",
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
    "Resuming execution after a breakpoint",
    "Single-step and multiple threads"
  ],
  "anchor": "1119134",
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
  "content_hash": "d0524eef839de84e",
  "level": 3
}
---

# Breakpoints view > Breakpoints view > Resuming execution after a breakpoint > Single-step and multiple threads

Single-step execution has unique behavior when multiple threads are running. One thread is always designated as the “foreground thread,” and is highlighted in the Threads view. Each click of Execute one step moves the procedure through the foreground thread one step at a time.

> **Note:** Note When you click Execute one step, the procedure pauses at the completion of each step in the foreground thread exactly as if it had reached a breakpoint. Other threads then pause on completion of their respective executing steps. If any other thread reaches a breakpoint, then that thread becomes the foreground thread from that point on.

Because of this behavior, We recommend that you use the Threads view to keep track of the foreground thread whenever you are single-stepping through a procedure with multiple threads.
