---
{
  "chunk_id": "action_signalwait__example_c02318f1cff2d935",
  "source_file": "topics/action_signalwait.htm",
  "source_original_path": "topics/action_signalwait.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalWait: Sleep the currently executing thread"
  ],
  "heading_path": [
    "signalWait: Sleep the currently executing thread",
    "signalWait: Sleep the currently executing thread",
    "Example"
  ],
  "anchor": "1530266",
  "context_ids": [
    "action_signalwait"
  ],
  "index_keywords": [
    "signalWait",
    "signalWait action"
  ],
  "index_keyword_paths": [
    "actions > signalWait",
    "signalWait action"
  ],
  "related_links": [],
  "images": [
    "topics/images/thread_safe_synch_2.1.jpg"
  ],
  "content_hash": "c02318f1cff2d935",
  "level": 2
}
---

# signalWait: Sleep the currently executing thread > signalWait: Sleep the currently executing thread > Example

1. The signalWait in step 2 of the main procedure ensures that the date command in step 3 of main does not occur until the DUTOpen event is active.

1. The DUTOpen event is activated by the signalActivate in step 3 of the initializeDUTs procedure.

1. As a result, the date command can not occur until it is certain that the session with the DUT is open)

![screenshot](topics/images/thread_safe_synch_2.1.jpg) <!-- image_chunk: img_bbc1b68572c38f16 -->
