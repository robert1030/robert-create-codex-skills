---
{
  "chunk_id": "debug_configure_itest_gui_as_an_agent__configure_velocity_agent_mode_83457b18d339478f",
  "source_file": "topics/debug_configure_itest_gui_as_an_agent.htm",
  "source_original_path": "topics/debug_configure_itest_gui_as_an_agent.htm",
  "toc_path": [
    "iTest Online Help",
    "Debug Velocity Drivers and Executions",
    "Configuring iTest GUI as an Agent"
  ],
  "heading_path": [
    "Configuring iTest GUI as an Agent",
    "Configuring iTest GUI as an Agent",
    "Configure Velocity Agent Mode"
  ],
  "anchor": "1447523",
  "context_ids": [
    "debug_configure_itest_gui_as_an_agent"
  ],
  "index_keywords": [
    "Agent",
    "preference settings"
  ],
  "index_keyword_paths": [
    "Agent > preference settings",
    "preference settings > Agent"
  ],
  "related_links": [
    "pal_preferences_session_level_control_agent.htm#1444627",
    "pal_python_automation_library_overview.htm#",
    "ui_perspective_overview.htm#1697086",
    "debugging_tests.1.htm#",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/debug_velocity_driver_and_executions.1.jpg"
  ],
  "content_hash": "83457b18d339478f",
  "level": 2
}
---

# Configuring iTest GUI as an Agent > Configuring iTest GUI as an Agent > Configure Velocity Agent Mode

Click Spirent > Velocity > Agent: enable Agent mode and complete as described below.

