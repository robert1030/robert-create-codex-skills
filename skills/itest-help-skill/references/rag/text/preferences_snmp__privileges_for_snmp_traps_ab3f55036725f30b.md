---
{
  "chunk_id": "preferences_snmp__privileges_for_snmp_traps_ab3f55036725f30b",
  "source_file": "topics/preferences_snmp.htm",
  "source_original_path": "topics/preferences_snmp.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "Setting preferences for monitoring SNMP traps"
  ],
  "heading_path": [
    "Setting preferences for monitoring SNMP traps",
    "Setting preferences for monitoring SNMP traps",
    "Privileges for SNMP traps"
  ],
  "anchor": "1556895",
  "context_ids": [
    "preferences_snmp"
  ],
  "index_keywords": [
    "SNMP",
    "SNMP preference settings"
  ],
  "index_keyword_paths": [
    "SNMP preference settings",
    "preference settings > SNMP"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "ab3f55036725f30b",
  "level": 2
}
---

# Setting preferences for monitoring SNMP traps > Setting preferences for monitoring SNMP traps > Privileges for SNMP traps

Executing the SNMP daemon on certain operating systems like Linux requires root privileges. Typically, however, you execute iTest as a regular user. As a result, you may not have privileges to listen to the default SNMP trap port 162. In this case, set a different trap port to listen on in either the SNMP session profile or in the iTest SNMP preferences settings. You must configure your SNMP agent to send traps on the new port



To configure the ports to monitor for traps

The Trap Configuration section of the page lists the ports that iTest is currently monitoring for traps. iTest listens for the listed traps regardless whether or not a iTest session is running. You can add, edit, or remove configuration settings. By default, iTest listens on port 162 for non‑V3 traps.

To add a port to listen on, click New and specify the following settings on the Configure SNMP Trap dialog box:

| Port | Specify the port to listen on for traps. |
| --- | --- |
| V3 Trap | Check the box if the SNMP protocol version of the agent is V3 Default: unchecked |
| Note The remaining properties apply only for SNMP V3 | Note |
| Note | The remaining properties apply only for SNMP V3 |
| Engine ID | Specify the snmpEngineID. |
| User name | Specify the user name. |
| Security level | Specify the security level. Default: No authentication, no privacy |
| Authentication algorithm | Note This property applies only if you specify a Security Level of Authentication, no privacy or Authentication, privacy Authentication Algorithm options are: MD5, SHA, SHA-224, SHA-226, SHA-384, SHA-512 Default: MD5 Note The Authentication password is specified on the SNMP MIB Browser page. Specify the authentication password. Specify the authentication algorithm. |
| Note | This property applies only if you specify a Security Level of Authentication, no privacy or Authentication, privacy |
| Note | The Authentication password is specified on the SNMP MIB Browser page. |
|  | Specify the authentication password. |
|  | Specify the authentication algorithm. |
| Privacy | Note This property applies only if you specify a Security Level of Authentication, privacy Specify the privacy password. Specify the encryption standard. Default: DES |
| Note | This property applies only if you specify a Security Level of Authentication, privacy |



To configure general behavior for SNMP traps

The following settings control iTest behavior when traps are received:

| Open SNMP Traps console when a trap is received | Open the SNMP Traps console in iTest when a trap is received. Default: unchecked |
| --- | --- |
| Open SNMP Traps view when a trap is received | Open the SNMP Traps view in iTest when a trap is received. Default: unchecked |
| Maximum number of traps on each port | Specify the maximum number of traps (for each port) to list in the SNMP Traps view. When the number of traps reaches the limit, then the oldest trap messages are deleted. Default: 100 |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
