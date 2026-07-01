---
{
  "chunk_id": "action_lock__example_4537bccaed55e1df",
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
    "Example"
  ],
  "anchor": "1530238",
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
  "images": [
    "topics/images/thread_safe_synch.1.jpg"
  ],
  "content_hash": "4537bccaed55e1df",
  "level": 2
}
---

# lock: Ensure one thread for a specified block of code > lock: Ensure one thread for a specified block of code > Example

The main procedure immediately calls the GetDate procedure.

1. Step 1 of the GetDate procedure sets a lock called s1_lock and then proceeds with its execution.

1. Meanwhile, as main moves on to step 2, it encounters a lock called s1_lock. Because s1_lock is currently in use, main cannot proceed to step 2.1 until the lock is released.

1. The GetDate procedure continues and eventually s1_lock is released after step 1.3 (because step 1.3 is the last step that is indented under the lock in step 1 of the GetDate procedure).

This arrangement ensures that the open action in step 2.1 of main does not occur until the GetDate procedure has finished executing.

![screenshot](topics/images/thread_safe_synch.1.jpg) <!-- image_chunk: img_26072bb0d773584d -->
