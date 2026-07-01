---
{
  "chunk_id": "session_windows_start_using_session_prof__starting_a_session_using_a_session_profi_1588a41de9366e2b",
  "source_file": "topics/session_windows_start_using_session_profile.htm",
  "source_original_path": "topics/session_windows_start_using_session_profile.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Windows",
    "Starting a session using a session profile"
  ],
  "heading_path": [
    "Starting a session using a session profile",
    "Starting a session using a session profile"
  ],
  "anchor": "1202313",
  "context_ids": [
    "session_windows_start_using_session_profile"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "session_concept.htm#1324557",
    "session_profile_configuring.htm#1305610"
  ],
  "images": [],
  "content_hash": "1588a41de9366e2b",
  "level": 1
}
---

# Starting a session using a session profile > Starting a session using a session profile

You can start an interactive session in any of the following ways:

- Double-click the session profile in the Favorites view

- Right-click the session profile in the Project Explorer and select Start

- Click Start in the Session Profile editor (the New Session page).

The session starts in a new session window, as described in Session windows.

> **Note:** Advanced Users Many of the property settings for session profiles support field replacements to enable you to parameterize settings so they can be determined dynamically at runtime. You might use tcl, param, or profile command field replacements to improve the flexibility and portability of automated test cases. Sometimes, to perform an interactive test, you might need to manually start a session that typically starts only for automated test sessions. To enable you to do this, if any tcl, param, or profile command field replacements are encountered while starting the session, iTest starts a Tcl interpreter so that the field replacement can be resolved.

> **Note:** When the session ends, the Tcl interpreter is disposed. If a Tcl interpreter service is requested on restart, a new interpreter will be created and returned. See Defining a session profile (configuring the session settings).
