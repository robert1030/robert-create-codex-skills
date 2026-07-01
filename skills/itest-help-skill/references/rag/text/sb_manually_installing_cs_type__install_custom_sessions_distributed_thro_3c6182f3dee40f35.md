---
{
  "chunk_id": "sb_manually_installing_cs_type__install_custom_sessions_distributed_thro_3c6182f3dee40f35",
  "source_file": "topics/sb_manually_installing_cs_type.htm",
  "source_original_path": "topics/sb_manually_installing_cs_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "Manually Installing Custom Session Type within iTest"
  ],
  "heading_path": [
    "Manually Installing Custom Session Type within iTest",
    "Manually Installing Custom Session Type within iTest",
    "Install custom sessions distributed through a Central Server"
  ],
  "anchor": "1358346",
  "context_ids": [
    "sb_manually_installing_cs_type"
  ],
  "index_keywords": [
    "manually install custom session type"
  ],
  "index_keyword_paths": [
    "session builder > manually install custom session type"
  ],
  "related_links": [
    "preferences.14.htm#1256571",
    "preferences_itest.htm#",
    "#1360101"
  ],
  "images": [
    "topics/images/07-install-custom-sessions.png"
  ],
  "content_hash": "3c6182f3dee40f35",
  "level": 2
}
---

# Manually Installing Custom Session Type within iTest > Manually Installing Custom Session Type within iTest > Install custom sessions distributed through a Central Server

Sessions built with the Session Builder may be deployed on a central server and distributed to your end-users by setting up the Update Site.

Step 1

Set up Central Site for software distribution

Go to Windows -> Preferences and set up the central site for software distribution as described in Preferences: Install/Update (Chapter , “Configuring iTest Preferences”).

Install new session types from the central site

Select menu Help > Find and install new session types on top of the iTest window. The iTest Session Settings display with two tabs: Available Session Types and Installed Session Types.

> **Note:** Note You may get to the iTest Session Settings window via iTest > Tools > Browse on iTest store. See Install custom session type using iTest > Tools > Browse on iTest Store

- Available Session Types:

The list is retrieved and populated from a Central Server. The list shows the name of the session type, version, date created, whether licensed, description of the session, and whether includes document, if any.

- Select the session type (s) to install and click Install.

- Click Yes when a message displays saying that iTest needs to restart in order to apply new session type, whether you to restart iTest.

iTest restarts and the installs the selected session (s), which will be available in the list of Session Types in the Start a new session window.

- Installed Session Type: Lists all the installed session types. You may uninstall session types as required. Uninstall also requires iTest to be restarted in order to apply the changes.

![screenshot](topics/images/07-install-custom-sessions.png) <!-- image_chunk: img_24bf31d07cbd15bc -->
