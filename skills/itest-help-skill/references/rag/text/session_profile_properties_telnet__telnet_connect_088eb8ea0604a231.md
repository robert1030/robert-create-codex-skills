---
{
  "chunk_id": "session_profile_properties_telnet__telnet_connect_088eb8ea0604a231",
  "source_file": "topics/session_profile_properties_telnet.htm",
  "source_original_path": "topics/session_profile_properties_telnet.htm",
  "toc_path": [
    "iTest Online Help",
    "Telnet Sessions",
    "Session profile property settings for Telnet sessions"
  ],
  "heading_path": [
    "Session profile property settings for Telnet sessions",
    "Session profile property settings for Telnet sessions",
    "Telnet > Connect"
  ],
  "anchor": "1152798",
  "context_ids": [
    "session_profile_properties_telnet"
  ],
  "index_keywords": [
    "Additional connection information property",
    "Configuring Telnet",
    "HA mode",
    "High Availability Mode property",
    "Negotiate Telnet options",
    "Telnet options",
    "Telnet property settings",
    "Telnet sessions",
    "configuring",
    "configuring socket",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Negotiate Telnet options",
    "Telnet > configuring socket",
    "Telnet options",
    "Telnet sessions > configuring",
    "Telnet sessions > session profile property settings",
    "configuring > Telnet sessions",
    "property settings > Telnet sessions",
    "session profiles > Telnet property settings",
    "socket > Configuring Telnet"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "088eb8ea0604a231",
  "level": 2
}
---

# Session profile property settings for Telnet sessions > Session profile property settings for Telnet sessions > Telnet > Connect

| Connect timeout | Specify how long to wait (in seconds) for the session to start. Default: 30 seconds |
| --- | --- |
| Retry count | Specify how often to retry the connection when the connection attempt times out. Default: 1 |
| Negotiate Telnet options | Cause the terminal application to negotiate Telnet options with the host. Default: checked |
| Ignore Telnet options in data stream | Uncheck the box to parse and implement the bytes in the data stream that encode Telnet options. Check the box to ignore the data. If you check the box and also uncheck the Negotiate Telnet options property, then the Telnet session is a raw socket client. Default: unchecked |
