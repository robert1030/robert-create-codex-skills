---
{
  "chunk_id": "activity_review_test_reports__to_add_steps_by_capturing_start_sessions_4c26f649a148d820",
  "source_file": "topics/activity_review_test_reports.htm",
  "source_original_path": "topics/activity_review_test_reports.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Activity View"
  ],
  "heading_path": [
    "Activity View",
    "Activity View",
    "Developing a test case",
    "To add steps by capturing (start sessions with devices and save the captured steps into a test case)"
  ],
  "anchor": "1713393",
  "context_ids": [],
  "index_keywords": [
    "Build a topology page",
    "Develop a test case page",
    "Execution view",
    "Manage workspace page",
    "Messages table",
    "Session Profile editor",
    "Work on a test case page",
    "adding session profiles to",
    "analysis rules",
    "defining for devices in topologies",
    "described",
    "editing",
    "examples",
    "find issues in",
    "importing",
    "in analysis rules defined",
    "issues in test reports",
    "preference settings",
    "project set files",
    "projects",
    "psf files",
    "session profiles in topologies",
    "setting criteria"
  ],
  "index_keyword_paths": [
    "Build a topology page",
    "Develop a test case page",
    "Execution view",
    "Manage workspace page",
    "Messages table",
    "Session Profile editor > preference settings",
    "Work on a test case page",
    "adding > session profiles in topologies",
    "analysis rules > described",
    "analysis rules > examples",
    "configuring > session profiles in topologies",
    "devices in topologies > adding session profiles to",
    "editing > session profiles in topologies",
    "editor preferences > Session Profile editor",
    "examples > analysis rules",
    "extractors > in analysis rules defined",
    "find > issues in test reports",
    "importing > project set files",
    "importing > projects",
    "importing > psf files",
    "issues > finding in test reports test reports > find issues in",
    "pass/fail > setting criteria",
    "preference settings > Session Profile editor",
    "processors > in analysis rules defined",
    "project set files > importing",
    "projects > importing",
    "psf files > importing",
    "session profiles > defining for devices in topologies",
    "topologies > adding session profiles to",
    "topologies > editing",
    "validating responses > analysis rules",
    "views > Execution view"
  ],
  "related_links": [
    "execute_pausing_resuming_stopping.htm#1233679",
    "single_stepping_overview.htm#1192549"
  ],
  "images": [
    "topics/images/views.02.jpg",
    "topics/images/views.03.jpg",
    "topics/images/views.04.jpg",
    "topics/images/views.05.jpg",
    "topics/images/views.06.jpg"
  ],
  "content_hash": "4c26f649a148d820",
  "level": 3
}
---

# Activity View > Activity View > Developing a test case > To add steps by capturing (start sessions with devices and save the captured steps into a test case)

1. 1

1. After opening or creating the test case, on the Develop a test case activity page, click Add steps by capturing. The Add steps to Test Case page opens.

1. 2

1. The current test case is identified at the top of the page. If a topology file or parameters file is associated with the test case, then they are also identified.

Click the filename to open the file in the appropriate editor

1. 3

1. Now start a session with a device: Click Start a Session . The Start a Session dialog box displays all devices defined in the topology that you associated with the test case. Navigate the tree to select the appropriate session and then click Start.

1. 4

1. Using the session profile settings that are defined for the device, iTest launches a session on the device.

- You can open as many sessions on as many devices as you like.

- Captured sessions are listed in the Sessions table.

- Captured steps are listed in the Steps table.

1. 5

1. Here are some tools for documenting or clearing captured steps

| Insert Comment | Select a step and click the button to add a comment step after the selected step. The comment step is added to the test case along with the captured steps. |
| --- | --- |
| Clear Steps | Clears all captured steps from the table, closes all open sessions, and cancels the capture activity. |

1. 6

1. When you are ready to add the captured steps from the Steps list into the test case, click Add Steps .

- To not add a particular step or session into the test case, right-click the step and select Exclude Item. Excluded steps are not added to the test case.

By default, excluded steps are not displayed in the table. To display excluded steps in the list (highlighted to indicate that they will not be added to the test case), right-click in the table and select Show Excluded Items.

- For new test cases, steps are added to the end of the test case.

- For existing test cases, the Insert Steps wizard prompts you to specify the location in the test case to add the steps.

- By default, the Close open sessions check box is checked; you can uncheck it to allow the sessions to remain active after you complete the process of adding the steps into the test case.

- When you click Finish, the steps are added to the test case.



To execute a test case

1. 1

1. After opening or creating the test case, on the Develop a test case activity page, click Execute test case. The Execute Test Case activity page opens.

1. 2

1. The current test case is identified at the top of the page. If a topology file or parameters file is associated with the test case, then they are also identified.

- Click the filename to open the file in the appropriate editor

- Click the button next to the filename to change to a different file

1. 3

1. To start execution, click . Use the following tools to control execution — you will find full details in Debugging: Executing procedures, Pausing, stopping, and single-stepping and Single-stepping through a test.

![inline_icon](topics/images/views.02.jpg) <!-- image_chunk: img_1fe4c415368ab4b0 -->

![screenshot](topics/images/views.03.jpg) <!-- image_chunk: img_39903a647452eac4 -->

![inline_icon](topics/images/views.04.jpg) <!-- image_chunk: img_8fefa18d0a7e1727 -->

![inline_icon](topics/images/views.05.jpg) <!-- image_chunk: img_01f52b9db1064ac7 -->

![inline_icon](topics/images/views.06.jpg) <!-- image_chunk: img_444967818e4f0b70 -->
