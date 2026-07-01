---
{
  "chunk_id": "action_signalwaitall__signalwaitall_wait_until_all_specified_e_272c161ea5087928",
  "source_file": "topics/action_signalwaitall.htm",
  "source_original_path": "topics/action_signalwaitall.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "signalWaitAll: Wait until all specified events have been signaled or activated"
  ],
  "heading_path": [
    "signalWaitAll: Wait until all specified events have been signaled or activated",
    "signalWaitAll: Wait until all specified events have been signaled or activated"
  ],
  "anchor": "1530280",
  "context_ids": [
    "action_signalwaitall"
  ],
  "index_keywords": [
    "signalWaitAll",
    "signalWaitAll action"
  ],
  "index_keyword_paths": [
    "actions > signalWaitAll",
    "signalWaitAll action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "272c161ea5087928",
  "level": 1
}
---

# signalWaitAll: Wait until all specified events have been signaled or activated > signalWaitAll: Wait until all specified events have been signaled or activated

The action signalWaitAll causes the currently executing thread to sleep until all specified events have been signaled or activated (by signal, signalAll, or signalActivate).

> **Note:** Note In contrast to Java’s implementation, threads that are waiting do not release locks and threads do not need to be inside locked blocks to call a wait.

| Action | Command property value (in the Description cell) |
| --- | --- |
| signalWaitAll | eventName [, eventName, ...] |
