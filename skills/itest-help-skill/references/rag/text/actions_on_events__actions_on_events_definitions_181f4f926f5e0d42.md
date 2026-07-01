---
{
  "chunk_id": "actions_on_events__actions_on_events_definitions_181f4f926f5e0d42",
  "source_file": "topics/actions_on_events.htm",
  "source_original_path": "topics/actions_on_events.htm",
  "toc_path": [
    "iTest Online Help",
    "Events: Taking Action when a Particular Event Occurs During Execution",
    "Actions on events: Definitions"
  ],
  "heading_path": [
    "Actions on events: Definitions",
    "Actions on events: Definitions"
  ],
  "anchor": "1206889",
  "context_ids": [
    "actions_on_events"
  ],
  "index_keywords": [
    "AbortExecution",
    "AbortStep",
    "AbortTest",
    "AbortThread",
    "Break",
    "CallProcedure",
    "Continue",
    "DeclareExecutionIssue",
    "Eval",
    "ExitExecution",
    "ExitProcedure",
    "FailTest",
    "PassTest",
    "PassTestIfNotAlreadyFailed",
    "PauseExecution",
    "RepeatStep",
    "ScriptEval",
    "SkipRemainingRules",
    "defined",
    "for events"
  ],
  "index_keyword_paths": [
    "AbortExecution action > for events",
    "AbortStep action > for events",
    "AbortTest action > for events",
    "AbortThread action > for events",
    "Break action > for events",
    "CallProcedure action > for events",
    "Continue action > for events",
    "DeclareExecutionIssue action > for events",
    "Eval action > for events",
    "ExitExecution action > for events",
    "ExitProcedure action > for events",
    "FailTest action > for events",
    "PassTest action > for events",
    "PassTestIfNotAlreadyFailed action > for events",
    "PauseExecution action > for events",
    "RepeatStep action > for events",
    "ScriptEval action > for events",
    "SkipRemainingRules action > for events",
    "actions for events > AbortExecution",
    "actions for events > AbortStep",
    "actions for events > AbortTest",
    "actions for events > AbortThread",
    "actions for events > Break",
    "actions for events > CallProcedure",
    "actions for events > Continue",
    "actions for events > DeclareExecutionIssue",
    "actions for events > Eval",
    "actions for events > ExitExecution",
    "actions for events > ExitProcedure",
    "actions for events > FailTest",
    "actions for events > PassTest",
    "actions for events > PassTestIfNotAlreadyFailed",
    "actions for events > PauseExecution",
    "actions for events > RepeatStep",
    "actions for events > ScriptEval",
    "actions for events > SkipRemainingRules",
    "actions for events > defined"
  ],
  "related_links": [
    "events.4.htm#1205849",
    "procedure_calling.htm#1291793",
    "commands_built_in_local_variables.htm#1705062",
    "arules_processor_properties.htm#1187991",
    "analysis_rules_concept.htm#",
    "action_signal.htm#1530304",
    "action_signalactivate.htm#1530343",
    "action_signalall.htm#1530328"
  ],
  "images": [],
  "content_hash": "181f4f926f5e0d42",
  "level": 1
}
---

# Actions on events: Definitions > Actions on events: Definitions

Events (described in Event definitions) can perform the following actions:

