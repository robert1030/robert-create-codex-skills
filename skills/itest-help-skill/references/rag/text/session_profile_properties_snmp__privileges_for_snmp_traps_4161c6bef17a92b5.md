---
{
  "chunk_id": "session_profile_properties_snmp__privileges_for_snmp_traps_4161c6bef17a92b5",
  "source_file": "topics/session_profile_properties_snmp.htm",
  "source_original_path": "topics/session_profile_properties_snmp.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "Session profile property settings for SNMP sessions"
  ],
  "heading_path": [
    "Session profile property settings for SNMP sessions",
    "Session profile property settings for SNMP sessions",
    "SNMP MIB Browser > Traps",
    "Privileges for SNMP traps"
  ],
  "anchor": "1556806",
  "context_ids": [
    "session_profile_properties_snmp"
  ],
  "index_keywords": [
    "SNMP sessions",
    "property settings"
  ],
  "index_keyword_paths": [
    "SNMP sessions > property settings",
    "property settings > SNMP sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "4161c6bef17a92b5",
  "level": 3
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Traps > Privileges for SNMP traps

Executing the SNMP daemon on the Linux or Apple Macintosh operating system requires root privileges. Typically, however, you execute iTest as a regular user. As a result, you may not have privileges to listen to the default SNMP trap port 162. In this case, set a different trap port to listen on in either the SNMP session profile or in the iTest SNMP preferences settings. You must configure your SNMP agent to send traps on the new port.
