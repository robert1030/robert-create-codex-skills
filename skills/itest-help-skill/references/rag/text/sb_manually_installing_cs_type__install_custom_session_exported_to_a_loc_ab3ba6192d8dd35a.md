---
{
  "chunk_id": "sb_manually_installing_cs_type__install_custom_session_exported_to_a_loc_ab3ba6192d8dd35a",
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
    "Install custom session exported to a local directory"
  ],
  "anchor": "1356712",
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
    "sb_creating_a_cs_type.htm#1336283",
    "#1360101",
    "#1358346"
  ],
  "images": [
    "topics/images/07-a-install-custom-sessions.png"
  ],
  "content_hash": "ab3ba6192d8dd35a",
  "level": 2
}
---

# Manually Installing Custom Session Type within iTest > Manually Installing Custom Session Type within iTest > Install custom session exported to a local directory

Use these steps to install custom sessions on a local directory copied using the Export to directory option when building custom session (Step 2Select QuickCall Libraries and location to save).

- Go to the Help > Find and install new session types menu on the top of the iTest window. The iTest Session Settings window displays with two tabs: Available Session Types and Installed Session Types.

> **Note:** Note You may get to the iTest Session Settings window via iTest > Tools > Browse on iTest store. See Install custom session type using iTest > Tools > Browse on iTest Store

- Available Session Types:

> **Note:** Note The list is retrieved and populated from a Central Server (see Install custom sessions distributed through a Central Server).

- Click Browse local directory, navigate to location of the custom session files, select the folder and click OK.

The Available Session Types tab get populated with the custom sessions in the folder. The list shows the name of the session type, version, date created, whether licensed, description of the session, and whether includes document, if any

- Select the Custom session file and click Install.

iTest displays a message asking you to confirm installation of the session type. When you confirm, iTest informs you that it requires to restart in order to apply the new session type and asks for your confirmation again.

iTest restarts and the installs the selected session (s), which will be available in the list of Session Types in the Start a new session window.

- Installed Session Type: Lists all the installed session types. You may uninstall session types as required. Uninstall also requires iTest to be restarted in order to apply the changes.

![screenshot](topics/images/07-a-install-custom-sessions.png) <!-- image_chunk: img_79393acd3f4b586b -->
