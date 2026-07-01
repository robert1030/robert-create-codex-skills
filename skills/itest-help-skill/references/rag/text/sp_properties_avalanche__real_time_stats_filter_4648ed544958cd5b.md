---
{
  "chunk_id": "sp_properties_avalanche__real_time_stats_filter_4648ed544958cd5b",
  "source_file": "topics/sp_properties_avalanche.htm",
  "source_original_path": "topics/sp_properties_avalanche.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Session profile property settings for Spirent Avalanche sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent Avalanche sessions",
    "Session profile property settings for Spirent Avalanche sessions",
    "Real-time Stats Filter"
  ],
  "anchor": "1196951",
  "context_ids": [
    "sp_properties_avalanche"
  ],
  "index_keywords": [
    "Avalanche sessions",
    "property settings",
    "sessions"
  ],
  "index_keyword_paths": [
    "Avalanche sessions",
    "Avalanche sessions > property settings",
    "Spirent Avalanche > sessions",
    "configuring > Avalanche sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "4648ed544958cd5b",
  "level": 2
}
---

# Session profile property settings for Spirent Avalanche sessions > Session profile property settings for Spirent Avalanche sessions > Real-time Stats Filter

During test execution, the server and client clusters return real-time statistics that depend on the test type. The full statistics table is quite large, and you can use the Real-time Stats Filter properties to limit the data that iTest captures and displays in the Console view.

| Client real-time stats filter | Optional. Specify a search string. You can use the * wildcard character. iTest then captures and displays only the client data with matching text. In the example, we applied the following filter text: *timeElapsed* *http* |
| --- | --- |
| Server real-time stats filter | Optional. Specify a search string. You can use the * wildcard character. iTest then captures and displays only the server data with matching text. In the example, we applied the following filter text: *timeElapsed* *tcpConn* |
