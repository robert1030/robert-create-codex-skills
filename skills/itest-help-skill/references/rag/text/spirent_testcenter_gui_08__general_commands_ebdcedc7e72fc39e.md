---
{
  "chunk_id": "spirent_testcenter_gui_08__general_commands_ebdcedc7e72fc39e",
  "source_file": "topics/spirent_testcenter_gui.08.htm",
  "source_original_path": "topics/spirent_testcenter_gui.08.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "General commands"
  ],
  "heading_path": [
    "General commands",
    "General commands"
  ],
  "anchor": "1357017",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_4.1.jpg"
  ],
  "content_hash": "ebdcedc7e72fc39e",
  "level": 1
}
---

# General commands > General commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| eval | Tcl_statement | — None — | Evaluates a Tcl statement for direct access to Spirent TestCenter’s TCL API. |
| saveConfiguration | filename |  | Saves the current configuration information returned by the device into a specified file for all or selected ports. Note Spirent limits the path to 256 characters. The file is used to configure the device exactly as if you had configured it using TestCenter: In test cases, you use configuration load to load the configuration settings to the device. You can specify the resulting file in the Configuration file setting in a session profile. The configuration is performed when the session starts. The configuration file is saved in XML format. with filename extension .xml, Argument filename is the configuration file to save the config to Example: project:///spirent.xml |
| Note | Spirent limits the path to 256 characters. |  |  |
| showTrafficGroups | — None — | — None — | Shows information about traffic groups |
| source | Tcl_script | — None — | Sources the specified TCL script from workspace |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/spirent_testcenter_gui_4.1.jpg) <!-- image_chunk: img_f5f13f713c1bf8ca -->
