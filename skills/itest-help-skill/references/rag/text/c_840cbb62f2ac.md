# iTest Commands > info commands > Commands for returning information: info > ‘info’ subcommands for execution, procedures, threads, parameters, and variables > 第2段

| 欄位1 | 欄位2 |
| --- | --- |
| Command | Description |
| info exists param paramName info('exists', 'param', 'paramName') | Returns 1 (one) if the parameter specified by paramName exists, otherwise returns 0 (zero). Similar to the info exists command. |
| info exists {local|global} varName info('exists', 'local|global', 'varName') | Returns 1 (one) if the local or global variable specified by varName exists, otherwise returns 0 (zero). Similar to the Tcl info exists command. |
| info issueCount {ok|info|warning|error|all} info('issueCount', ['ok'|'info'|'warning'|'error'|'al']) | Returns, for this moment in the current execution, the current number of execution issues of the specified severity |
| info procedure info('procedure') | Returns the name of the procedure that contains the currently executing step |
| info status info('status') | Returns the current execution Result of the test case being executed: Pass, Fail, Abort, or Indeterminate. If no test case is running, returns Indeterminate. |
| info step report info('step', 'report') | Returns the step ID (for example, 2.3.1.5) of the currently executing step from the test report currently being executed. When executing Python scripts (e.g., a Tcl test case exported to Python), the command info(’step’) displays a message saying that the info command is not supported. |
| info step testCase info('step', 'testCase') | Returns the step ID (for example, 2.5.3) of the currently executing step. |
| info step sessionID info('step', 'sessionID') | Returns then Session ID (the value in the Session cell) of the currently executing step. Example To handle unexpected events (for example, OnExecutionTimeout) in a test case, you could define a callProcedure action for the event. Use the info step sessionName command to obtain the session ID for the step that timed out. The callProcedure action would pass the session ID for the step as an argument to the procedure. As a result, when the event occurs, the procedure can clean up all devices to a known state before the test case ends. |
| info testReportID info('testReportID') | Returns the report ID of the current test report. You can use the report ID to access the report. |
| info threadID info('threadID') | Returns the ID of the current thread |
| info time info('time') | Returns the number of seconds (floating point) since execution of the current test case started, excluding pauses. If not currently executing, returns 0. |
