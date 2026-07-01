---
{
  "chunk_id": "snmp_test_cases__snmp_action_types_that_you_can_perform_i_61d9ab1ff5b8f696",
  "source_file": "topics/snmp_test_cases.htm",
  "source_original_path": "topics/snmp_test_cases.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "Creating SNMP test case steps"
  ],
  "heading_path": [
    "Creating SNMP test case steps",
    "Creating SNMP test case steps",
    "SNMP action types that you can perform in test case steps"
  ],
  "anchor": "1276806",
  "context_ids": [
    "snmp_test_cases"
  ],
  "index_keywords": [
    "SNMP",
    "SNMP action",
    "adding SNMP",
    "creating"
  ],
  "index_keyword_paths": [
    "SNMP test cases > creating",
    "get > SNMP action",
    "getNext > SNMP action",
    "getTable > SNMP action",
    "listTraps > SNMP action",
    "set > SNMP action",
    "steps > adding SNMP",
    "test cases > SNMP",
    "waitForTrap > SNMP action",
    "walk > SNMP action"
  ],
  "related_links": [
    "session_profile_properties_snmp.htm#1582552",
    "session_profile_properties_snmp.htm#1268025",
    "snmp_traps_view.htm#1284761"
  ],
  "images": [
    "topics/images/snmp.3.jpg"
  ],
  "content_hash": "61d9ab1ff5b8f696",
  "level": 2
}
---

# Creating SNMP test case steps > Creating SNMP test case steps > SNMP action types that you can perform in test case steps

