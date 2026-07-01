---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_authentication_snmpv3_o_81492de625eb3e76",
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
    "SNMP MIB Browser > Authentication (SNMPv3 only)"
  ],
  "anchor": "1556138",
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
  "content_hash": "81492de625eb3e76",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Authentication (SNMPv3 only)

> **Note:** Note These settings apply only for SNMPv3.

| V3 Context | Specify a context name (per RFC 2275) for the SNMPv3 request. Default: <empty string> |
| --- | --- |
| Security level | Specify the security level. Default: No authentication, no privacy Options: No authentication, no privacy Authentication, no Privacy Authentication, privacy |
|  | No authentication, no privacy |
|  | Authentication, no Privacy |
|  | Authentication, privacy |
| Authentication algorithm | Specify the authentication algorithm. Availability and default selection depends on the Security Level option selected. If No authentication, no privacy is selected, the Authentication Algorithm options are grayed. If Authentication, no Privacy or Authentication, privacy is selected, these Authentication Algorithm options are available. MD5, SHA, SHA-224, SHA-226, SHA-384, SHA-512 Default: MD5 Note The Authentication password is specified on the SNMP MIB Browser page. |
|  | If No authentication, no privacy is selected, the Authentication Algorithm options are grayed. |
|  | If Authentication, no Privacy or Authentication, privacy is selected, these Authentication Algorithm options are available. |
| Note | The Authentication password is specified on the SNMP MIB Browser page. |
| Privacy | The Privacy options are available only when Security Level option Authentication, privacy is selected. Specify the privacy password. Default: [none] Mask Content: Selected by default. |
| Specify the encryption standard. Default: DES Options: DES, AES-128, AES-192, AES-256 |  |
