---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_mibs_e529b03782573b5f",
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
    "SNMP MIB Browser > MIBs"
  ],
  "anchor": "1528948",
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
  "related_links": [
    "mibs_loading.htm#1586070"
  ],
  "images": [],
  "content_hash": "e529b03782573b5f",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > MIBs

| MIBs folder | By default, iTest loads MIB definitions from the default MIBs folder in the resources project: project://resources/SNMP/Mibs/ The default paths are: Linux: ~/iTest/ workspace/resources/SNMP/Mibs Windows: C:\Documents and Settings\<user_name>\My Documents\iTest_<version>\resources\SNMP\Mibs For instructions on specifying additional or proprietary MIB definitions to load, see Loading your proprietary MIB files into iTest. |
| --- | --- |
| Strict MIB parsing | If unchecked, iTest loads all valid objects in the MIB file even if some objects in the file cannot be resolved. Check the box to cause iTest to perform strict MIB parsing: Before loading the MIB file, ensure that every SNMP MIB object in the file is fully resolved. Default: unchecked |
| Show duplicates in MIB tree | Check the box to display all MIBs that have the same OID. For example, if .iso.org and .iso.dod have the same OID of .1.3, they will both appear in the MIB tree (in random order). If unchecked, only one of the duplicate MIBs (selected randomly) will appear in the tree. Default: unchecked |
