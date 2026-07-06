# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/run.html > run

A run step executes the specified test case (the child test case) and optionally passes parameter values. The child test case executes exactly as if it had been executed using iTest Runtime (itestcli), except that execution occurs within the current process context.

You have the option to configure the response to run steps. The response to the run step includes summary information for each child test case execution (enabling you to work with the data without having to open the individual test reports). In addition, run can return a table of all child test case executions (either the test case that was executed directly by the run or the test cases that were executed indirectly when a run step executed inside one of the child test cases, and so on) You can run child test cases without loading a testbed for the parent main procedure.

For details on creating and configuring run steps, see the online help: The run action.
