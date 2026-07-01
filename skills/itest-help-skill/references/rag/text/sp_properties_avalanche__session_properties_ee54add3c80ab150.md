---
{
  "chunk_id": "sp_properties_avalanche__session_properties_ee54add3c80ab150",
  "source_file": "topics/sp_properties_avalanche.htm",
  "source_original_path": "topics/sp_properties_avalanche.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Session profile property settings for Spirent Avalanche sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent Avalanche sessions",
    "Session profile property settings for Spirent Avalanche sessions",
    "Session Properties"
  ],
  "anchor": "1224272",
  "context_ids": [
    "sp_properties_avalanche"
  ],
  "index_keywords": [
    "Avalanche sessions",
    "property settings",
    "sessions"
  ],
  "index_keyword_paths": [
    "Avalanche sessions",
    "Avalanche sessions > property settings",
    "Spirent Avalanche > sessions",
    "configuring > Avalanche sessions"
  ],
  "related_links": [
    "spirent_avalanche.06.htm#1297886",
    "avalanche_session_window.htm#1273889",
    "spirent_avalanche.12.htm#1289807",
    "spirent_avalanche.05.htm#1293574",
    "#1218428"
  ],
  "images": [],
  "content_hash": "ee54add3c80ab150",
  "level": 2
}
---

# Session profile property settings for Spirent Avalanche sessions > Session profile property settings for Spirent Avalanche sessions > Session Properties

The first two properties are associated with the option to execute the test defined in the Avalanche-generated test.tcl and config.tcl files. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode).

| Use Avalanche Tcl test files | Check the box to execute the test defined in the Avalanche-generated test.tcl and config.tcl files. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode). If you check the box, then you must specify the path to the folder that holds the config.tcl and test.tcl files in the Tcl test folder property Uncheck the box to cause iTest to execute the test.tcl script and execute a default config.tcl script. When iTest processes test.tcl, several settings are parameterized, enabling you to configure them during the session using the Configure button. See Test Control section for details. Default: unchecked |
| --- | --- |
| Tcl test folder | Used only if Use Avalanche Tcl test files is checked. Specify the path to the Tcl test folder that holds the Avalanche-generated test.tcl and config.tcl scripts. Note This is also the working folder for test Specifying cards, slots, port groups, and ports/virtual portst execution. All files that are generated during execution (for example, results) are stored in this folder. Default: [blank] |
| Note | This is also the working folder for test Specifying cards, slots, port groups, and ports/virtual portst execution. All files that are generated during execution (for example, results) are stored in this folder. |

The following property settings are used only if Use Avalanche Tcl test files is unchecked. See Running an Avalanche test on a TestCenter device (Normal mode).

| Chassis IP | Required. Specify the IP address or hostname of the Spirent device. |
| --- | --- |
| Client cluster units | Required. Space-separated list of unit IDs for the client. Note Be sure to review Specifying cards, slots, port groups, and ports/virtual ports before setting values. Each Unit ID has either of the following formats: <portGroup> When Avalanche is being run on an appliance, specify the port group number. or <slotNumber>,<portGroupNumber>;<unitNumber> <slotNumber>,<portGroupNumber> unitNumber is the number of the unit on which the port belongs. For Avalanche 4.10 and newer, specify 0 to auto‑select the unit number. For configing multiple chassis, enter as follows: Appliance: Client cluster units: chassis/card/port or chassis/port or STC chassis : Client cluster units : chassis/card/group;virtualport The virtualport must match the Virtual port set in the Port Provision List. |
| Note | Be sure to review Specifying cards, slots, port groups, and ports/virtual ports before setting values. |
| Server cluster units | Required. Space-separated list of unit IDs for the server. See the description for Client cluster units |
| config.tcl file | Required. Specify the path to the TCL initialization script (config.tcl) for sessions that use this session profile. The script includes all required parameters for test execution. When iTest processes the script, several settings are parameterized, enabling you to configure them during test execution using the Configure button. See Test Control section for details. See the Enable pass-through mode property. |
| Test execution folder | Optional.This is the folder whose contents are displayed in the Data Files tree in the session window. Specify the URI pointing to the working directory for test execution. All files that are generated during execution (for example, results) are stored in the specified directory. If you do not specify a folder, then iTest creates a temporary folder for this purpose. |
