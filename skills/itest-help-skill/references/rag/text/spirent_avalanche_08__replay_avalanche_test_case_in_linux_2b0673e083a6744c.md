---
{
  "chunk_id": "spirent_avalanche_08__replay_avalanche_test_case_in_linux_2b0673e083a6744c",
  "source_file": "topics/spirent_avalanche.08.htm",
  "source_original_path": "topics/spirent_avalanche.08.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Replay Avalanche test case in Linux"
  ],
  "heading_path": [
    "Replay Avalanche test case in Linux",
    "Replay Avalanche test case in Linux"
  ],
  "anchor": "1316291",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "settingup_avalanche_automation_on_linux.htm#1316224",
    "spirent_avalanche.02.htm#1284850"
  ],
  "images": [
    "topics/images/05-AV_Linux_generate_tcl_test.png",
    "topics/images/05-a-AV_Linux_generate_tcl_test.png",
    "topics/images/07-AV_Linux_extract_AV.png",
    "topics/images/09_AV_Linux_setup_Session_AVL.png",
    "topics/images/10-a-AV_Linux_config_tcl_tab.png"
  ],
  "content_hash": "2b0673e083a6744c",
  "level": 1
}
---

# Replay Avalanche test case in Linux > Replay Avalanche test case in Linux

Generating TCL Tests

Use any of the following two methods to get Avalanche TCL tests: Write them yourself or export a GUI test to TCL. The example below illustrates exporting a GUI test to TCL.

1. Copy Tcl folder to /opt folder.

Open an Avalanche Commander session, load a test, and then go to File > Generate Tcl Test. The following window displays.

1. 2

1. Extract Layer_4_7_Auto_Linux_4.61

Extract Layer_4_7_Auto_Linux_4.61 into the folder: /opt/api/spirent/Layer_4_7_Application_Linux.

Setup Session Avalanche Linux

1. Configure the Chassis IP, Server Cluster / Client cluster unit and especially the config tcl would be the exact config.tcl extracted from a real TCL project.

1. 2

1. Configure the Tcl tab with the path specified inStep 2 on page 1650.

1. 3

1. As in Windows (Options for performing Avalanche tests), start the session, replay the test case, and display the report generated with Avalanche in Linux.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/05-AV_Linux_generate_tcl_test.png) <!-- image_chunk: img_c6ef076b80d1c145 -->

![screenshot](topics/images/05-a-AV_Linux_generate_tcl_test.png) <!-- image_chunk: img_19139ff8327d3cd1 -->

![screenshot](topics/images/07-AV_Linux_extract_AV.png) <!-- image_chunk: img_e0ae05f440c6a01b -->

![screenshot](topics/images/09_AV_Linux_setup_Session_AVL.png) <!-- image_chunk: img_12bcd38a6d648591 -->

![screenshot](topics/images/10-a-AV_Linux_config_tcl_tab.png) <!-- image_chunk: img_895c2273e70f456a -->
