---
{
  "chunk_id": "stc_rest_create_tc_toinclude_stc_rest_se__to_create_a_test_case_that_includes_spir_e901293646daa14f",
  "source_file": "topics/stc_rest_create_tc_toInclude_STC_REST_Sessions.htm",
  "source_original_path": "topics/stc_rest_create_tc_toInclude_STC_REST_Sessions.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session window",
    "To create a test case that includes Spirent TestCenter REST sessions"
  ],
  "heading_path": [
    "To create a test case that includes Spirent TestCenter REST sessions",
    "To create a test case that includes Spirent TestCenter REST sessions"
  ],
  "anchor": "1252284",
  "context_ids": [
    "stc_rest_create_tc_toInclude_STC_REST_Sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "stc_rest_session_profile_properties.htm#1256431",
    "stc_vlan_configure_2.htm#1371413",
    "capture_add_to_test_case_wizard.htm#1322677",
    "spirent_testcenter_gui.02.htm#1238638",
    "spirent_testcenter_gui.02.htm#1252284",
    "test_cases_creating_by_capture.htm#",
    "test_case_editor_overview.htm#"
  ],
  "images": [
    "topics/images/spirent_testcenter_rest_2.1.jpg",
    "topics/images/spirent_testcenter_rest.2.jpg",
    "topics/images/stc_rest_object_view_dropdown.png",
    "topics/images/stc_rest_object_action_dropdown.png",
    "topics/images/spirent_testcenter_rest.5.jpg",
    "topics/images/stc_RESTconfigPort_New_properties-06-20-19.png"
  ],
  "content_hash": "e901293646daa14f",
  "level": 1
}
---

# To create a test case that includes Spirent TestCenter REST sessions > To create a test case that includes Spirent TestCenter REST sessions

You typically save captured manual steps as a test case. Follow these steps:

1. Ensure that the TestCenter REST session profile or device is properly configured. See Session profile property settings for Spirent TestCenter REST sessions.

1. 2

1. Click to begin the direct-to-test process of saving the interactive session as a test case.

1. 3

1. Start the TestCenter REST session and perform the test as needed. You work in the iTest TestCenter REST session the same way you work in TestCenter. When you interact with a TestCenter component, iTest performs a TestCenter action and captures both the action and the response from TestCenter. For example:

You first select Port 1. When you click Auto Negotiate, iTest opens the Auto Negotiate Editor to view or create session (just like TestCenter). Then, click OK in the editor.

You may select Port 1 and change the default settings, for example, MIMO Configuration (option 4x4:4), Power Settings, Channel Frequency (option Dual Band), and Mode options. Click Apply and the action ConfigurePort reflects your changes on the Console. Then click Apply in the editor.

iTest submits command to TestCenter REST on the Spirent device (e.g., add a stream block on the generator’s port 1, configure port, and so on).

In the TestCenter REST Console window, iTest displays the command you entered. The response from TestCenter includes settings that were implemented on the Spirent device.

> **Note:** Note While not all TestCenter commands are available using buttons or other controls on the page, you can perform any TestCenter REST command by entering it on the iTest Console view (as described in Spirent TestCenter Command reference).

You may also select an object, right-click (for e.g., on Device) to view the properties and perform a required function.

In addition, you may select an object (e.g., Port 1) and right-click, to view the object handlers and their properties, and perform the required action.

1. 4

1. When you finish, click to save the captured steps into a test case. (The Add Test Case wizard opens and help you through the process. For details on saving captured steps to test cases, see Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard.)

1. 5

1. The Test Case editor opens the new test case. See Step 6 on page 1334 (section “To create a test case that includes Spirent TestCenter sessions”) for more details.

Example: The Port Steps properties for IEEE80211 (Wireless port) in the test case.

1. 6

1. Continue editing the test case by adding analysis rules and flow-control steps as needed.

- For information on working with test cases, see “Test Cases”.

- For information on using the Test Case editor, see “Test Case Editor”.

![unknown](topics/images/spirent_testcenter_rest_2.1.jpg) <!-- image_chunk: img_36eee345afa0372e -->

![screenshot](topics/images/spirent_testcenter_rest.2.jpg) <!-- image_chunk: img_437d3689175e56db -->

![screenshot](topics/images/stc_rest_object_view_dropdown.png) <!-- image_chunk: img_ed7aecb1974cfe13 -->

![screenshot](topics/images/stc_rest_object_action_dropdown.png) <!-- image_chunk: img_cc782bf1639187a0 -->

![unknown](topics/images/spirent_testcenter_rest.5.jpg) <!-- image_chunk: img_6f8e11426ea38c24 -->

![screenshot](topics/images/stc_RESTconfigPort_New_properties-06-20-19.png) <!-- image_chunk: img_5e4f7dd723852ee4 -->
