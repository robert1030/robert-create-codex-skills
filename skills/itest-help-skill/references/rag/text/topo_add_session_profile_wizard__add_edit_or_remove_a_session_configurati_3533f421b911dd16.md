---
{
  "chunk_id": "topo_add_session_profile_wizard__add_edit_or_remove_a_session_configurati_3533f421b911dd16",
  "source_file": "topics/topo_add_session_profile_wizard.htm",
  "source_original_path": "topics/topo_add_session_profile_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Overview: iTest Topologies",
    "Add, edit, or remove a session configuration for a iTest topology device"
  ],
  "heading_path": [
    "Add, edit, or remove a session configuration for a iTest topology device",
    "Add, edit, or remove a session configuration for a iTest topology device"
  ],
  "anchor": "1396646",
  "context_ids": [
    "topo_add_session_profile_wizard",
    "topo_edit_session_profile_wizard"
  ],
  "index_keywords": [
    "adding session profiles to",
    "defining for devices in topologies",
    "session profiles in topologies"
  ],
  "index_keyword_paths": [
    "adding > session profiles in topologies",
    "configuring > session profiles in topologies",
    "devices in topologies > adding session profiles to",
    "session profiles > defining for devices in topologies",
    "topologies > adding session profiles to"
  ],
  "related_links": [
    "preferences.04.htm#1253281",
    "preferences_itest.htm#",
    "#1288239",
    "session_profile_reference_sp_configuring.htm#1316032",
    "session_profile_property_settings.htm#1483852",
    "field_replacements_tasks.htm#1128496"
  ],
  "images": [
    "topics/images/topologies_2.1.jpg",
    "topics/images/topologies_2.2.jpg",
    "topics/images/topologies_2.4.jpg",
    "topics/images/topologies_2.5.jpg",
    "topics/images/topologies_2.6.jpg",
    "topics/images/topologies.7.jpg",
    "topics/images/topologies.8.jpg"
  ],
  "content_hash": "3533f421b911dd16",
  "level": 1
}
---

# Add, edit, or remove a session configuration for a iTest topology device > Add, edit, or remove a session configuration for a iTest topology device

Important Session profiles that you define for devices in a topology are saved as part of the topology file and are not saved as separate session profile documents.

To define a session for a device, you use one of the following methods:

- Session type: Inherit all property settings from the default iTest template for a session type and then configure particular properties as needed.

- Create reference session profile: Select an existing or create a new session profile (typically a reference profile) document (.ffsp), from which the new session configuration will inherit property settings. You can change property settings as needed.



To define a session for a resource

1. On the canvas, right‑click the resource and select Add Session.

(Alternatively, select the device on the canvas. On the Properties view, click the Session tab and then click ) The Add Session Profile page displays. Enter the details as below.

1. 2

1. Profile Name: type the Profile name for this particular set of session configuration settings. iTest provides a default name that includes the session type.

1. 3

1. Language: Select the language that will be used to create the session profile. You may use the default language displayed (as set in Preferences: Spirent > General > General preference settings, Chapter , “Configuring iTest Preferences”) or select a different language from the list.

1. 4

1. Specify the Session type (Telnet, SNMP, Web, and so on). This is a default iTest template for a session. If you will use the session type as the basis for this session configuration, then skip the next step and continue at Step 6.

1. 5

1. In this step, you specify that the current session configuration should inherit all property settings from an existing session profile — either a reference session profile or any other session profile. This is the most common and the most powerful way to define a session profile, as described in Defining a reference session profile.

1. Check Use a reference session profile.

1. In the Create reference session profile box, specify the session profile from which to inherit settings.

When you click Browse, the dialog box enables you to select from both reference and non-reference session profiles, either in the Workspace (the document is in the current iTest workspace) or File system (the document is in an itar file somewhere in the file system).

1. 6

1. The current property settings appear in the middle of the page. Modify the settings as needed. For an SNMP session, for example, you would specify the IP address for the device that you’re connecting to. Other session types have different required settings. The property settings associated with each session type are described in the chapter for the particular session type in a section titled “Session profile property settings for <session type> sessions”.

- Required property settings are marked with the * character.

- A blue text box indicates that the setting is being inherited from the session profile that this session profile is based upon. See About property settings.

- The indicates that you can use field replacements in the text of the property setting. See Field replacements: Substituting values into properties and commands.

You have the option to specify additional session properties like screen color, timeouts, non-standard prompts, and so on. Click to display a tree of all available properties. you will find details on property settings for each session type in the appropriate chapter.

1. 7

1. Click Save to save the new session configuration with the topology document. Click Save and Start to save the definition and start a session with the device.



To update a session configuration for a resource

On the canvas, right‑click the resource and select Edit Session.

(Alternatively, select the device on the canvas. On the Properties view, click the Session tab and then click )

The Edit Session Profile page enables you to view or edit property settings for the session profile.



To remove a session configuration for a resource

On the canvas, right‑click the resource and select Remove Session.

(Alternatively, select the device on the canvas. On the Properties view, click the Session tab and then click )

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/topologies_2.1.jpg) <!-- image_chunk: img_7102090bdf482df9 -->

![inline_icon](topics/images/topologies_2.2.jpg) <!-- image_chunk: img_f88bf637480a346c -->

![unknown](topics/images/topologies_2.4.jpg) <!-- image_chunk: img_fd42b0542d87348f -->

![inline_icon](topics/images/topologies_2.5.jpg) <!-- image_chunk: img_bae4e633141bdd4a -->

![inline_icon](topics/images/topologies_2.6.jpg) <!-- image_chunk: img_775d4488086d716a -->

![inline_icon](topics/images/topologies.7.jpg) <!-- image_chunk: img_6c66f6bf0392f6bb -->

![inline_icon](topics/images/topologies.8.jpg) <!-- image_chunk: img_a60f837b79a2a0dd -->
