---
{
  "chunk_id": "syslog_session_editor_concept__syslog_session_window_66b9a62aacacf825",
  "source_file": "topics/syslog_session_editor_concept.htm",
  "source_original_path": "topics/syslog_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Syslog Sessions",
    "Syslog session window"
  ],
  "heading_path": [
    "Syslog session window",
    "Syslog session window"
  ],
  "anchor": "1090092",
  "context_ids": [
    "syslog_session_editor_concept"
  ],
  "index_keywords": [
    "Syslog session window"
  ],
  "index_keyword_paths": [
    "Syslog session window"
  ],
  "related_links": [
    "preferences_syslog.htm#1123701"
  ],
  "images": [
    "topics/images/syslog.1.jpg"
  ],
  "content_hash": "66b9a62aacacf825",
  "level": 1
}
---

# Syslog session window > Syslog session window

In the Syslog session window, you can use a syslog utility to review and/or wait for certain syslog messages. Each Syslog session monitors the syslog messages that arrive at the built-in iTest syslog server (visible in the Syslog view). Only single-line messages are supported.

While the syslog server receives all messages from all network interfaces on its specified ports, any syslog session can filter the messages based on the following property settings in the session profile:

- Hostname of the originating computer

- Facility number

- Severity level

- Tag (process): In messages that conform to RFC3164, the first word in the message body is called the “tag”.

As a result of configuring one or more of the settings, only the messages that meet the filter settings appear in the session window. This enables your test cases to analyze the particular responses (messages) of interest and to ignore irrelevant messages.

In addition, in the session profile, you can specify a timeout for responses to wait commands.

See Session profile property settings for Syslog sessions.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/syslog.1.jpg) <!-- image_chunk: img_44148eb870885819 -->
