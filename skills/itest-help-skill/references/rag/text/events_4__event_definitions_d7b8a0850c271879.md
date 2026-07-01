---
{
  "chunk_id": "events_4__event_definitions_d7b8a0850c271879",
  "source_file": "topics/events.4.htm",
  "source_original_path": "topics/events.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Events: Taking Action when a Particular Event Occurs During Execution",
    "Event definitions"
  ],
  "heading_path": [
    "Event definitions",
    "Event definitions"
  ],
  "anchor": "1205849",
  "context_ids": [],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "events > defined"
  ],
  "related_links": [
    "actions_on_events.htm#1206889",
    "events.5.htm#1251139",
    "tce_general_page.htm#1965477",
    "tce_step_properties_timing.htm#1716076"
  ],
  "images": [],
  "content_hash": "d7b8a0850c271879",
  "level": 1
}
---

# Event definitions > Event definitions

Actions that can be performed when an event occurs are described in Actions on events: Definitions.

| Group / Event | Description |
| --- | --- |
| Action: Repeat Step |  |
| OnRepeatStepMaxCountExceeded | Occurs when the execution time of "RepeatStep" action has exceeded the specified MaxCount value. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Maximum repeat count of {0} has reached the limit |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Maximum repeat count of {0} has reached the limit |
| Analysis Extractor: Query |  |
| OnQueryExtractorInvalidQuery | Occurs when performing the response mapping during executing the test case, an invalid query was found (either because the query string itself is not valid or the query does not match the runtime response map definition). Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid query: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid query: {0} |
| Analysis Extractor: Regex |  |
| OnIllegalRegexPatternError | Occurs when the regular expression is empty or has a syntax error. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid regex pattern: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid regex pattern: {error} |
| Analysis Processor: Assert |  |
| OnAssertMultipleMatches | Occurs when multiple values extracted for the assertion in analysis rule. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Expected single value extracted but found multiple using “{extraction}” |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Expected single value extracted but found multiple using “{extraction}” |
| Analysis Processor: Store |  |
| OnNoMatchesFoundToStore | Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: No matches found to store in variable "{0}" |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: No matches found to store in variable "{0}" |
| OnStoreProcessorInvalidLocation | Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Unable to store result at specified location: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Unable to store result at specified location: {0} |
| Application: Agilent N2X |  |
| OnAgilentCommandFailed | — |
| OnAgilentConfigurationLoadFailed | — |
| OnAgilentSessionDisconnected | — |
| Application: HTTP |  |
| OnAuthenticationFailure | Occurs when basic authentication information is absent. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Authentication error for URL {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Authentication error for URL {0} |
| OnCommandFailed | Occurs when an I/O exception (not an authentication error) occurs. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Connect to {0} failed, reason: {1} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Connect to {0} failed, reason: {1} |
| OnConnectionRefused | Occurs when connection exception is thrown Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Host refused connection on URL {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Host refused connection on URL {0} |
| OnFileNotFound | Occurs when a URL is not found Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: URL {0} is not found |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: URL {0} is not found |
| OnServerUnreachable | Occurs when the host designated by URL is not reachable Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Host for URL {0} is unreachable |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Host for URL {0} is unreachable |
| OnUnavailableEncoding | Occurs when the charset is not set in the charset property page. Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Encoding {exp} unavailable, using {act} instead |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Encoding {exp} unavailable, using {act} instead |
| Application: IxLoad |  |
| OnIxLoadCommandFailed | Occurs when executing a test case step failed Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
| OnIxLoadConfigurationLoadFailed | Not implemented |
| OnIxLoadSessionDisconnected | Not implemented |
| Application: IxNetwork |  |
| OnIxNetworkCommandFailed | Occurs when executing a test case step failed. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
| OnIxNetworkConfigurationLoadFailed | Occurs when executing "load configuration" command failed or the session loads configuration file failed. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Failed to load configuration: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Failed to load configuration: {0} |
| OnIxNetworkSessionDisconnected | Occurs when executing a test case step and the response contains "not connected to IxNetwork". Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
| Application: Ixia Traffic |  |
| OnIxiaCommandFailed | Occurs when executing a test case step failed Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
| OnIxiaConfigurationLoadFailed | Occurs when the configuration file fails to load. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Failed to load configuration: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Failed to load configuration: {0} |
| OnIxiaSessionDisconnected | Not implemented |
| Application: Mail |  |
| OnInvalidMailProperties | Occurs when the mail properties are invalid, for example: an empty SMTP URL. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid Mail properties: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid Mail properties: {0} |
| OnMailSendFailure | Occurs when the mail ‘send’ action has issues Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Failed to send mail: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Failed to send mail: {error} |
| Application: Process |  |
| OnProcessLaunchFailure | Occurs when the process cannot be started Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error while starting process: {command} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error while starting process: {command} |
| OnProcessLimitExceeded | Occurs when the started process number exceeds the limitation. Default is 100 Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Process limit ({limit} instances) exceeded |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Process limit ({limit} instances) exceeded |
| Application: SNMP |  |
| OnSnmpErrorLoadingMibFiles | Occurs when any of the following conditions is encountered: Undefined MIB folder Specified MIB folder URI is invalid Could not open specified MIB folder No files found in specified MIB folder Could not load or parse MIB file The Strict MIB parsing property is enabled in the SNMP session profile, and an error while resolving a MIB object in the MIB file fired the event. (You can disable the Strict MIB parsing property in the SNMP session profile and then restart the test case.) Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Error while loading MIB files: {0} |
|  | Undefined MIB folder |
|  | Specified MIB folder URI is invalid |
|  | Could not open specified MIB folder |
|  | No files found in specified MIB folder |
|  | Could not load or parse MIB file |
|  | The Strict MIB parsing property is enabled in the SNMP session profile, and an error while resolving a MIB object in the MIB file fired the event. (You can disable the Strict MIB parsing property in the SNMP session profile and then restart the test case.) |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Error while loading MIB files: {0} |
| OnSnmpInvalidAction | Occurs when executing getTable action on a non-table node on the MIB tree Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: The requested action “{action}” is not appropriate for this MIB variable “{nodeName}”:{reason} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: The requested action “{action}” is not appropriate for this MIB variable “{nodeName}”:{reason} |
| OnSnmpInvalidCommandSyntax | Occurs when the argument of set command is blank Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid command syntax: {reason} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid command syntax: {reason} |
| OnSnmpOpenFail | Occurs when any of the following conditions is encountered: Specified trap port is not a number or is not between 1 and 65535 A daemon is already running on the specified port with different settings The third‑party iReasoning SNMP API throws an error for new SnmpSession(target) Default actions: FailTest AbortExecution DeclareExecutionIssue with a Severity of Error and with a default Message of: Error while opening SNMP session: {0} |
|  | Specified trap port is not a number or is not between 1 and 65535 |
|  | A daemon is already running on the specified port with different settings |
|  | The third‑party iReasoning SNMP API throws an error for new SnmpSession(target) |
|  | FailTest |
|  | AbortExecution |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error while opening SNMP session: {0} |
| OnSnmpRequestFail | Occurs when any of the following conditions is encountered: Loop or duplicate MIBs found in get/getNext/getTable/walk action SNMP session is closed before get/getNext/getTable/walk/set action is finished New MIB value is invalid for set action Cannot find the MIB definition in the loaded MIB files for set action Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: SNMP request failed: {0} |
|  | Loop or duplicate MIBs found in get/getNext/getTable/walk action |
|  | SNMP session is closed before get/getNext/getTable/walk/set action is finished |
|  | New MIB value is invalid for set action |
|  | Cannot find the MIB definition in the loaded MIB files for set action |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: SNMP request failed: {0} |
| OnSnmpStartTrapListeningFail | Occurs if the test executes a WaitForTrap action before a trap daemon is successfully started. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error trying to start listening for SNMP traps: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error trying to start listening for SNMP traps: {error} |
| OnTrapPortBindFailed | Occurs in the following cases: Specified trap port is not a number or is not between 1 and 65535 A daemon is already running on the specified port with different settings Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: SNMP trap daemon failed to bind to port {port} : {error} |
|  | Specified trap port is not a number or is not between 1 and 65535 |
|  | A daemon is already running on the specified port with different settings |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: SNMP trap daemon failed to bind to port {port} : {error} |
| Application: SmartBits |  |
| OnSmartBitsCommandFailed | — |
| OnSmartBitsSessionDisconnected | — |
| Application: Spirent TestCenter |  |
| OnSpirentTestCenterCommandFailed | — |
| OnSpirentTestCenterConfigurationLoadFailed | — |
| OnSpirentTestCenterSessionDisconnected | — |
| Application: Swing |  |
| OnSwingGeneralError | Occurs when general errors happen in a Swing session Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid swing action: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid swing action: {0} |
| OnSwingHeadless | Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {error} |
| OnSwingExecutionError | Occurs when swing session execution errors happen Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Action failed: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Action failed: {0} |
| Application: Syslog |  |
| OnSyslogCommandFailed | Not implemented |
| OnSyslogSessionDisconnected | Not implemented |
| Application: Tcl Shell |  |
| OnTclshCreateInterpreterFail | Not implemented |
| Application: Web |  |
| OnClearCacheError | Occurs when new issues are introduced after clearing cache. Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnClearCookiesError | Occurs when new issues are introduced after clearing cookies. Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnInvalidMouseEventArgument | Occurs when mouse event arguments in step property are not valid. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {error} |
| OnWebExternalBrowserError | For Web session with external browser: Occurs when cannot connect to the browser Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error communicating with external browser: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error communicating with external browser: {0} |
| OnWebHeadless | Not implemented |
| OnWebHttpError | For Web session with external browser: Occurs when HTTP status code is higher than 400. |
| OnWebInvalidProperties | Occurs in the following cases: Web session tries to get form map library but fails The open step is executing but the application property is not of the open step. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid web properties: {0} |
|  | Web session tries to get form map library but fails |
|  | The open step is executing but the application property is not of the open step. |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid web properties: {0} |
| OnWebOpenExternalBrowserFail | For Web session with external browser: Occurs when system tries to connect to the external browser but fails. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error attempting to open connection to external browser: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error attempting to open connection to external browser: {0} |
| OnWebOpenFail | Occurs when web session fails to open web editor for the internal session Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {error} |
| OnWebStepAborted | Occurs in the following cases: Session step execution is canceled; Session step is trying to get the target from web page but the XPCOMException is thrown Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Web step aborted |
|  | Session step execution is canceled; |
|  | Session step is trying to get the target from web page but the XPCOMException is thrown |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Web step aborted |
| OnWebStepSyntaxError | This event will occur for any issue generated during Web session execution Occurs in the following cases: For a selectWindow step, no window is specified For a popup window, no popup wait time is specified For a step that needs a target, no target is specified For a step that needs a target, no target wait time is specified When loading a new web page, no popup wait time is specified Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid web step: {0} |
|  | For a selectWindow step, no window is specified |
|  | For a popup window, no popup wait time is specified |
|  | For a step that needs a target, no target is specified |
|  | For a step that needs a target, no target wait time is specified |
|  | When loading a new web page, no popup wait time is specified |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid web step: {0} |
| OnWebTargetNotFound | Occurs when a specified target is not found on the web page (either because it is not on the page or it has not appeared during the period specified for the Maximum time to wait for a target property). No default actions. name variable value: <targetName> message variable value: "Specified target {name} was not found on the browser page {name} at {URL}" |
| Application: Wireshark |  |
| OnWiresharkCommandFailed | Occurs when a command fails Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Command {0} failed: {1} |
| Data extractor: XML |  |
| OnInvalidXPathQuery | Not implemented |
| OnResponseIsNotValidXml | Not implemented |
| Data extractors |  |
| OnNoMatchesFound | Occurs when the search string (as defined by query or regular expression) is not found Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: No matches found for {type}: {info} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: No matches found for {type}: {info} |
| OnUnknownExtractorError | Occurs while handling an analysis rule when no corresponding extractor is defined Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Extractor {extractor} does not exist or is obsolete |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Extractor {extractor} does not exist or is obsolete |
| OnEmulationInvalidStructuredData | Occurs when the structured data for an emulated response (after substitution of field replacement text) is invalid. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid structured data: <errorText> |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Invalid structured data: <errorText> |
| onEmulationSampleNameNotFound | Occurs when a step that is configured to use a sample response as the emulated response cannot locate a sample in a response map with the specified Sample name. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: No sample response with Sample name <specifiedName> was found |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: No sample response with Sample name <specifiedName> was found |
| OnEmulationSourceNotFound | Occurs when the External source property is not blank and the source is not found or fails to open. Note When the source response map or response map library is not found, then normally a validation error with a problem marker results. Default action DeclareExecutionIssue with a Severity of Error and with a default Message of: Emulation source not found: <errorText> |
| Note | When the source response map or response map library is not found, then normally a validation error with a problem marker results. |
| Execution |  |
| OnAbortExecution | Default action: AbortTest |
| OnAbortTestAction | Occurs each time an AbortTest action is performed — even if the test result is currently Abort and the AbortTest action does not change the result. Often used, for example, to perform a CallProcedure or PauseExecution action. Note If the OnAbortTestAction event occurs because an AbortTest action resulted in an earlier OnAbortExecution event, then the current OnAbortTestAction event cannot perform a procedureCall action (because execution has been aborted). No default actions. |
| Note | If the OnAbortTestAction event occurs because an AbortTest action resulted in an earlier OnAbortExecution event, then the current OnAbortTestAction event cannot perform a procedureCall action (because execution has been aborted). |
| OnAbortTestResult | Default action DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: {message}” |
| OnDeserializationWarning | Occurs when the user attempts to open a iTest file with deserialization issues, for example, a document in a format that is no longer supported by the current version of iTest. Default action DeclareExecutionIssue with a Severity of Warning and with a default Message of “Warning during deserialization: {warning}” |
| OnExecutionCompleted | Occurs immediately after the test case finishes executing. Does not execute deferred actions (see Deferred actions). OnExecutionCompleted can initiate only immediate actions (actions that are not deferred, as described in Deferred actions). Default action DeclareExecutionIssue with a Severity of Information and with a default Message of: “Information: {message}” |
| OnExecutionStarted | Occurs immediately before the first step in the test case is executed. Often used, for example, to call an initialization procedure. Default action DeclareExecutionIssue with a Severity of Information and with a default Message of: “Information: {message}” |
| OnExecutionTimeout | Occurs when the time period specified for the Execution Time Limit property is exceeded (see Execution Behavior). Does not execute deferred actions (see Deferred actions). Default actions FailTest AbortExecution DeclareExecutionIssue with a Severity of Error and with a default Message of: Test execution has timed out |
|  | FailTest |
|  | AbortExecution |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: |
| OnFailTestAction | Occurs each time a FailTest, action is performed — even if the test result is currently Fail and the FailTest action does not change the result. Often used, for example, to perform a CallProcedure or PauseExecution action. No default actions. |
| OnFailedTestResult | Default action DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: {message}” |
| OnFatalThreadError | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Fatal Error: {0}” FailTest AbortThread |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Fatal Error: {0}” |
|  | FailTest |
|  | AbortThread |
| OnInternalError | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Internal Error: {0}” FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Internal Error: {0}” |
|  | FailTest |
| OnInterpreterError | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: {error}” FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: {error}” |
|  | FailTest |
| OnInvalidArguments | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Error processing description: {0}” FailTest AbortExecution |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Error processing description: {0}” |
|  | FailTest |
|  | AbortExecution |
| OnInvalidEncryptedCommand | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: The command must evaluate to a single encrypted string (and nothing else additional)” FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: The command must evaluate to a single encrypted string (and nothing else additional)” |
|  | FailTest |
| OnInvalidStepPropertyType | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Application properties associated with the step are of a type that is invalid for this step: {0}” FailTest AbortStep |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Application properties associated with the step are of a type that is invalid for this step: {0}” |
|  | FailTest |
|  | AbortStep |
| OnInvalidTestCase | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Fail to load test case: {message}” FailTest AbortStep |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Fail to load test case: {message}” |
|  | FailTest |
|  | AbortStep |
| OnLoadingTestCaseFailure | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Error loading test case {testcase}: {errorMsg}” AbortExecution |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Error loading test case {testcase}: {errorMsg}” |
|  | AbortExecution |
| OnPassIfNotAlreadyFailedAction | Occurs each time a PassTestIfNotAlreadyFailed, action is performed — even if the test result is currently Pass or Fail and the PassTestIfNotAlreadyFailed action does not change the result. Often used, for example, to perform a CallProcedure or PauseExecution action. No default actions. |
| OnPassTestAction | Occurs each time a PassTest, action is performed — even if the test result is currently Pass and the PassTest action does not change the result. Often used, for example, to perform a CallProcedure or PauseExecution action. No default actions. |
| OnPassTestResult | Default action DeclareExecutionIssue with a Severity of OK and with a default Message of: “OK: {message}” |
| OnPreExecutionCompleted | Occurs immediately before test case finishes executing. Often used, for example, to call a “cleanup” procedure. No default actions. |
| OnProcedureEnter | Occurs when a procedure or QuickCall starts execution. No default actions. Caution Do not add a CallProcedure action — this results in an infinite loop. name variable value: <procedureName> message variable value: “Entering procedure {name}” |
| Caution | Do not add a CallProcedure action — this results in an infinite loop. |
| OnProcedureExit | Occurs when a procedure or QuickCall exits execution. No default actions. Caution Do not add a CallProcedure action — this results in an infinite loop. name variable value: <procedureName> message variable value: “Exiting procedure {name}” |
| Caution | Do not add a CallProcedure action — this results in an infinite loop. |
| OnReportingTestbed | Default action DeclareExecutionIssue with a Severity of Information and with a default Message of: “Information: Testbed used in execution: {testbed URL}” |
| OnStackOverflow | Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Execution causes stack overflow” AbortExecution |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Execution causes stack overflow” |
|  | AbortExecution |
| OnStepTimeout | Occurs when step execution time exceeds the Timeout for this step property setting (see Step Properties section: Timing properties group). If the step is still executing, iTest aborts the step and does not process any analysis rules If the step is executing an analysis rule, then iTest finishes the current rule and then skips all other analysis rules Note iTest does not enforce timeout settings for call steps (for procedures or QuickCalls). Default actions DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Step has timed out” FailTest |
|  | If the step is still executing, iTest aborts the step and does not process any analysis rules |
|  | If the step is executing an analysis rule, then iTest finishes the current rule and then skips all other analysis rules |
| Note | iTest does not enforce timeout settings for call steps (for procedures or QuickCalls). |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: “Error: Step has timed out” |
|  | FailTest |
| OnTestResultChange | Occurs each time the test result changes. From Indeterminate to Pass, Fail or Abort From Pass to Fail or from Fail to Pass From Pass or Fail to Abort Often used, for example, to perform a CallProcedure action. The procedure must determine the current test result (Pass, Fail, Abort, or Indeterminate) using either a summarize step or the [info status] command. No default actions. |
|  | From Indeterminate to Pass, Fail or Abort |
|  | From Pass to Fail or from Fail to Pass |
|  | From Pass or Fail to Abort |
| OnThreadEnter | Occurs when a thread starts execution. Deferred steps are called after the first step in the thread has executed. If the thread step is a call step, deferred steps are part of “call” step. Otherwise, they are executed after the first step in the thread. If you use OnThreadEnter, then you should create a comment step for the thread (if the asynch step is not a call step) and nest the actual steps under the comment step. name variable value: <threadID> message variable value: “Entering thread {name}” No default actions. |
| OnThreadExit | Occurs when a thread exits execution. name variable value: <threadID> message variable value: “Exiting thread {name}” No default actions. |
| OnWarningTestResult | Occurs when test case pass/fail criteria are nt set for the test case Default action DeclareExecutionIssue with a Severity of Warning and with a default Message of “Warning: {message}” |
| Execution: Non-Session Actions |  |
| OnExecAssertionError | Not implemented |
| OnExecCallInvalidUri | Occurs when calling a procedure with invalid URI (typically the URI was manually typed by the user). Default actions: Abort step FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Call to an invalid test case uri: {0} |
|  | Abort step |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Call to an invalid test case uri: {0} |
| OnExecCallUnknownProcedureError | Occurs when calling a procedure that cannot be found by the specified URI Default actions: Abort step FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Call to unknown procedure: {0} |
|  | Abort step |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Call to unknown procedure: {0} |
| OnExecGoToLabelNotFound | Occurs when the goto label does not refer to a valid step label Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnExecIllegalActionError | Occurs when calling an action that is not valid for current state. For example, calling the break or continue action outside of a for loop. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Illegal action {action} : {explanation} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Illegal action {action} : {explanation} |
| OnExecInvalidCallArguments | Occurs when calling the procedure with invalid arguments Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error processing procedure call arguments: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error processing procedure call arguments: {0} |
| OnExecReadFileError | Occurs when attempting to read a file but cannot access the file. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error accessing file: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error accessing file: {0} |
| OnExecRunInvalidParameterFile | Occurs when attempting to read the parameter file but cannot access the file. For example, the file does not exist or the parameter file URI is invalid. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnExecRunInvalidTestReport | Not Implemented |
| OnExecRunInvalidTestbed | Occurs when the testbed is invalid. For example: the testbed file does not exist, the testbed file cannot be loaded, the testbed URI is not valid, and so on. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnExecRunInvalidTestcaseUri | Occurs when the test case is invalid. For example: the test case does not exist, the test case cannot be loaded, the test case URI is not valid, and so on. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnExecRunResultMatch | Occurs when the running result matches the expectation. Default actions: PassTestIfNotAlreadyFailed DeclareExecutionIssue with a default Message of: OK: Test case "{testcase}" run result was "{completion}" as expected. |
|  | PassTestIfNotAlreadyFailed |
|  | DeclareExecutionIssue with a default Message of: OK: Test case "{testcase}" run result was "{completion}" as expected. |
| OnExecRunResultMismatch | Occurs when the running result does not match the expectation Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unexpected result "{completion}" when executing test case "{testcase}". Expected "{expected}" |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unexpected result "{completion}" when executing test case "{testcase}". Expected "{expected}" |
| OnExecSummarizeError | Occurs when generating the running result summary has exceptions Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Fail to generate summary : {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Fail to generate summary : {0} |
| OnExecSyntaxError | Occurs when executing a step with invalid syntax. For example, a for statement with fewer than three arguments or the sleep time is not a valid number Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid syntax: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid syntax: {0} |
| OnExecUnknownActionError | Occurs when executing a step with invalid action that cannot be interpreted by the iTest kernel Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unknown action: {action} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unknown action: {action} |
| OnExecWriteError | Occurs when executing a write action that is not in the current thread Default actions: FailTest DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Write action is not supported in a new thread outside its own procedure context. Write will be ignored. |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Write action is not supported in a new thread outside its own procedure context. Write will be ignored. |
| OnExecWriteFileError | Occurs when exceptions occur while attempting to write a file. For example, the file URI is not valid or the file cannot be written Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error writing to file: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error writing to file: {0} |
| OnExecWriteFileSyntaxError | Occurs when executing a step with invalid write file syntax. For example, requires 2 arguments but only 1 is provided. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error writing to file: Syntax Error ({0}) |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error writing to file: Syntax Error ({0}) |
| OnInvalidPath | Occurs when executing commands yamlGet, yamlSet, yamlAdd, yamlDelete. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unexpected syntax in query segment: found unexpected end of stream at line. |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unexpected syntax in query segment: found unexpected end of stream at line. |
| OnInvalidSource | Occurs when executing commands with and invalid syntax of YAML source content is found. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: The 'Content' field contains invalid YAML: mapping values are not allowed here at line: x, column: x |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: The 'Content' field contains invalid YAML: mapping values are not allowed here at line: x, column: x |
| OnInvalidValue | Occurs when executing commands yamlSet, yamlAdd and YAML syntax error is encountered. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: The 'Value' field contains invalid YAML: found unexpected end of stream at line: 0, column: 3 |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: The 'Value' field contains invalid YAML: found unexpected end of stream at line: 0, column: 3 |
| OnNotFound | Occurs when executing commands and node is not found (index out of bounds, no matching key). Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: No document found of index 5 Error:No matches found in mapping node for key '4' |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: |
|  | Error: No document found of index 5 |
|  | Error:No matches found in mapping node for key '4' |
| Execution:Tcl Interpreter |  |
| OnTclInterpreterError | Occurs when Tcl fail to interpret actions such as set, get, or eval Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error using Tcl interpreter: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error using Tcl interpreter: {0} |
| OnTclInterpreterUnavailable | Occurs when the session executor tries to get the Tcl interpreter but failed. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: TCL interpreter unavailable: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: TCL interpreter unavailable: {0} |
| Processor |  |
| OnUnknownProcessorError | Occurs when executing a step with invalid write file syntax. For example when two arguments are required, but only one argument is provided. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error writing to file> Syntax Error ({0}) |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error writing to file> Syntax Error ({0}) |
| Response Mapping |  |
| OnApplicableMapsNotFound | Occurs when no applicable response map could be used during step post‑processing No default actions |
| OnMappingFail | Occurs when response mapping fails during step post‑processing. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
| OnMappingInfo | Occurs when response mapping passes. Provides standard information about the mapping process during step post‑processing. Default actions: DeclareExecutionIssue with a Severity of Information and with a default Message of: Information:{0} |
|  | DeclareExecutionIssue with a Severity of Information and with a default Message of: Information:{0} |
| OnMappingResponseEmpty | Occurs during step post‑processing if the response is empty. No default actions |
| OnMappingWarning | Occurs during step post-processing.when response mapping passes but with warning information about the mapping Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: {0} |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: {0} |
| OnResponseMapLibraryNotFound | Occurs when the response map library could not be found during step post‑processing. For example, the map library path is not valid. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
| OnResponseMapNotFound | Occurs when the response map is not available during step post‑processing Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
| OnResponseMappingIssue | Occurs for each response mapping issue during step post‑processing Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {message} |
| OnResponseMappingWarning | Occurs for each “warning” level response mapping issue during step post‑processing Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: {message} |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: {message} |
| Session Handling |  |
| OnOpenWithSessionAlreadyActive | Occurs when error happens when trying to execute an open step in an active session Default actions: AbortStep FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Session "{session}" is already opened and therefore action "{action}" is not allowed |
|  | AbortStep |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Session "{session}" is already opened and therefore action "{action}" is not allowed |
| OnSessionDeviceNotFound | Occurs when session device or session profile is not found. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Device "{0}" was not found in the testbed |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Device "{0}" was not found in the testbed |
| OnSessionIllegalAction | Occurs when session is in illegal state Default actions: FailTest DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Action "{action}" is not allowed when the session is in the current state. Step will be ignored. |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Action "{action}" is not allowed when the session is in the current state. Step will be ignored. |
| OnSessionNoTestbedAvailable | Occurs when the device URI cannot be used because there is no testbed available. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: A device URI cannot be used because there is no testbed available |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: A device URI cannot be used because there is no testbed available |
| OnSessionNotOpen | Occurs while attempting an action if the session is not open Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Session "{session}" is not open and therefore action "{action}" is not allowed |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Session "{session}" is not open and therefore action "{action}" is not allowed |
| OnSessionOpenFileMissing | Occurs when the file referenced in open step is missing. Default actions: AbortStep FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: File referenced in open step "{file}" is missing |
|  | AbortStep |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: File referenced in open step "{file}" is missing |
| OnSessionOpenInvalidProfile | Occurs when there are errors or warnings when reading session profile. Default actions: AbortStep FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Errors or warnings when reading session profile |
|  | AbortStep |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Errors or warnings when reading session profile |
| OnSessionOpenSyntaxError | Occurs when session open syntax is invalid. Default actions: AbortStep FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid syntax on open: {0} |
|  | AbortStep |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Invalid syntax on open: {0} |
| OnSessionProfileNotFound | Occurs when session profile is not found. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Session profile for device "{0}" was not found in the testbed |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Session profile for device "{0}" was not found in the testbed |
| OnSessionStepAfterSessionTerminated | Occurs when executing session steps after the session has terminated Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Session has already terminated. Remaining steps in this session will be skipped. |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Session has already terminated. Remaining steps in this session will be skipped. |
| OnSessionStepExecutorCreateFail | Occurs when errors happen while creating session step executor. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error creating step executor |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error creating step executor |
| OnSessionStepSubstitutionError | Occurs when command and variable substitution failed on the step. Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Command and variable substitution failed on the step: {0} |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: Command and variable substitution failed on the step: {0} |
| OnSessionUnknownApplication | Occurs when the application for the application name is unknown Default actions: AbortStep FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: The application "{appName}" is unknown |
|  | AbortStep |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: The application "{appName}" is unknown |
| OnUnsupportedSessionAction | Occurs when the action is not supported by this type of session. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Action "{action}" is not supported for this type of session |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Action "{action}" is not supported for this type of session |
| Terminal-Based Applications |  |
| OnProcessorNotFound | Occurs when executing the command step in HA mode but the processor can't be found. Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unable to find a processor in appropriate state: {0} |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unable to find a processor in appropriate state: {0} |
| OnPromptNotFoundTimeout | Occurs when executing a step but no prompt found and the wait time is exceeded. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Step timed out waiting for the prompt |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Step timed out waiting for the prompt |
| OnTclCreateInterpreterFail | Occurs when creating local TCL interpreter fails. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: {0} |
| OnTerminalConnClosedBeforeCommand | Occurs when the terminal connection has been lost before sending the command. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Connection was already closed before sending the command ''{0}'' |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Connection was already closed before sending the command ''{0}'' |
| OnTerminalConnClosedWaitingForResponse | Occurs when waiting for the step response but the terminal connection has been closed. No default actions |
| OnTerminalLoggingFailure | Occurs when logging the terminal session to file has IO exceptions Default actions: DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unable to log session data: {0} |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Unable to log session data: {0} |
| OnTerminalOpenConnectionFail | Occurs when opening the command session has exceptions. For example, the session parameter is invalid or the session has already opened Default actions: AbortExecution FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error attempting to open connection to server: {0} |
|  | AbortExecution |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error: Error attempting to open connection to server: {0} |
| OnWaitingForPromptTimeoutExtended | Occurs when waiting for the prompt in terminal session exceeds the max idle time. And indicate the user to increase the "Extra wait before alerting" property Default actions: DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: You waited for a prompt. Consider increasing the \"Extra wait before alerting\" property to {0} seconds. |
|  | DeclareExecutionIssue with a Severity of Warning and with a default Message of: Warning: You waited for a prompt. Consider increasing the \"Extra wait before alerting\" property to {0} seconds. |
| Tool |  |
| OnToolCloseSessionError | Occurs for the following cases: No open action is defined before close action Unexpected corrupted state Try to execute close action when the session is in NOT_STARTED or OPENING state Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Error closing session : {error} |
|  | No open action is defined before close action |
|  | Unexpected corrupted state |
|  | Try to execute close action when the session is in NOT_STARTED or OPENING state |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Error closing session : {error} |
| OnToolCreateSessionError | Occurs for the following cases: Session opening was interrupted Underlying Eclipse throws internal error when opening session Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Unable to create session : {error} |
|  | Session opening was interrupted |
|  | Underlying Eclipse throws internal error when opening session |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Unable to create session : {error} |
| OnToolError | Occurs when a test case step is executed before corresponding session is opened. Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: {error} |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: {error} |
| OnToolOpenSessionError | Occurs for the following cases: Session is already open Session is in the process of being closed by another thread Session is in the process of being opened by another thread Open method is not defined for this kind of profile or testbed or topology Default actions: FailTest DeclareExecutionIssue with a Severity of Error and with a default Message of: Unable to open session : {error} |
|  | Session is already open |
|  | Session is in the process of being closed by another thread |
|  | Session is in the process of being opened by another thread |
|  | Open method is not defined for this kind of profile or testbed or topology |
|  | FailTest |
|  | DeclareExecutionIssue with a Severity of Error and with a default Message of: Unable to open session : {error} |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
