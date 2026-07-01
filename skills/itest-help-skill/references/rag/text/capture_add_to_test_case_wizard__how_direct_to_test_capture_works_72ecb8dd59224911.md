---
{
  "chunk_id": "capture_add_to_test_case_wizard__how_direct_to_test_capture_works_72ecb8dd59224911",
  "source_file": "topics/capture_add_to_test_case_wizard.htm",
  "source_original_path": "topics/capture_add_to_test_case_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard"
  ],
  "heading_path": [
    "Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard",
    "Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard",
    "How direct-to-test capture works"
  ],
  "anchor": "1322154",
  "context_ids": [
    "capture_add_to_test_case_wizard"
  ],
  "index_keywords": [
    "Add to Test Case wizard",
    "captured steps into test cases",
    "inserting captured into test cases"
  ],
  "index_keyword_paths": [
    "Add to Test Case wizard",
    "inserting > captured steps into test cases",
    "steps > inserting captured into test cases"
  ],
  "related_links": [],
  "images": [
    "topics/images/capture_tasks.3.jpg",
    "topics/images/capture_tasks.4.jpg",
    "topics/images/capture_tasks.5.jpg",
    "topics/images/capture_tasks.6.jpg"
  ],
  "content_hash": "72ecb8dd59224911",
  "level": 2
}
---

# Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard > Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard > How direct-to-test capture works

- If you start direct-to-test capture while a session is open, then the wizard uses Step mode. As a result, only steps in that session are added to the test case. Actions in other sessions are not direct captured (iTest will remind you whenever you perform an action in another session). For this reason, if you want to direct-capture multiple sessions, then close all sessions, click , and then start the manual sessions.

- If you first select a step, click , and then start a new manual session, then, when you click , the entire manual session is added after the selected step as a new procedure.

- If you select a step that is not associated with a session before you start direct-to-test capture, then the wizard uses Session mode. As a result, all steps in the interactive session are added to the test case, even if you performed only a few steps after clicking .

- Comments and markers in manual sessions are saved as comment steps. (During interactive sessions, you add comments using the Capture Comments view and you add markers using Insert Marker in the Capture view.)

For devices with more than one session attached or for multiple captures that use the same session profile: To create the Session IDs that appear in the Session cells in the Test Case editor and in test reports, Spirent iTest uses the combination of Session name from the session profile (for example, myDUT) and a unique session number for the day. (for example, myDUT.1 and myDUT.2). If the session profile does not specify a Session name, then Spirent iTest uses the filename of the session profile in its place.

![unknown](topics/images/capture_tasks.3.jpg) <!-- image_chunk: img_ce4dc4a707f90a2a -->

![unknown](topics/images/capture_tasks.4.jpg) <!-- image_chunk: img_678bb984e7725cd2 -->

![unknown](topics/images/capture_tasks.5.jpg) <!-- image_chunk: img_defbdf22c7fbbc26 -->

![unknown](topics/images/capture_tasks.6.jpg) <!-- image_chunk: img_698f43bc6a5c6206 -->
