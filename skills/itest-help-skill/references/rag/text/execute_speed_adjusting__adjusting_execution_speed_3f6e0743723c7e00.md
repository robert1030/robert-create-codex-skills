---
{
  "chunk_id": "execute_speed_adjusting__adjusting_execution_speed_3f6e0743723c7e00",
  "source_file": "topics/execute_speed_adjusting.htm",
  "source_original_path": "topics/execute_speed_adjusting.htm",
  "toc_path": [
    "iTest Online Help",
    "Debugging Test Cases",
    "Adjusting execution speed"
  ],
  "heading_path": [
    "Adjusting execution speed",
    "Adjusting execution speed"
  ],
  "anchor": "1119799",
  "context_ids": [
    "execute_speed_adjusting"
  ],
  "index_keywords": [
    "adjusting execution speed",
    "adjusting speed"
  ],
  "index_keyword_paths": [
    "execution > adjusting speed",
    "speed > adjusting execution speed"
  ],
  "related_links": [],
  "images": [
    "topics/images/debugging_tests_5.1.jpg"
  ],
  "content_hash": "3f6e0743723c7e00",
  "level": 1
}
---

# Adjusting execution speed > Adjusting execution speed

You can change execution speed during execution using the Speed control in the Execution view.

- During execution, change the execution speed at any time.

- Specify the default speed for any test case step in the Timing > Start properties group.

Fast: Submit commands as quickly as the computer can send them while allowing each step run to completion before starting the next step. Asynchronous (concurrent) steps, in contrast, are executed at original speed.

Original: Execute no faster than the original capture. Execution may be slightly slower because each step will start no sooner than the original delay from the previous step end, but may be later because it will wait for the previous step to complete before starting.

Slow: Use this setting to give you a chance to observe behavior that you might miss at a higher execution speed.

![screenshot](topics/images/debugging_tests_5.1.jpg) <!-- image_chunk: img_90e6cb40b176add4 -->
