---
{
  "chunk_id": "snmp_test_cases__snmp_action_types_that_are_captured_duri_677ca1a4ab8d7bb7",
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
    "SNMP action types that are captured during interactive SNMP sessions"
  ],
  "anchor": "1276707",
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
  "related_links": [],
  "images": [
    "topics/images/snmp.2.jpg"
  ],
  "content_hash": "677ca1a4ab8d7bb7",
  "level": 2
}
---

# Creating SNMP test case steps > Creating SNMP test case steps > SNMP action types that are captured during interactive SNMP sessions

The following SNMP actions and their responses are captured while you browse and edit an SNMP MIB.

| get | Returns the OID and Value of a single MIB variable. iTest uses the Get PDU to get values for scalar MIBs. The response contains the printable value of the specified MIB variable. For octet strings, the result is displayed as a string of 2-digit hex values for each byte, separated by colons (typical MAC address format). For strings, non-printable characters (except for CR/LF) are converted into printable versions using the standard iTest field replacement syntax (for example, [char CTRL-C] or [char \t]). |
| --- | --- |
| getTable | Returns all OIDs, Types, and Values of variables in the table. To use GetTable in an interactive session, double-click a MIB table in the MIB tree. iTest uses a Get PDU with multiple OIDs to read the values for each row. |
| set | Sets the value of a single MIB variable. iTest uses a Set PDU to set the value. In the example that appears below the table, we selected a read-write variable in a table, and can change and then set its value. |
| walk | Returns all of the data in a MIB under a specified root. For SNMPv2c or SNMPv3, when use GETBULK is enabled, iTest uses the GetBulk PDU to get values for container nodes For SNMPv1 or when use GETBULK is disabled, iTest uses the Get PDU for each OID. |

![screenshot](topics/images/snmp.2.jpg) <!-- image_chunk: img_ae0b2ec2908a075e -->
