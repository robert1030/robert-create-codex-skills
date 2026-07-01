---
{
  "chunk_id": "snmp_session_editor_concept__snmp_actions_that_are_captured_for_repla_8a6ee4a6a8f9a45a",
  "source_file": "topics/snmp_session_editor_concept.htm",
  "source_original_path": "topics/snmp_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "SNMP session window"
  ],
  "heading_path": [
    "SNMP session window",
    "SNMP session window",
    "SNMP actions that are captured for replay"
  ],
  "anchor": "1268355",
  "context_ids": [
    "snmp_session_editor_concept"
  ],
  "index_keywords": [
    "SNMP",
    "SNMP Console",
    "SNMP Traps view",
    "session window"
  ],
  "index_keyword_paths": [
    "SNMP > session window",
    "SNMP Console",
    "SNMP Traps view",
    "session windows > SNMP",
    "views > SNMP Console",
    "views > SNMP Traps view"
  ],
  "related_links": [],
  "images": [
    "topics/images/snmp.29.jpg",
    "topics/images/snmp.30.jpg"
  ],
  "content_hash": "8a6ee4a6a8f9a45a",
  "level": 2
}
---

# SNMP session window > SNMP session window > SNMP actions that are captured for replay

The following SNMP actions and their responses are captured while you browse and edit an SNMP variable.

To save the responses, save the captured items as a Capture report.

To replay captured items, drop selected items onto the SNMP editor.

| Get | Returns the OID and Value of a single MIB variable. iTest uses the Get PDU to get values for scalar variables. To get a value, double-click a scalar variable or } in the MIB tree. The get Action and the returned Value are captured. |
| --- | --- |
| GetTable | Returns all OIDs, Types, and Values of variables in the table. To use GetTable, double-click a MIB table in the MIB tree. iTest uses a Get PDU with multiple OIDs to read the values for each row. |
| Set | Sets the value of a single MIB variable. 1. To set a value, first get the value. 2. Select the value to make it editable, type the new value, and then press Enter (alternatively, click Set in the toolbar). iTest uses a Set PDU to set the value. In the example that appears below this table, we selected a read-write variable in a table, changed its value, and then set the value. |
| 1. | To set a value, first get the value. |
| 2. | Select the value to make it editable, type the new value, and then press Enter (alternatively, click Set in the toolbar). iTest uses a Set PDU to set the value. |
| Walk | Returns all of the data in a MIB under a specified root. For SNMPv2c or SNMPv3, when use GETBULK is enabled, iTest uses the GetBulk PDU to get values for container nodes For SNMPv1 or when use GETBULK is disabled, iTest uses the Get PDU for each OID. To use walk in an interactive session, double-click a container node |

![inline_icon](topics/images/snmp.29.jpg) <!-- image_chunk: img_1a681e0faa802112 -->

![inline_icon](topics/images/snmp.30.jpg) <!-- image_chunk: img_c1193c63b3979d96 -->
