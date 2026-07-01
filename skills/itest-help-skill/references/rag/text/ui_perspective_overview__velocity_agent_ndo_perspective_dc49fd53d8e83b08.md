---
{
  "chunk_id": "ui_perspective_overview__velocity_agent_ndo_perspective_dc49fd53d8e83b08",
  "source_file": "topics/ui_perspective_overview.htm",
  "source_original_path": "topics/ui_perspective_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "Overviews of the default iTest perspectives"
  ],
  "heading_path": [
    "Overviews of the default iTest perspectives",
    "Overviews of the default iTest perspectives",
    "Velocity Agent/NDO Perspective"
  ],
  "anchor": "1697086",
  "context_ids": [
    "ui_perspective_overview"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "debug_configure_itest_gui_as_an_agent.htm#1447523",
    "itest_as_ndo_configure_gui_as_an_ndo_agent.htm#1447523",
    "ui_perspective_concept.htm#1703576"
  ],
  "images": [],
  "content_hash": "dc49fd53d8e83b08",
  "level": 2
}
---

# Overviews of the default iTest perspectives > Overviews of the default iTest perspectives > Velocity Agent/NDO Perspective

When iTest is running in an Agent mode (Velocity Agent or Network DevOps Agent mode), if iTest encounters a breakpoint in the first step, it switches to the Velocity Agent/NDO perspective to facilitate single-stepping and other debugging tasks.

During execution, the Agent perspective either opens automatically or not depending on the Breakpoint at first step setting.

- When enabled, execution automatically pauses at the first line of a test case and the Velocity Agent/NDO Perspective always open automatically.

- When disabled, execution does not pause, and the Velocity Agent/NDO Perspective does not open automatically or come to the foreground.

See Configure Velocity Agent Mode and Configure NDO Agent Mode for details.

> **Note:** Note The iTest toolbar provides an easy way to toggle running iTest as either a Velocity Agent or an NDO Agent when iTest is connected to Velocity. See Velocity Agent/NDO Execution Mode Toggle.

The Agent perspective includes these views:

- The Test Report view:

- The Test Report view is brought to the foreground (made active) after execution or debugging completes, enabling users to easily select and open a report if required.

- When the Velocity Agent or NDO Agent execution completes:

- The Test Report view is brought to the foreground. If it was closed, it is reopened.

- The Execution Report is not opened.

- All session windows opened during execution are closed.

- The Velocity Execution Explorer view located in the lower right-hand corner, shows the execution to indicate that iTest is running in Agent Mode.

- The Response view, located in the lower right-hand corner, displays the command and response for the currently selected captured item or test case step.

- The Threads view located in the lower right-hand corner, enables you to monitor detailed execution progress.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
