---
{
  "chunk_id": "session_profile_properties_snmp__itest_3_1_compatibility_mode_dc0eab176cb94492",
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
    "SNMP MIB Browser > Step Defaults > GetTable",
    "iTest 3.1 compatibility mode"
  ],
  "anchor": "1268009",
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
  "images": [
    "topics/images/snmp_2.3.jpg"
  ],
  "content_hash": "dc0eab176cb94492",
  "level": 3
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults > GetTable > iTest 3.1 compatibility mode

For iTest versions after 3.1, the format of the structured data for SNMP tables changed. This setting applies for SNMP getTable actions only.

iTest versions after 3.1 render the structured data with the row identifier (the part that gets suffixed to the OID) added as an attribute. The key attribute is added to the entry element (in the old format, the oid attribute was added to each field). The value for key is the same as the eliminated oid attribute and is up a level.

Each field gets a same-named query which takes key as its single argument. A values query will return all the keys.

Default: Unchecked

For example, MIB-2::at.atTable has a compound key:

![screenshot](topics/images/snmp_2.3.jpg) <!-- image_chunk: img_443291d25a6dd710 -->
