---
{
  "chunk_id": "session_profile_configuring__to_define_a_session_profile_bbae99ca1264d90a",
  "source_file": "topics/session_profile_configuring.htm",
  "source_original_path": "topics/session_profile_configuring.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Defining a session profile (configuring the session settings)"
  ],
  "heading_path": [
    "Defining a session profile (configuring the session settings)",
    "Defining a session profile (configuring the session settings)",
    "To define a session profile"
  ],
  "anchor": "1305640",
  "context_ids": [
    "session_profile_configuring"
  ],
  "index_keywords": [
    "New Session page",
    "Session Profile editor",
    "Start a New Session tab",
    "adding new",
    "defining",
    "deleting",
    "editing",
    "moving",
    "renaming",
    "session profiles",
    "working with"
  ],
  "index_keyword_paths": [
    "New Session page",
    "Session Profile editor",
    "Start a New Session tab",
    "editing > session profiles",
    "editors > Session Profile editor",
    "renaming > session profiles",
    "session profiles > adding new",
    "session profiles > defining",
    "session profiles > deleting",
    "session profiles > editing",
    "session profiles > moving",
    "session profiles > renaming",
    "session profiles > working with"
  ],
  "related_links": [
    "session_profile_concept.htm#1304145",
    "#1536785",
    "#1316241",
    "inheritance_property.htm#1128847",
    "field_replacements_tasks.htm#1128496",
    "tce_steps_page.htm#1823591",
    "preferences.04.htm#1253281",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/session_profiles_2.1.jpg",
    "topics/images/spe_basic_label.png",
    "topics/images/spe_basic_profile_hierarchy.png",
    "topics/images/session_profiles.5.jpg"
  ],
  "content_hash": "bbae99ca1264d90a",
  "level": 2
}
---

# Defining a session profile (configuring the session settings) > Defining a session profile (configuring the session settings) > To define a session profile

This example describes the Start page of the Session Profile editor. Each of the other editor pages is described in turn.

> **Tip:** Tip Whenever the Session Profile editor is selected, the Session Profile menu appears in the menu bar. The options that appear in the menu vary depending on the editor page in use.

Click to open the Start page of the Session Profile editor.

1. Session Type: There are three ways to start defining a new session profile:

- Inherit all property settings from the default iTest template for a session type. Specify the Session type (Telnet, SNMP, Web, and so on).

- Inherit all property settings from an existing session profile — either a reference session profile or any other session profile. This is the most common and the most powerful way to define a session profile, as described in Reference session profiles.

To specify that this is a reference session profile:

1. Specify the session type (we selected SNMP in this example).

1. Check This is a reference session profile.

From now on, when you are defining other session profiles, the reference session profile will appear in the drop-down Inherits from list on the Session Profile editor’s Start page.

To specify that this session profile should inherit settings from a reference session profile:

Specify the session type (we selected SNMP in this example).

1. Check the This session profile inherits settings from another session profile check box

1. In the Inherits from box, specify the session profile to inherit settings from.

- All session profiles that are defined as reference session profiles appear in the drop-down list.

- When you click Browse, the dialog box enables you to select from both reference and non-reference session profiles, either in the Workspace (the document is in the current iTest workspace) or File system (the document is in an itar file somewhere in the file system).

1. Click Show Hierarchy to display the inheritance hierarchy of the session profile on the Profile Hierarchy page.

> **Note:** Note The Show Hierarchy button is enabled only after saving a Session Profile.

The Profile Hierarchy page displays the parent session and a list of children sessions that inherit settings from other session profiles. (That is, sessions added in Step a and Step c.)

| Command | Description |
| --- | --- |
| Refresh | Refresh the selected elements and their direct children. |
| Cancel Current Search | Cancels the current search (useful for long running searches). |
| Show Parent Hierarchy | Displays all parents of the selected element. |
| Show Child Hierarchy | Shows all inherited session profiles used by the currently selected Session Profile. |
| Show History List | Displays a history of previously displayed hierarchies. |
| Pin the Hierarchy View | Pins the current view and allows you to open multiple hierarchy views at the same time. |
| Right-Click | Opens a context menu with these options: |
| Open: Open selected element in the default editor (Session Profile Editor) |  |
| Refresh: Refresh the selected elements and their direct children. |  |
| Focus On: Focus Hierarchy View on the selected element. |  |

1. 2

1. Session Properties: Specify a Session name for this particular set of configuration settings (the session profile). For example, SNMP_myDUT. The name is important because:

- The name appears in the list whenever you are selecting a session to start. If you do not specify a name, then a default name like s1 is used.

- The name appears in captured steps, making it easy to associate captured steps with a particular device.

- The name is used as the default session name when you create a test case from captured steps or add an open step to a test case. The session name appears in the Session column for each step in the session.

1. 3

1. In the SNMP example, you will next specify the IP address or hostname for the device that you are connecting to.

> **Note:** Note To use IPv6 with a session, use the following syntax:

- Without substitution: [<IPv6>]

- With substitution: ['\[']::<IPv6>['\]'] Python: eval IPv6="http://[::1]:8080/dashboard/" TCL: eval set IPv6 "http://\[::1\]:8080/dashboard/"

Each session type has different required settings. The property settings associated with each session type are described in the chapter for the particular session type in a section titled “Session profile property settings for <session type> sessions”.

- Required property settings are marked with the * character.

- A blue text box indicates that the setting is being inherited from the session profile that the current session profile is based upon. If you are creating a session profile “from scratch”, then the settings are inherited from the iTest default session profile. See Property values: Inheriting settings.

- The indicates that you can use field replacements in the text of the property setting. See Field replacements: Substituting values into properties and commands.

> **Caution:** By default, iTest auto-validates property values as you set them. The validation process adds a marker to the property setting when there is a problem with a setting. Hold the cursor over the marker to read the details. If, instead, you configure iTest to perform validation only when you request it, then settings are not validated and no markers appear for invalid property settings. See Validation of steps and property settings.

1. 4

1. You have the option to specify additional session properties like screen color, timeouts, non-standard prompts, and so on. Click to open the Session Properties page. you will find details on property settings for each session type in the appropriate chapter.

1. 5

1. Optional. Language: Select the language that will be used to create the session profile.

Click the Settings tab. On the Settings page, use the default language displayed (as set in Preferences: Spirent > General > General preference settings, Chapter , “Configuring iTest Preferences”) or select a different language from the list.

When you select Language as Python, you may export the entire iTest test case (FFTC) to a Python script.

1. 6

1. Click Save to save the current property settings as a session profile. We recommend a <session type>_<Session name>.ffsp filename convention, for example, telnet_Myrouter.ffsp or snmp_10.235.34.5.ffsp. You have the option to save the profile to the Favorites view for easy access (recommended if you expect to use the profile often to start interactive sessions — you just double-click the profile name to start a session).

Click Start to start the session.

Click Reset to reset all properties to their default settings.

You can rename and edit profiles to meet particular needs. Every time you modify session profile settings, you must save the session profile before starting the session.

![inline_icon](topics/images/session_profiles_2.1.jpg) <!-- image_chunk: img_5f321b539dc9c688 -->

![screenshot](topics/images/spe_basic_label.png) <!-- image_chunk: img_e11bcf6f0190fd7c -->

![screenshot](topics/images/spe_basic_profile_hierarchy.png) <!-- image_chunk: img_18fe8031992deb41 -->

![unknown](topics/images/session_profiles.5.jpg) <!-- image_chunk: img_5fbc921713780425 -->
