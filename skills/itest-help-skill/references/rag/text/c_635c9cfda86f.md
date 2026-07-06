# iTest Topology Editor > Overview: iTest Topologies > Add, edit, or remove a session configuration for a iTest topology device > 第2段

When you click Browse, the dialog box enables you to select from both reference and non-reference session profiles, either in the Workspace (the document is in the current iTest workspace) or File system (the document is in an itar file somewhere in the file system).

1. 6 The current property settings appear in the middle of the page. Modify the settings as needed. For an SNMP session, for example, you would specify the IP address for the device that you’re connecting to. Other session types have different required settings. The property settings associated with each session type are described in the chapter for the particular session type in a section titled “Session profile property settings for <session type> sessions”.

![*](bullet_blue.jpg) <!-- image_ref -->

- Required property settings are marked with the * character.

![*](bullet_blue.jpg) <!-- image_ref -->

- A blue text box indicates that the setting is being inherited from the session profile that this session profile is based upon. See About property settings.

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/topologies_2.3.jpg) <!-- image_ref -->

- The indicates that you can use field replacements in the text of the property setting. See Field replacements: Substituting values into properties and commands.

![](images/topologies_2.4.jpg) <!-- image_ref -->

You have the option to specify additional session properties like screen color, timeouts, non-standard prompts, and so on. Click to display a tree of all available properties. you will find details on property settings for each session type in the appropriate chapter.

1. 7 Click Save to save the new session configuration with the topology document. Click Save and Start to save the definition and start a session with the device.



To update a session configuration for a resource

![](images/topologies_2.5.jpg) <!-- image_ref -->

On the canvas, right‑click the resource and select Edit Session.

![](images/topologies_2.6.jpg) <!-- image_ref -->

(Alternatively, select the device on the canvas. On the Properties view, click the Session tab and then click )

The Edit Session Profile page enables you to view or edit property settings for the session profile.



To remove a session configuration for a resource

![](images/topologies.7.jpg) <!-- image_ref -->

On the canvas, right‑click the resource and select Remove Session.

![](images/topologies.8.jpg) <!-- image_ref -->
