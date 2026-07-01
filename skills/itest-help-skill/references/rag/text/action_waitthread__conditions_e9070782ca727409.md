---
{
  "chunk_id": "action_waitthread__conditions_e9070782ca727409",
  "source_file": "topics/action_waitthread.htm",
  "source_original_path": "topics/action_waitthread.htm",
  "toc_path": [
    "iTest Online Help",
    "Making your test case thread-safe",
    "waitThread: Wait for steps to complete"
  ],
  "heading_path": [
    "waitThread: Wait for steps to complete",
    "waitThread: Wait for steps to complete",
    "Conditions"
  ],
  "anchor": "1518729",
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
  "content_hash": "e9070782ca727409",
  "level": 2
}
---

# waitThread: Wait for steps to complete > waitThread: Wait for steps to complete > Conditions

- If iTest encounters a waitThread step and none of the currently active thread is one of the threads listed in the waitThread step’s command, then execution continues immediately.

- If multiple threads have the same name, then the waitThread step completes only when the last thread with that name finishes.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