| get | Returns the OID and Value of a single MIB variable. iTest uses the Get PDU to get values for scalar MIBs. The response contains the printable value of the specified MIB variable. For octet strings, the result is displayed as a string of 2-digit hex values for each byte, separated by colons (typical MAC address format). For strings, non-printable characters (except for CR/LF) are converted into printable versions using the standard iTest field replacement syntax (for example, [char CTRL-C] or [char \t]). |
| --- | --- |
| getNext | Returns the value of the single MIB variable that follows the specified OID. The structured data includes the OID value and Velocity iTest generates queries for OID and RAW_OID. Tip To use getNext in a loop for returning multiple values, the device's agent must implement a variable (the “next” variable) for loop control. If you intend to get values for all variables in a MIB, use walk instead. Example getNext in a While loop In this example, we obtain the OID and use it to control a while loop around the getNext: |
| Tip | To use getNext in a loop for returning multiple values, the device's agent must implement a variable (the “next” variable) for loop control. If you intend to get values for all variables in a MIB, use walk instead. |
| getTable | Returns all OIDs, Types, and Values of variables in the table. iTest uses a Get PDU with multiple OIDs to read the values for each row. |
| set | Sets the value of a single MIB variable. iTest uses a Set PDU to set the value. Note You have the option to configure iTest to execute a get action before executing any set action. See the session profile setting described in SNMP MIB Browser > Step Defaults > Set. |
| Note | You have the option to configure iTest to execute a get action before executing any set action. See the session profile setting described in SNMP MIB Browser > Step Defaults > Set. |
| walk | Returns all of the data in a MIB under a specified root. Returns the following statistics: Number of nodes visited Deepest node level visited Number of errors happened (error codes from API) For SNMPv2c or SNMPv3, when Use GETBULK is enabled, iTest uses the GetBulk PDU to get values for container nodes. For SNMPv1 or when Use GETBULK is disabled, iTest uses the Get PDU for each OID. Tip To enable tests to exit infinite loops caused by self-referencing OIDs, consider setting the Stop on cycle property for the session. See SNMP MIB Browser > Step Defaults > Walk. |
|  | Number of nodes visited |
|  | Deepest node level visited |
|  | Number of errors happened (error codes from API) |
| Tip | To enable tests to exit infinite loops caused by self-referencing OIDs, consider setting the Stop on cycle property for the session. See SNMP MIB Browser > Step Defaults > Walk. |
| listTraps | If a port is specified for the SNMP port property in the session associated with the step, then listTraps lists all traps that have been received on the port since executing the first SNMP step (or previous listTraps calls, depending on the Clear Traps After List property setting as described in a moment). Traps on the ports specified in preferences are not included in the response. If no port is specified for the SNMP port property, then traps on the ports specified in preferences are included in the response. If no port is specified for the SNMP port property and no port is specified in preferences, then all traps are included in the response. listTraps steps do not send commands to the device. Depending on the Clear Traps After List property setting in the session profile, iTest either leaves the queue unchanged or clears it after listTraps steps. The response body contains an XML document listing the following elements for each trap: Timestamp Trap objects See SNMP Traps view Note The listTraps and waitForTrap commands filter on the the IP address specified in the session's open step. Both these commands list and wait for traps whose source IP address is the one defined in the open step of the session. In test case steps, it is recommend to use waitForTrap before using listTraps. In SNMP sesions, Step properties > SNMP MIB Browser > Traps, the following settings are recommneded: Enable Override existing settings for same trap port bound when the session starts Specify NIC address value as 127.0.0.1 for listening to SNMP traps.. If NIC address for SNMP session is not specified, iTest chooses any of the available interfaces. If Override existing settings for same trap port bound when the session starts is not enabled, and if a test case has been executed, iTest uses the listening port configured in the first test for subsequent tests. That is, the trap port configured in the subsequent tests with a different NIC will still use the previously configured port. To clean up the SNMP values manually, go to Preferences> Spirent >Session Types>SNMP and press Apply. This will remove all session 'open' step defined listening ports. |
|  | If a port is specified for the SNMP port property in the session associated with the step, then listTraps lists all traps that have been received on the port since executing the first SNMP step (or previous listTraps calls, depending on the Clear Traps After List property setting as described in a moment). Traps on the ports specified in preferences are not included in the response. |
|  | If no port is specified for the SNMP port property, then traps on the ports specified in preferences are included in the response. |
|  | If no port is specified for the SNMP port property and no port is specified in preferences, then all traps are included in the response. |
|  | Timestamp |
|  | Trap objects |
| Note | The listTraps and waitForTrap commands filter on the the IP address specified in the session's open step. Both these commands list and wait for traps whose source IP address is the one defined in the open step of the session. |
|  | Enable Override existing settings for same trap port bound when the session starts |
|  | Specify NIC address value as 127.0.0.1 for listening to SNMP traps.. |
| waitForTrap | If a port is specified for the SNMP port property in the session associated with the step, then waitForTrap causes execution to wait until a trap is received for the port. Traps on the ports specified in preferences are not considered. If no port is specified for the SNMP port property, then waitForTrap causes execution to wait until a trap is received for one of the ports specified in preferences If no port is specified for the SNMP port property and no port is specified in preferences, then waitForTrap causes execution to wait until a trap is received for any port. waitForTrap has two modes: If the step specifies an OID in the Command property, then waitForTrap waits for the specified trap (or any trap with the specified prefix). If the step does not specify an OID in the Command property, then waitForTrap waits for any trap. Depending on the Use received traps for wait property setting in the session profile, the step executes as follows: If Use received traps for wait is selected (default), then iTest first checks the receive queue. If a trap is in the queue (either any trap or a trap for the specified MIB, as appropriate), execution proceeds. If the queue is empty, then execution proceeds upon receipt of a trap (either any trap or a trap for the specified MIB, as appropriate). If Use received traps for wait is not selected, then iTest ignores the queue and awaits a trap (either any trap or a trap for the specified MIB, as appropriate). If non-matching traps are received, they are added to the queue. See the description of the Use received traps for wait property. Depending on the Clear after listing property setting, iTest leaves the queue unchanged or clears it after waitForTrap steps. Response The response contains an XML document listing the following elements for the trap that ended the wait: Timestamp Trap objects The response will always include one trap unless the step times out or is canceled. If the step times out or is canceled, then the response is an XML document listing no traps. See SNMP Traps view. |
|  | If a port is specified for the SNMP port property in the session associated with the step, then waitForTrap causes execution to wait until a trap is received for the port. Traps on the ports specified in preferences are not considered. |
|  | If no port is specified for the SNMP port property, then waitForTrap causes execution to wait until a trap is received for one of the ports specified in preferences |
|  | If no port is specified for the SNMP port property and no port is specified in preferences, then waitForTrap causes execution to wait until a trap is received for any port. |
|  | If the step specifies an OID in the Command property, then waitForTrap waits for the specified trap (or any trap with the specified prefix). |
|  | If the step does not specify an OID in the Command property, then waitForTrap waits for any trap. |
|  | Timestamp |
|  | Trap objects |

![screenshot](topics/images/snmp.3.jpg) <!-- image_chunk: img_25599b379992ee51 -->
