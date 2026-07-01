---
{
  "chunk_id": "session_profile_properties_serial__serial_port_high_availability_9c543481f91f03b2",
  "source_file": "topics/session_profile_properties_serial.htm",
  "source_original_path": "topics/session_profile_properties_serial.htm",
  "toc_path": [
    "iTest Online Help",
    "Serial Sessions",
    "Session profile property settings for Serial sessions"
  ],
  "heading_path": [
    "Session profile property settings for Serial sessions",
    "Session profile property settings for Serial sessions",
    "Serial Port > High Availability"
  ],
  "anchor": "1157471",
  "context_ids": [
    "session_profile_properties_serial"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Serial property settings",
    "Serial sessions",
    "configuring",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Serial sessions > configuring",
    "Serial sessions > session profile property settings",
    "configuring > Serial sessions",
    "property settings > Serial sessions",
    "session profiles > Serial property settings"
  ],
  "related_links": [
    "ha_test_cases.1.htm#"
  ],
  "images": [],
  "content_hash": "9c543481f91f03b2",
  "level": 2
}
---

# Session profile property settings for Serial sessions > Session profile property settings for Serial sessions > Serial Port > High Availability

For details on implementing tests for HA devices, see “Testing High‑Availability (HA) Devices”.

| High Availability | Check the box to enable HA operation. (The default setting, unchecked, specifies normal, non‑HA operation.) |
| --- | --- |
| Additional connections | Specify the IP address and port pair for each redundant node (nodes other than the master node.). This information is used only by the open step for a session. The values in the list represent nodes 1, 2, 3, ... n. Use the following format, one node per line: <IP_or_hostname>:<portnumber> Important: Be sure not to enter the values for node 0 — the master node — those values are specified by the IP Address and Port properties. |
