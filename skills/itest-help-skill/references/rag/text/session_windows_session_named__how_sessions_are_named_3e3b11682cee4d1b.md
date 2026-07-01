---
{
  "chunk_id": "session_windows_session_named__how_sessions_are_named_3e3b11682cee4d1b",
  "source_file": "topics/session_windows_session_named.htm",
  "source_original_path": "topics/session_windows_session_named.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Windows",
    "How sessions are named"
  ],
  "heading_path": [
    "How sessions are named",
    "How sessions are named"
  ],
  "anchor": "1210706",
  "context_ids": [
    "session_windows_session_named"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/session_windows_3.1.jpg"
  ],
  "content_hash": "3e3b11682cee4d1b",
  "level": 1
}
---

# How sessions are named > How sessions are named

The tabs for active session windows display a name that is generated from several sources: First, an icon reflecting the session type, then the Session ID, followed by a colon and the name of the session profile that was used to launch the session. In the example,

- The session profile is named SNMP_10.23.45.67

- The Session ID is myDUT.5

For devices with more than one session attached or for multiple captures that use the same session profile: To create the Session IDs that appear in the Session cells in the Test Case editor and in test reports, Spirent iTest uses the combination of Session name from the session profile (for example, myDUT) and a unique session number for the day. (for example, myDUT.1 and myDUT.2). If the session profile does not specify a Session name, then Spirent iTest uses the filename of the session profile in its place.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/session_windows_3.1.jpg) <!-- image_chunk: img_e4117183f36d46f4 -->
