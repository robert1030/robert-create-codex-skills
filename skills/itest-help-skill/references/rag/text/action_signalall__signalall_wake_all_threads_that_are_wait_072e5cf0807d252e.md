---
{
  "chunk_id": "action_signalall__signalall_wake_all_threads_that_are_wait_072e5cf0807d252e",
  "source_file": "topics/action_signalall.htm",
  "source_original_path": "topics/action_signalall.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalAll: Wake all threads that are waiting on an event"
  ],
  "heading_path": [
    "signalAll: Wake all threads that are waiting on an event",
    "signalAll: Wake all threads that are waiting on an event"
  ],
  "anchor": "1530328",
  "context_ids": [
    "action_signalall"
  ],
  "index_keywords": [
    "signalAll",
    "signalAll action"
  ],
  "index_keyword_paths": [
    "actions > signalAll",
    "signalAll action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "072e5cf0807d252e",
  "level": 1
}
---

# signalAll: Wake all threads that are waiting on an event > signalAll: Wake all threads that are waiting on an event

If there are any threads waiting on eventName, then signalAll eventName wakes all of the threads and causes them to continue execution. If no threads are currently waiting on eventName, then the signalAll step does nothing.

| Action | Command property value (in the Description cell) |
| --- | --- |
| signalAll | eventName |

> **Tip:** Tip If no threads are currently waiting on eventName and you want the event to “stay around” until explicitly “told not to”, then use signalActivate instead.

In addition to configuring signalAll as an Action in a step, you can specify signalAll as an Action for an Event.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
