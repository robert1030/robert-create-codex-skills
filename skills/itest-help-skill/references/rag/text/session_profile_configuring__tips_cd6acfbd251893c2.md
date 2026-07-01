---
{
  "chunk_id": "session_profile_configuring__tips_cd6acfbd251893c2",
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
    "Tips"
  ],
  "anchor": "1125591",
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
    "parameters_overview.htm#",
    "inheritance_property.htm#1128847",
    "tce_step_properties_open_step.htm#1716227"
  ],
  "images": [],
  "content_hash": "cd6acfbd251893c2",
  "level": 2
}
---

# Defining a session profile (configuring the session settings) > Defining a session profile (configuring the session settings) > Tips

- Whenever possible in test case open steps and device definitions, use a reference session profile that uses parameters for device- or session-specific values. For example, use a [param ipAddress] field replacement for the IP address property. This will save you a lot of time and frustration when compared with creating and maintaining a unique profile for each device (especially if the session returns a variety of prompts). See “Parameters” and Property values: Inheriting settings.

- If you use a profile often (for example, a Telnet session with Router 5 and green text on a black background named telnet_router5-green), then add it to the Favorites view when you save the profile. From then on, in the Favorites view, you can just double-click telnet_router5-green to open a Telnet session with the settings that you prefer.

- You can launch a group of related session profiles at the same time. In the Project Explorer or Favorites view, select the sessions, right-click the selection, and then select Start All Sessions. In the Project Explorer, you can also right-click a folder containing multiple sessions.

- In the Test Case editor for an open step, you can override any session profile setting. You change the property settings in the <Session Type> Session Properties group (for example, Telnet Session Properties). See Step Properties section: Session Properties: Overriding device or session profile settings in the open step.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
