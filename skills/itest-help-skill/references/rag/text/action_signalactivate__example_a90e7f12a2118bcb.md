---
{
  "chunk_id": "action_signalactivate__example_a90e7f12a2118bcb",
  "source_file": "topics/action_signalactivate.htm",
  "source_original_path": "topics/action_signalactivate.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalActivate: Turn a signal on"
  ],
  "heading_path": [
    "signalActivate: Turn a signal on",
    "signalActivate: Turn a signal on",
    "Example"
  ],
  "anchor": "1530356",
  "context_ids": [
    "action_signalactivate"
  ],
  "index_keywords": [
    "signalActivate",
    "signalActivate action"
  ],
  "index_keyword_paths": [
    "actions > signalActivate",
    "signalActivate action"
  ],
  "related_links": [],
  "images": [
    "topics/images/thread_safe_synch_5.1.jpg"
  ],
  "content_hash": "a90e7f12a2118bcb",
  "level": 2
}
---

# signalActivate: Turn a signal on > signalActivate: Turn a signal on > Example

1. The signalWait in step 2 of the main procedure ensures that the date command in step 3 of main does not occur until the DUTOpen event is active.

1. The DUTOpen event is activated by the signalActivate in step 3 of the initializeDUTs procedure.

1. As a result, the date command can not occur until it is certain that the session with the DUT is open)

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/thread_safe_synch_5.1.jpg) <!-- image_chunk: img_69eeed28b6bf841a -->
