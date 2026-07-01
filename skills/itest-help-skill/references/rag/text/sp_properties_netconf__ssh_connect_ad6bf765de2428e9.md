---
{
  "chunk_id": "sp_properties_netconf__ssh_connect_ad6bf765de2428e9",
  "source_file": "topics/sp_properties_netconf.htm",
  "source_original_path": "topics/sp_properties_netconf.htm",
  "toc_path": [
    "iTest Online Help",
    "NetConf Sessions",
    "Session profile property settings for NetConf sessions"
  ],
  "heading_path": [
    "Session profile property settings for NetConf sessions",
    "Session profile property settings for NetConf sessions",
    "Spirent NetConf",
    "SSH > Connect"
  ],
  "anchor": "1089421",
  "context_ids": [
    "sp_properties_netconf"
  ],
  "index_keywords": [
    "NetConf sessions",
    "configuring",
    "session profile property settings for"
  ],
  "index_keyword_paths": [
    "NetConf sessions > configuring",
    "NetConf sessions > session profile property settings for",
    "configuring > NetConf sessions",
    "session profile property settings > NetConf sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "ad6bf765de2428e9",
  "level": 3
}
---

# Session profile property settings for NetConf sessions > Session profile property settings for NetConf sessions > Spirent NetConf > SSH > Connect

| Connect timeout | Specify how long to wait (in seconds) for the session to start. Default: 30 seconds |
| --- | --- |
| Retry count | Specify how often to retry the connection when the connection attempt times out. Default: 1 |
| Seconds between keepalives | Some devices are configured to close a session if no traffic occurs for a specified period. To ensure that the session is not auto-closed, iTest can send keepalive signals during periods of silence on the line. Specify the number of seconds that should elapse between keepalives. Default: 0 (do not send keepalives) |
