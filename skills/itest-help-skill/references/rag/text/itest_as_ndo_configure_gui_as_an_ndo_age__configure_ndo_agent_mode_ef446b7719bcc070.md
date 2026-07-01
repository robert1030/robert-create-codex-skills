---
{
  "chunk_id": "itest_as_ndo_configure_gui_as_an_ndo_age__configure_ndo_agent_mode_ef446b7719bcc070",
  "source_file": "topics/itest_as_ndo_configure_gui_as_an_ndo_agent.htm",
  "source_original_path": "topics/itest_as_ndo_configure_gui_as_an_ndo_agent.htm",
  "toc_path": [
    "iTest Online Help",
    "Run iTest as Network DevOps agent",
    "Configuring iTest GUI as NDO Agent"
  ],
  "heading_path": [
    "Configuring iTest GUI as NDO Agent",
    "Configuring iTest GUI as NDO Agent",
    "Configure NDO Agent Mode"
  ],
  "anchor": "1447523",
  "context_ids": [
    "itest_as_ndo_configure_gui_as_an_ndo_agent"
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
    "ui_perspective_overview.htm#1697086",
    "debugging_tests.1.htm#",
    "preferences_itest.htm#"
  ],
  "images": [
    "topics/images/ndo_agent_preferences_configureNDOAgent.png"
  ],
  "content_hash": "ef446b7719bcc070",
  "level": 2
}
---

# Configuring iTest GUI as NDO Agent > Configuring iTest GUI as NDO Agent > Configure NDO Agent Mode

Click Spirent > Velocity > NDO and complete as described below.

| Start automatically | Default: Not Selected Select Start automatically option to start iTest as NDO agent when iTest starts. When you select the Start automatically option (or modify any property), a message displays saying that the properties have changed and that you should apply (click Apply button) for starting as NDO Agent. |
| --- | --- |
| Custom Templates folder | Custom templates folder is blank by default and NDO will use uploaded resources.itar or files from iTest (resources project) templates. You may browse to a location and upload the report template to be used. |
| Breakpoint at first step | Default: Selected Select to insert breakpoint at first step, if required. See also Enable this option to debug Python scripts and drivers on iTest agent. Enabled: When enabled, execution automatically pauses at the first line of a test case. In addition, The Agent Perspective always open automatically. See Velocity Agent/NDO Perspective. Disabled: When disabled, execution will not pause. In addition, The Agent Perspective does not automatically open or brought to foreground. See Velocity Agent/NDO Perspective. Note Breakpoints tell iTest to pause execution. See “Debugging Test Cases”. |
|  | Enabled: When enabled, execution automatically pauses at the first line of a test case. |
|  | Disabled: When disabled, execution will not pause. |
| Note | Breakpoints tell iTest to pause execution. See “Debugging Test Cases”. |
| Agent Name | Enter a name for the Agent. |
| Port | Indicates the port used by the Agent during execution. Port for NDO Agent: Default: 8443 (secure connection) |
| Agent Capabilities and Restrictions | Specify a unique capability/restriction to limit the volume of test executions. Note The name/value pair you enter is not case sensitive. iTest converts the name and value pair to lower case. Capabilities: Enter a name value pair for Agent capabilities. Example: language, python os.type, linux Restrictions: Enter a name value pair of Agent capabilities exclusive for your use. Indicates, that the agent (name, value pair) are used to limit the volume of test executions. For example, when using itest as NDO Agent, you would ensure that the agent capabilities are restricted for your test executions only. |
| Note | The name/value pair you enter is not case sensitive. iTest converts the name and value pair to lower case. |
| Start/Stop | Start: Displays when all the properties modified have been applied. That is, you have clicked the Apply button after a property is changed. Stop: Displays when NDO server is started. |
| Apply | Apply: Click to apply the changes made. |
| Restore Defaults | Restore default: Click to discard all the changes made and reset to the default values. |
| Apply and close | Click to apply settings and Connect as Agent and close the window. |

> **Note:** Note General information on setting and sharing preference settings appears in “Configuring iTest Preferences”.

![screenshot](topics/images/ndo_agent_preferences_configureNDOAgent.png) <!-- image_chunk: img_70473152dfb05e11 -->
