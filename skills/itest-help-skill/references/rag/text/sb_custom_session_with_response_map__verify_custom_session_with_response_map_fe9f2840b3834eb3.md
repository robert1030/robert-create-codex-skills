---
{
  "chunk_id": "sb_custom_session_with_response_map__verify_custom_session_with_response_map_fe9f2840b3834eb3",
  "source_file": "topics/sb_custom_session_with_response_map.htm",
  "source_original_path": "topics/sb_custom_session_with_response_map.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "Verify Custom Session with response map"
  ],
  "heading_path": [
    "Verify Custom Session with response map",
    "Verify Custom Session with response map"
  ],
  "anchor": "1440419",
  "context_ids": [
    "sb_custom_session_with_response_map"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "sb_creating_a_cs_type.htm#1362263",
    "#1441898",
    "tce_step_properties_other_postprocessing.htm#1716159",
    "test_case_editor_overview.htm#"
  ],
  "images": [
    "topics/images/respMap_QC_Procedure.png",
    "topics/images/resMap_QC_in_TC-Before_export.png",
    "topics/images/session_builder_3.3.jpg"
  ],
  "content_hash": "fe9f2840b3834eb3",
  "level": 1
}
---

# Verify Custom Session with response map > Verify Custom Session with response map

iTest exports any procedure-level response map defined in your QuickCall to a custom session. This allows furnishing the custom session with valuable queries and structures that returns output data with response mapped queries and structures.

The following illustrates an example QuickCall with procedure level response map that was exported as a custom session, a test case that uses the created custom session, and the response map applied to the output of the custom step.

Step 1

Example QuickCall with procedure-level response map

The response map file specified on the Procedure Properties> General page of a QuickCall.

Export QuickCall and create custom session as described in Creating a custom session type.

Example QuickCall (not Custom Session) used in a Testcase

The example below shows the QuickCall used in a test case step and the response map applied to the test case step after test execution.

Example Custom Session (exported QuickCall with response map) in a Test Case

The example below shows the Custom Session (with exported QuickCall with response map) used in a test case step and the response map applied to the test case step after test execution.

The same blue boxes that appear in the response window of a QuickCall step (Example QuickCall (not Custom Session) used in a Testcase), also appears in the response window of a custom session step (above). iTest ensures that all response map Pattern, Block, and Table maps are applied to the custom session step responses (as configured at the QuickCall procedure level).

In addition to the response map file configured at the custom session level (exported QuickCall procedure level), iTest allows you to define custom response map file.

When a step has no response map defined, toggle Use an auto-generated response map if no other map is available. Unselect the option to display a blank Queries view or select option to display an auto-generated response map.

See Expected Response (“Test Case Editor”).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/respMap_QC_Procedure.png) <!-- image_chunk: img_45fe7440ebca6a25 -->

![screenshot](topics/images/resMap_QC_in_TC-Before_export.png) <!-- image_chunk: img_411ee57906ff9ee8 -->

![screenshot](topics/images/session_builder_3.3.jpg) <!-- image_chunk: img_01d06803ad427b23 -->
