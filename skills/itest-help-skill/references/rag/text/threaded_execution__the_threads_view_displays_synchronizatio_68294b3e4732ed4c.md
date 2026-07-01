---
{
  "chunk_id": "threaded_execution__the_threads_view_displays_synchronizatio_68294b3e4732ed4c",
  "source_file": "topics/threaded_execution.htm",
  "source_original_path": "topics/threaded_execution.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "Overview: Synchronizing threaded execution in iTest"
  ],
  "heading_path": [
    "Overview: Synchronizing threaded execution in iTest",
    "Overview: Synchronizing threaded execution in iTest",
    "The Threads view displays synchronization information"
  ],
  "anchor": "1530096",
  "context_ids": [
    "threaded_execution"
  ],
  "index_keywords": [
    "asynchronous execution overview",
    "multi-threaded execution overview"
  ],
  "index_keyword_paths": [
    "asynchronous execution overview",
    "multi-threaded execution overview"
  ],
  "related_links": [
    "threads_view.htm#1119502"
  ],
  "images": [],
  "content_hash": "68294b3e4732ed4c",
  "level": 2
}
---

# Overview: Synchronizing threaded execution in iTest > Overview: Synchronizing threaded execution in iTest > The Threads view displays synchronization information

To support you while you develop and debug Tcl test cases, the following columns in the Threads view display synchronization information:

| Awaited signals | Displays the names of any signals that must be activated for the step to proceed. The signal can come from a signal, signalAll, or signalActivate step. For signalWaitAll steps, all of the signals in the list must be active before the step can proceed. |
| --- | --- |
| Owned locks | Displays the names of all locks that the step owns — locks that were set by the step or by a parent step. |
| Awaited lock | Displays the name of the lock that must be released for the step to proceed. |

For more information on the Threads view, see Threads view.
