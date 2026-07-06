# SNMP Sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Traps > iTest receives traps in two ways:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- At any time, whether a iTest SNMP session is running or not, iTest receive traps on the ports specified in the iTest preferences (Window > Preferences. Spirent > Session Types > SNMP).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- When a iTest SNMP session is running, it communicates with one SNMP agent. The session can bind to a port to listen for SNMP traps from the agent (the Port specified here). The session receives traps only from the agent. The SNMP Traps view shows traps received from any agent.

The waitForTrap action has an empty Command property by default. waitForTrap waits for any trap received from the agent of the session on the Port specified here. If you specify the expected trap name in the Command property, the action waits for a trap from the agent with a name that starts with the specified text (the Command text acts as a prefix).