| AbortExecution | Stops execution. Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after an AbortExecution action, the AbortExecution action does not execute until the FailTest action is finished executing. No configurable properties. | Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after an AbortExecution action, the AbortExecution action does not execute until the FailTest action is finished executing. |
| --- | --- | --- | --- |
| Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after an AbortExecution action, the AbortExecution action does not execute until the FailTest action is finished executing. |  |  |
| AbortStep | Immediately stops executing the step and then proceed to the next step. In an analysis rule, this action has the effect of not performing remaining analysis rules and then continuing to the next step. No configurable properties. |  |  |
| AbortTest | Set the test result as Abort. Continue to execute. Note that execution is not stopped. No configurable properties. |  |  |
| AbortThread | Immediately stop executing the current thread. No configurable properties. |  |  |
| AppendToProcedureResponse | Writes the specified text to a procedure’s return buffer. To return the full response, set the Content text to [response .] Supports field replacements. |  |  |
| AppendToStepResponse | Writes to the specified text to a step’s return buffer. To return the full response, set the Content text to [response .] Supports field replacements. |  |  |
| Break | Break out of a for, foreach, or while loop. Use this break action to stop executing a loop and continue executing at the step after the loop. Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing. No configurable properties. | Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing. |
| Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing. |  |  |
| CallProcedure | Call the specified procedure (local or foreign) or the specified QuickCall. iTest provides interactive support for specifying the procedure. See Calling a procedure in a test case step or in a property setting. Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a CallProcedure action, the CallProcedure action does not execute until the FailTest action is finished executing. Note Do not add a CallProcedure action to either an OnProcedureEnter or an OnProcedureExit event—this results in an infinite loop. Property: Procedure name and arguments: Specify the procedure name followed by argument values if appropriate. For example, SetupDevice -deviceNumber 3. | Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a CallProcedure action, the CallProcedure action does not execute until the FailTest action is finished executing. |
| Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a CallProcedure action, the CallProcedure action does not execute until the FailTest action is finished executing. |  |  |
| Note | Do not add a CallProcedure action to either an OnProcedureEnter or an OnProcedureExit event—this results in an infinite loop. |  |  |
| Continue | The Continue action causes the current step to be aborted out to the innermost containing for, foreach, or while loop command. The loop then continues with the next iteration of the loop. Use the Continue action when you want to execute particular steps for some iterations of the loop, but not for other iterations. Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after a Continue action, the Continue action does not execute until the FailTest action is finished executing. No configurable properties. | Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after a Continue action, the Continue action does not execute until the FailTest action is finished executing. |
| Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after a Continue action, the Continue action does not execute until the FailTest action is finished executing. |  |  |
| DeclareExecutionIssue | Generate an execution issue with a particular severity and display an associated execution message in the Execution view, in the Step Issues view, and in test reports. Properties: Severity: This setting specifies the type of issue: OK (executed as expected), Information, Warning, Error (did not execute as expected) Note In HTML, text, and XML format reports, the OK severity is listed as “pass” and Error is listed as “fail”. Message: Specify the text message to display in the Execution view, in the Step Issues view, and in test reports. Field replacements are supported. Note iTest can generate a plain language sentence for the execution message (for example, “Extracted value $value is equal to “Up”). To use this feature, specify a Message value of {auto_message_true} or {auto_message_false}, as appropriate. You can use any of several built-in variables to customize the message text. Information on built-in variables like $value appears in Tcl interpreter local variables. Note To ensure access to certain data that is available when the message is generated, iTest first applies its standard field substitution and then uses Java-style format strings for messages. Java format strings uses escaping rules that differ from Tcl rules. For example, Java string format uses single quote ' as its special character and you need two of these for escaping. So, to cause ‘ to appear in the message, use two single quotes ‘’ in the message text. For the Java string format rules, see https://docs.oracle.com/javase/7/docs/api/java/text/MessageFormat.html | Note | In HTML, text, and XML format reports, the OK severity is listed as “pass” and Error is listed as “fail”. |
| Note | In HTML, text, and XML format reports, the OK severity is listed as “pass” and Error is listed as “fail”. |  |  |
| Note | iTest can generate a plain language sentence for the execution message (for example, “Extracted value $value is equal to “Up”). To use this feature, specify a Message value of {auto_message_true} or {auto_message_false}, as appropriate. |  |  |
| Note | To ensure access to certain data that is available when the message is generated, iTest first applies its standard field substitution and then uses Java-style format strings for messages. Java format strings uses escaping rules that differ from Tcl rules. |  |  |
| Eval | Evaluate the statements specified in the Properties cell. No configurable properties. |  |  |
| ExitExecution | Immediately stop executing the current procedure and all threads to end test case execution. The ExitExecution action does not change the existing execution result of the test case (Pass, Fail, Abort, or Indeterminate). Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing. No configurable properties. | Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing. |
| Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing. |  |  |
| ExitProcedure | Stop executing the current procedure and return execution from the current procedure to the caller. You can specify a return value for the procedure in the Return value property. Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after an ExitProcedure action, the ExitProcedure action does not execute until the FailTest action is finished executing. No configurable properties. | Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after an ExitProcedure action, the ExitProcedure action does not execute until the FailTest action is finished executing. |
| Note | Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after an ExitProcedure action, the ExitProcedure action does not execute until the FailTest action is finished executing. |  |  |
| FailTest | Set the test result as Fail. Continue to execute. No configurable properties. |  |  |
| PassTest | Set the test result as Pass. Continue to execute. No configurable properties. |  |  |
| PassTestIfNotAlreadyFailed | If the test result is not already Fail, then set the test result as Pass. Continue to execute. No configurable properties. |  |  |
| PauseExecution | Immediately pause execution. Bring the Execution view to the front. No configurable properties. |  |  |
| RepeatStep | Repeat the current step. The RepeatStep action cannot be used with an async step (a step that has the Start this step (in a new thread) and proceed to the next step property checked). Properties: Maximum repeat count: Specify the maximum number of times to repeat the step. Delay between repeats: Specify how long to wait between repetitions of the step (in seconds). |  |  |
| ScriptEval | Evaluate the script specified in the Properties cell using the Tcl interpreter attached to the execution kernel. The response is populated (including structured data) in a way consistent with how a Tcl Shell Command step works (including result, STDOUT, and/or STDERR). The following types of substitution are not made to the text of the Command property before the step is executed: Command field replacements Variables Backslash characters used to escape special characters No configurable properties. |  | Command field replacements |
|  | Command field replacements |  |  |
|  | Variables |  |  |
|  | Backslash characters used to escape special characters |  |  |
| SetResponseValue | Configure a action response, which returns the appropriate value during test execution. For example, to specify the actions that should occur upon True and False results, specify Rule Actions for When True and When False. That is, enter the ActionSetResponseValue and specify a response. See also Assert processor (“Analysis Rules: Validating Responses”). |  |  |
| SkipRemainingRules | iTest does not perform any further analysis rules associated with the current step. For example, you might set this Action so that when an analysis rule concludes that something has gone wrong and there is no point in performing additional analysis, then skip further analysis. No configurable properties. |  |  |
| signal eventName | For synchronous execution: Wakes a thread that is waiting on eventName and causes it to continue execution. See signal: Wake a thread that is waiting on an event. |  |  |
| signalActivate eventName | For synchronous execution: Turns on the event called eventName. See signalActivate: Turn a signal on. |  |  |
| signalAll eventName | For synchronous execution: Causes the currently executing thread to sleep until all specified events have been signaled or activated (signal, signalAll, or signalActivate). See signalAll: Wake all threads that are waiting on an event. |  |  |
| signalClear eventName | For synchronous execution: Removes any instances of the event named eventName that had previously been activated either by a signalActivate step or by a signal command. See signalActivate: Turn a signal on. |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
