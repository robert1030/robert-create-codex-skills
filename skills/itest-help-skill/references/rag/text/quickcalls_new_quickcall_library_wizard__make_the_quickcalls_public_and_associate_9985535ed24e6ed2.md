---
{
  "chunk_id": "quickcalls_new_quickcall_library_wizard__make_the_quickcalls_public_and_associate_9985535ed24e6ed2",
  "source_file": "topics/quickcalls_new_quickcall_library_wizard.htm",
  "source_original_path": "topics/quickcalls_new_quickcall_library_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Defining QuickCalls",
    "Defining a QuickCall"
  ],
  "heading_path": [
    "Defining a QuickCall",
    "Defining a QuickCall",
    "Make the QuickCalls “public” and associate them with a topology device or session profile:"
  ],
  "anchor": "1399715",
  "context_ids": [
    "quickcalls_new_quickcall_library_wizard"
  ],
  "index_keywords": [
    "defining",
    "procedures"
  ],
  "index_keyword_paths": [
    "defining > procedures",
    "procedures > defining"
  ],
  "related_links": [
    "capture_add_procedure_wizard.htm#1322541",
    "capture_view.htm#",
    "quickcalls_arguments_in_quickcall_steps.htm#1403617",
    "sb_session_builder_overview.htm#"
  ],
  "images": [
    "topics/images/quickcalls.04.jpg",
    "topics/images/quickcalls.06.jpg",
    "topics/images/quickcalls.09.jpg",
    "topics/images/quickcalls.10.jpg",
    "topics/images/quickcalls.11.jpg",
    "topics/images/proc_includeThis_unchecked.png"
  ],
  "content_hash": "9985535ed24e6ed2",
  "level": 4
}
---

# Defining a QuickCall > Defining a QuickCall > Make the QuickCalls “public” and associate them with a topology device or session profile:

| Include this test case when listing QuickCall libraries | Check the Include this test case check box to make the library “public”, that is, to cause iTest to display the test case name whenever a user asks to see a list of available QuickCall libraries. This settings adds the QuickCall library to the drop-down list when you edit a session profile or device to associate with the library. Default: checked for QuickCall libraries and procedure libraries, unchecked otherwise |
| --- | --- |
| Session profile or device | Specify the topology device or session profile to associate with the QuickCalls that are defined in the library. Once you have specified a device or profile, the link becomes active and opens the item in the appropriate editor. |

Define the QuickCalls that make up the library

Use the following instructions to add as many QuickCalls as needed to the QuickCall library. You define a QuickCall in either of the following ways:

- The easiest way to add a QuickCall is to manually execute the steps that you want to include in the QuickCall and then, using the capture-to-test feature or from the Capture view, save the captured session as a procedure in a test case. The QuickCall is added as a procedure definition after the last step in the test case.

- Drag captured items into the Test Case Editor of a new QuickCall definition or an existing QuickCall).

OR

- Right-click on the selected captured session item, select Add to iTest Test Case and follow the steps in Adding captured sessions or steps into a procedure in a iTest Test Case “Capturing Manual (Interactive) Sessions”.

- Alternatively, while working in the Test Case editor, you can add a QuickCall “manually” by adding a procedure definition and then adding steps to the procedure or copy Test Case steps (not a QuickCall) and paste them into a QuickCall test case.

> **Tip:** Tip While working on QuickCall definitions on the Test Case editor Steps page, click Collapse All to view only the QuickCall names and not the individual steps. You can then work on a single QuickCall definition without the clutter.

> **Caution:** CAUTION Do not use the open action (open a session) in a QuickCall.

1. In the Test Case editor:

- If you added the QuickCall by adding a captured session, then select the procedure step (the step with an Action of “Procedure” that you just added). (Remember that each QuickCall definition is a procedure definition.)

- If you add the QuickCall manually, select a step, click Insert , and then select Insert Procedure. iTest adds a blank procedure definition below the selected step. (Remember that each QuickCall definition is a procedure definition.)

The predefined variable $session (Tcl) or [session] (Python) refers to the session in which the QuickCall is being invoked. (Any session that calls the QuickCall passes its session ID to the quickCall steps using the session variable.)

