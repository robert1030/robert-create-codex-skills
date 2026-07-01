---
{
  "chunk_id": "wireshark_session_window__wireshark_session_window_eac14f2d3e7b9137",
  "source_file": "topics/wireshark_session_window.htm",
  "source_original_path": "topics/wireshark_session_window.htm",
  "toc_path": [
    "iTest Online Help",
    "Wireshark sessions",
    "Wireshark session window"
  ],
  "heading_path": [
    "Wireshark session window",
    "Wireshark session window"
  ],
  "anchor": "1203251",
  "context_ids": [
    "wireshark_session_window"
  ],
  "index_keywords": [
    "Wireshark",
    "session window"
  ],
  "index_keyword_paths": [
    "Wireshark sessions > session window",
    "sessions > Wireshark"
  ],
  "related_links": [],
  "images": [
    "topics/images/wireshark.1.jpg"
  ],
  "content_hash": "eac14f2d3e7b9137",
  "level": 1
}
---

# Wireshark session window > Wireshark session window

Wireshark must be added to the system PATH for correct execution of Wireshark sessions.

| OS | The path to TShark executable will be listed in PATH environment variable |
| --- | --- |
| Microsoft Windows | Advanced system settings > Environment variables> Path |
| Linux | /usr/local/bin |
| macOS | /Applications/Wireshark.app/Contents/MacOS |

> **Tip:** Tip If TShark is not installed in the above paths, ensure that you configure TShark path manually in the Session profile properties.

> **Note:** Note After installing WireShark, ensure that you reboot the host before launching WireShark shell and iTest.

Wireshark sessions provide a command line interface for interactively capturing packets from a network interface. For commands that return status and packet data, iTest saves the responses as structured data and generates associated queries to simplify pass/fail analysis.

While the native Wireshark command set is designed to manage the application, iTest uses an abstracted command set that is optimized for automation (for example, commands like waiting for a capture to be completed while filtering the particular data to capture). Session profile properties specify the network interface, a capture filter and display filter, and advanced capture properties for use with tshark.

When a Wireshark session is closed, capture stops and all resources used by the session are released.

![screenshot](topics/images/wireshark.1.jpg) <!-- image_chunk: img_6d811bab88ca90d1 -->
