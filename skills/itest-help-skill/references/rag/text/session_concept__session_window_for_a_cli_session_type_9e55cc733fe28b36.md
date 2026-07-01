---
{
  "chunk_id": "session_concept__session_window_for_a_cli_session_type_9e55cc733fe28b36",
  "source_file": "topics/session_concept.htm",
  "source_original_path": "topics/session_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Windows",
    "Session windows"
  ],
  "heading_path": [
    "Session windows",
    "Session windows",
    "Session window for a CLI session type"
  ],
  "anchor": "1208825",
  "context_ids": [
    "session_concept",
    "session_editor"
  ],
  "index_keywords": [
    "defined",
    "interacting with",
    "session window",
    "session windows",
    "the session windows"
  ],
  "index_keyword_paths": [
    "browsers and terminals > session windows",
    "session window",
    "sessions > defined",
    "sessions > interacting with",
    "terminals and browsers > the session windows"
  ],
  "related_links": [],
  "images": [
    "topics/images/session_windows.1.jpg",
    "topics/images/session_windows.2.jpg"
  ],
  "content_hash": "9e55cc733fe28b36",
  "level": 2
}
---

# Session windows > Session windows > Session window for a CLI session type

For example, the Telnet session window looks just like a Telnet client terminal session. When you type a command and press Enter, the editor displays both the command text that you submitted and the device’s response. (The command/response pair (plus some session information) is called a captured item and is listed in the Capture view.)

Each session window’s tab displays an icon that represents the session type, the unique Session ID (s3 in the example), and the name of the session profile that was used to start the session (telnet_DUT4 in the example).

This example Telnet session with a device shows the login process, a show ip traffic command, and the device’s response — all just like a typical terminal display.

When you close a session (for example, by issuing an exit command), iTest captures a close Action and then dims the session window. At that time, you can save the session or steps from the captured session into a test case.

| o |
| --- |

![screenshot](topics/images/session_windows.1.jpg) <!-- image_chunk: img_b91c859a76412e90 -->

![screenshot](topics/images/session_windows.2.jpg) <!-- image_chunk: img_0ccfe495ce6bb68a -->
