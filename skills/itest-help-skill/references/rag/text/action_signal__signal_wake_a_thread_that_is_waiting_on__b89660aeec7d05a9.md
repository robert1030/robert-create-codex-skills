---
{
  "chunk_id": "action_signal__signal_wake_a_thread_that_is_waiting_on__b89660aeec7d05a9",
  "source_file": "topics/action_signal.htm",
  "source_original_path": "topics/action_signal.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signal: Wake a thread that is waiting on an event"
  ],
  "heading_path": [
    "signal: Wake a thread that is waiting on an event",
    "signal: Wake a thread that is waiting on an event"
  ],
  "anchor": "1530304",
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
  "images": [],
  "content_hash": "b89660aeec7d05a9",
  "level": 1
}
---

# signal: Wake a thread that is waiting on an event > signal: Wake a thread that is waiting on an event

A signal eventName step wakes one thread that is waiting on eventName and causes it to continue execution.

- If several threads are waiting on eventName, then one randomly selected thread continues and the rest continue to wait.

- If no threads are waiting on eventName, then eventName remains signaled until a thread consumes the event or a signalClear action removes it.

| Action | Command property value (in the Description cell) |
| --- | --- |
| signal | eventName |

In addition to configuring signal as an Action in a step, you can specify signal as an Action for an Event.
