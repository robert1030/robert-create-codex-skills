---
{
  "chunk_id": "tce_step_properties_open_step__using_parameters_in_open_steps_d8a8d7b68aee1303",
  "source_file": "topics/tce_step_properties_open_step.htm",
  "source_original_path": "topics/tce_step_properties_open_step.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Step Properties section: Session Properties: Overriding device or session profile settings in the open step"
  ],
  "heading_path": [
    "Step Properties section: Session Properties: Overriding device or session profile settings in the open step",
    "Step Properties section: Session Properties: Overriding device or session profile settings in the open step",
    "Using parameters in open steps"
  ],
  "anchor": "1716239",
  "context_ids": [
    "tce_step_properties_open_step"
  ],
  "index_keywords": [
    "Open Step properties",
    "open action",
    "overriding",
    "overriding session profile settings",
    "properties of"
  ],
  "index_keyword_paths": [
    "Step Properties page > Open Step properties",
    "open steps > properties of",
    "overriding session profile settings",
    "properties > open action",
    "session profile property settings > overriding"
  ],
  "related_links": [],
  "images": [
    "topics/images/test_case_editor_3.2.jpg"
  ],
  "content_hash": "d8a8d7b68aee1303",
  "level": 2
}
---

# Step Properties section: Session Properties: Overriding device or session profile settings in the open step > Step Properties section: Session Properties: Overriding device or session profile settings in the open step > Using parameters in open steps

You can use test case parameters to overwrite property settings that you make in the session profile. As a result, the test case can make property settings dynamically set at runtime. For example, let's say you created a session profile named telnet_myDUT.ffsp with an IP address setting of 99.88.77.66.

You then create a test case parameter named ip_address and set its value to 11.22.33.44. In the Test Case editor, use the param command as a field replacement in the open step's IP address property setting:

As a result, at runtime, the open step's IP address setting overwrites the IP address specified in the session profile and the session opens using 11.22.33.44.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/test_case_editor_3.2.jpg) <!-- image_chunk: img_c563182e29248b60 -->
