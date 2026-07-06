# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/exitprocedure.html > ExitProcedure

Stop executing the current procedure and return execution from the current procedure to the caller.

Important: Because this action alters the flow of execution, it is deferred (not executed) until all other actions for the step are executed. This is true even if this action appears before other actions in the list of actions for the event and if there are additional analysis rules listed after the current rule for the step. For example, even if a FailTest action appears last in the list after an ExitProcedure action, the ExitProcedure action does not execute until the FailTest action is finished executing.

An appropriate execution message appears in the Execution view and in test reports.
