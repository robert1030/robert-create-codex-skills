# Wizards and Dialog boxes > Selecting a session profile or device

The Select a Session Profile or Device dialog box enables you to specify which session profile or device definition to use to launch a session.

For Test Case, the open step allows selecting device type in topology and session profile, and disables application type.

![*](bullet_blue.jpg) <!-- image_ref -->

- Device in Topology: The box displays each device definition associated with the current test case a topology, testbed, or global testbed specified for the test case). Select the device from the list and then click OK.

The text in the Description cell will be a device URI of the format device:device_name. For example, device:telnet_DUT6 means: “From the topology, testbed, or global testbed specified for the test case (on the Test Case editor General page), fetch a device definition named telnet_DUT6.”

![*](bullet_blue.jpg) <!-- image_ref -->

- Session profile or reference session profile: The box displays a tree of all projects in the current workspace. Navigate to the session profile and then click OK.

The resulting text in the Description cell will be the URI of the session profile that will start the session, for example, project://my_project/session_profiles/telnet_DUT6.ffsp

For instructions on configuring this value to be determined at runtime, see Determining the device or session profile (dynamically) at runtime.

![*](bullet_blue.jpg) <!-- image_ref -->

- iTest default session type: This option starts a session without referencing a particular session profile. If you specify iTest default session type, then you must also (typically) specify additional property settings for the open step (for example, the IP address of the device). In this SNMP example, we hold the cursor over the error marker for the step to learn that we need to specify the IP address for the device in the SNMP Session Properties > SNMP MIB Browsers properties group.

![](images/context_ids_3.1.jpg) <!-- image_ref -->
