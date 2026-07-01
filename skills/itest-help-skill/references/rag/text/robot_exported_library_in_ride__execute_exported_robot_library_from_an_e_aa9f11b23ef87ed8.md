---
{
  "chunk_id": "robot_exported_library_in_ride__execute_exported_robot_library_from_an_e_aa9f11b23ef87ed8",
  "source_file": "topics/robot_exported_library_in_ride.htm",
  "source_original_path": "topics/robot_exported_library_in_ride.htm",
  "toc_path": [
    "iTest Online Help",
    "Export a QuickCall to Robot Library",
    "Execute exported Robot library from an external environment"
  ],
  "heading_path": [
    "Execute exported Robot library from an external environment",
    "Execute exported Robot library from an external environment"
  ],
  "anchor": "1360606",
  "context_ids": [
    "robot_exported_library_in_ride"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/robot_ride.png",
    "topics/images/robot_framework.2.jpg"
  ],
  "content_hash": "aa9f11b23ef87ed8",
  "level": 1
}
---

# Execute exported Robot library from an external environment > Execute exported Robot library from an external environment

You may create a Robot test script with the exported Robot library as required.

These steps provides an example of a Robot script with the exported Robot library and executing from an external environment.

Create Robot test case (e.g., in Robot Framework IDE). The diagram shows an example of iTest exported keywords file in RIDE.

1. Go to the folder that contains the exported Robot library file

Example: C:/Users/<username>/Robot_Library/

1. 2

1. Open Robot Framework IDE.

1. 3

1. Import the exported Robot library and the support file

Example: library_CMD_quickcall_library.py and iTestCommon.py

1. 4

1. Create a Robot test case with default value:

Library.../lib/library_CMD_quickcall_library.py

Library Collections

***Test Cases***

....

1. 5

1. Save and Run the Robot test case in Robot Framework IDE.

The following shows an example Robot test case and the corresponding log file that includes keyword and output.

| *** Settings *** Library library_ssh_1.py Library library_wireshark1.py Library iTestCommon.py Library Collections *** Test Cases *** My simple test Connect iTest Open project iTest72 Start session ssh_1_ffsp alias=ssh Start session wireshark1_ffsp alias=ws Switch session ssh ${response}= Get Interface ens33 Dictionary Should Contain Item ${response} mac a4:4e:31:74:71:d4 Switch session ws Load Pcap 1.pcap ${response}= Show Ds Field 2 Dictionary Should Contain Item ${response} ipdsfield 0x00000000 Switch session ssh ${response}= Get Cpu Info Dictionary Should Contain Item ${response} vendor_id GenuineIntel Close Session |
| --- |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/robot_ride.png) <!-- image_chunk: img_94deb900f596c9f9 -->

![screenshot](topics/images/robot_framework.2.jpg) <!-- image_chunk: img_30a02911418b31e6 -->
