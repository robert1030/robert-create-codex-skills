---
{
  "chunk_id": "telnet_session_editor_concept__telnet_session_window_0625fc8be9444e9e",
  "source_file": "topics/telnet_session_editor_concept.htm",
  "source_original_path": "topics/telnet_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Telnet Sessions",
    "Telnet session window"
  ],
  "heading_path": [
    "Telnet session window",
    "Telnet session window"
  ],
  "anchor": "1202625",
  "context_ids": [
    "telnet_session_editor_concept"
  ],
  "index_keywords": [
    "Telnet",
    "session window"
  ],
  "index_keyword_paths": [
    "Telnet > session window",
    "session windows > Telnet"
  ],
  "related_links": [],
  "images": [
    "topics/images/telnet.1.jpg"
  ],
  "content_hash": "0625fc8be9444e9e",
  "level": 1
}
---

# Telnet session window > Telnet session window

The Telnet session window displays your commands and the device's responses. You can think of the editor as a terminal client that iTest is monitoring and capturing.

- The Telnet session window looks just like a Telnet client terminal session. When you type a command and press Enter, the editor displays both the command text that you submitted and the device’s response.

The command/response pair, plus some session information is called a captured item and is listed in the Capture view. Each captured item becomes a step when you save the session as a test case.

- Each session window’s tab displays the session type icon and Session ID (S3 in the example) followed by the name of the session profile that was used to start the session (telnet_DUT4).

- This example Telnet session with a device shows the login process, a show ip traffic command, and the device’s response.

- When you close a session (for example, by issuing an exit command), iTest captures a close Action and then dims the session window.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/telnet.1.jpg) <!-- image_chunk: img_2f82fe02eceba25e -->
