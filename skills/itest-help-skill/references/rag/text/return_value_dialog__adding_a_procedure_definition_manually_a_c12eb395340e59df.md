---
{
  "chunk_id": "return_value_dialog__adding_a_procedure_definition_manually_a_c12eb395340e59df",
  "source_file": "topics/return_value_dialog.htm",
  "source_original_path": "topics/return_value_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Procedures",
    "Defining a procedure"
  ],
  "heading_path": [
    "Defining a procedure",
    "Defining a procedure",
    "Adding a procedure definition manually and modifying procedure properties (like arguments)"
  ],
  "anchor": "1279058",
  "context_ids": [
    "procedures_defining",
    "return_value_dialog"
  ],
  "index_keywords": [
    "defining",
    "enable json response",
    "procedure properties",
    "procedures"
  ],
  "index_keyword_paths": [
    "defining > procedures",
    "enable json response",
    "procedure > procedure properties",
    "procedures > defining"
  ],
  "related_links": [
    "view_outline.htm#1706583",
    "view_concept.htm#",
    "quickcalls_overview.htm#"
  ],
  "images": [
    "topics/images/prc_tags.png",
    "topics/images/proc_resp_struc_json.png"
  ],
  "content_hash": "c12eb395340e59df",
  "level": 2
}
---

# Defining a procedure > Defining a procedure > Adding a procedure definition manually and modifying procedure properties (like arguments)

1. In the Test Case editor, select a step and click Insert , and then select Insert Procedure. iTest adds a blank procedure definition below the selected step.

Select the procedure label to display the Procedure Properties tree at the bottom with the following branch structure:

General, Description, Inputs and Outputs with sub-branches, Arguments and Response.

| Note While working on a test case in the Test Case editor, right-click and on the menu displayed, select (Show Properties View). The Properties view appears as a tabbed pane on the iTest window. The Properties View pane display is context-specific and varies depending on where your cursor is positioned. You may edit step properties using either the Step Properties section (within the Test Case Editor) or via the Properties View tab. For example, if your cursor is at the procedure label (Steps > Action> procedure) and then select from the right-click menu, the Properties pane opens to display Procedure Properties (which is also displayed below the Steps > Actions section). Note You may position and resize the tabbed Properties view window as required. | Note | You may position and resize the tabbed Properties view window as required. |
| --- | --- | --- |
| Note | You may position and resize the tabbed Properties view window as required. |  |

1. 2

1. General page: In the Procedure Properties tree, click General. On the General page, specify values for the following properties. The text that you provide for the Name, Headline, Author, and Version properties (along with the Description property specified on the Description page) are displayed on the popup help for the procedure. (The popup help appears when the test developer types Ctrl+Space while in the Description cell.)

| Name | Required. Provide a meaningful name for the procedure. This is the string that test developers use to call the procedure. For procedures: This string will appear in the drop-down list of procedures in the Description cell for call steps or CallProcedure actions. For QuickCalls: Do not use the name of an existing iTest action. If you do, then during execution, iTest generates an Execution Issue Warning and then executes the built-in action. |
| --- | --- |
| Include this procedure when listing callable procedures | Check the box to include this procedure's name in the drop-down list of procedures in the Description cell for call steps or CallProcedure actions. This option makes the procedure available for use in any test case in the current workspace. Default: Checked Note The checkbox Include this procedure when listing callable procedures is enabled by default when you insert a new procedure in test case (except for main procedure). |
| Note | The checkbox Include this procedure when listing callable procedures is enabled by default when you insert a new procedure in test case (except for main procedure). |
| Headline | Optional. Type a single line of text that describes the procedure. This string will appear with the procedure name in the drop-down list of procedures in the Description cell for call steps or CallProcedure actions. This text also appears in the Headline column of the Favorites view to help you when selecting a procedure. |
| Author | Optional. Type the name of the person who created the procedure definition. This helps coworkers who have questions about the procedure. |
| Version | Optional. If you track changes to the procedure definition, use this property to specify the version number of the procedure. |
| Tags | Procedure tags help organize procedures, which may be related to each other, and applies to QuickCall libraries and regular procedure libraries. A tag is a user-defined text string that provides a way to identify and/or group procedures in a test case as required. You may create, edit, and delete procedure tags. Add a tag text as required and save the test case. Note Procedure tags are different from the testcase and parameter tags. Note When creating a procedure tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing procedure tags in the open test case. iTest allows a maximum of 64 Tag names which you may add to a procedure in a test case. Tag name supports only 64 alpha-numeric (from the UTF8 character set), dash, and underscore characters without space. If you add a tag containing characters not compliant with these requirements or more than 64 tags, a warning message displays. If you enter more than 64 characters in the tag name, the value will be truncated and a message displays saying that only 64 characters are supported. If you add more than 64 tags, the additional tag will not be added and a message displays saying that only 64 tags may be added. Note If you already have tags which are not compliant with the above, a error displays asking you to fix this. You cannot save these tags until you make the tags compliant with the above requirements or run the test if you do not fix the procedure tags issues. Add a new tag as required and save the test case. The new tag will be displayed in the Search list only after you save the test case. See Outline View (“iTest Views”) to view the test case outline and filter the list by Tags or procedure name. When you select a procedure in the Outline View, TestCase Editor jumps to the corresponding procedure in the current testcase and expands to display the child steps. |
| Note | Procedure tags are different from the testcase and parameter tags. |
| Note | When creating a procedure tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of existing procedure tags in the open test case. |
|  | iTest allows a maximum of 64 Tag names which you may add to a procedure in a test case. |
|  | Tag name supports only 64 alpha-numeric (from the UTF8 character set), dash, and underscore characters without space. |
|  | If you enter more than 64 characters in the tag name, the value will be truncated and a message displays saying that only 64 characters are supported. |
|  | If you add more than 64 tags, the additional tag will not be added and a message displays saying that only 64 tags may be added. |
| Note | If you already have tags which are not compliant with the above, a error displays asking you to fix this. You cannot save these tags until you make the tags compliant with the above requirements or run the test if you do not fix the procedure tags issues. |
|  | Search Click Search to display the Search Tags dialog. When searching a procedure tag, iTest supports auto-completion, that is, as you type text, iTest displays a list of tags to select. The Search Tags dialog lists tags from the test case. Select tag(s) as required, click OK, and save the test case. Note Tags in-memory cache will reset when you restart iTest. Procedure tags are not part of testcase and parameter files tags and are not synced with Velocity Core |
| Note |  |
|  | Tags in-memory cache will reset when you restart iTest. |
|  | Procedure tags are not part of testcase and parameter files tags and are not synced with Velocity Core |
| Response Map | Optional. Specify the response map to apply to the value returned by the procedure (via a return step in the procedure). Note Spirent recommends that you specify the response map here, rather than in the call step in the caller. (The call step does not need to have a response map configured for it.) In this situation, consider defining a QuickCall to perform the procedure’s function. Because a QuickCall is associated with a session profile, you can associate the required response map with the session profile and do not need to worry about response maps while defining test case steps. See “QuickCalls: Defining and using a library of custom actions”. |
| Note | Spirent recommends that you specify the response map here, rather than in the call step in the caller. (The call step does not need to have a response map configured for it.) In this situation, consider defining a QuickCall to perform the procedure’s function. Because a QuickCall is associated with a session profile, you can associate the required response map with the session profile and do not need to worry about response maps while defining test case steps. See “QuickCalls: Defining and using a library of custom actions”. |
| Default session | Optional. Specify a session type in the following situation: If the Session ID of the steps in the procedure are parameterized so that the Session ID value can be set at runtime, then specify the appropriate session type here. This enables the system (at design-time, while you are designing the procedure) to populate the Action cell with actions that are appropriate for the session type. |

