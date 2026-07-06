# SNMP Sessions > SNMP session window > Traps

iTest receives traps in two ways:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- At any time, whether a iTest SNMP session is running or not, iTest receive traps on the ports specified in the iTest preferences (Window > Preferences.Spirent > Session Types > SNMP).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- When a iTest SNMP session is running, it communicates with one SNMP agent. The session can bind to a port to listen for SNMP traps from the agent (the port is specified for the Trap Port properties in the session profile). While the session receives traps only from the agent, the SNMP Traps view shows traps received from any agent.

See Configuring trap settings.
