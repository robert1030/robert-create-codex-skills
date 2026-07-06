# Testing High‑Availability (HA) Devices > Viewing the current states of all nodes

A getstate step returns an XML table with the current master/slave and index number states of all nodes.

The return data depends on the setting of the Verify status property.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If Verify status is checked (default), then iTest refreshes state information by sending state verification commands to the nodes before it polls for responses to the getstate step.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If Verify status is unchecked for the step, then getstate returns the current states.



To set the ‘Verify status’ property

![*](bullet_blue.jpg) <!-- image_ref -->

1. Select the getstate step.

1. 2 In the Step Properties section, select the Telnet getstate Properties node in the tree.

1. 3 The Verify status checkbox appears on the HighAvailability page.
