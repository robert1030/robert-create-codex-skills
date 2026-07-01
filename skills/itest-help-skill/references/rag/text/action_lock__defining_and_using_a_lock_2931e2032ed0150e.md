---
{
  "chunk_id": "action_lock__defining_and_using_a_lock_2931e2032ed0150e",
  "source_file": "topics/action_lock.htm",
  "source_original_path": "topics/action_lock.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "lock: Ensure one thread for a specified block of code"
  ],
  "heading_path": [
    "lock: Ensure one thread for a specified block of code",
    "lock: Ensure one thread for a specified block of code",
    "Defining and using a lock"
  ],
  "anchor": "1530231",
  "context_ids": [
    "action_lock"
  ],
  "index_keywords": [
    "lock",
    "lock action"
  ],
  "index_keyword_paths": [
    "actions > lock",
    "lock action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "2931e2032ed0150e",
  "level": 2
}
---

# lock: Ensure one thread for a specified block of code > lock: Ensure one thread for a specified block of code > Defining and using a lock

All of the steps that are indented under the lock step are included in the lock. The lock is released when all of the locked steps finish executing.

When a thread arrives at a step that is locked (for example, with lock name lockA), it determines whether the lock is currently in use. Then:

- If the lock is not in use, the thread executes the step

- If the lock is in use, the thread waits until the lock is released

- If the thread owns lockA, it can enter any step that is locked on lockA. (This prevents deadlock if a locked step calls a procedure that has a step that is locked on the same lock.)

> **Caution:** CAUTION You are allowed to start new threads of execution inside a locked block, but this practice can render the code not thread safe. The new thread will own no locks and will proceed until either the thread ends or it hits another locked region.
