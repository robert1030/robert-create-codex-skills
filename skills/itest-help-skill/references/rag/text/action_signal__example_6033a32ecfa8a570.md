---
{
  "chunk_id": "action_signal__example_6033a32ecfa8a570",
  "source_file": "topics/action_signal.htm",
  "source_original_path": "topics/action_signal.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signal: Wake a thread that is waiting on an event"
  ],
  "heading_path": [
    "signal: Wake a thread that is waiting on an event",
    "signal: Wake a thread that is waiting on an event",
    "Example"
  ],
  "anchor": "1530318",
  "context_ids": [
    "action_signal"
  ],
  "index_keywords": [
    "signal",
    "signal action"
  ],
  "index_keyword_paths": [
    "actions > signal",
    "signal action"
  ],
  "related_links": [],
  "images": [
    "topics/images/thread_safe_synch_4.1.jpg"
  ],
  "content_hash": "6033a32ecfa8a570",
  "level": 2
}
---

# signal: Wake a thread that is waiting on an event > signal: Wake a thread that is waiting on an event > Example

The signalWait in step 4 of the initializeDUTs procedure can proceed only when the DUTClose event is signaled. In step 4 of the main procedure, the signal action signals the DUTClose event to enable the thread that is executing the initializeDUTs procedure to proceed.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/thread_safe_synch_4.1.jpg) <!-- image_chunk: img_bf929e224a1861a0 -->
