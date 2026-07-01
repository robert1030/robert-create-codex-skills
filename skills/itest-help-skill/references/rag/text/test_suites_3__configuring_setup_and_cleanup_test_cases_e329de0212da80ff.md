---
{
  "chunk_id": "test_suites_3__configuring_setup_and_cleanup_test_cases_e329de0212da80ff",
  "source_file": "topics/test_suites.3.htm",
  "source_original_path": "topics/test_suites.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Suites",
    "Configuring setup and cleanup test cases for folders"
  ],
  "heading_path": [
    "Configuring setup and cleanup test cases for folders",
    "Configuring setup and cleanup test cases for folders"
  ],
  "anchor": "1303166",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tse_test_groups_page.htm#1304133",
    "tse_test_groups_page.htm#1196514"
  ],
  "images": [],
  "content_hash": "e329de0212da80ff",
  "level": 1
}
---

# Configuring setup and cleanup test cases for folders > Configuring setup and cleanup test cases for folders

Often, you need to run setup procedures before executing all tests in a folder and/or before each test. Similarly, you might need to run cleanup procedures after tests. Test suites support all such cases.

> **Note:** Note To specify that setup/ cleanup should occur for a test group, see Global Setup / Cleanup properties.

To enable this feature:

- Check the Run setup/cleanup tests per folder and/or Run setup/cleanup tests per test properties, as described in Sorting properties: Specify the order of execution.

- Name the setup/cleanup test cases as described here .

- Setup before executing all the test cases in a directory: If a directory includes a test case named _setup, then it is executed before executing any of the test cases in the directory (or its subdirectories). If there is also a _setup test case in a subdirectory, then it also runs before the test cases in its directory (and further subdirectories).

> **Note:** Note The top-most _setup always executes first, even if the first test case eligible for execution is in a subdirectory.

- Setup before executing each test case in a directory: If a directory includes a test case named _setup_each, then it is executed before each eligible test case in its directory (including subdirectories). If there is a _setup_each in a child directory, then it executes after the _setup_each test case in its parent directory but before each test in its directory.

- Cleanup after executing all the test cases in a directory: A test case named _cleanup behaves in a similar way as _setup, but after all test cases have been executed and after its child directories.

- Cleanup after executing each test case in a directory: A test case named _cleanup_each behaves in a similar way as _setup_each, but after each eligible test case in its directory (including child directories). For test cases in child directories, it executes after any _cleanup_each in the child directory.

> **Note:** Note All test cases starting with "_" are excluded from the test case filtering process.
