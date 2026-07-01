---
{
  "chunk_id": "preferences_syslog__spirent_session_types_syslog_865da8b269d746e7",
  "source_file": "topics/preferences_syslog.htm",
  "source_original_path": "topics/preferences_syslog.htm",
  "toc_path": [
    "iTest Online Help",
    "Syslog Sessions",
    "Session profile property settings for Syslog sessions"
  ],
  "heading_path": [
    "Session profile property settings for Syslog sessions",
    "Session profile property settings for Syslog sessions",
    "Spirent > Session Types > Syslog"
  ],
  "anchor": "1123595",
  "context_ids": [
    "preferences_syslog",
    "sp_properties_syslog"
  ],
  "index_keywords": [
    "Syslog sessions",
    "preference settings",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Syslog sessions > preference settings",
    "Syslog sessions > session profile property settings",
    "preference settings > Syslog sessions",
    "session profile property settings > Syslog sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "865da8b269d746e7",
  "level": 2
}
---

# Session profile property settings for Syslog sessions > Session profile property settings for Syslog sessions > Spirent > Session Types > Syslog

| Comma-separated list of syslog ports | The syslog server receives all messages from all network interfaces on the ports that you specify here. Separate ports using commas. Changes to this setting take effect immediately, with the following exception: Currently active Syslog sessions lose the additional ports that are specified in the session profile (unless they are now specified in this property setting). To activate the ports specified in the session profile, you must restart the sessions. Default: 514 Note For some platforms (such as Linux and Solaris), port numbers in this range may be disallowed for use by normal processes like iTest. In these cases, use a different port number (above 1024 in most cases). You must also configure Syslog clients to send to this new port. | Note | For some platforms (such as Linux and Solaris), port numbers in this range may be disallowed for use by normal processes like iTest. In these cases, use a different port number (above 1024 in most cases). You must also configure Syslog clients to send to this new port. |
| --- | --- | --- | --- |
| Note | For some platforms (such as Linux and Solaris), port numbers in this range may be disallowed for use by normal processes like iTest. In these cases, use a different port number (above 1024 in most cases). You must also configure Syslog clients to send to this new port. |  |  |
| Maximum number of messages in Syslog view before aging | The syslog server holds a large number of messages, up to the specified limit. When the message count exceeds the limit, the syslog server deletes (ages) the oldest messages to make room for new messages. Default: 400 |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
