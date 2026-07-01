---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_traps_f1a1f32f8e174ea8",
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
    "SNMP MIB Browser > Traps"
  ],
  "anchor": "1585770",
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
    "#1615656",
    "#1607663"
  ],
  "images": [],
  "content_hash": "f1a1f32f8e174ea8",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Traps

| Port | Specify the port where traps should be received by the waitForTrap and listTraps actions. The setting serves two functions: Adds this port for listening (if the port is not configured in preferences) Acts as a filter for incoming traps Note 1. See Port binding.2. If no port is specified, then the session captures all traps from the ports specified in preferences, as noted in iTest receives traps in two ways:. |  | Adds this port for listening (if the port is not configured in preferences) |  | Acts as a filter for incoming traps | Note | 1. See Port binding.2. If no port is specified, then the session captures all traps from the ports specified in preferences, as noted in iTest receives traps in two ways:. |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Adds this port for listening (if the port is not configured in preferences) |  |  |  |  |  |  |
|  | Acts as a filter for incoming traps |  |  |  |  |  |  |
| Note | 1. See Port binding.2. If no port is specified, then the session captures all traps from the ports specified in preferences, as noted in iTest receives traps in two ways:. |  |  |  |  |  |  |
| NIC address | Specify the IP address of the NIC where traps should be received. Tip To determine the IP address of the NICs on a computer, use the ipconfig/all command, Note When the receiving computer has multiple NICs: If you do not specify an IP address, then iTest listens to one of the NICs at random (on the specified Port). | Tip | To determine the IP address of the NICs on a computer, use the ipconfig/all command, | Note | When the receiving computer has multiple NICs: If you do not specify an IP address, then iTest listens to one of the NICs at random (on the specified Port). |  |  |
| Tip | To determine the IP address of the NICs on a computer, use the ipconfig/all command, |  |  |  |  |  |  |
| Note | When the receiving computer has multiple NICs: If you do not specify an IP address, then iTest listens to one of the NICs at random (on the specified Port). |  |  |  |  |  |  |
| Engine ID | This setting applies only for SNMPv3 Specify the snmpEngineID. |  |  |  |  |  |  |
| Override existing settings for same trap port bound when the session starts | Select to override the properties of specific trap port. When selected, SNMP trap port could rebind to new properties for every execution of SNMP session and allow reuse of trap port for different properties (e.g., different SNMP versions). When not selected, iTest does not allow binding different properties to the same trap port unless restarted. For example, when running tests and waiting for SNMP traps for version 2 and 3 at random on the same port, the SNMP sessions display error when switching between the two sessions. When running an SNMPv3 test case after a successful SNMPv2c test case, an error may display as follows: SNMP trap daemon failed to bind to port N: a daemon is already running on the port with settings (V3=false) Similarly, when running an SNMPv2c test case after a successful SNMPv3 test case: SNMP trap daemon failed to bind to port N: a daemon is already running on the port with settings (V3=true, ...) |  | When running an SNMPv3 test case after a successful SNMPv2c test case, an error may display as follows: |  | Similarly, when running an SNMPv2c test case after a successful SNMPv3 test case: |  |  |
|  | When running an SNMPv3 test case after a successful SNMPv2c test case, an error may display as follows: |  |  |  |  |  |  |
|  | Similarly, when running an SNMPv2c test case after a successful SNMPv3 test case: |  |  |  |  |  |  |
