---
{
  "chunk_id": "capture_view_working_with__using_keyboard_shortcuts_4937845b4110cca6",
  "source_file": "topics/capture_view_working_with.htm",
  "source_original_path": "topics/capture_view_working_with.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Working in the Capture view"
  ],
  "heading_path": [
    "Working in the Capture view",
    "Working in the Capture view",
    "Using keyboard shortcuts"
  ],
  "anchor": "1132622",
  "context_ids": [
    "capture_view_working_with"
  ],
  "index_keywords": [
    "Capture view",
    "saving as Capture reports",
    "saving as procedures",
    "sessions as Capture reports"
  ],
  "index_keyword_paths": [
    "Capture view",
    "saving > sessions as Capture reports",
    "sessions > saving as Capture reports",
    "sessions > saving as procedures",
    "views > Capture view"
  ],
  "related_links": [],
  "images": [
    "topics/images/capture_tasks.07.jpg"
  ],
  "content_hash": "4937845b4110cca6",
  "level": 2
}
---

# Working in the Capture view > Working in the Capture view > Using keyboard shortcuts

For CLI sessions, iTest “cleans up” any keyboard shortcuts like backspace, tab-completion, and up-arrow keystrokes so that the command text in the Capture view reads as if you typed it fully and correctly. (You can configure capture cleanup while defining the session profile properties.)

In the following example, iTest captured the show ip traffic command correctly, even though we actually typed show ip tr<tab>. iTest discarded the intermediate show ip tr<tab> form of the command that we actually typed and uses the “fully-typed” form of the command. This makes it easier to read test cases.

In this example, the command completion form of the command was deleted (show ip tr<tab>). Only the “cleaned up” version of the command (“show ip traffic”) is captured.

![screenshot](topics/images/capture_tasks.07.jpg) <!-- image_chunk: img_52ee21c695962489 -->
