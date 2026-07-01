---
{
  "chunk_id": "thread_safe_synch_02__overview_actions_that_help_you_to_synchr_d1db6e842debab09",
  "source_file": "topics/thread_safe_synch.02.htm",
  "source_original_path": "topics/thread_safe_synch.02.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "Overview: Actions that help you to synchronize (lock) threads"
  ],
  "heading_path": [
    "Overview: Actions that help you to synchronize (lock) threads",
    "Overview: Actions that help you to synchronize (lock) threads"
  ],
  "anchor": "1530124",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "action_lock.htm#1530220",
    "action_signalwait.htm#1530254",
    "action_signalwaitall.htm#1530280",
    "action_signalactivate.htm#1530343",
    "action_signalall.htm#1530328",
    "action_signalclear.htm#1530368"
  ],
  "images": [],
  "content_hash": "d1db6e842debab09",
  "level": 1
}
---

# Overview: Actions that help you to synchronize (lock) threads > Overview: Actions that help you to synchronize (lock) threads

Follow these guidelines in naming signal events:

- Must be alphanumeric and can include underscore characters

- Support field substitution.

| Action | Command property value (in the Description cell) | Description |
| --- | --- | --- |
| Note You can perform the following actions only as EXEC actions in steps (and not as Actions for Events). | Note | You can perform the following actions only as EXEC actions in steps (and not as Actions for Events). |
| Note | You can perform the following actions only as EXEC actions in steps (and not as Actions for Events). |  |
| lock | lockName | Ensures that only one thread at a time is working inside the set of steps that is locked on lockName. See lock: Ensure one thread for a specified block of code. |
| signalWait | eventName [, eventName, ...] | Causes the currently executing thread to sleep until it is resumed by a call from signal, signalAll, or signalActivate with any one of the specified event names. See signalWait: Sleep the currently executing thread. |
| signalWaitAll | eventName [, eventName, ...] | Causes the currently executing thread to sleep until all specified events have been signaled or activated (by signal, signalAll, or signalActivate), and proceeds only when all the signals in the list are active. See signalWaitAll: Wait until all specified events have been signaled or activated. |
| Note You can configure the following actions both as EXEC Actions in steps and as Actions defined for Events. | Note | You can configure the following actions both as EXEC Actions in steps and as Actions defined for Events. |
| Note | You can configure the following actions both as EXEC Actions in steps and as Actions defined for Events. |  |
| signal | eventName | Wakes the current thread waiting on eventName and causes it to continue execution. See signalActivate: Turn a signal on. |
| signalAll | eventName | Wakes all threads that are waiting on the eventName. and causes it to continue execution. See signalAll: Wake all threads that are waiting on an event. |
| signalActivate | eventName | Turns on the event called eventName. See signalActivate: Turn a signal on. |
| signalClear | eventName | Removes any instances of the event named eventName that had previously been activated either by a signalActivate step or by a signal command. See signalClear: Deactivate a signal. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
