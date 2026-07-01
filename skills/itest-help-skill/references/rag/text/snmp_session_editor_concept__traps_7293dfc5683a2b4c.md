---
{
  "chunk_id": "snmp_session_editor_concept__traps_7293dfc5683a2b4c",
  "source_file": "topics/snmp_session_editor_concept.htm",
  "source_original_path": "topics/snmp_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "SNMP session window"
  ],
  "heading_path": [
    "SNMP session window",
    "SNMP session window",
    "Traps"
  ],
  "anchor": "1268286",
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
  "related_links": [
    "snmp.2.htm#1555474"
  ],
  "images": [],
  "content_hash": "7293dfc5683a2b4c",
  "level": 2
}
---

# SNMP session window > SNMP session window > Traps

iTest receives traps in two ways:

- At any time, whether a iTest SNMP session is running or not, iTest receive traps on the ports specified in the iTest preferences (Window > Preferences.Spirent > Session Types > SNMP).

- When a iTest SNMP session is running, it communicates with one SNMP agent. The session can bind to a port to listen for SNMP traps from the agent (the port is specified for the Trap Port properties in the session profile). While the session receives traps only from the agent, the SNMP Traps view shows traps received from any agent.

See Configuring trap settings.
