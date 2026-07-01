---
{
  "chunk_id": "process_3__tips_for_process_sessions_5dc2fe374135e3ab",
  "source_file": "topics/process.3.htm",
  "source_original_path": "topics/process.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Process Sessions",
    "Tips for Process sessions"
  ],
  "heading_path": [
    "Tips for Process sessions",
    "Tips for Process sessions"
  ],
  "anchor": "1189774",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences.10.htm#1245626",
    "preferences_itest.htm#1186560",
    "quickcalls_overview.htm#1388913",
    "quickcalls_overview.htm#"
  ],
  "images": [
    "topics/images/process.1.jpg"
  ],
  "content_hash": "5dc2fe374135e3ab",
  "level": 1
}
---

# Tips for Process sessions > Tips for Process sessions

- Determining the operating system at runtime: If your test case does not know ahead of time which operating system it will use, then, at runtime, the test case can use a Process show platform command to return the value of the operating system running on the local computer. Subsequent steps can then use this information to specify either backslash \ or forward slash / characters in commands.

- You can set preferences for Process sessions. See Preferences: Spirent > Sessions and Setting iTest preferences.

- A simple and powerful way to execute a series of commands is to save the command text in a text file (for example, a Notepad text file). Use one command per line. Copy the commands and paste them into an active session at the prompt. The commands execute immediately.

- During an interactive session, click in the toolbar and then select the QuickCall from the drop-down list. iTest then executes all of the steps in the QuickCall as if you had typed them yourself. With a single click (typically), you can execute a QuickCall that performs a complex initialization routine or executes a long sequence of related steps.

QuickCalls will save you a lot of time setting up and tearing down, and, for example, can quickly perform the 20 steps that you usually have to type to bring the device into the proper state for that single crucial test step. See Overview: QuickCalls, “QuickCalls: Defining and using a library of custom actions”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/process.1.jpg) <!-- image_chunk: img_e8f0ccea5477f8ac -->
