---
{
  "chunk_id": "test_suites_3__example_execution_sequence_using_all_opt_f4494b889467d6ee",
  "source_file": "topics/test_suites.3.htm",
  "source_original_path": "topics/test_suites.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Suites",
    "Configuring setup and cleanup test cases for folders"
  ],
  "heading_path": [
    "Configuring setup and cleanup test cases for folders",
    "Configuring setup and cleanup test cases for folders",
    "Example execution sequence using all options"
  ],
  "anchor": "1303173",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "f4494b889467d6ee",
  "level": 3
}
---

# Configuring setup and cleanup test cases for folders > Configuring setup and cleanup test cases for folders > Example execution sequence using all options

_setup

folder1/_setup

folder1/folder2/_setup

folder1/_setup_each

folder1/folder2/_setup_each

folder1/folder2/testcase1

folder1/folder2/_cleanup_each

folder1/_cleanup_each

folder1/_setup_each

folder1/folder2/_setup_each

folder1/folder2/testcase2

folder1/folder2/_cleanup_each

folder1/_cleanup_each

folder1/folder2/_cleanup

folder1/_cleanup

_cleanup

> **Tip:** Tip You might want to perform comparatively “bigger” setup/cleanup operations at the higher levels and smaller, faster setup/cleanup at the lower levels and/or in individual setup/cleanup procedures.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