iTest automatically sets the session ID as $session (if language=tcl) or [session] (if language=python) (session is the variable name used in QuickCall libraries).

> **Note:** Note In QuickCall libraries, $session or [session] is a reserved word.

| While working on a test case in the Test Case editor, right-click and on the menu displayed, select (Show Properties View). The Properties view appears as a tabbed pane on the iTest window. The Properties View pane display is context-specific and varies depending on where your cursor is positioned. You may edit step properties using either the Step Properties section (within the Test Case Editor) or via the Properties View tab. For example, if your cursor is at the procedure label (Steps > Action> procedure) and then select from the right-click menu, the Properties pane opens to display Procedure Properties (which is also displayed below the Steps > Actions section). Note You may position and resize the tabbed Properties view window as required. | Note | You may position and resize the tabbed Properties view window as required. |
| --- | --- | --- |
| Note | You may position and resize the tabbed Properties view window as required. |  |

1. 2

1. In the Procedure Properties tree, click General. On the General page, specify values for the following properties.

> **Note:** Note The text that you provide for the Name, Headline, Author, and Version properties (and for the Description property specified on the Description properties page) are displayed on the popup help for the QuickCall. The popup help appears when the test developer starts to type a QuickCall in the Action cell or types Ctrl+Space while in the Description cell for a QuickCall step.

| Name | Required. Provide a meaningful name for the QuickCall. This string appears: In the Test Case editor In the drop-down list of QuickCalls in the Action cell During an interactive session, in the drop-down list of QuickCalls that appears when the user clicks In the Favorites view, under the associated QuickCall library Note Do not use the name of an existing iTest action (for example, comment or readFile). If you do, then during execution, iTest generates an Execution Issue Warning and then executes the built-in action. |  | In the Test Case editor In the drop-down list of QuickCalls in the Action cell |  | During an interactive session, in the drop-down list of QuickCalls that appears when the user clicks |  | In the Favorites view, under the associated QuickCall library | Note | Do not use the name of an existing iTest action (for example, comment or readFile). If you do, then during execution, iTest generates an Execution Issue Warning and then executes the built-in action. |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | In the Test Case editor In the drop-down list of QuickCalls in the Action cell |  |  |  |  |  |  |  |  |
|  | During an interactive session, in the drop-down list of QuickCalls that appears when the user clicks |  |  |  |  |  |  |  |  |
|  | In the Favorites view, under the associated QuickCall library |  |  |  |  |  |  |  |  |
| Note | Do not use the name of an existing iTest action (for example, comment or readFile). If you do, then during execution, iTest generates an Execution Issue Warning and then executes the built-in action. |  |  |  |  |  |  |  |  |
| Include this procedure when listing callable procedures | Check the box to display the QuickCall's name in: The drop-down list of QuickCalls in the Action cell that appears when a test developer is adding a QuickCall step to a test case. The drop-down list of QuickCalls that appears when the user clicks during a manual session The Favorites view (indented under the QuickCall library) This option makes the QuickCall available for use in any test case in the current workspace. Software developers call this “making a procedure public”. Default: checked for QuickCall libraries and procedure libraries, unchecked otherwise Note When you select Include this procedure when listing callable procedures, an icon () next to the procedure name (Steps > Action > Procedure) indicates that the procedure is callable. When not selected, the default procedure icon () displays without the green dot. |  | The drop-down list of QuickCalls in the Action cell that appears when a test developer is adding a QuickCall step to a test case. |  | The drop-down list of QuickCalls that appears when the user clicks during a manual session |  | The Favorites view (indented under the QuickCall library) | Note | When you select Include this procedure when listing callable procedures, an icon () next to the procedure name (Steps > Action > Procedure) indicates that the procedure is callable. |
|  | The drop-down list of QuickCalls in the Action cell that appears when a test developer is adding a QuickCall step to a test case. |  |  |  |  |  |  |  |  |
|  | The drop-down list of QuickCalls that appears when the user clicks during a manual session |  |  |  |  |  |  |  |  |
|  | The Favorites view (indented under the QuickCall library) |  |  |  |  |  |  |  |  |
| Note | When you select Include this procedure when listing callable procedures, an icon () next to the procedure name (Steps > Action > Procedure) indicates that the procedure is callable. |  |  |  |  |  |  |  |  |
| Headline | Optional. Type a single line of text that describes the QuickCall. This string will appear with the QuickCall name in the drop-down list of procedures in the Action cell for a step . This text also appears in the Headline column of the Favorites view to help you when selecting a QuickCall. |  |  |  |  |  |  |  |  |
| Author | Optional. Type the name of the person who created the QuickCall definition. This helps coworkers who have questions about the QuickCall. |  |  |  |  |  |  |  |  |
| Version | Optional. If you track changes to the QuickCall definition, use this property to specify the version number of the QuickCall. |  |  |  |  |  |  |  |  |
| Response Map | Optional. Specify the response map to apply to the value returned by the QuickCall (via a return step in the QuickCall). |  |  |  |  |  |  |  |  |
| Default session | Optional. Because the Session ID of the steps in a QuickCall definition are typically parameterized so that the Session ID value can be set at runtime, you specify the topology device or session profile URI here. This enables iTest (at design-time, while you are designing the QuickCall) to populate the Action cell with actions that are appropriate for the session type. If you are working in a QuickCall library and the Session ID is specified as $session, then this property defaults to the URI that is specified in the Session profile or device property on the General page of the Test Case editor. |  |  |  |  |  |  |  |  |

