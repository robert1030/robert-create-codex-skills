# Testing High‑Availability (HA) Devices > Specifying that a particular node should be master (or slave)

During default HA operation, iTest determines mastership automatically by sending empty commands and using prompts to determine which is master. In the case that you cannot distinguish master/slave using the prompts, you might want to specify that a particular node should be master.

you will use the setmaster action to explicitly set a particular node to master (and setslave to set a slave). As a result, the master node becomes the intended recipient for all steps for which the Send to property is set to Master. Steps with the Send to property set to Slave are sent to the first node (in index order) that is not master.



To specify which node should be master (or slave)

![*](bullet_blue.jpg) <!-- image_ref -->

1. Create a step and select setmaster (or setslave) in the Action cell.

1. 2 In the Description cell, type the index number that identifies the node that you want to set to master (or to slave). See Specifying a node by index.
