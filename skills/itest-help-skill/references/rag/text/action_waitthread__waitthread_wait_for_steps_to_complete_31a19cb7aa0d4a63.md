---
{
  "chunk_id": "action_waitthread__waitthread_wait_for_steps_to_complete_31a19cb7aa0d4a63",
  "source_file": "topics/action_waitthread.htm",
  "source_original_path": "topics/action_waitthread.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "waitThread: Wait for steps to complete"
  ],
  "heading_path": [
    "waitThread: Wait for steps to complete",
    "waitThread: Wait for steps to complete"
  ],
  "anchor": "1547585",
  "context_ids": [
    "action_waitthread"
  ],
  "index_keywords": [
    "waitThread",
    "waiting to complete"
  ],
  "index_keyword_paths": [
    "threads > waiting to complete",
    "waitThread action > actions > waitThread"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "31a19cb7aa0d4a63",
  "level": 1
}
---

# waitThread: Wait for steps to complete > waitThread: Wait for steps to complete

Use a waitThread step to ensure that execution does not continue until specified threads finish execution. A waitThread step completes only when the last thread finishes (you specify which threads to wait for). Execution then continues with the next step.

For example, the setup portion of a test case involves configuring three devices (using a call step to each of three different setup procedures). To speed up overall execution by executing the procedures concurrently, you configure each call step to run in a separate thread. You would use a waitThread step after the calls to ensure that execution does not continue until all three procedures finish. In this example, the waitThread step completes only when the last device is configured. Execution then continues with the rest of the test case.