1. 3

1. Description: In the Procedure Properties tree, click Description. For the Description property, type the text that should appear in the help popup for the procedure. Spirent recommends that you show all forms of the procedure call (for example, provide examples of all permitted combinations of required and optional arguments). Show each form of the call on a new line.

1. 4

1. Inputs and Outputs: Procedures can use both named arguments and numbered arguments. Perform this step if the procedure uses named arguments. The order of arguments in the list that you create here is the order in which they appear when a test case developer is creating a call step or CallProcedure action.

Arguments: In the Procedure Properties> Inputs and Outputs tree, click Arguments. On the Arguments page, click to add a new argument definition.

Specify values for the following properties for arguments to the procedure:

| Name | Provide a meaningful, short name. This is the string that test developers use to specify the argument value. |
| --- | --- |
| This argument is required | Check the box to require that the test developer must specify the argument when calling the procedure. In the popup help for the procedure, the text (required) will appear next to the argument name. (The popup help appears when the test developer types a hyphen “-” while adding arguments.) Default: Unchecked |
| Default value | Optional. Provide a single value that the procedure will use for the argument if the user does not specify a value for the argument.] |
| Description | Optional. Type one or more lines of text to completely describe the argument. This text will appear in popup help for the procedure when the test developer types Ctrl + Space. |

Arguments page toolbar

| Add | Add a new named argument definition. |
| --- | --- |
| Remove | Delete the selected argument definition. |
| Move Up / Move Down | Move the selected argument definition up or down in the list. When a test developer adds a call step or CallProcedure action, the help text that appears for the procedure displays the arguments in the listed order. |

1. Response: In the Procedure Properties> Inputs and Output tree, click Response. On the Response page, select Enable JSON Response to configure the sample JSON response. Use the text area to edit the JSON string, or use the JSON tree to generate the JSON string.

| Enable JSON Response | Select to enable JSON Response, which allows you to define the JSON response. When enabled, the response node in the Procedure Properties > Inputs and Outputs tree allows you to configure the JSON response for this procedure. When disabled, the sample JSON structure controls (raw text and nested/indented layout) is not available (grayed out). |
| --- | --- |

You can also get a sample data from response map, if you Enable JSON Response and the sample JSON response is empty (not defined yet). The first sample data from the response map file will be fetched and populated on the Response page.

You may define QuickCall procedures with JSON Response, and insert these calls in a Test Case. The insterted step populates the Response View with the JSON response from the called procedure (the Response View background is light grey before running a test case). It is not necessary to execute the test case to see the format of the response.

> **Note:** Note The response map should use JSON mapper for the data to be populated in the Response window.

![screenshot](topics/images/prc_tags.png) <!-- image_chunk: img_05808ff2750458e3 -->

![screenshot](topics/images/proc_resp_struc_json.png) <!-- image_chunk: img_d501a86a3efc0501 -->
