---
{
  "chunk_id": "snmp_session_editor_concept__snmp_session_window_5347832a682a6a8f",
  "source_file": "topics/snmp_session_editor_concept.htm",
  "source_original_path": "topics/snmp_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "SNMP session window"
  ],
  "heading_path": [
    "SNMP session window",
    "SNMP session window"
  ],
  "anchor": "1284311",
  "context_ids": [
    "snmp_session_editor_concept"
  ],
  "index_keywords": [
    "SNMP",
    "SNMP Console",
    "SNMP Traps view",
    "session window"
  ],
  "index_keyword_paths": [
    "SNMP > session window",
    "SNMP Console",
    "SNMP Traps view",
    "session windows > SNMP",
    "views > SNMP Console",
    "views > SNMP Traps view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "5347832a682a6a8f",
  "level": 1
}
---

# SNMP session window > SNMP session window

iTest supports the Simple Network Management Protocol: SNMPv1, SNMPv2C, and SNMPv3.

The SNMP session window is a MIB browser that displays the tree for the specified MIB on the specified device, the variable definitions from the MIB file, and the value of a selected variable.

You can replay captured actions by dropping them from the Capture view into the SNMP session window.

Most devices support SNMP for monitoring and configuration. Because you typically use one software tool for CLI and a different tool for SNMP, it is difficult to automate SNMP tests. As a result, over time, a device’s CLI command interface can get out of synch with the SNMP interface. iTest makes it easy to compare the operation of a device’s CLI interface and the SNMP interface in a single test case. For example, a test case can send traffic and then compare the SNMP responses to the CLI responses.

You will use the SNMP session window to get and set MIB variables.

> **Warning:** WARNING MIB parser sometimes cannot handle duplicate names very well (if you load only DOCS-QOS3-MIB-110210.txt then there is no problem). This issue will be addressed in the future release.
