# Events: Taking Action when a Particular Event Occurs During Execution > Deferred actions

Because some actions alter the flow of execution, they are deferred (not executed) until all other actions for the step are executed. This is true even if the action appears before other actions in the list of actions for the event. For example, even if a FailTest action appears last in the list after an AbortExecution action, the AbortExecution action does not execute until the FailTest action is finished executing. The following actions are deferred and are fully described in the table in Actions on events: Definitions:

AbortExecution

Break

CallProcedure

Continue

ExitExecution

ExitProcedure

Goto [Deprecated. We strongly recommend that you not use this action.]
