# SNMP Sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser

Note This property appears only for SNMPv1 and SNMPv2c.

Note This property appears only for SNMPv1 and SNMPv2c.

Note This property appears for SNMPv1, SNMPv2c, and SNMPV3.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Hex: value in hex mode “0x00 0xBA...” Human-readable: non-printable characters are replaced with dots Auto Hex: switch to Hex if the text has non-printable characters iTest 4.3 compatibility mode

Note This property appears only for SNMPv3.

Note This property appears only for SNMPv3. This property is disabled if the No authentication, no privacy option is selected for the Security level property in the Authentication (SNMPv3 only) property group.

- **IP address**：Specify the IP address or hostname of the agent that you want to interact with in the SNMP session window
- **SNMP port**：Specify the port for the agent. Default: 161
- **SNMP version**：Specify the SNMP protocol version of the agent. Default: Version V2c Options: Version 1, Version 2C, Version 3
- **Read community**：Specify the Read community string (the community to use for requests to the agent). Default: public
- **Write community**：Specify the Write community string (the community to use for SNMP SET requests). Default: [none]
- **OctetString representation**：Select one of these SNMP compatibility options to specify how OctetStrings are represented in the responses. Default: iTest 4.3 compatibility mode
- **User name**：Specify the user name.
- **Authentication password**：Specify the authentication password.
