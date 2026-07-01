---
{
  "chunk_id": "test_cases_portable_tc__making_your_test_cases_more_portable_a5b32a9a243dd6b4",
  "source_file": "topics/test_cases_portable_tc.htm",
  "source_original_path": "topics/test_cases_portable_tc.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Cases",
    "Test suites: Organizing tests for group execution",
    "Making your test cases more portable"
  ],
  "heading_path": [
    "Making your test cases more portable",
    "Making your test cases more portable"
  ],
  "anchor": "1713980",
  "context_ids": [
    "test_cases_portable_tc"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "a5b32a9a243dd6b4",
  "level": 1
}
---

# Making your test cases more portable > Making your test cases more portable

In an open step, if you use the URI of a device (for example, device:my_devices/DUT_34) rather than a session profile, your test case becomes portable — it can execute as it is on any topology that includes a reference to the device. (In contrast, if the step refers to a session profile, then, when you hand it off to a coworker, you have to include the session profile too — the profile can get out-of-synch over time.) Follow this process to create an open step that refers to a device URI rather than to a session profile:

1. 1

1. Start a session from the Favorites view: Open a topology. Right-click the device and select Start.

1. 2

1. Perform the manual session as you normally would.

1. 3

1. When you save the captured steps to a test case, the resulting open step uses a “device:” URI instead of a reference to a session profile. In addition, the Local Topology property for the test case is updated to refer to the corresponding file.
