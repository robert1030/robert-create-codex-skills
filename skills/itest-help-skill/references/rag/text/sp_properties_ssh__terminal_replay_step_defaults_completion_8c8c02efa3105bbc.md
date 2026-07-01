---
{
  "chunk_id": "sp_properties_ssh__terminal_replay_step_defaults_completion_8c8c02efa3105bbc",
  "source_file": "topics/sp_properties_ssh.htm",
  "source_original_path": "topics/sp_properties_ssh.htm",
  "toc_path": [
    "iTest Online Help",
    "SSH Sessions",
    "Session profile property settings for SSH sessions"
  ],
  "heading_path": [
    "Session profile property settings for SSH sessions",
    "Session profile property settings for SSH sessions",
    "Terminal > Replay > Step Defaults > Completion"
  ],
  "anchor": "1260667",
  "context_ids": [
    "sp_properties_ssh"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions",
    "configuring",
    "session profile property settings for"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions > configuring",
    "SSH sessions > session profile property settings for",
    "configuring > SSH sessions",
    "session profile property settings > SSH sessions"
  ],
  "related_links": [
    "tl1.1.htm#1152885",
    "prompts.1.htm#1100299",
    "prompts.5.htm#1272830"
  ],
  "images": [],
  "content_hash": "8c8c02efa3105bbc",
  "level": 2
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > Terminal > Replay > Step Defaults > Completion

You use Completion settings to define when the execution of a step should be considered complete. The determination of when a step is complete is protocol-specific. Defining “completion” for a step is important because:

- Some steps cannot start until the preceding step is complete.

- For some steps, you might have defined analysis logic to examine the response to determine whether the step succeeded. Analysis of the response can begin only when the step is complete.

> **Note:** Note In addition, all protocols support the notion of a timeout on a step. If the timeout is exceeded, then the step terminates and execution continues even if the protocol thinks that the work is not yet done. Other than the timeout case, it is up to the protocol to determine when the step is complete.

For CLI protocols, you can specify any of several conditions to define when the step is complete, for example, the existence of certain text in the response or the time elapsed after sending the command. The default setting of the Completion criteria property is that the step is complete when:

The session channel is idle for the time specified by the Idle channel interval property

and

1. The last line of the response matches one of the prompt definitions specified for the session profile or device.

| Idle channel interval | This setting helps in cases where you do not know what response to expect and can use a specified idle time (for example, 100 milliseconds) or when you expect no response whatsoever, for example, when talking to a terminal server. Default: 100 |
| --- | --- |
| Wait for first character before starting idle | Some devices do not respond to a typed command immediately. This setting enables you to ignore the idle time after the last character of the command is echoed and the first character of the actual response is returned. This way, the delay is not misinterpreted as idle channel time for the purpose of determining completion. Default: True |
| Completion criteria | Prompt matches AND device has not sent data during the Idle channel interval: The step is complete when the channel is idle for the time specified by the Idle channel interval property and last line of the response matches one of the prompt definitions specified for the session profile. Prompt matches OR device has not sent data during the Idle channel interval: The step is complete when the channel is idle for the time specified by the Idle channel interval property or the last line of the response matches one of the prompt definitions specified for the session profile. The following processing order occurs: The step is completed once one of the defined prompts is received. If none of the defined prompts is received or no prompt is defined, then the system waits for the specified Idle channel interval time (during which the device sends no response data) and then completes the step. Device has not sent data during the Idle channel interval: The step is complete when the channel is idle for the time specified by the Idle channel interval property. Completion time has expired: The step is complete when the time specified by the Completion time property has elapsed. If you specify Completion time has expired, then the Idle channel interval property setting is ignored. TL1 End of Message: For session profiles that will support TL1 devices, see Configuring sessions and test case steps for TL1 devices Default:Prompt matches AND device has not sent data during the Idle channel interval |
| Completion time | Specify the time interval that must elapse for the step to be complete. To apply this setting during execution, the Completion citeria property must be set to Completion time has expired. |
| Where to find prompt | Specify where the prompt in a response normally appears. Last line Last non-empty line The Any line setting is a special case that you can use to detect a change in state for an ongoing response. For example, you can detect a port's connection status based on whether the first character of a ping response is u or s. Be sure to use wildcard characters as needed in the Content property. Default: Last line |
| Command to send when a step is cancelled | Specify the characters to send when the user cancels step execution. Default: \03 (Ctrl-C) |
| Capture only the last screen of response text | Use this property when you expect a very large response, but the only data of interest appears at the end of the response text. Check the box to cause iTest to save only the last screen of response text. Default: Unchecked |
| Unknown Prompts During Automated Execution For an overview on how iTest recognizes prompts, see Overview: Prompts in iTest. For instructions on defining prompts, see Editing prompt definitions. |  |
| Expected maximum Idle channel interval | The time to wait for a prompt during automated execution. When this time is reached, iTest displays a Learn this prompt link in the status bar. If the user clicks the link, then iTest opens the Learn Prompt dialog box to enable you to add the prompt definition. If the user chooses not to click the link and the waiting period expires, then iTest raises an execution issue that it failed to find a prompt and sets the test result to Fail. The test case then continues. Default: 5 |
|  | If the user clicks the link, then iTest opens the Learn Prompt dialog box to enable you to add the prompt definition. |
|  | If the user chooses not to click the link and the waiting period expires, then iTest raises an execution issue that it failed to find a prompt and sets the test result to Fail. The test case then continues. |
| Extra wait before alerting user | Additional time to wait for a prompt during automated execution after the Expected maximum Idle channel interval time has been exceeded. When (Expected maximum Idle channel interval + Extra wait before alerting user) has elapsed, then: A countdown timer in the status bar starts to count down the Time for user to respond time period. iTest displays a Keep waiting link in the status bar. If the user clicks the Keep waiting link, then iTest waits for an additional (Expected maximum Idle channel interval + Extra wait before alerting user) has elapsed period. If the waiting period expires, then iTest raises an execution issue that it failed to find a prompt and sets the test result to Fail. The test case then continues Default: 15 |
|  | A countdown timer in the status bar starts to count down the Time for user to respond time period. |
|  | iTest displays a Keep waiting link in the status bar. |
|  | If the user clicks the Keep waiting link, then iTest waits for an additional (Expected maximum Idle channel interval + Extra wait before alerting user) has elapsed period. |
|  | If the waiting period expires, then iTest raises an execution issue that it failed to find a prompt and sets the test result to Fail. The test case then continues |
| Time for user to respond | Specify the amount of time in seconds to wait for the user to respond once the status bar displays the Waiting for prompt timer. Default: 30 |
