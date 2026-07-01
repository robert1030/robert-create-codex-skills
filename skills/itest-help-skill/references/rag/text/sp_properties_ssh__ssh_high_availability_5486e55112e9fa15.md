---
{
  "chunk_id": "sp_properties_ssh__ssh_high_availability_5486e55112e9fa15",
  "source_file": "topics/sp_properties_ssh.htm",
  "source_original_path": "topics/sp_properties_ssh.htm",
  "toc_path": [
    "iTest Online Help",
    "SSH Sessions",
    "Session profile property settings for SSH sessions"
  ],
  "heading_path": [
    "Session profile property settings for SSH sessions",
    "Session profile property settings for SSH sessions",
    "Session Properties > More",
    "SSH > High Availability"
  ],
  "anchor": "1175636",
  "context_ids": [
    "sp_properties_ssh"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions",
    "configuring",
    "session profile property settings for"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions > configuring",
    "SSH sessions > session profile property settings for",
    "configuring > SSH sessions",
    "session profile property settings > SSH sessions"
  ],
  "related_links": [
    "ha_test_cases.1.htm#"
  ],
  "images": [],
  "content_hash": "5486e55112e9fa15",
  "level": 3
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > Session Properties > More > SSH > High Availability

For details on implementing tests for HA devices, see “Testing High‑Availability (HA) Devices”.

| High Availability | Check the box to enable HA operation. (The default setting, unchecked, specifies normal, non‑HA operation.) |
| --- | --- |
| Additional connections | Specify the IP address and port pair for each redundant node (nodes other than the master node.). This information is used only by the open step for a session. The values in the list represent nodes 1, 2, 3, ... n. Use the following format, one node per line: <IP_or_hostname>:<portnumber> Important: Be sure not to enter the values for node 0 — the master node — those values are specified by the IP Address and Port properties. |
