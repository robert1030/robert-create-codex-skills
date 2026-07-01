---
{
  "chunk_id": "sb_verify_cs_type__generating_a_test_case_from_capture_view_11bc1ba40f3f19d1",
  "source_file": "topics/sb_verify_cs_type.htm",
  "source_original_path": "topics/sb_verify_cs_type.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "Verify the customized session type"
  ],
  "heading_path": [
    "Verify the customized session type",
    "Verify the customized session type",
    "Generating a test case from capture view"
  ],
  "anchor": "1348287",
  "context_ids": [
    "sb_verify_cs_type"
  ],
  "index_keywords": [
    "verify custom session type"
  ],
  "index_keyword_paths": [
    "session builder > verify custom session type"
  ],
  "related_links": [],
  "images": [
    "topics/images/05-b-generate-tc-from-capture-view.png",
    "topics/images/05-c-view-generated-tc-from-capture-view.png",
    "topics/images/session_builder_2.3.jpg"
  ],
  "content_hash": "11bc1ba40f3f19d1",
  "level": 2
}
---

# Verify the customized session type > Verify the customized session type > Generating a test case from capture view

The commands executed in the previous step are captured and display in the Capture View. Select the session, right-click, and add to a test case.

The selected session gets rendered into a new test case. Open the test case and view the step to see the custom value captured and displayed.

> **Note:** Note In custom sessions, the input argument value in Step properties mirror the Steps Description column.

You may replay the test case and view results. Notice that the custom session hides the implementation associated with the native session, and outputs a customized response instead of, for example, the original REST response in case of OpenStack Neutron sessions.

![screenshot](topics/images/05-b-generate-tc-from-capture-view.png) <!-- image_chunk: img_b4a2ecd50cb34113 -->

![screenshot](topics/images/05-c-view-generated-tc-from-capture-view.png) <!-- image_chunk: img_465e8ba0af4c16e2 -->

![screenshot](topics/images/session_builder_2.3.jpg) <!-- image_chunk: img_23e41cc28d6d59b8 -->
