---
{
  "chunk_id": "session_profile_properties_snmp__example_3345e2a9724da03b",
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
    "SNMP MIB Browser > Aliases",
    "Example"
  ],
  "anchor": "1530254",
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
    "inheritance_property.htm#1128847"
  ],
  "images": [
    "topics/images/snmp_2.2.jpg"
  ],
  "content_hash": "3345e2a9724da03b",
  "level": 3
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Aliases > Example

When you specify an alias of ACME, then

ACME::IMAGE-MIB

appears in the list instead of the full OID prefix and MIB name:

iso.org.dod.internet.private.enterprises.acme.IMAGE-MIB



To add an alias for a proprietary set of MIBs

1. Check Include inherited values to enable you to specify additional lists of proprietary MIBs. (For a discussion on inheriting MIB set aliases from reference session profiles, see Property values: Inheriting settings.)

1. 2

1. Check Include additional values from list.

1. 3

1. Click Add to add an alias. The new alias appears in the list. Specify the following properties for the new alias:

| Name | Specify a name for the alias. In the example, the Name is ACME. Default Names and Contents: MIB-2 / .iso.org.dod.internet.mgmt.mib-2 SNMPv2 / .iso.org.dod.internet.snmpV2 |
| --- | --- |
| Content | Type or paste the OID prefix that you want to alias. In the example, the Content is: iso.org.dod.internet.private.enterprises.acme |

1. 4

1. During sessions, the sets of MIBs are searched in the listed order. Move any alias up or down in the list by selecting it and using the arrow buttons.

![inline_icon](topics/images/snmp_2.2.jpg) <!-- image_chunk: img_eed0b6492ed5f0ae -->
