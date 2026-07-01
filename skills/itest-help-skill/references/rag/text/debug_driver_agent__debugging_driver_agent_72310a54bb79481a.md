---
{
  "chunk_id": "debug_driver_agent__debugging_driver_agent_72310a54bb79481a",
  "source_file": "topics/debug_driver_agent.htm",
  "source_original_path": "topics/debug_driver_agent.htm",
  "toc_path": [
    "iTest Online Help",
    "Debug Velocity Drivers and Executions",
    "Debugging Driver Agent"
  ],
  "heading_path": [
    "Debugging Driver Agent",
    "Debugging Driver Agent"
  ],
  "anchor": "1460736",
  "context_ids": [
    "debug_driver_agent"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "debug_configure_itest_gui_as_an_agent.htm#1442060",
    "sharing.3.htm#1094115",
    "export_document_wizard.htm#",
    "debugging_tests.1.htm#"
  ],
  "images": [
    "topics/images/agent_capabilities.png",
    "topics/images/agent_restriction.png",
    "topics/images/agent_debug_example.png",
    "topics/images/agent_SLCdebug_example-Velocity.png",
    "topics/images/debug_velocity_driver_and_executions.5.jpg"
  ],
  "content_hash": "72310a54bb79481a",
  "level": 1
}
---

# Debugging Driver Agent > Debugging Driver Agent

Important The steps in this section are applicable for debugging driver agents with Velocity 7.x and later. For debugging Driver Agent for Velocity 6.1 see iTest 6.1 User Guide.

To ensure that the iTest UI connects to Velocity as a driver Agent, make sure you have set up the Window > Preferences correctly as in Configuring iTest GUI as an Agent.

1. In the iTest > Windows > Preferences dialog:.

Enter a name for the Agent in Agent Name, example: AgentDegugger

Enter pool/driver as a Name/Value pair in the Capabilities tab.

In the Restrictions tab, enter a Name/Value pair with unique values. This is so that your driver will only execute on the agent you are debugging with.

Example:

Click Apply to see for the changes to be affected).

> **Tip:** Tip In Velocity UI (REPORTS>Velocity Agents), see that the Agent is listed under Name section. Also that the Capabilities and Restrictions match your environment.

SLC Driver

1. 2

1. Find the driver to debug:

In Velocity, go to Library > Drivers and download the driver you wish to debug (e.g., Ping Driver 1.1.0).

1. In iTest, import the driver files from the downloaded archive file. (see “iTest Import wizard” on page 1727, in Chapter 97, “Wizards and Dialog boxes”).

1. You may want to rename the project (so that you don’t break or interfere with existing drivers).

1. In iTest, open the driver in Test Case editor and add the following on the Requirements tab as capabilities name/value pair with unique values.

Important The Agent Requirements must match the Restrictions of the driver in Velocity. This is so that your agent will only execute the driver you are debugging and not execute other drivers.

Example:

Save the test case.

1. In iTest, export the driver test case and the manifest project as an iTar file. (see Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity, in “Sharing iTest Resources”).

1. 3

1. In Velocity UI (LIBRARY>Drivers):

Upload the new driver to Velocity. For a new driver, click the Add button. For an existing driver, select the driver and click Edit button.

1. Create a resource that uses the new driver and then discover it (click Discover on the INVENTORY>Resource page).

1. 4

1. For example, if you choose to discover some basic resource from Velocity, the corresponding driver from Velocity will open, in iTest, in the iTest Debugging perspective for investigation.

Click the items in the Velocity Explorer to view. Edit as needed. Save files and export to back to Velocity

> **Note:** Note For more on debugging any iTest Test case. See “Debugging Test Cases”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/agent_capabilities.png) <!-- image_chunk: img_a4964fbe9d673711 -->

![screenshot](topics/images/agent_restriction.png) <!-- image_chunk: img_46ef7f136ff55358 -->

![screenshot](topics/images/agent_debug_example.png) <!-- image_chunk: img_2fb590bd305665f6 -->

![screenshot](topics/images/agent_SLCdebug_example-Velocity.png) <!-- image_chunk: img_88b8a98b2b828c22 -->

![screenshot](topics/images/debug_velocity_driver_and_executions.5.jpg) <!-- image_chunk: img_3078a2d51e2843bb -->
