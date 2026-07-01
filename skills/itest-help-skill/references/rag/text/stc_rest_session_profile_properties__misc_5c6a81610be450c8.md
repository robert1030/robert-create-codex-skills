---
{
  "chunk_id": "stc_rest_session_profile_properties__misc_5c6a81610be450c8",
  "source_file": "topics/stc_rest_session_profile_properties.htm",
  "source_original_path": "topics/stc_rest_session_profile_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session profiles",
    "Session profile property settings for Spirent TestCenter REST sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent TestCenter REST sessions",
    "Session profile property settings for Spirent TestCenter REST sessions",
    "Misc"
  ],
  "anchor": "1314724",
  "context_ids": [
    "stc_rest_session_profile_properties"
  ],
  "index_keywords": [
    "Spirent TestCenter GUI sessions",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Spirent TestCenter GUI > session profile property settings",
    "session profile property settings > Spirent TestCenter GUI sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "5c6a81610be450c8",
  "level": 2
}
---

# Session profile property settings for Spirent TestCenter REST sessions > Session profile property settings for Spirent TestCenter REST sessions > Misc

| Display slot:port format in responses | When iTest returns responses to commands, it can display port references either in slot:port format (for example, 2:3) or in sequential portIndex format (just the port identifier, for example, 5). Check the box to display in slot:port format. Uncheck to display in portIndex format. Default: unchecked |
| --- | --- |
| Use slot:port format in captured steps | When iTest captures responses to commands, it can create test case steps that use port references in either slot:port format (for example, 2:3) or in sequential portIndex format (just the port identifier, for example, 5). Check the box to create command arguments in slot:port format. Uncheck to use portIndex format. Default: unchecked |
| Use zero-based stream block indices | Check the box to begin counting stream blocks at 0 (zero). That is, the first stream block is 0. If unchecked, then the first stream block is 1. |
| Connect time-out (seconds) | (Mandatory) Specify the maximum number of seconds to wait for a session to connect. Default: 180 |