| Agent Mode | Select to enable Agent Mode. If iTest is in use as NDO Agent, an error message displays saying the iTest is already in use as NDS Agent. Important iTest does not allow simultaneous start of iTest as NDO Agent and Velocity Agent. | Important | iTest does not allow simultaneous start of iTest as NDO Agent and Velocity Agent. |
| --- | --- | --- | --- |
| Important | iTest does not allow simultaneous start of iTest as NDO Agent and Velocity Agent. |  |  |
| Agent Connection Mode | Select an option below to indicate how you wish to be connected to the Agent. Automatically connect as Agent: Select to ensure that iTest automatically connects as an Agent at startup. Prompt to connect as Agent every time: Select to ensure that iTest prompts you at startup to confirm whether iTest should connect to Velocity Server as Agent. (Default) Do not automatically connect as Agent at startup: Select to ensure that iTest does not automatically connect to Velocity Server as an Agent at startup. Note The Listen for incoming Python connection is disabled when Agent Connection Mode is selected. |  | Automatically connect as Agent: Select to ensure that iTest automatically connects as an Agent at startup. |
|  | Automatically connect as Agent: Select to ensure that iTest automatically connects as an Agent at startup. |  |  |
|  | Prompt to connect as Agent every time: Select to ensure that iTest prompts you at startup to confirm whether iTest should connect to Velocity Server as Agent. (Default) |  |  |
|  | Do not automatically connect as Agent at startup: Select to ensure that iTest does not automatically connect to Velocity Server as an Agent at startup. |  |  |
| Note | The Listen for incoming Python connection is disabled when Agent Connection Mode is selected. |  |  |
| Listen for incoming Python connections | N/A in Agent Connection Mode. See Configure Listening Mode (Listen for incoming Python connections) (“Python Automation Library”). This option enables the listening mode. iTest GUI does not connect to Velocity as an Agent, but waits for the incoming connections instead. Note The Velocity Agent Mode is disabled when Listen for incoming Python connection is selected. iTest either connects as an Agent or acts as a Listen for incoming Python connection server. In Listen for incoming Python connection mode, the Agent listens for Python connections (iTest GUI waits for connections) and the Python Automation Library connects to iTest GUI when available. | Note | The Velocity Agent Mode is disabled when Listen for incoming Python connection is selected. |
| Note | The Velocity Agent Mode is disabled when Listen for incoming Python connection is selected. |  |  |
| Step capture | The Step capture option becomes available only when the Listen for incoming Python connection is selected. Selected: (Default), the session actions performed by the Python Automation Library on this iTest GUI instance are captured. Not selected: the session actions performed by the Python Automation Library on this iTest GUI instance are not captured. |  | Selected: (Default), the session actions performed by the Python Automation Library on this iTest GUI instance are captured. |
|  | Selected: (Default), the session actions performed by the Python Automation Library on this iTest GUI instance are captured. |  |  |
|  | Not selected: the session actions performed by the Python Automation Library on this iTest GUI instance are not captured. |  |  |
| Breakpoint at first step | Default: Selected Select to insert breakpoint at first step, if required. Enable this option to debug Python scripts and drivers on iTest agent. Enabled: When enabled, execution automatically pauses at the first line of a script. In addition, The Agent Perspective always open automatically. See Velocity Agent/NDO Perspective. Disabled: When disabled, execution will not pause. In addition, The Agent Perspective does not automatically open or brought to foreground. See Velocity Agent/NDO Perspective. Note Breakpoints tell iTest to pause execution. See “Debugging Test Cases” |  | Enabled: When enabled, execution automatically pauses at the first line of a script. |
|  | Enabled: When enabled, execution automatically pauses at the first line of a script. |  |  |
|  | Disabled: When disabled, execution will not pause. |  |  |
| Note | Breakpoints tell iTest to pause execution. See “Debugging Test Cases” |  |  |
| Agent Name: | Enter a name for the Agent. |  |  |
| Port | Indicates the port used by the Agent during execution. Port for Test Agent: Default: 443 443 (secure connection) Port for Session Level Control Agent: Default 9005 |  | Port for Test Agent: Default: 443 443 (secure connection) |
|  | Port for Test Agent: Default: 443 443 (secure connection) |  |  |
|  | Port for Session Level Control Agent: Default 9005 |  |  |
| Step timeout (sec) | Specify a time limit in seconds to apply to all steps in the test cases using this Agent. if a step is not completed within the specified time limit, iTest stops the test execution. Note This setting overrides the Default step timeout property specified on the General page of the Test Case editor. | Note | This setting overrides the Default step timeout property specified on the General page of the Test Case editor. |
| Note | This setting overrides the Default step timeout property specified on the General page of the Test Case editor. |  |  |
| User feedback timeout (min) | Default: 30 iTest pauses execution for a period specified in User feedback timeout (min) and prompts you to confirm where you wish to continue execution. This is to prevent deadlocks and endless executions. Velocity displays a message saying that the Agent Execution will automatically be aborted in the species number of minutes, displays a count-down time and asks you whether to Continue Execution or Abort. |  |  |
| Agent Capabilities and Restrictions | Specify a unique capability/restriction to limit the volume of test executions. Note The name/value pair you enter is not case sensitive. iTest converts the name and value pair to lower case. Capabilities: Enter a name value pair for Agent capabilities. Example: os.type, win 32 os.type, linux To debug drivers, ensure to define Agent with capability value as driver. For example name = pool, value = driver To debug drivers that use SLC session, ensure to define Agent with capability value as real-time. For example name = pool, value = real-time. Restrictions: Enter a name value pair of Agent capabilities exclusive for your use. Indicates, that the agent (name, value pair) are used to limit the volume of test executions. For example, when debugging a test case or a driver, you would ensure that the agent capabilities are restricted for your executions only. | Note | The name/value pair you enter is not case sensitive. iTest converts the name and value pair to lower case. |
| Note | The name/value pair you enter is not case sensitive. iTest converts the name and value pair to lower case. |  |  |
| Apply and close | Click to apply settings and Connect as Agent and close the window. |  |  |
| Restore Defaults Apply | Restore default: Click to discard all the changes made and reset to the default values. Apply: Click to apply the changes made. |  |  |

> **Note:** Note General information on setting and sharing preference settings appears in “Configuring iTest Preferences”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/debug_velocity_driver_and_executions.1.jpg) <!-- image_chunk: img_6896586f9a392bb4 -->
