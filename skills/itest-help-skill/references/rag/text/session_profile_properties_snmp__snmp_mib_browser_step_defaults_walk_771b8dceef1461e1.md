---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_step_defaults_walk_771b8dceef1461e1",
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
    "SNMP MIB Browser > Step Defaults > Walk"
  ],
  "anchor": "1268025",
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
  "content_hash": "771b8dceef1461e1",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults > Walk

| Maximum number of items to fetch during automated execution | This setting applies only during automated execution (when replaying a step). Specify the maximum number of values to return for a Walk action. Default: 10,000 |
| --- | --- |
| Stop on cycle | Enables tests to exit infinite loops caused by self-referencing OIDs and OIDs that incorrectly duplicate OIDs that appear earlier in the MIB. Default: unchecked |
| Trim “.0” from OID | During an interactive session, to view the scalar value of a variable, you can either Click the variable in the MIB tree Use “.0” as the final characters of the OID in the OID text box and then press Enter or click Get . During interactive sessions, iTest performs the get operation and, by default, to make it easier to read the OID, strips the trailing “.0” text as displayed in the OID text box and in the command for the captured step. Adding the “.0” text explicitly ensures that iTest will use the full OID text in the command for the captured step. Uncheck the box to display the trailing “.0” text in the OID text box and to capture it in the command for the step. Check the box to strip the trailing “.0” text. Default: checked |
|  | Click the variable in the MIB tree |
|  | Uncheck the box to display the trailing “.0” text in the OID text box and to capture it in the command for the step. |
|  | Check the box to strip the trailing “.0” text. |