1. 3

1. In the Procedure Properties tree, click Description. For the Description property, type the text that should appear in the help popup for the QuickCall. We recommend that you show all forms of the QuickCall (for example, provide examples of all permitted combinations of required and optional arguments). Show each form on a new line.

1. 4

1. QuickCalls can use both named arguments and numbered arguments. Perform this step if the QuickCall uses named arguments. The order of arguments in the list that you create here is the order in which they appear when a test case developer is adding a step that performs a QuickCall action.

For more detail on how QuickCalls use arguments, see About arguments in QuickCall steps.

In the Procedure Properties tree, click Arguments. On the Arguments page, click to add a new argument definition.

Specify values for the following properties for arguments:

| Name | Provide a meaningful, short name. This is the string that test developers use to specify the argument value. |
| --- | --- |
| This argument is required | Check the box to require that the test developer must specify the argument when adding the QuickCall step. In the popup help for the QuickCall, the text “(required)” will appear next to the argument name. (The popup help appears when the test developer types a hyphen “-” while adding arguments.) Default: unchecked |
| Default value | Optional. Provide a single value that the QuickCall will use for the argument if the user does not specify a value for the argument. Note The Procedure argument default values are always type string. When language is Python, variables must be type casted when used as any other type. |
| Note |  |
| Description | Optional. Type one or more lines of text to completely describe the argument. This text will appear in popup help for the QuickCall when the test developer types Ctrl + Space. Note You may define validation rules and properties of commands in the QuickCall argument description as per the syntax shown below. <Procedure argument description> -- <validation rules and properties separate by semicolon> When exporting quickcall library, commands for the new custom session type will be developed as per the validation rules and properties defined.See Chapter , “Session Builder” |
| Note | You may define validation rules and properties of commands in the QuickCall argument description as per the syntax shown below. |

![unknown](topics/images/quickcalls.04.jpg) <!-- image_chunk: img_768417637a48b3ee -->

![screenshot](topics/images/quickcalls.06.jpg) <!-- image_chunk: img_84e13ef081cedd19 -->

![unknown](topics/images/quickcalls.09.jpg) <!-- image_chunk: img_38a4cb84e0cce5a7 -->

![unknown](topics/images/quickcalls.10.jpg) <!-- image_chunk: img_58a5bae2e9e9bf9a -->

![inline_icon](topics/images/quickcalls.11.jpg) <!-- image_chunk: img_35e51a8a5d31df2a -->

![inline_icon](topics/images/proc_includeThis_unchecked.png) <!-- image_chunk: img_76d990683c099a8f -->
