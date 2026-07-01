---
{
  "chunk_id": "session_profile_property_settings__about_property_settings_54d32b585eacf6b4",
  "source_file": "topics/session_profile_property_settings.htm",
  "source_original_path": "topics/session_profile_property_settings.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "About property settings"
  ],
  "heading_path": [
    "About property settings",
    "About property settings"
  ],
  "anchor": "1483852",
  "context_ids": [
    "session_profile_property_settings"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "session_profile_concept.htm#1304370",
    "field_replacements_tasks.htm#",
    "tce_step_properties_open_step.htm#1716227"
  ],
  "images": [
    "topics/images/session_profiles.1.jpg"
  ],
  "content_hash": "54d32b585eacf6b4",
  "level": 1
}
---

# About property settings > About property settings

This topic describes the property settings that you can configure for sessions.

Device definitions, session definitions, and session profile documents supply the configuration settings that tell iTest how to open a connection with (launch) a session. For basic information on configuring a device or session profile, see Session profiles: Session configuration settings.

- On the Connect to Devices activity page, when you double-click a session type or click Edit, the properties appear on the Start Session dialog box

- On the Topology editor, when you select the session on the Session tab in the Properties view and click Edit, the properties appear on the Edit Session Profile dialog box

- On the Testbed editor, the properties appear in the Device Properties section

- On the Session Profile editor, the first group of properties appears on the Start a New Session page (the Start tab of the Session Profile editor). To access the other settings, click .

> **Note:** Note If you have already saved a device or session profile document with the appropriate settings, then you do not need to configure another document to start an interactive session. Instead, you can quickly start a session using one of the following methods:

- On the Connect to Devices activity page, select a session and click Edit

- In the Favorites view, expand the appropriate topology or testbed and double-click the device

- In the Favorites view, double-click the existing session profile

- In the Project Explorer, right-click the existing session profile and select Start

> **Note:** Tips Here are some ideas that apply to any session profile:

- Remember that you can use field replacements to provide values for most properties in the session profile (properties with the indicator). For example, you can specify the IP address property dynamically at runtime by passing a parameter value to the session. Let’s say that the parameter is named ip_addr. In the session profile, for the IP address property, you would type: [param ip_addr]. See “Field Replacements”.

- For an open step in a test case, you have the option to override any of the property settings so that all steps in the session use the new property settings. Change any of the properties for the open step that appears in the <sessionType> Session Properties section. See Step Properties section: Session Properties: Overriding device or session profile settings in the open step.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/session_profiles.1.jpg) <!-- image_chunk: img_5084a3229cda9bb5 -->
