---
{
  "chunk_id": "debugging_python_drivers_itest_agent_mod__install_pydev_in_itest_478d622bce9a616f",
  "source_file": "topics/Debugging_Python_drivers_iTest_Agent_mode.htm",
  "source_original_path": "topics/Debugging_Python_drivers_iTest_Agent_mode.htm",
  "toc_path": [
    "iTest Online Help",
    "Debug Velocity Drivers and Executions",
    "Debugging Python drivers in iTest Agent mode"
  ],
  "heading_path": [
    "Debugging Python drivers in iTest Agent mode",
    "Debugging Python drivers in iTest Agent mode",
    "Connecting to Velocity as Driver Agent",
    "Install PyDev in iTest"
  ],
  "anchor": "1497222",
  "context_ids": [
    "Debugging_Python_drivers_iTest_Agent_mode"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "debug_configure_itest_gui_as_an_agent.htm#1442060",
    "debug_configure_itest_gui_as_an_agent.htm#1447523",
    "import_wizard.htm#1157470",
    "sharing.3.htm#1094115",
    "export_document_wizard.htm#",
    "debugging_tests.1.htm#"
  ],
  "images": [
    "topics/images/agent_python_debug_restart.png",
    "topics/images/agent_pythonDebug.png",
    "topics/images/agent_debug_pythonDriver.png",
    "topics/images/agent_pyhton_debugPerspective.png",
    "topics/images/debug_velocity_driver_and_executions_2.5.jpg",
    "topics/images/agent_python_driver_debug.png"
  ],
  "content_hash": "478d622bce9a616f",
  "level": 4
}
---

# Debugging Python drivers in iTest Agent mode > Debugging Python drivers in iTest Agent mode > Connecting to Velocity as Driver Agent > Install PyDev in iTest

- iTest bundles Python IDE PyDev with iTest on Windows and Linux platforms.

- You are required to manually install PyDev in iTest on MacOS to work with this feature.

iTest Installer for macOS does not include PyDev (Python IDE). You are required to manually install PyDev version 26.2 in iTest on MacOS to debug Python drivers in iTest Agent Mode. On iTest GUI main menu, navigate to Help > Install New Software, in the dialog use PyDev 26.2 update-site https://www.pydev.org/update_sites/12.0.0/. Restart iTest after the installation is completed.

> **Note:** Note iTest uses PyDev to launch scripts associated with the Python interpreter (referenced in the script manifest). If PyDev is not installed, iTest will execute Python scripts and drivers without pausing (not in debug mode). PyDev automatically opens the Debug perspective (if requested). Scripts and driver will be executed irrespective of whether PyDev is installed.

The following limitations apply to PyDev use:

- Python script is recommended to be written in an ASCII compatible encoding (UTF-8 is compatible while wide encodings like UTF-16 is not).

- As deep inspection of process under debug is available to you, all parameter type Secret passed as arguments or environment variable to script under debug will be available for inspection.

- Only one Python execution may be debugged at a time in the same workspace.

- Restart/relaunch of Python driver debugging is not supported. In addition, terminating and attempting to relaunch from Debug view causes an error about missing project.

- Due to a defect in PyDev, a frame in Debug view may need to be explicitly selected to execute Run and Step commands.

1. 1

1. Set up the Window > Preferences correctly as in Configuring iTest GUI as an Agent.

In the iTest > Windows > Preferences dialog do the following:

Select Breakpoint On first Step to ensure the execution of driver stops on first encounter (true). See Configure Velocity Agent Mode for a detailed description.

Enter a name for the Agent in Agent Name, example: AgentDebug

Enter Name/Value pair in the Agent Capabilities and Restrictions section:

- Capabilities tab: Enter language = python (for script debugging you need to specify the capabilities as language = python)

- Restrictions tab: Enter pool = driver (only for driver debug). This is to ensure that your driver will only execute on the agent being debugged.

Click Apply to see for the changes to be affected.

> **Tip:** Tip In Velocity UI (REPORTS>Velocity Agents), see that the Agent is listed under Name section. Also that the Capabilities and Restrictions match your environment.

1. 2

1. When debugging Python scripts:

Go to Velocity > Library > Automation Assets, run the Python Script, select the iTest Agent to run the script.

1. Debug perspective automatically displays in iTest shows with the following details:

(Configured in Windows > Preferences > Run/Debug > Perspectives. See 'Open the associated perspective when an application suspends'

- Console output

- Variables view/information. You may also see the Velocity environment variables (shown with prefix VELOCITY_PRAM_).

- Arguments (you may see the command-line arguments used to invoke the Python script).

> **Note:** Note If certain information requires the Python script to load certain python library, iTest displays a runtime error when the required libraries are not included.

1. 3

1. Find the driver to debug:

In Velocity, go to Library > Drivers and download the driver you wish to debug (e.g., Python_driver_online).

1. In iTest, import the driver files from the downloaded archive file. (see “iTest Import wizard, in “Debug Velocity Drivers and Executions”).

1. You may want to rename the project (so that you don’t break or interfere with existing drivers).

1. In iTest, open the driver in Test Case editor and add the following on the Requirements tab as capabilities name/value pair with unique values.

Important The Agent Requirements must match the Restrictions of the driver in Velocity. This is so that your agent will only execute the driver you are debugging and not execute other drivers.

Example:

Save the test case.

1. In iTest, export the driver test case and the manifest project as an iTar file. (see Exporting iTest projects as iTar files, Network DevOps Agent, or Velocity, in “Sharing iTest Resources”).

1. 4

1. In Velocity UI (LIBRARY>Drivers):

Upload the new driver to Velocity. For a new driver, click the Add button. For an existing driver, select the driver and click Edit button.

1. Create a resource that uses the new driver and then discover it (click Discover on the INVENTORY>Resource page).

1. 5

1. For example, if you choose to discover some basic resource from Velocity, the corresponding driver from Velocity will open, in iTest, in the Debug perspective for investigation (if requested).

Click the items in the Velocity Explorer to view. Edit as needed. Save files and export to back to Velocity

> **Note:** Note For more on debugging any iTest Test case. See “Debugging Test Cases”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/agent_python_debug_restart.png) <!-- image_chunk: img_76ebc7329a272e18 -->

![screenshot](topics/images/agent_pythonDebug.png) <!-- image_chunk: img_0bec2ef829fc48b7 -->

![screenshot](topics/images/agent_debug_pythonDriver.png) <!-- image_chunk: img_d082184d48ff85e6 -->

![screenshot](topics/images/agent_pyhton_debugPerspective.png) <!-- image_chunk: img_09763e982bdc81ed -->

![screenshot](topics/images/debug_velocity_driver_and_executions_2.5.jpg) <!-- image_chunk: img_573c2fada6669743 -->

![screenshot](topics/images/agent_python_driver_debug.png) <!-- image_chunk: img_2c799cf8c090fa3e -->
