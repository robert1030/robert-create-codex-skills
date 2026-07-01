---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_step_defaults_set_7def1c0c64700376",
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
    "SNMP MIB Browser > Step Defaults > Set"
  ],
  "anchor": "1582552",
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
  "content_hash": "7def1c0c64700376",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults > Set

| Execute a get action before executing set | Check the box to cause iTest to execute a get action before executing any set action.This option enables you to correctly set a variable whose type you do not know before execution — the type returned by the get action is used to perform the set action. Uncheck the box to execute only a set action for a set step. You specify the type using the Value type property. Note If you check the box, the Value type property is ignored. Default: unchecked | Note | If you check the box, the Value type property is ignored. |
| --- | --- | --- | --- |
| Note | If you check the box, the Value type property is ignored. |  |  |
| Value type | If you know the type of the value to set for any set action, then you can specify the type here. (This option is available only if you uncheck the Execute a get action before executing set check box.) Note It is typically best to set this property for an individual step in the Test Case editor. Default: [blank] (that is, no type is specified) | Note | It is typically best to set this property for an individual step in the Test Case editor. |
| Note | It is typically best to set this property for an individual step in the Test Case editor. |  |  |
