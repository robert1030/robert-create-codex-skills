---
{
  "chunk_id": "pal_python_automation_library_overview__modes_of_operation_75f93ae4a256688b",
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
    "Modes of Operation"
  ],
  "anchor": "1472318",
  "context_ids": [
    "pal_python_automation_library_overview"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1446634",
    "pal_preferences_session_level_control_agent.htm#1444627",
    "#1463271",
    "#1446719",
    "param_parameters_type_secret.htm#1554375"
  ],
  "images": [],
  "content_hash": "75f93ae4a256688b",
  "level": 2
}
---

# Overview > Overview > Modes of Operation

The Python Automation Library provides these modes of Operation, connectivity, license usage.

- Connect to an iTest GUI instance (iTest GUI Mode)

- On the local host or remote host

- Requires that Session Level Control agent be enabled and in listening mode (see Configure Listening Mode (Listen for incoming Python connections))

- iTest GUI can use either Enterprise or Runtime license

- Connect to an agent (running agent instance) on a remote workstation (Remote Mode).

- On the local host or remote host

- Requires that the agent is already started and in “listening” mode for SLC connections (see Configure Listening Mode (Listen for incoming Python connections))

- Agent requires a Runtime license at startup

- Connect to a standalone workstation (Standalone Mode)

- On the local host

- Auto-launch an agent in the background

- Agent requires a Runtime license at startup

In the first two cases, iTest opens a socket and listens for connections. The listening mode is enabled via a specific agent command line parameter “–listeningMode”, and on iTest GUI via “Configure Listening Mode (Listen for incoming Python connections)”.

> **Note:** Note When running an execution as an iTest agent (either Velocity agent or Python SLC agent), the masked values of the parameter type Secret cannot be un-masked. See About the Parameter Type ‘Secret’.
