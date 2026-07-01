---
{
  "chunk_id": "snmp_session_editor_concept__important_loading_mib_definitions_40fd4e903a4264b5",
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
    "Important: Loading MIB definitions"
  ],
  "anchor": "1268278",
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
  "content_hash": "40fd4e903a4264b5",
  "level": 2
}
---

# SNMP session window > SNMP session window > Important: Loading MIB definitions

- Sessions may load MIB files from various locations. This may result in odd behavior if the files have conflicting definitions.

- By default, to ensure faster execution, iTest loads a MIB file into the MIB cache only one time during the lifetime of the current instance of iTest. iTest loads MIB files when a session starts (either the default MIB definitions or the MIB files that are specified in the session profile). Once a MIB file has been loaded, however, iTest does not reload it (even if the session starts again). This means that:

- Changes that you make to a MIB file after a session has run are not loaded when the session starts again.

- MIB errors that were displayed the first time a MIB file was loaded (for example, when a session started) are not displayed again even if the session starts again.
