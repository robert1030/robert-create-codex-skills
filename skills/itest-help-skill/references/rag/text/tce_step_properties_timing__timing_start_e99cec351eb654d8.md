---
{
  "chunk_id": "tce_step_properties_timing__timing_start_e99cec351eb654d8",
  "source_file": "topics/tce_step_properties_timing.htm",
  "source_original_path": "topics/tce_step_properties_timing.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Step Properties section: Timing properties group"
  ],
  "heading_path": [
    "Step Properties section: Timing properties group",
    "Step Properties section: Timing properties group",
    "Timing > Start"
  ],
  "anchor": "1716083",
  "context_ids": [
    "tce_step_properties_timing"
  ],
  "index_keywords": [
    "specifying",
    "specifying step",
    "steps"
  ],
  "index_keyword_paths": [
    "Timing properties > steps",
    "step timing > specifying",
    "timing > specifying step"
  ],
  "related_links": [],
  "images": [
    "topics/images/test_case_editor_2.2.jpg"
  ],
  "content_hash": "e99cec351eb654d8",
  "level": 2
}
---

# Step Properties section: Timing properties group > Step Properties section: Timing properties group > Timing > Start

Adjust the properties on this page to change when a step begins relative to the beginning of the previous step.

Normal and Fast set the “scale” on the speed control in the Replay view. “Original” in that control is defined by the Normal property. The “Fast” value on the speed control is set by the Fast property. “Slow” is 10 times the Normal property.

Remember that all of these offsets are minimum delays for starting the selected step after the beginning of the previous step. Unless the previous step is set to run asynchronously iTest always waits until the end of that step before beginning the next step. If the preceding step takes longer than the delays set here then the step will execute immediately upon completion of the previous step.

If you set Normal to 10 seconds and then select Original as the execution speed, then the step will start 10 seconds after the previous step starts even if that step takes one second to execute.

You can set Fast to be less than Normal. If you set Fast to 0 seconds and then select Fast as the execution speed, then the step will start as soon as the previous step ends.

- During execution, change the execution speed at any time.

- Specify the default speed for any test case step in the Timing > Start properties group.

> **Note:** Note Certain steps require a minimum time to execute. For example, if you send four ping packets to a server, then the ping command is not complete until all four packets have been sent. In such a case set the Fast property for that step to allow the command enough time to execute properly even on the fastest replay speed.

![screenshot](topics/images/test_case_editor_2.2.jpg) <!-- image_chunk: img_4398e16c7eb73893 -->
