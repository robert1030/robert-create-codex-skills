---
{
  "chunk_id": "tce_step_properties_general__general_properties_group_452090e930d4a1b5",
  "source_file": "topics/tce_step_properties_general.htm",
  "source_original_path": "topics/tce_step_properties_general.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Step Properties section: General properties group"
  ],
  "heading_path": [
    "Step Properties section: General properties group",
    "Step Properties section: General properties group",
    "General properties group"
  ],
  "anchor": "1973109",
  "context_ids": [
    "tce_step_properties_general"
  ],
  "index_keywords": [
    "General properties group",
    "steps"
  ],
  "index_keyword_paths": [
    "General properties group > steps",
    "Step Properties section > General properties group"
  ],
  "related_links": [
    "test_report_set_steps_that_appear_in_report.htm#1466765",
    "threads_view.htm#1119502",
    "threaded_execution.htm#",
    "action_concept.htm#1527558",
    "parameters_page.htm#1135242"
  ],
  "images": [],
  "content_hash": "452090e930d4a1b5",
  "level": 2
}
---

# Step Properties section: General properties group > Step Properties section: General properties group > General properties group

| Skip this step when executing | Prevent the step from being run when the procedure is executed. Skipped steps have a gray dotted background in the Test Case editor. |
| --- | --- |
| Include this step and its children in test reports | By default, each step that executes in a test is added to the test report. Uncheck the box to specify that a particular step and any of its children should not appear in test reports (the step executes normally, it simply is not reported). Execution issues If a child step of any step that is configured not to appear in reports has an execution issue, then, in the in the list of execution messages in the Execution view, the issue’s icon appears next to the message for the nearest ancestor. The step index for the issue is associated with the child step that had the issue. Overriding this setting You can override this setting for all test cases by setting a preference. See Controlling which executed steps appear in test reports. Default: checked |
| Start this step (in a new thread) and proceed to the next step | Select to cause the step to run after the preceding step and concurrently (asynchronously) with the following step or steps. This feature is commonly referred to as Specify how long to wait for the prompt to appear execution, async execution, concurrent execution, or concurrency. Note The Shared sessions property cannot be use when you select this option, as this step runs in a separate thread. See Threads view |
| Note | The Shared sessions property cannot be use when you select this option, as this step runs in a separate thread. |
| Cancel execution of the resulting thread if still running when the test case ends | Some steps may still be waiting for a response when the test case ends. Check the box to end the test in this case. The test result is set to Fail. |
| Thread name | Specify a name for the thread associated with this step. See “Making your test case thread-safe”. |
| Session | The reference label for the session associated with the step. A procedure may access any number of sessions, with the first action for each being the open action. |
| Action | The session-specific action to take for the step. See Actions |
| Command | Typically, the Command property holds the command to send to the session as part of the associated Action. Additionally, the property can hold the URI of a file. Examples For a CLI command action, the Command might be show routes. For an open step, the Command might be the URI of the session profile or the name of the device to use to start the session For a comment step, the Command is the text of the comment. For a configure step (used by many traffic-generator device session types), the Command is the text of the multi-line configuration file For open and readFile steps, Browse opens a dialog box so you can specify the file to access. For steps that involve text, Details opens a multi-line text box (so you can enter, for example, a multi-line command). Type or paste the text into a text box. |
|  | For a CLI command action, the Command might be show routes. |
|  | For an open step, the Command might be the URI of the session profile or the name of the device to use to start the session |
|  | For a comment step, the Command is the text of the comment. |
|  | For a configure step (used by many traffic-generator device session types), the Command is the text of the multi-line configuration file |
| Mask command contents | Check this box to cause iTest to display sensitive information (passwords, for example) as asterisks. |
| For the Command field, perform command, variable, and backslash substitutions | Check the box if the string specified for the Command property uses a command field replacement, a variable, or a backslash that is used to escape a special character. As a result, the substitutions will be performed before iTest uses the text that appears in the Command field. Note Field Replacement for a Call action step is disabled by default. The following warning message displays to caution you about the consequences: Do not enable substitution for this step. This results in incorrect double substitution. |
| Note | Field Replacement for a Call action step is disabled by default. The following warning message displays to caution you about the consequences: Do not enable substitution for this step. This results in incorrect double substitution. |
| Command field contains an encrypted value | Check the box if the Command text includes a reference to a parameter whose value is masked (encrypted and hidden from the user). For example, the text might include a param command in a field replacement. For instructions on masking a parameter's value, see Working with parameters: The Parameters page. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
