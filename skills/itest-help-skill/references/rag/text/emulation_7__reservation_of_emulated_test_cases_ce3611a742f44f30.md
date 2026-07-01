---
{
  "chunk_id": "emulation_7__reservation_of_emulated_test_cases_ce3611a742f44f30",
  "source_file": "topics/emulation.7.htm",
  "source_original_path": "topics/emulation.7.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Reservation of emulated test cases"
  ],
  "heading_path": [
    "Reservation of emulated test cases",
    "Reservation of emulated test cases"
  ],
  "anchor": "1297061",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences_emulation.htm#1297129"
  ],
  "images": [
    "topics/images/vtb_emulate-selected-evalsteps.png",
    "topics/images/vtb_emulate_notselected-evalsteps.png"
  ],
  "content_hash": "ce3611a742f44f30",
  "level": 1
}
---

# Reservation of emulated test cases > Reservation of emulated test cases

The following applies during reservation of emulated test case depending on the emulation preferences settings (see Setting preferences for emulation).

- When Do not require reservation for testcases with topology is enabled in a test case (page 685):

- The eval step with "tbml" command will use a local topology for test execution (even without a reservation).

- The "eval" step with "velocity" command will display an execution error if a reservation does not exist.

- When Do not require reservation for testcases with topology is not enabled in a test case (page 685):

- The "eval" step with "tbml" command does not use the local topology for test execution will display an execution error if a reservation does not exist.

- The "eval" step with "velocity" command will display an execution error if a reservation does not exist.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/vtb_emulate-selected-evalsteps.png) <!-- image_chunk: img_40eeb8f9e02e6c97 -->

![screenshot](topics/images/vtb_emulate_notselected-evalsteps.png) <!-- image_chunk: img_ba78d2222ba48f9c -->
