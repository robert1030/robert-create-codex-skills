---
{
  "chunk_id": "tce_preferences_tce__properties_in_spirent_editors_test_case__33ea8c2c0cecc48f",
  "source_file": "topics/tce_preferences_tce.htm",
  "source_original_path": "topics/tce_preferences_tce.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Quality Center page on the Test Case Editor",
    "Setting preferences for the Test Case Editor"
  ],
  "heading_path": [
    "Setting preferences for the Test Case Editor",
    "Setting preferences for the Test Case Editor",
    "Properties in: Spirent > Editors > Test Case Editor"
  ],
  "anchor": "1452307",
  "context_ids": [
    "tce_preferences_tce"
  ],
  "index_keywords": [
    "Test Case editor",
    "preference settings",
    "test case preferences"
  ],
  "index_keyword_paths": [
    "Test Case editor > preference settings",
    "editors > test case preferences",
    "preference settings > Test Case editor"
  ],
  "related_links": [
    "procedures_call_proc_add_args.htm#1342624"
  ],
  "images": [
    "topics/images/test_case_editor_8.1.jpg"
  ],
  "content_hash": "33ea8c2c0cecc48f",
  "level": 2
}
---

# Setting preferences for the Test Case Editor > Setting preferences for the Test Case Editor > Properties in: Spirent > Editors > Test Case Editor

| Ask for confirmation when starting capture to test case | starts direct-to-test case capture. Check the box to request confirmation to start the direct-to-test process. Default: checked |
| --- | --- |
| Display a warning when the user renames the main (entry point) procedure | If you rename the entry point to a test case (typically, the entry point procedure is named main), the test case will not start. This is not an issue if the file is a library of procedures that are meant to be called from test cases. (See Creating a procedure ‘call’ step using in-line editing) Check the box to warn users when they rename the entry point. Experienced users that are creating procedure libraries will uncheck the box. Default: checked |
| Display Step IDs | Check the box to include a column titled Step IDs in reports. Default: checked |
| Perform step validation only when requested | By default, iTest auto-validates steps as you create them. Validation determines whether there is a a problem with a step and whether any property settings are non-default. Check the box to cause iTest to validate test case steps only when you click Validate in the toolbar. Default: unchecked |

![unknown](topics/images/test_case_editor_8.1.jpg) <!-- image_chunk: img_45a712a0a966a5bb -->
