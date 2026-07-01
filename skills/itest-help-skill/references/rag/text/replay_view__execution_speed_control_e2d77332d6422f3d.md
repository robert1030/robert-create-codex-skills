---
{
  "chunk_id": "replay_view__execution_speed_control_e2d77332d6422f3d",
  "source_file": "topics/replay_view.htm",
  "source_original_path": "topics/replay_view.htm",
  "toc_path": [
    "iTest Online Help",
    "Executing Tests",
    "Execution view"
  ],
  "heading_path": [
    "Execution view",
    "Execution view",
    "Execution speed control"
  ],
  "anchor": "1245682",
  "context_ids": [
    "replay_view"
  ],
  "index_keywords": [
    "Execution view",
    "find issues in",
    "issues in test reports"
  ],
  "index_keyword_paths": [
    "Execution view",
    "find > issues in test reports",
    "issues > finding in test reports test reports > find issues in",
    "views > Execution view"
  ],
  "related_links": [
    "executing_tests_preferences_execution_view.htm#1155333"
  ],
  "images": [
    "topics/images/executing_tests_2.11.jpg"
  ],
  "content_hash": "e2d77332d6422f3d",
  "level": 2
}
---

# Execution view > Execution view > Execution speed control

By default, the speed control does not appear in the Execution view. To display the control, set the preference setting as described in the Spirent > Execution section of the Preferences page. See Setting preferences for the Execution view.

You can change the execution speed setting during execution to any one of the following settings or any setting in between.

Fast: Submit commands as quickly as the computer can send them while allowing each step run to completion before starting the next step. asynchronous (concurrent) steps, in contrast, are executed at original speed.

- Original: Execute no faster than the original capture. Execution may be slightly slower because each step will start no sooner than the original delay from the previous step end, but may be later because it will wait for the previous step to complete before starting.

- Slow: Use this setting to give you a chance to observe behavior that you might miss at a higher speed.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/executing_tests_2.11.jpg) <!-- image_chunk: img_4601e0ea5f36f3b8 -->
