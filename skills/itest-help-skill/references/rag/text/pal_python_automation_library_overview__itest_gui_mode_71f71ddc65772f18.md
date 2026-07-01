---
{
  "chunk_id": "pal_python_automation_library_overview__itest_gui_mode_71f71ddc65772f18",
  "source_file": "topics/pal_python_automation_library_overview.htm",
  "source_original_path": "topics/pal_python_automation_library_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Automation Library",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview",
    "Modes of Operation",
    "iTest GUI Mode"
  ],
  "anchor": "1446634",
  "context_ids": [
    "pal_python_automation_library_overview"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "pal_preferences_session_level_control_agent.htm#1444627"
  ],
  "images": [],
  "content_hash": "71f71ddc65772f18",
  "level": 3
}
---

# Overview > Overview > Modes of Operation > iTest GUI Mode

You may configure the listening mode for the iTest GUI via the Session Level Control Agent option (see Configure Listening Mode (Listen for incoming Python connections)). If enabled, iTest GUI opens the listening socket at startup (or when enabled). The agent can either be connected to Velocity or available as a session level control agent, but not both at the same time.

> **Note:** Note iTest GUI becomes the agent running in listening mode. That is, the Python library can act as a client, controlling iTest at a step level.

In the iTest GUI mode, the Python Automation Library connects to the iTest GUI. If already connected (e.g., another instance of the library on a remote workstation), a new connection attempt would fail. Thus, only one Spirent Python Automation Library instance can use an iTest GUI instance at a time.
