---
{
  "chunk_id": "serial_session_editor_concept__serial_session_window_852ff2bd4b7ab11c",
  "source_file": "topics/serial_session_editor_concept.htm",
  "source_original_path": "topics/serial_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Serial Sessions",
    "Serial session window"
  ],
  "heading_path": [
    "Serial session window",
    "Serial session window"
  ],
  "anchor": "1090918",
  "context_ids": [
    "serial_session_editor_concept"
  ],
  "index_keywords": [
    "Serial",
    "session window"
  ],
  "index_keyword_paths": [
    "Serial  sessions > session window",
    "session windows > Serial"
  ],
  "related_links": [],
  "images": [
    "topics/images/serial.1.jpg"
  ],
  "content_hash": "852ff2bd4b7ab11c",
  "level": 1
}
---

# Serial session window > Serial session window

For Serial sessions, the computer running iTest communicates directly over a serial port connection with the device under test.

For each open session, the Serial Port session window displays your commands and the device's responses. You can think of the session window as a terminal client — a terminal that iTest is monitoring and capturing.

The session window looks just like a client terminal session. When you type a command and press Enter, the editor displays both the command text that you submitted and the device’s response. (The command/response pair (plus some session information) is called a captured item and is listed in the Capture view.)

1. The tab for the session window displays the session type icon and the name of the session profile that was used to start the session as the Session ID (serial_dev_ttyS0 in this example).

1. 2

1. This example session shows the login process, a show log command, and the device’s response.

When you close a session (for example, by issuing an exit command), iTest captures a close Action and then dims the session window.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/serial.1.jpg) <!-- image_chunk: img_0d1f980d49eaf86d -->
