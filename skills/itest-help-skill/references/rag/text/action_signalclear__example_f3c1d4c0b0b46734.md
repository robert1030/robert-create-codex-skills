---
{
  "chunk_id": "action_signalclear__example_f3c1d4c0b0b46734",
  "source_file": "topics/action_signalclear.htm",
  "source_original_path": "topics/action_signalclear.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalClear: Deactivate a signal"
  ],
  "heading_path": [
    "signalClear: Deactivate a signal",
    "signalClear: Deactivate a signal",
    "Example"
  ],
  "anchor": "1530380",
  "context_ids": [
    "action_signalclear"
  ],
  "index_keywords": [
    "signalClear",
    "signalClear action"
  ],
  "index_keyword_paths": [
    "actions > signalClear",
    "signalClear action"
  ],
  "related_links": [],
  "images": [
    "topics/images/thread_safe_synch_6.1.jpg"
  ],
  "content_hash": "f3c1d4c0b0b46734",
  "level": 2
}
---

# signalClear: Deactivate a signal > signalClear: Deactivate a signal > Example

The signalWait in step 4 of the initializeDUTs procedure can proceed as soon as the DUTClose signal is sent by step 4 of the main procedure. Now that the session will be closed in step 6, we ensure that the DUTOpen signal is deactivated by performing a signalClear in step 5.

This programming practice ensures that any step in some other procedure that depends upon the session with the DUT being open cannot incorrectly try to execute in a session that is closed.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/thread_safe_synch_6.1.jpg) <!-- image_chunk: img_181bc6e2f10129b1 -->
