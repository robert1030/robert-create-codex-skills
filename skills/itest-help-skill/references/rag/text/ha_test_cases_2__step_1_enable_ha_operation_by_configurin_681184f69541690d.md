---
{
  "chunk_id": "ha_test_cases_2__step_1_enable_ha_operation_by_configurin_681184f69541690d",
  "source_file": "topics/ha_test_cases.2.htm",
  "source_original_path": "topics/ha_test_cases.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Testing HA devices: Detailed instructions"
  ],
  "heading_path": [
    "Testing HA devices: Detailed instructions",
    "Testing HA devices: Detailed instructions",
    "Step 1: Enable HA operation by configuring HA properties"
  ],
  "anchor": "1128980",
  "context_ids": [],
  "index_keywords": [
    "Additional connection information property",
    "Close action",
    "HA indication property",
    "HA mode",
    "HA prompts",
    "HA sessions",
    "HA test cases",
    "High Availability Mode property",
    "High Availability indication property",
    "Open action",
    "Verify State property",
    "creating",
    "defining",
    "prompt property setting"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA devices > Close action",
    "HA devices > Open action",
    "HA indication property",
    "HA master > defining",
    "HA mode",
    "HA prompts",
    "HA slave > defining",
    "HA test cases > creating",
    "High Availability Mode property",
    "High Availability indication property",
    "Master > prompt property setting",
    "Other > prompt property setting",
    "Slave > prompt property setting",
    "Verify State property",
    "creating > HA test cases",
    "prompts > HA sessions"
  ],
  "related_links": [],
  "images": [
    "topics/images/ha_test_cases.1.jpg"
  ],
  "content_hash": "681184f69541690d",
  "level": 2
}
---

# Testing HA devices: Detailed instructions > Testing HA devices: Detailed instructions > Step 1: Enable HA operation by configuring HA properties

> **Tip:** Tip We recommend that you configure all HA property settings in the testbed document to ensure that the settings are portable and maintainable across topologies or testbeds and test cases.

1. Specify the SSH or Telnet session type with HA nodes in either of the following locations:

- On the Testbed editor Devices page

- On the Session Profile editor Start page

1. 2

1. In the Telnet or SSH property group, specify the IP address and Port values for the master node. (You can specify a hostname instead of an IP address.)

> **Note:** Note The IP address and port values that you just added identify the node with index value 0. In a later step, you will specify the IP address and port values for nodes 1, 2, 3, ... n.

1. 3

1. If you are working in the Session Profile editor, click to open the Session Properties pages (the structured list of properties for a testbed device, session, or step).

1. 4

1. In the list, select Telnet (or SSH) > High Availability to open the High Availability property group and set the following HA properties:

| High Availability | Check the box to enable HA operation. (The default setting, unchecked, specifies normal, non‑HA operation.) |
| --- | --- |
| Additional connections | Specify the IP address and port pair for each redundant node (nodes other than the master node.). This information is used only by the open step for a session. The values in the list represent nodes 1, 2, 3, ... n. Use the following format, one node per line: <IP_or_hostname>:<portnumber> Important: Be sure not to enter the values for node 0 — the master node — those values are specified by the IP Address and Port properties. |

1. 5

1. In the list, select Terminal > Replay > Step Defaults > High Availability to open the High Availability property group and set the following HA properties:

| Verify status | If checked, then, during execution, before a command or getstate step (but not a break step), send an empty command to all nodes and then analyze the prompts to determine mastership. This setting ensures that the step sends the command to the correct node (in the case that mastership changed since the preceding step). The extra empty commands are not included in test reports. If unchecked, then use the most recent prompt from each node to determine which is master. Default: checked |
| --- | --- |
| Wait for master / slave status | This setting specifies the action to take for command steps if the intended recipient of the command (specified by the Send to property) does not respond. If the box is not checked (default) and the intended recipient is not found, then iTest generates an OnProcessorNotFound event. If the box is checked and the Verify status box is checked, then: Every several seconds, send an empty command to each node and then assess the prompts to determine whether the intended recipient is available. Once the intended recipient is available, continue execution by executing the command step. The extra empty commands are not included in the Execution view or in test reports. Default: unchecked |
| Send to | Identifies the node to which a command will be sent for command and break steps. Master: (default) Send the command to the master — node 0 (based on the prompt or as set by a preceding setmaster command). Slave: Send the command to the first node (in index order) that is not Master and not Other. Specific: This setting is typically used to log in to a particular node and to test HA redundancy operation. Specify the particular node to which the command should be sent using the Send to index property. |
| Send to index | This property is used only if you set the Send to property to Specific. Specify the processor index (0, 1, 2, 3, ... n) to send the command to. node 0 is the node specified by the IP Address and Port properties. Nodes 1, 2, 3, ... n are specified in the Other IP addresses property. |

![unknown](topics/images/ha_test_cases.1.jpg) <!-- image_chunk: img_2008250b9a56924e -->
