# Python Automation Library > Overview > Modes of Operation

The Python Automation Library provides these modes of Operation, connectivity, license usage.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Connect to an iTest GUI instance (iTest GUI Mode)

![*](bullet_blue.jpg) <!-- image_ref -->

- On the local host or remote host

![*](bullet_blue.jpg) <!-- image_ref -->

- Requires that Session Level Control agent be enabled and in listening mode (see Configure Listening Mode (Listen for incoming Python connections))

![*](bullet_blue.jpg) <!-- image_ref -->

- iTest GUI can use either Enterprise or Runtime license

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Connect to an agent (running agent instance) on a remote workstation (Remote Mode).

![*](bullet_blue.jpg) <!-- image_ref -->

- On the local host or remote host

![*](bullet_blue.jpg) <!-- image_ref -->

- Requires that the agent is already started and in “listening” mode for SLC connections (see Configure Listening Mode (Listen for incoming Python connections))

![*](bullet_blue.jpg) <!-- image_ref -->

- Agent requires a Runtime license at startup

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Connect to a standalone workstation (Standalone Mode)

![*](bullet_blue.jpg) <!-- image_ref -->

- On the local host

![*](bullet_blue.jpg) <!-- image_ref -->

- Auto-launch an agent in the background

![*](bullet_blue.jpg) <!-- image_ref -->

- Agent requires a Runtime license at startup

In the first two cases, iTest opens a socket and listens for connections. The listening mode is enabled via a specific agent command line parameter “–listeningMode”, and on iTest GUI via “Configure Listening Mode (Listen for incoming Python connections)”.

> **Note：** Note When running an execution as an iTest agent (either Velocity agent or Python SLC agent), the masked values of the parameter type Secret cannot be un-masked. See About the Parameter Type ‘Secret’.
