# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/return.html > return

A return step stops executing the current procedure and returns execution from the current procedure to the caller.

This means to either continue processing the procedure whose call step (or CallProcedure action) caused the procedure to start, or end test case execution if the procedure was the initial entry point. Any threads started by the procedure continue.

You can return a value for the procedure. The text specified for the specified in the Description cell (the value of the Command property) of the return step is appended to the response of the call step. The text string can contain field replacements (for example, [response var_name]). The Start this step in a new thread and proceed to the next step (asynchronous execution) property on a return step is ignored. Steps nested inside return steps are never executed.

Tip: You can use a return step in the main procedure to exit a test case. Because you do not typically want to return every time the test case runs, you'll probably include the return step within an if construct.

For details, see the online help: The return action.

Also, see the help for the related write action.
