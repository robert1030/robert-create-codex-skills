---
{
  "chunk_id": "waitthread__intro_6560a4c3a8bb93a2",
  "source_file": "popups/waitthread.html",
  "source_original_path": "popups/waitthread.html",
  "toc_path": null,
  "heading_path": [
    "waitthread.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/action_waitthread.html"
  ],
  "images": [],
  "content_hash": "6560a4c3a8bb93a2",
  "level": 0
}
---

# waitthread.html

A waitThread step completes only when each thread that you specify finishes execution. You specify the threads to wait for in the Command property for the step.

To use the feature:

For each asynch step to wait for:

- Check the Start this step (in a new thread) and proceed to the next step box.
- Specify a name for the thread in the threadName property. The name need not be unique. Field replacements are supported.

Create the the step that will wait:

- After the asynch steps, add a step with an EXEC action of waitThread.
- Specify the threads that the waitThread step should wait for: In the Command property, specify the threadName values of the threads. This can be a wildcarded list and can make use of field substitution.

More detailed description and instructions appear in the online help at: The waitThread action: Waiting for asynchronous steps to complete.
