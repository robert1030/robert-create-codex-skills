---
{
  "chunk_id": "executing_tests_05__handling_test_cases_that_lasts_more_than_bd3ed37bee569455",
  "source_file": "topics/executing_tests.05.htm",
  "source_original_path": "topics/executing_tests.05.htm",
  "toc_path": [
    "iTest Online Help",
    "Executing Tests",
    "Handling test cases that lasts more than a minute"
  ],
  "heading_path": [
    "Handling test cases that lasts more than a minute",
    "Handling test cases that lasts more than a minute"
  ],
  "anchor": "1390377",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences.08.htm#1249844",
    "preferences_itest.htm#"
  ],
  "images": [],
  "content_hash": "bd3ed37bee569455",
  "level": 1
}
---

# Handling test cases that lasts more than a minute > Handling test cases that lasts more than a minute

iTest supports logging to analyze issues with premature Python interpreter termination when executing Python testcases. If a Python testcase performs long running operations, an INFO level message, Execution is too long, may appear in the Error log (Preferences: Spirent > Log Settings, “Configuring iTest Preferences”). By default, these messages are generated every minute.

If Python testcases contain long-running operations that last more than a minute, you may increase the timeout value and turn of messages using the following commands:

- Increase the timeout value using java option:

-Dlogging.long.execution.seconds=<number of seconds>

- Turn off the messages using -1 as option value:

-Dlogging.long.execution.seconds=-1

To set java option value in iTest GUI and iTestRT follow the instructions below.
