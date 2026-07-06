# SNMP Sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Traps > Privileges for SNMP traps

Executing the SNMP daemon on the Linux or Apple Macintosh operating system requires root privileges. Typically, however, you execute iTest as a regular user. As a result, you may not have privileges to listen to the default SNMP trap port 162. In this case, set a different trap port to listen on in either the SNMP session profile or in the iTest SNMP preferences settings. You must configure your SNMP agent to send traps on the new port.
