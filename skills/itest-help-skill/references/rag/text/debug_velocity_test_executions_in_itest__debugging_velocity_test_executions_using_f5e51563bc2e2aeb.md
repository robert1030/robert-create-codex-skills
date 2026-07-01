---
{
  "chunk_id": "debug_velocity_test_executions_in_itest__debugging_velocity_test_executions_using_f5e51563bc2e2aeb",
  "source_file": "topics/debug_velocity_test_executions_in_itest.htm",
  "source_original_path": "topics/debug_velocity_test_executions_in_itest.htm",
  "toc_path": [
    "iTest Online Help",
    "Debug Velocity Drivers and Executions",
    "Debugging Velocity Test Executions using iTest GUI"
  ],
  "heading_path": [
    "Debugging Velocity Test Executions using iTest GUI",
    "Debugging Velocity Test Executions using iTest GUI"
  ],
  "anchor": "1450936",
  "context_ids": [
    "debug_velocity_test_executions_in_itest"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "debug_configure_itest_gui_as_an_agent.htm#1447523"
  ],
  "images": [
    "topics/images/debug_velocity_driver_and_executions_2.1.jpg",
    "topics/images/agent_res_page_in_itest_vel_exec.png",
    "topics/images/agent_sharing_res_report.png"
  ],
  "content_hash": "f5e51563bc2e2aeb",
  "level": 1
}
---

# Debugging Velocity Test Executions using iTest GUI > Debugging Velocity Test Executions using iTest GUI

To ensure that the iTest UI connects to Velocity as a Test Agent, make sure you have set up the Window > Preferences correctly as in Configure Velocity Agent Mode.

> **Note:** Note Ensure that the Driver Executions only option is not selected and, agent capabilities and restrictions are specified. The test agent and capabilities will be listed in Velocity > Reports> Velocity Agents. The agent will not be listed if you specify restrictions.

In Velocity, select the Automation Asset to execute, when the execution starts, go to the iTest GUI and notice the following.

- Velocity Execution Explorer, displays the files included in the iTar. If you share resource between iTest and Velocity, these resources are hidden in the iTest Project Explorer until the Velocity execution completes.

If the Velocity execution included a Topology, you may view it in iTest GUI from the Reservation tab.

- If you have configured Breakpoint at first step option, iTest pauses execution until you click to continue execution.

- If a test case step execution is not completed within the time limit specified in A Step timeout (sec), iTest stops the test case.

- iTest pauses execution for a period specified in User feedback timeout (min). iTest displays a message saying that the Agent Execution will automatically be aborted in the specified number of minutes, displays a count-down time and asks you whether to Continue Execution or Abort. This prevents deadlocks and endless executions.

- After execution completes, the full test reports are stored in derby or external database.

Once the execution completes, the shared resources are displayed in iTest Project Explorer and the Velocity Execution Explorer displays blank. Select the test case from the Test Reports tab to view details.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/debug_velocity_driver_and_executions_2.1.jpg) <!-- image_chunk: img_93f7efaba8644878 -->

![screenshot](topics/images/agent_res_page_in_itest_vel_exec.png) <!-- image_chunk: img_10ae3fae78ab354c -->

![screenshot](topics/images/agent_sharing_res_report.png) <!-- image_chunk: img_b250a6986a3910fc -->
