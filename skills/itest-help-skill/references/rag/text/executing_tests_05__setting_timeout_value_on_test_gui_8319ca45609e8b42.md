---
{
  "chunk_id": "executing_tests_05__setting_timeout_value_on_test_gui_8319ca45609e8b42",
  "source_file": "topics/executing_tests.05.htm",
  "source_original_path": "topics/executing_tests.05.htm",
  "toc_path": [
    "iTest Online Help",
    "Executing Tests",
    "Handling test cases that lasts more than a minute"
  ],
  "heading_path": [
    "Handling test cases that lasts more than a minute",
    "Handling test cases that lasts more than a minute",
    "Setting timeout value on Test GUI"
  ],
  "anchor": "1390605",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "8319ca45609e8b42",
  "level": 3
}
---

# Handling test cases that lasts more than a minute > Handling test cases that lasts more than a minute > Setting timeout value on Test GUI

1. Edit the file in the installation folder: <installation folder>/iTest.ini file.

1. 2

1. Insert option on a separate line after -vmargs line:

-vmargs

-Dlogging.long.execution.seconds=-1

..

1. 3

1. Save file and restart iTest.
