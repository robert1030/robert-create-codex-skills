---
{
  "chunk_id": "session_profile_properties_snmp__itest_receives_traps_in_two_ways_1c59822aa1e04528",
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
    "iTest receives traps in two ways:"
  ],
  "anchor": "1607663",
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
  "content_hash": "1c59822aa1e04528",
  "level": 3
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Traps > iTest receives traps in two ways:

- At any time, whether a iTest SNMP session is running or not, iTest receive traps on the ports specified in the iTest preferences (Window > Preferences. Spirent > Session Types > SNMP).

- When a iTest SNMP session is running, it communicates with one SNMP agent. The session can bind to a port to listen for SNMP traps from the agent (the Port specified here). The session receives traps only from the agent. The SNMP Traps view shows traps received from any agent.

The waitForTrap action has an empty Command property by default. waitForTrap waits for any trap received from the agent of the session on the Port specified here. If you specify the expected trap name in the Command property, the action waits for a trap from the agent with a name that starts with the specified text (the Command text acts as a prefix).
