---
{
  "chunk_id": "action_signalwait__signalwait_sleep_the_currently_executing_f64e603179a971f5",
  "source_file": "topics/action_signalwait.htm",
  "source_original_path": "topics/action_signalwait.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalWait: Sleep the currently executing thread"
  ],
  "heading_path": [
    "signalWait: Sleep the currently executing thread",
    "signalWait: Sleep the currently executing thread"
  ],
  "anchor": "1530254",
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
  "images": [],
  "content_hash": "f64e603179a971f5",
  "level": 1
}
---

# signalWait: Sleep the currently executing thread > signalWait: Sleep the currently executing thread

The action signalWait causes the currently executing thread to sleep until it is resumed by a call from signal, signalAll, or signalActivate with any one of the specified event names.

| Action | Command property value (in the Description cell) |
| --- | --- |
| signalWait | eventName [, eventName, ...] |

> **Note:** Note In contrast to Java’s implementation, threads that are waiting do not release locks and threads do not need to be inside locked blocks to call a wait.
