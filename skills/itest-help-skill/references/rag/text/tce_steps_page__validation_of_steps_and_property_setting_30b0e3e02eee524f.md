---
{
  "chunk_id": "tce_steps_page__validation_of_steps_and_property_setting_30b0e3e02eee524f",
  "source_file": "topics/tce_steps_page.htm",
  "source_original_path": "topics/tce_steps_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Test Case editor: Steps page"
  ],
  "heading_path": [
    "Test Case editor: Steps page",
    "Test Case editor: Steps page",
    "Validation of steps and property settings"
  ],
  "anchor": "1823591",
  "context_ids": [
    "tce_steps_page"
  ],
  "index_keywords": [
    "Python Action syntax, warnings",
    "Steps page",
    "Test Case editor",
    "editing"
  ],
  "index_keyword_paths": [
    "Python Action syntax, warnings",
    "Steps page",
    "Steps page > Test Case editor",
    "Test Case editor > Steps page",
    "step properties > editing",
    "steps > editing"
  ],
  "related_links": [
    "tce_preferences_tce.htm#1452307"
  ],
  "images": [
    "topics/images/test_case_editor_2.09.jpg",
    "topics/images/tce_python_step_warning_message.png"
  ],
  "content_hash": "30b0e3e02eee524f",
  "level": 2
}
---

# Test Case editor: Steps page > Test Case editor: Steps page > Validation of steps and property settings

By default, iTest auto-validates property values as you set them. Validation determines whether there is a problem with a step and whether any property settings are invalid or non-default.

- In the Test Case editor, the validation process marks a step with an icon in the first column:

For Python test cases, step Action with syntax errors display a warning when creating tests. This is to help you address the errors right away instead of finding them at runtime.

- Warning icon appears in TestCase Editor for steps with invalid syntax.

- Hover over the warning icon to display a warning message.

- The warning message also appears in the Problems view.

- In the Session Profile editor, the validation process marks a problematic property value with an error marker and identifies a non-default property setting by changing the property value field from blue (default) to white (non-default).

You have the option to configure iTest to not perform validation — steps are not auto-validated and no markers appear for invalid or non-default property settings.

- If auto-validation is disabled, you can perform validation on‑demand in the Test Case editor — click Validate

- You cannot perform on‑demand validation in the Session Profile editor.

You control the option using the Perform step validation only when requested property on the Spirent > Editors > Test Case Editor preferences page. See Properties in: Spirent > Editors > Test Case Editor.

![screenshot](topics/images/test_case_editor_2.09.jpg) <!-- image_chunk: img_126d1557bb86298d -->

![screenshot](topics/images/tce_python_step_warning_message.png) <!-- image_chunk: img_6aa1e85914585d33 -->
