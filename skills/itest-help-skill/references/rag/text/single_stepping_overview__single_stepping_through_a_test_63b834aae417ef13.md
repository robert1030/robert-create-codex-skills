---
{
  "chunk_id": "single_stepping_overview__single_stepping_through_a_test_63b834aae417ef13",
  "source_file": "topics/single_stepping_overview.htm",
  "source_original_path": "topics/single_stepping_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Debugging Test Cases",
    "Single-stepping through a test"
  ],
  "heading_path": [
    "Single-stepping through a test",
    "Single-stepping through a test"
  ],
  "anchor": "1192549",
  "context_ids": [
    "single_stepping_overview"
  ],
  "index_keywords": [
    "single-stepping"
  ],
  "index_keyword_paths": [
    "single-stepping"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "63b834aae417ef13",
  "level": 1
}
---

# Single-stepping through a test > Single-stepping through a test

Single-stepping is a very convenient way to closely monitor the operation of a test case. Using step-into or step-over in the main toolbar will ask iTest to execute one more step and then stop again. (Executing one step can take a long time in some cases but execution will stop when the next step is complete.)

If multiple threads are running, you will be single-stepping in just one of the threads. When you start executing (even by single-stepping), all threads will start running again, and then execution will pause after the next step in the foreground thread is reached. But at that point, iTest will ask all other threads to pause after they complete the current step, and you will get control back again after all threads indicate that they have paused. If you would like to single-step through a different thread, you can select a different thread in the Threads view to make it the foreground thread for single-stepping.

Step-into is used to move to execute the next step. If the current step is a call step, then execution will stop after the first step in the called procedure. Step-over is identical except when the step is a call step, then execution will stop after the called procedure has completed execution and returned.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
