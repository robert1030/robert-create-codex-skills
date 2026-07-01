---
{
  "chunk_id": "capture_add_to_test_case_wizard__using_direct_to_test_capture_9e31251010288185",
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
    "Using direct-to-test capture"
  ],
  "anchor": "1322175",
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
    "topics/images/capture_tasks.8.jpg",
    "topics/images/capture_tasks.9.jpg"
  ],
  "content_hash": "9e31251010288185",
  "level": 2
}
---

# Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard > Saving interactive steps as steps in a test case: The ‘Add to iTest Test Case’ wizard > Using direct-to-test capture

1. Optional. In the Test Case editor, select a step. The new steps are added after the selected step.

If you do not select a step, then the captured steps are added either to a new test case or to the end of an existing test case.

1. 2

1. Click .

1. 3

1. Start sessions and perform the steps that you want to add to the test case.

1. 4

1. Click .

1. 5

1. The Add to iTest Test Case wizard starts.

1. 6

1. On the Test Case page, you have the option to create a new test case and add the procedure to it or to add the procedure to an existing test case. In either case, iTest suggests a project, folder, and test case file name into which to add the new steps. In the File name field, type or browse to the path and name for the test case.

| Create a new test case using the captured items | When you finish with the wizard, iTest creates a new test case, opens it in the Test Case editor, and then adds the procedure steps to the test case. You can then edit and save the test case as needed. If you use a test case template, then, on the next wizard page, you will specify the procedure to add the steps to. The steps are added after any existing steps in the specified procedure. |
| --- | --- |
| Add captured items to an existing test case | When you finish with the wizard, the Test Case editor opens to the specified test case and then iTest adds the procedure after the last test case step. The Test Case editor remains open. |

1. 7

1. On the Insert page, specify whether to add the new steps as a procedure or as individual steps after the steps that you had selected in the test case before starting direct-to-test capture.

> **Tip:** Tip If you have used the wizard before and you feel confident that the wizard will take appropriate actions, then you can click Finish at any time.

1. 8

1. The Procedure page appears only if you chose to add a procedure to an existing test case. On the Procedure page, specify the following values and then click Next.

| Name | Type the name of the procedure. This is the name that test case developers will use to call the procedure. Alternatively, if you use a test case template, then, from the list, select the procedure to add the steps to. For example, GetPortSettings. |
| --- | --- |
| Headline | Optional. Type a single line of text that describes the procedure. This string will appear with the procedure name in the drop-down list of procedures in the Description cell for call steps or CallProcedure actions. This text also appears in the Headline column of the Favorites view to help you when selecting a procedure. |

1. 9

1. On the Finish page, if you are confident in your selections, click Finish. The steps are added to the specified test case. Move the procedure or steps and edit as needed and then save the test case.

> **Tip:** Tip If you are confident in your selections at any point while using the wizard, you can click Finish to add the steps.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/capture_tasks.8.jpg) <!-- image_chunk: img_b6731b1bda6d78d6 -->

![unknown](topics/images/capture_tasks.9.jpg) <!-- image_chunk: img_5733591c207425be -->
