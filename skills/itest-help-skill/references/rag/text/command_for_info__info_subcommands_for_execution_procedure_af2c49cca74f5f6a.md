---
{
  "chunk_id": "command_for_info__info_subcommands_for_execution_procedure_af2c49cca74f5f6a",
  "source_file": "topics/command_for_info.htm",
  "source_original_path": "topics/command_for_info.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "info commands",
    "Commands for returning information: info"
  ],
  "heading_path": [
    "Commands for returning information: info",
    "Commands for returning information: info",
    "‘info’ subcommands for execution, procedures, threads, parameters, and variables"
  ],
  "anchor": "1810679",
  "context_ids": [
    "command_for_info"
  ],
  "index_keywords": [
    "info",
    "info command",
    "info env",
    "info env command",
    "info homeDir",
    "info homeDir command",
    "info hostIp",
    "info hostIp command",
    "info hostName",
    "info hostName command",
    "info issueCount",
    "info issueCount command",
    "info paramFile",
    "info paramFile command",
    "info platform",
    "info platform command",
    "info profile",
    "info profile command",
    "info status",
    "info status command",
    "info step report",
    "info step report command",
    "info step sessionId",
    "info step sessionId command",
    "info step testCase",
    "info step testCase command",
    "info tempDir",
    "info tempDir command",
    "info testCaseFile",
    "info testCaseFile command",
    "info testCaseName",
    "info testCaseName command",
    "info testCaseProject",
    "info testCaseProject command",
    "info testCaseProjectPath",
    "info testCaseProjectPath command",
    "info testReport id",
    "info testReport id command",
    "info threadId",
    "info threadId command",
    "info time",
    "info time command",
    "info timestamp",
    "info timestamp command",
    "info user",
    "info user command",
    "info version",
    "info version command",
    "info workingDir",
    "info workingDir command",
    "info workspacePath",
    "info workspacePath command"
  ],
  "index_keyword_paths": [
    "commands > info",
    "commands > info env",
    "commands > info homeDir",
    "commands > info hostIp",
    "commands > info hostName",
    "commands > info issueCount",
    "commands > info paramFile",
    "commands > info platform",
    "commands > info profile",
    "commands > info status",
    "commands > info step report",
    "commands > info step sessionId",
    "commands > info step testCase",
    "commands > info tempDir",
    "commands > info testCaseFile",
    "commands > info testCaseName",
    "commands > info testCaseProject",
    "commands > info testCaseProjectPath",
    "commands > info testReport id",
    "commands > info threadId",
    "commands > info time",
    "commands > info timestamp",
    "commands > info user",
    "commands > info version",
    "commands > info workingDir",
    "commands > info workspacePath",
    "info command",
    "info env command",
    "info homeDir command",
    "info hostIp command",
    "info hostName command",
    "info issueCount command",
    "info paramFile command",
    "info platform command",
    "info profile command",
    "info status command",
    "info step report command",
    "info step sessionId command",
    "info step testCase command",
    "info tempDir command",
    "info testCaseFile command",
    "info testCaseName command",
    "info testCaseProject command",
    "info testCaseProjectPath command",
    "info testReport id command",
    "info threadId command",
    "info time command",
    "info timestamp command",
    "info user command",
    "info version command",
    "info workingDir command",
    "info workspacePath command"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "af2c49cca74f5f6a",
  "level": 2
}
---

# Commands for returning information: info > Commands for returning information: info > ‘info’ subcommands for execution, procedures, threads, parameters, and variables

| Command | Description |
| --- | --- |
| info exists param paramName info('exists', 'param', 'paramName') | Returns 1 (one) if the parameter specified by paramName exists, otherwise returns 0 (zero). Similar to the info exists command. |
| info exists {local|global} varName info('exists', 'local|global', 'varName') | Returns 1 (one) if the local or global variable specified by varName exists, otherwise returns 0 (zero). Similar to the Tcl info exists command. |
| info issueCount {ok|info|warning|error|all} info('issueCount', ['ok'|'info'|'warning'|'error'|'al']) | Returns, for this moment in the current execution, the current number of execution issues of the specified severity |
| info procedure info('procedure') | Returns the name of the procedure that contains the currently executing step |
| info status info('status') | Returns the current execution Result of the test case being executed: Pass, Fail, Abort, or Indeterminate. If no test case is running, returns Indeterminate. |
| info step report info('step', 'report') | Returns the step ID (for example, 2.3.1.5) of the currently executing step from the test report currently being executed. When executing Python scripts (e.g., a Tcl test case exported to Python), the command info(’step’) displays a message saying that the info command is not supported. |
| info step testCase info('step', 'testCase') | Returns the step ID (for example, 2.5.3) of the currently executing step. |
| info step sessionID info('step', 'sessionID') | Returns then Session ID (the value in the Session cell) of the currently executing step. Example To handle unexpected events (for example, OnExecutionTimeout) in a test case, you could define a callProcedure action for the event. Use the info step sessionName command to obtain the session ID for the step that timed out. The callProcedure action would pass the session ID for the step as an argument to the procedure. As a result, when the event occurs, the procedure can clean up all devices to a known state before the test case ends. |
| info testReportID info('testReportID') | Returns the report ID of the current test report. You can use the report ID to access the report. Note When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| Note | When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| info threadID info('threadID') | Returns the ID of the current thread Note When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| Note | When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| info time info('time') | Returns the number of seconds (floating point) since execution of the current test case started, excluding pauses. If not currently executing, returns 0. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
