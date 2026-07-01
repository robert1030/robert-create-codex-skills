---
{
  "chunk_id": "action_waitthread__creating_a_waitthread_step_23e515dffea46fee",
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
    "Creating a waitThread step"
  ],
  "anchor": "1518716",
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
  "related_links": [
    "test_cases_naming_variables_procedures.htm#1562803"
  ],
  "images": [],
  "content_hash": "23e515dffea46fee",
  "level": 2
}
---

# waitThread: Wait for steps to complete > waitThread: Wait for steps to complete > Creating a waitThread step

1. For each step that you want to wait for, set the following property values (in the General property group):

- Specify that the step should execute asynchronously: Check the Start this step (in a new thread) and proceed to the next step box.

- Specify a name for the thread in the threadName property.

Follow the naming guidelines listed in Naming variables and procedures.

The name need not be unique. If multiple threads share a name, then the waitThread step is activated only when the last thread with the shared name finishes.

Because field replacements are supported in the text, you can define a name that can be generated dynamically (for example, in a loop with the loop count as the replacement text).

1. 2

1. Create the step that will wait:

- After the asynch steps, add a step with an EXEC action of waitThread.

- Specify the threads that the waitThread step should wait for: In the Command property, specify the threadName values of the threads. This can be a wildcarded list and can make use of field substitution.
