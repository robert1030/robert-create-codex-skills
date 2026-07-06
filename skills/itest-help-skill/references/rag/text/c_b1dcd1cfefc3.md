# iTest Topology Editor > Overview: iTest Topologies > Add, edit, or remove a session configuration for a iTest topology device > 第1段

> **Important：** Important Session profiles that you define for devices in a topology are saved as part of the topology file and are not saved as separate session profile documents.

To define a session for a device, you use one of the following methods:

![*](bullet_blue.jpg) <!-- image_ref -->

- Session type: Inherit all property settings from the default iTest template for a session type and then configure particular properties as needed.

![*](bullet_blue.jpg) <!-- image_ref -->

- Create reference session profile: Select an existing or create a new session profile (typically a reference profile) document (.ffsp), from which the new session configuration will inherit property settings. You can change property settings as needed.



To define a session for a resource

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/topologies_2.1.jpg) <!-- image_ref -->

1. On the canvas, right‑click the resource and select Add Session.

![](images/topologies_2.2.jpg) <!-- image_ref -->

(Alternatively, select the device on the canvas. On the Properties view, click the Session tab and then click ) The Add Session Profile page displays. Enter the details as below.

1. 2 Profile Name: type the Profile name for this particular set of session configuration settings. iTest provides a default name that includes the session type.

1. 3 Language: Select the language that will be used to create the session profile. You may use the default language displayed (as set in Preferences: Spirent > General > General preference settings, Chapter , “Configuring iTest Preferences”) or select a different language from the list.

1. 4 Specify the Session type (Telnet, SNMP, Web, and so on). This is a default iTest template for a session. If you will use the session type as the basis for this session configuration, then skip the next step and continue at Step 6.

1. 5 In this step, you specify that the current session configuration should inherit all property settings from an existing session profile — either a reference session profile or any other session profile. This is the most common and the most powerful way to define a session profile, as described in Defining a reference session profile.

![*](bullet_blue.jpg) <!-- image_ref -->

1. Check Use a reference session profile.

![*](bullet_blue.jpg) <!-- image_ref -->

1. In the Create reference session profile box, specify the session profile from which to inherit settings.
