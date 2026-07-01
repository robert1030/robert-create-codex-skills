---
{
  "chunk_id": "test_case_editor_steps_page__test_case_editor_toolbar_41b8fc583ce27ba3",
  "source_file": "topics/test_case_editor_steps_page.htm",
  "source_original_path": "topics/test_case_editor_steps_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Overview",
    "Working with steps on the Steps page"
  ],
  "heading_path": [
    "Working with steps on the Steps page",
    "Working with steps on the Steps page",
    "Test Case editor toolbar"
  ],
  "anchor": "1284656",
  "context_ids": [
    "test_case_editor_steps_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tce_preferences_tce.htm#1452307",
    "procedure_call_wizard.htm#1291944",
    "quickcalls_new_quickcall_library_wizard.htm#1292200",
    "quickcalls_overview.htm#",
    "test_case_editor_step_concept.htm#1284488",
    "test_report_editor.htm#1174232"
  ],
  "images": [
    "topics/images/test_case_editor.04.jpg",
    "topics/images/test_case_editor.05.jpg",
    "topics/images/test_case_editor.07.jpg",
    "topics/images/test_case_editor.08.jpg",
    "topics/images/test_case_editor.09.jpg",
    "topics/images/test_case_editor.13.jpg",
    "topics/images/test_case_editor.14.jpg",
    "topics/images/test_case_editor.15.jpg",
    "topics/images/test_case_editor.20.jpg",
    "topics/images/test_case_editor.21.jpg"
  ],
  "content_hash": "41b8fc583ce27ba3",
  "level": 2
}
---

# Working with steps on the Steps page > Working with steps on the Steps page > Test Case editor toolbar

