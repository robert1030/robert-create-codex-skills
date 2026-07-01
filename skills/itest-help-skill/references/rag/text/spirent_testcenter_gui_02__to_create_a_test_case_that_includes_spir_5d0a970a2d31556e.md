---
{
  "chunk_id": "spirent_testcenter_gui_02__to_create_a_test_case_that_includes_spir_5d0a970a2d31556e",
  "source_file": "topics/spirent_testcenter_gui.02.htm",
  "source_original_path": "topics/spirent_testcenter_gui.02.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "To create a test case that includes Spirent TestCenter sessions"
  ],
  "heading_path": [
    "To create a test case that includes Spirent TestCenter sessions",
    "To create a test case that includes Spirent TestCenter sessions"
  ],
  "anchor": "1252284",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "session_profile_properties_testcenter.htm#1256431",
    "tgen_cmds_testcenter.htm#1332853",
    "tgen_results_testcenter.htm#1378416",
    "tgen_cmds_testcenter.htm#1371413",
    "capture_add_to_test_case_wizard.htm#1322677"
  ],
  "images": [
    "topics/images/spirent_testcenter_gui.01.jpg",
    "topics/images/spirent_testcenter_gui.02.jpg",
    "topics/images/spirent_testcenter_gui.04.jpg",
    "topics/images/spirent_testcenter_gui.07.jpg",
    "topics/images/STC_Port_config_06-19-19.png",
    "topics/images/STC_WirelessPort_ConsoleCapture.png",
    "topics/images/spirent_testcenter_gui.11.jpg",
    "topics/images/spirent_testcenter_gui.12.jpg"
  ],
  "content_hash": "5d0a970a2d31556e",
  "level": 1
}
---

# To create a test case that includes Spirent TestCenter sessions > To create a test case that includes Spirent TestCenter sessions

You typically save captured manual steps as a test case. Follow these steps:

1. Ensure that the TestCenter session profile or device is properly configured. See Session profile property settings for Spirent TestCenter sessions.

1. 2

1. Click to begin the direct-to-test process of saving the interactive session as a test case.

1. 3

1. Start the TestCenter session and perform the test as needed. You work in the iTest TestCenter session the same way you work in TestCenter. When you interact with a TestCenter component, iTest performs a TestCenter action and captures both the action and the response from TestCenter.

Example 1:

You first select Traffic Generator Port 1. When you click , iTest opens the StreamBlock Editor to enable you to configure the stream block (just like TestCenter). Then, when you click OK in the editor:

iTest submits an addStreamBlock 1 command to TestCenter on the Spirent device (add a stream block on the generator’s port 1).

In the session’s Console window, iTest displays the addStreamBlock 1 command. The response from TestCenter includes stream block settings that were implemented on the Spirent device.

> **Tip:** Tip You can execute the Tcl source and eval actions and all STC commands at the command line.

iTest captures an addStreamBlock step. Notice that the test case steps that iTest created from captured step refers to the port using the port ID (1 in the example). You can configure iTest to create steps using a variety or port formats (see To specify a list of port locations). The captured step includes the command that was sent to TestCenter on the Spirent device and its response. The captured step will become a step in the resulting test case, and it will execute exactly as you performed it in the interactive test.

Example 2: Properties for IEEE80211 (Wireless port)

Select Port 1. Change the default settings, for example, MIMO/SMA settings, Power Settings, Channel Frequency (option Dual Band), and MIMO Mode options..

Click Apply and the action reflects your changes on the Console. Example 1 shows updates to the ConfigurePort and Example 2 shows changes to the Channel band width.

1. 4

1. Continue working in the interactive TestCenter session. iTest captures both commands and responses. (See Spirent TestCenter result types in iTest for details.)

> **Note:** Note While not all TestCenter commands are available using buttons or other controls on the page, you can perform any TestCenter command by entering it on the iTest Console view (as described in Spirent TestCenter Command reference).

1. 5

1. When you finish, click to save the captured steps into a test case. (The Add Test Case wizard opens and help you through the process. For details on saving captured steps to test cases, see Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard.)

1. 6

1. The Test Case editor opens the new test case.

Example 1: The steps in the test case and the properties of the example step.

![unknown](topics/images/spirent_testcenter_gui.01.jpg) <!-- image_chunk: img_4f32692f23d621a6 -->

![screenshot](topics/images/spirent_testcenter_gui.02.jpg) <!-- image_chunk: img_f986270766b95517 -->

![unknown](topics/images/spirent_testcenter_gui.04.jpg) <!-- image_chunk: img_31e1e161b689d2e2 -->

![screenshot](topics/images/spirent_testcenter_gui.07.jpg) <!-- image_chunk: img_d7ba5b273eb64e77 -->

![screenshot](topics/images/STC_Port_config_06-19-19.png) <!-- image_chunk: img_06635680bc3b29fa -->

![screenshot](topics/images/STC_WirelessPort_ConsoleCapture.png) <!-- image_chunk: img_7a55c6e318dc533d -->

![unknown](topics/images/spirent_testcenter_gui.11.jpg) <!-- image_chunk: img_0f0b4d16e009c5ae -->

![screenshot](topics/images/spirent_testcenter_gui.12.jpg) <!-- image_chunk: img_199c19483afff93a -->
