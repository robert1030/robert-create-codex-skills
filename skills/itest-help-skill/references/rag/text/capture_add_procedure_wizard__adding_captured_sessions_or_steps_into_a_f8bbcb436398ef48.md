---
{
  "chunk_id": "capture_add_procedure_wizard__adding_captured_sessions_or_steps_into_a_f8bbcb436398ef48",
  "source_file": "topics/capture_add_procedure_wizard.htm",
  "source_original_path": "topics/capture_add_procedure_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Adding captured steps into a test case or Python Script"
  ],
  "heading_path": [
    "Adding captured steps into a test case or Python Script",
    "Adding captured steps into a test case or Python Script",
    "Adding captured sessions or steps into a procedure in a iTest Test Case"
  ],
  "anchor": "1322541",
  "context_ids": [
    "capture_add_procedure_wizard"
  ],
  "index_keywords": [
    "Add Procedure wizard",
    "adding",
    "procedures",
    "saving as procedures"
  ],
  "index_keyword_paths": [
    "Add Procedure wizard",
    "adding > procedures",
    "captured items > saving as procedures",
    "captured sessions > saving as procedures",
    "creating > procedures",
    "procedures > adding"
  ],
  "related_links": [
    "quickcalls_overview.htm#"
  ],
  "images": [],
  "content_hash": "f8bbcb436398ef48",
  "level": 2
}
---

# Adding captured steps into a test case or Python Script > Adding captured steps into a test case or Python Script > Adding captured sessions or steps into a procedure in a iTest Test Case

1. In the Capture view, select one or more captured items (use Ctrl-click and Shift-click to select multiple items).

Important If you select items from more than one session, then you must include an open step for each session

1. 2

1. Click Add to iTest Test Case . (Alternatively, right-click the selection and select Add to Test Case.) The Add to Test Case wizard opens.

1. 3

1. On the Test Case page, you have the option to create a new test case and add the procedure to it or to add the procedure to an existing test case. In either case, iTest suggests a project, folder, and test case file name into which to add the procedure. In the File name field, type or browse to the path and name for the test case.

| Create a new test case using the captured items | When you finish with the wizard, iTest creates a new test case, opens it in the Test Case editor, and then adds the procedure steps to the test case. You can then edit and save the test case as needed. If you use a test case template, then, on the next wizard page, you will specify the procedure to add the steps to. The steps are added after any existing steps in the specified procedure. |
| --- | --- |
| Add captured items to an existing test case | When you finish with the wizard, the Test Case editor opens to the specified test case and then iTest adds the procedure after the last test case step. The Test Case editor remains open. |

1. 4

1. On the Procedure page, specify the following values.

> **Tip:** Tip If you have used the wizard before and you feel confident that the wizard will take appropriate actions, then you can click Finish at any time.

1. 5

1. The Procedure page appears only if you chose to add a procedure to an existing test case. On the Procedure page, specify the following values. You will define the procedure more fully in the Test Case editor. Click Next.

| Name | Type the name of the procedure. This is the name that test case developers will use to call the procedure. Alternatively, if you use a test case template, then, from the list, select the procedure to add the steps to. For example, GetPortSettings. |
| --- | --- |
| Headline | Optional. Type a single line of text that describes the procedure. This string will appear with the procedure name in the drop-down list of procedures in the Description cell for call steps or CallProcedure actions. This text also appears in the Headline column of the Favorites view to help you when selecting a procedure. |

1. 6

1. On the Generate QuickCall wizard, specify the following values.

| Generate QuickCall in the associated QuickCall Library | Select to generate the QuickCall into the associated QuickCall library of the referenced session profile. Not selecting or clearing your selection prevents the QuickCall from being generated and the rest of the options wills not be available for input or selection. |
| --- | --- |
| Procedure Name | Type the name of the procedure. This is the name that test case developers will use to call procedure/QuickCall. |
| Procedure Description | Optional. Type a single line of text that describes the procedure. This string will appear with the procedure name in the drop-down list of procedures in the Quickcall. |
| Delete the open and close steps | Select to delete all the open and close steps during the generation process, and substitute the session ids with $session. If you do not select the option, then the session Ids are not replaced. |
| Create Quickcall Library if it does not exist | Note The Create Quickcall Library if it does not exist option is enabled only when there is no QuickCall library associated with the referenced session profile. Enabled when Generate QuickCall in the associated QuickCall Library is selected. When the option is enabled and selected, the wizard does the following: creates a QuickCall library in the default library and QuickCall library associated with the referenced session profile Add the captured steps to the QuickCall library. For example: project://my_project/libraries/Command_prompt_quickCall_library.fftc. Click Browse, navigate to the required target location, select location and click OK. Click Finish and iTest generates the QuickCall procedure in the specified library. Note An error message displays if the library extension.fftc is not specified. |
| Note | The Create Quickcall Library if it does not exist option is enabled only when there is no QuickCall library associated with the referenced session profile. |
|  | creates a QuickCall library in the default library and QuickCall library associated with the referenced session profile |
|  | Add the captured steps to the QuickCall library. For example: project://my_project/libraries/Command_prompt_quickCall_library.fftc. |
| Note | An error message displays if the library extension.fftc is not specified. |

See also “QuickCalls: Defining and using a library of custom actions”

1. 7

1. On the Finish page, click Finish. The Test Case editor opens, displaying the procedure at the end of the test case. Edit as needed and then save the test case.

> **Tip:** Tip If you are confident in your selections at any point while using the wizard, you can click Finish to add the procedure.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
