---
{
  "chunk_id": "pal_preferences_session_level_control_ag__configure_listening_mode_listen_for_inco_c3bb07f576bef7ee",
  "source_file": "topics/pal_preferences_session_level_control_agent.htm",
  "source_original_path": "topics/pal_preferences_session_level_control_agent.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Automation Library",
    "Configure Listening Mode (Listen for incoming Python connections)"
  ],
  "heading_path": [
    "Configure Listening Mode (Listen for incoming Python connections)",
    "Configure Listening Mode (Listen for incoming Python connections)"
  ],
  "anchor": "1444627",
  "context_ids": [
    "pal_preferences_session_level_control_agent"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "debug_configure_itest_gui_as_an_agent.htm#1442060",
    "debug_velocity_drivers_executions_overview.htm#",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/python_ALib_agent_preferences.png"
  ],
  "content_hash": "c3bb07f576bef7ee",
  "level": 1
}
---

# Configure Listening Mode (Listen for incoming Python connections) > Configure Listening Mode (Listen for incoming Python connections)

Click Windows> Preferences> Spirent > Velocity > Agent: enable Agent mode and complete as described below to enable Listen for incoming Python connections mode. The following set up enables iTest to operate as an agent in listening mode:

- Configure Velocity Agent to run either as a Velocity client agent or an SLC server agent.

- Configure TCP listener port for incoming SLC agent connections.

- Configure Capture (optional Step Capture) mode for quick calls and commands issued from the Python API.

| Agent Mode | Select to enable Agent Mode |
| --- | --- |
| Agent Connection Mode | N/A in listening mode. |
| Listen for incoming Python connections | This option enables the listening mode for incoming Python connections. iTest GUI will wait for client connections and does not connect to Velocity as an Agent. The Velocity Agent Mode is disabled when Listen for incoming Python connection is selected. iTest either connects to Velocity as an agent or acts as a Session Level Agent server. In Listen for incoming Python connection mode, the agent listens for Python connection (iTest GUI waits for connections) and the Python Automation Library connects to iTest GUI when available. Note Communication with the agent goes by sending and receiving Protobuf-serialized objects over TCP. |
| Note | Communication with the agent goes by sending and receiving Protobuf-serialized objects over TCP. |
| Step capture | The Step capture option is available only when the Listen for incoming Python connections is selected. Selected: (Default), captures session actions (quick calls and commands) performed from the Python Automation Library on this iTest GUI instance. Not selected: the session actions performed from the Python Automation Library on this iTest GUI instance are not captured. |
|  | Selected: (Default), captures session actions (quick calls and commands) performed from the Python Automation Library on this iTest GUI instance. |
|  | Not selected: the session actions performed from the Python Automation Library on this iTest GUI instance are not captured. |
| Breakpoint at first step | N/A in listening mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”). |
| Agent Name: | Enter a name for the Agent. |
| Port | Indicates the port used by the Agent during execution. Port for Test Agent: Default: 443 (secure connection) Port for Session Level Control Agent: Default 9005 |
|  | Port for Test Agent: Default: 443 (secure connection) |
|  | Port for Session Level Control Agent: Default 9005 |
| Step timeout (sec) | N/A in listening mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”). |
| User feedback timeout (min) | N/A in listening mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”). |
| Agent Capabilities and Restrictions | N/A in listening Mode. See Configuring iTest GUI as an Agent (“Debug Velocity Drivers and Executions”). |
| Apply and Close | Click to apply settings and connect as Session Level Control Agent and close the window. The Preferences window displays the connection state message depending on whether the Agent is connected or not as follows. When not connected: Agent is listening for incoming Python connection When connected: Agent is connected. |
| Restore Defaults Apply | Restore default: Click to discard all the changes made and reset to the default values. Apply: Click to apply the changes made. |

> **Note:** Note See “Configuring iTest Preferences” for general information on preference settings.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/python_ALib_agent_preferences.png) <!-- image_chunk: img_09faaa89ceae90d5 -->
