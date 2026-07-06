# Testing High‑Availability (HA) Devices > Testing HA devices: Overview > iTest HA Operation

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- iTest’s HA feature treats the HA device (with multiple redundant nodes) as a single virtual device — iTest takes care of directing commands to the appropriate node.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- HA supports multiple connections inside a single session (either Telnet or SSH) connected to nodes via Telnet/SSH sockets to different IP addresses and/or port numbers. One HA session window appears for each connection.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- By default, iTest determines master/slave/other state based on the prompts returned to commands (you specify the master/slave/other prompts in the session profile or testbed device).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- In the most common situations, test cases send commands to the master. You can override the session’s default HA behavior by setting a property for any step to direct commands to a slave node or to a specified node.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Responses from the master node appear in the Response view and responses from other nodes appear in the structured data in the Structure view

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can configure what should happen when an intended recipient (be it master, slave, or other) cannot be found, including an option to poll waiting for a recipient to be identified.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- You can use setmaster and setslave actions to explicitly set master/slave status.
