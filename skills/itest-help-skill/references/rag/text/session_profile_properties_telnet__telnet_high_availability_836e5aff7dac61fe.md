---
{
  "chunk_id": "session_profile_properties_telnet__telnet_high_availability_836e5aff7dac61fe",
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
    "Telnet > High Availability"
  ],
  "anchor": "1130080",
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
  "related_links": [
    "ha_test_cases.1.htm#"
  ],
  "images": [],
  "content_hash": "836e5aff7dac61fe",
  "level": 2
}
---

# Session profile property settings for Telnet sessions > Session profile property settings for Telnet sessions > Telnet > High Availability

For details on implementing tests for HA devices, see “Testing High‑Availability (HA) Devices”.

| High Availability | Check the box to enable HA operation. (The default setting, unchecked, specifies normal, non‑HA operation.) |
| --- | --- |
| Additional connections | Specify the IP address and port pair for each redundant node (nodes other than the master node.). This information is used only by the open step for a session. The values in the list represent nodes 1, 2, 3, ... n. Use the following format, one node per line: <IP_or_hostname>:<portnumber> Important: Be sure not to enter the values for node 0 — the master node — those values are specified by the IP Address and Port properties. |
