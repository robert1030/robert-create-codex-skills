---
{
  "chunk_id": "add_parameter_dialog__adding_a_parameter_definition_while_inse_36cad639e7eb46b2",
  "source_file": "topics/add_parameter_dialog.htm",
  "source_original_path": "topics/add_parameter_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Using Parameters in Properties or Steps",
    "Adding a parameter definition while inserting parameters"
  ],
  "heading_path": [
    "Adding a parameter definition while inserting parameters",
    "Adding a parameter definition while inserting parameters"
  ],
  "anchor": "1144750",
  "context_ids": [
    "add_parameter_dialog"
  ],
  "index_keywords": [
    "creating while inserting",
    "parameters while inserting"
  ],
  "index_keyword_paths": [
    "creating > parameters while inserting",
    "parameters > creating while inserting"
  ],
  "related_links": [],
  "images": [
    "topics/images/insert_parameter_dialog_annotated_2.png"
  ],
  "content_hash": "36cad639e7eb46b2",
  "level": 1
}
---

# Adding a parameter definition while inserting parameters > Adding a parameter definition while inserting parameters

While inserting a parameter into a test case step, you may want to create a new parameter. This dialog box appears when you click Add on the Insert Parameter dialog box.

When you click OK, the new parameter is added at the end of the list of test case parameters.

> **Note:** Note The parameter is not actually created until you click Insert on the Insert Parameters dialog box.

You can specify only the following properties on this page. To specify advanced properties like inheritance rules, use the Parameters page.

| Name | Specify a friendly name for the parameter (for example, port, slot, deviceID, IPaddress). The name appears in the Data view. |
| --- | --- |
| Type | Select the appropriate parameter type. For example, int for port, Secret for password. Since the parameter Type Secret is automatically masked, the Mask the value option is automatically selected and grayed. |
| Value | Specify the value of the parameter. The value appears in the Data view, where you can modify it when execution is paused or loaded for execution. You can create an empty parameter (that is, no value). To create a parameter with multiple values, create multiple parameters with the same name. Multiple values for a single parameter are useful, for example, in foreach constructs. |
|  | You can create an empty parameter (that is, no value). |
|  | To create a parameter with multiple values, create multiple parameters with the same name. Multiple values for a single parameter are useful, for example, in foreach constructs. |
| Description | Optional. Describe the function and use of the parameter. The text appears in the Data view to help you when setting parameter values while executing or single-stepping the test case. |
| Mask the value | Note This option is available for selection only when the Type is text and grayed for the rest of the parameter Type. The Mask the value option is automatically enabled when you select the parameter Type Secret, as it is automatically masked. Check the box for sensitive information that should be hidden from view in any user-visible windows (for example, you might mask passwords). iTest performs the following actions for masked parameter values to ensure that the value remains confidential: Encrypt the parameter value Display the value only as asterisks (********) in any editor, view, or report The param and profile commands never decrypt any parameter whose value is masked. As a result, the value never appears in clear (unencrypted) form in any file or in any editor, view, or report visible to a user. |
| Note |  |
|  | Encrypt the parameter value |
|  | Display the value only as asterisks (********) in any editor, view, or report |
|  | The param and profile commands never decrypt any parameter whose value is masked. As a result, the value never appears in clear (unencrypted) form in any file or in any editor, view, or report visible to a user. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/insert_parameter_dialog_annotated_2.png) <!-- image_chunk: img_744a0d2ee2f85aba -->
