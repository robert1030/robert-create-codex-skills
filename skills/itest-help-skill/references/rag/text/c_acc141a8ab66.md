# Events: Taking Action when a Particular Event Occurs During Execution > Actions on events: Definitions > 第1段

Events (described in Event definitions) can perform the following actions:

Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after an AbortExecution action, the AbortExecution action does not execute until the FailTest action is finished executing.

Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a Break action, the Break action does not execute until the FailTest action is finished executing.

Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after a CallProcedure action, the CallProcedure action does not execute until the FailTest action is finished executing. Note Do not add a CallProcedure action to either an OnProcedureEnter or an OnProcedureExit event—this results in an infinite loop.

Note Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after a Continue action, the Continue action does not execute until the FailTest action is finished executing.

Note In HTML, text, and XML format reports, the OK severity is listed as “pass” and Error is listed as “fail”.

Note iTest can generate a plain language sentence for the execution message (for example, “Extracted value $value is equal to “Up”). To use this feature, specify a Message value of {auto_message_true} or {auto_message_false}, as appropriate.
