---
{
  "chunk_id": "capture_open_and_close_concept__open_and_close_steps_in_test_cases_59ea8435da1b6fe6",
  "source_file": "topics/capture_open_and_close_concept.htm",
  "source_original_path": "topics/capture_open_and_close_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Open and Close steps"
  ],
  "heading_path": [
    "Open and Close steps",
    "Open and Close steps",
    "Open and close steps in test cases"
  ],
  "anchor": "1131859",
  "context_ids": [
    "capture_open_and_close_concept"
  ],
  "index_keywords": [
    "defined",
    "open and close"
  ],
  "index_keyword_paths": [
    "captured items > open and close",
    "close and open actions > defined",
    "open and close actions > defined",
    "session open and close actions > defined"
  ],
  "related_links": [
    "action_open.htm#1530382",
    "action_close.htm#1530707"
  ],
  "images": [
    "topics/images/capture_tasks_4.2.jpg"
  ],
  "content_hash": "59ea8435da1b6fe6",
  "level": 2
}
---

# Open and Close steps > Open and Close steps > Open and close steps in test cases

Each session in a test case starts with an open action as its first step. See The open action: Start a session.

The Command property for an open step must be a full Spirent URL (typically, the URL of a session profile, but other URL types are supported, as described in The open action: Start a session. (iTest populates the URL when you save a captured session as a procedure.)

There are special properties for an open step.

Each step in a test case that interacts with a session must specify the name of the session in the Session property.

The last step for a session is typically a close step.

When you add the first step to a new procedure, iTest inserts an open step. You complete the step by selecting a session profile from the drop-down list in the Description cell.

Notice that open and close actions appear in a separate group in the Action drop-down list. This indicates that open and close are special: All sessions must start with an open step and typically include a close step. See The open action: Start a session and The close action: Close a session.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/capture_tasks_4.2.jpg) <!-- image_chunk: img_4c2047696b970da9 -->