|  | Validate | This button appears only if you configure manual validation of steps. Click the button to validate all steps. When there is a non-default property setting or a problem with a step, the validation process adds a marker in the first column. By default, iTest auto-validates steps as you create them and the button does not appear. To configure iTest to perform validation only when you request it, see Properties in: Spirent > Editors > Test Case Editor. |
| --- | --- | --- |
|  | Test Plan | Save the test case procedures and steps as test plan (text file) to a desired location. |
|  | Insert | Click the down-arrow to Insert Procedure, Steps, Analysis Rule, Analysis Rule Action, and JSON Steps |
| Insert Procedure | Add a new local procedure immediately following the selected step. |  |
| Insert Procedure Using Wizard | Use the wizard to configure a call step and add it. See Creating a ‘call’ step using the Procedure Call wizard |  |
| Insert Step | Add a new step immediately following the selected step or procedure. Ctrl-Enter (OPTION-Enter on macOS) also inserts a step. iTest uses the combination of Session name from the session profile and the unique session number for the day (for example, myDUT5) to create the Session ID that appears in the Session cell. Note By default, iTest sends a carriage return + line-feed sequence when the Command cell is blank, so there is no need to include [char \r\n] in the Command cell for blank commands. Note For QuickCalls, iTest sets the session ID (on the Test Case Editor Session cell) as $session (if language=tcl) or [session] (if language=python) (session is the variable name used in QuickCall libraries). See Defining a QuickCall, “QuickCalls: Defining and using a library of custom actions” | Note |
| Note | By default, iTest sends a carriage return + line-feed sequence when the Command cell is blank, so there is no need to include [char \r\n] in the Command cell for blank commands. |  |
| Note | For QuickCalls, iTest sets the session ID (on the Test Case Editor Session cell) as $session (if language=tcl) or [session] (if language=python) (session is the variable name used in QuickCall libraries). See Defining a QuickCall, “QuickCalls: Defining and using a library of custom actions” |  |
| Insert Analysis Rule | Add a new analysis rule immediately following the selected line. iTest adds a default rule with a regex extractor and assert processor, but you can edit the rule as needed. |  |
| Insert Rule Action | Add a new Action line to the immediately following the selected line in a When True or When False entry for an assert processor in an analysis rule. |  |
| Insert JSON Step | Formulate a JSON document from the test case editor (Provides an easy point-and-click way to perform CRUD operations on nodes in a JSON document) Manipulate the JSON response (provides a programmatic way of performing CRUD operations on block response of a procedure). |  |
|  | Move Selected Items Up or Down | Places the selected steps or procedure immediately before/after the preceding step or procedure. Steps cannot be moved from one procedure to another. Steps within looping constructs (if, for, foreach, while) move only within the construct. If multiple steps are selected, they must be consecutive. If a procedure is selected then it will be placed before/after the preceding procedure. |
|  | Steps cannot be moved from one procedure to another. |  |
|  | Steps within looping constructs (if, for, foreach, while) move only within the construct. |  |
|  | If multiple steps are selected, they must be consecutive. |  |
|  | If a procedure is selected then it will be placed before/after the preceding procedure. |  |
|  | Sort Procedures By Name | Re-sequences Procedures in the test case in alphabetical order. Sorts the procedures in the QuickCall libraries and other procedure libraries to help you quickly find the procedure(s) that you are working on in the Test Case Editor. The entry point procedure will be listed as the first procedure. For example, if a Procedure called main is set as the entry point in the test case, it is always listed as the first procedure, then all other procedures are sorted in alpha-numeric order. The Sort Procedures By Name option is not available if the test case has only one procedure or no procedure. Note Only the order of the procedures will be changed and the no other content is changed. After sorting the procedures, click Edit >Undo Sort Procedure by Name (on the iTest Menu toolbar) to restore the original order of the Procedures. |
| Note | Only the order of the procedures will be changed and the no other content is changed. |  |
|  | Increase Indent Decrease Indent | iTest uses indentation to represent membership in loops and other constructs. Move the selected steps down/up one level in the step nesting hierarchy. If multiple steps are selected, they must be consecutive. |
|  | Delete Selected Items | Remove the selected steps or procedure from the test case. Use Ctrl-click (OPTION-Ctrl-Click on macOS) and Shift-click (OPTION-Shift-Click on macOS) to select multiple items Deleting a for, if, or while construct deletes all steps in the construct Deleting a procedure deletes all steps in the procedure. Tip: Ctrl-Delete (OPTION-Delete on macOS) also deletes the selected items. |
|  | Use Ctrl-click (OPTION-Ctrl-Click on macOS) and Shift-click (OPTION-Shift-Click on macOS) to select multiple items |  |
|  | Deleting a for, if, or while construct deletes all steps in the construct |  |
|  | Deleting a procedure deletes all steps in the procedure. |  |
|  | Analysis Rule Wizard | Start the Analysis Rule wizard (You must first select the step to apply the rule to.) |
|  | Skip / Unskip | Toggle the skip status of the selected steps, procedures, or analysis rules. (Use Ctrl+click or Shift+click for multi-select.) Skipped steps are marked by being dimmed (grayed -out). In the example, steps 3 and 4 are skipped. Tip: Add a comment step and indent (nest) any number of steps under the comment. You can then skip all of the steps by skipping only the comment step. In addition, you can collapse the comment step to hide the nested steps temporarily. See Tips on working with test case steps. |
|  | Toggle Breakpoint | For the selected steps or procedure, apply or remove a breakpoint. During execution, when iTest encounters a breakpoint, it switches to the Test Case Debugging perspective to facilitate single-stepping and other debugging tasks. Tip: While execution is paused, you can perform interactive actions in the session to view the results. If a step is useful, you might later add it to the test case. All current breakpoints are identified on the Breakpoints view |
|  | Expand | Click to Expand All Steps, Summarize Rules as described here. Click the arrow to select one of the following options: Expand All Steps, Summarize Rules (Default): Expand all executable steps and display the first line of any analysis rules Expand All Steps but Not Rules: Expand all executable steps and collapse all analysis rules Expand All Steps and All Rules: Expand all executable steps and all analysis rules Expand Selected Items One Level: For currently selected items, expand the first item in the next nesting level. If the nested item had previously been expanded, then it appears expanded Expand Selected Items Completely: For currently selected items, expand all levels of nested items |
|  | Collapse | Collapse All: Collapse all executable steps and all analysis rules Collapse All Selected Items: For currently selected items, collapse all levels of nested items |
|  | Open recent test reports | While working on a test case in the Test Case editor, the fastest way to view a test report is to click . This opens the most recent report in the Test Report editor. Click the arrow to display the list of the five most recent reports and then select a report to open it. The Test Report editor is described in Test Report editor. |
|  | Show Properties View | While working on a test case in the Test Case editor, right-click and on the menu displayed, select (Show Properties View). The Properties view appears as a tabbed pane on the iTest window. The Properties View pane display is context-specific and varies depending on where your cursor is positioned. You may edit step properties using either the Step Properties section (within the Test Case Editor) or via the Properties View tab. For example, if your cursor is at the procedure label (Steps > Action> procedure) and then select from the right-click menu, the Properties pane opens to display Procedure Properties (which is also displayed below the Steps > Actions section). Note You may position and resize the tabbed Properties view window as required. |
| Note | You may position and resize the tabbed Properties view window as required. |  |

![inline_icon](topics/images/test_case_editor.04.jpg) <!-- image_chunk: img_2e8d9fc12d93842e -->

![unknown](topics/images/test_case_editor.05.jpg) <!-- image_chunk: img_0f773d43c268cd48 -->

![inline_icon](topics/images/test_case_editor.07.jpg) <!-- image_chunk: img_d76af42b0f0c7074 -->

![unknown](topics/images/test_case_editor.08.jpg) <!-- image_chunk: img_b2b4fcce56782eae -->

![screenshot](topics/images/test_case_editor.09.jpg) <!-- image_chunk: img_bc435d5494ddc117 -->

![inline_icon](topics/images/test_case_editor.13.jpg) <!-- image_chunk: img_271d04b273107bf5 -->

![inline_icon](topics/images/test_case_editor.14.jpg) <!-- image_chunk: img_5bce902c460b2705 -->

![screenshot](topics/images/test_case_editor.15.jpg) <!-- image_chunk: img_0284f8c3e8524c45 -->

![unknown](topics/images/test_case_editor.20.jpg) <!-- image_chunk: img_bf69b347f78414e4 -->

![inline_icon](topics/images/test_case_editor.21.jpg) <!-- image_chunk: img_a26433eec17f6b32 -->
