# SNMP Sessions > Creating SNMP test case steps > SNMP action types that you can perform in test case steps > 第2段

If a port is specified for the SNMP port property in the session associated with the step, then waitForTrap causes execution to wait until a trap is received for the port. Traps on the ports specified in preferences are not considered. If no port is specified for the SNMP port property, then waitForTrap causes execution to wait until a trap is received for one of the ports specified in preferences If no port is specified for the SNMP port property and no port is specified in preferences, then waitForTrap causes execution to wait until a trap is received for any port.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

If the step specifies an OID in the Command property, then waitForTrap waits for the specified trap (or any trap with the specified prefix). If the step does not specify an OID in the Command property, then waitForTrap waits for any trap.

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

Timestamp Trap objects
