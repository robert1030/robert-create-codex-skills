---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_fc0a3eefcd78a1bc",
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
    "SNMP MIB Browser"
  ],
  "anchor": "1556137",
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
  "content_hash": "fc0a3eefcd78a1bc",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser

| IP address | Specify the IP address or hostname of the agent that you want to interact with in the SNMP session window |
| --- | --- |
| SNMP port | Specify the port for the agent. Default: 161 |
| SNMP version | Specify the SNMP protocol version of the agent. Default: Version V2c Options: Version 1, Version 2C, Version 3 |
| Read community | Note This property appears only for SNMPv1 and SNMPv2c. Specify the Read community string (the community to use for requests to the agent). Default: public |
| Note | This property appears only for SNMPv1 and SNMPv2c. |
| Write community | Note This property appears only for SNMPv1 and SNMPv2c. Specify the Write community string (the community to use for SNMP SET requests). Default: [none] |
| Note | This property appears only for SNMPv1 and SNMPv2c. |
| OctetString representation | Note This property appears for SNMPv1, SNMPv2c, and SNMPV3. Select one of these SNMP compatibility options to specify how OctetStrings are represented in the responses. Hex: value in hex mode “0x00 0xBA...” Human-readable: non-printable characters are replaced with dots Auto Hex: switch to Hex if the text has non-printable characters iTest 4.3 compatibility mode Default: iTest 4.3 compatibility mode |
| Note | This property appears for SNMPv1, SNMPv2c, and SNMPV3. |
|  | Hex: value in hex mode “0x00 0xBA...” |
|  | Human-readable: non-printable characters are replaced with dots |
|  | Auto Hex: switch to Hex if the text has non-printable characters |
|  | iTest 4.3 compatibility mode |
| User name | Note This property appears only for SNMPv3. Specify the user name. |
| Note | This property appears only for SNMPv3. |
| Authentication password | Note This property appears only for SNMPv3. This property is disabled if the No authentication, no privacy option is selected for the Security level property in the Authentication (SNMPv3 only) property group. Specify the authentication password. |
| Note | This property appears only for SNMPv3. This property is disabled if the No authentication, no privacy option is selected for the Security level property in the Authentication (SNMPv3 only) property group. |
