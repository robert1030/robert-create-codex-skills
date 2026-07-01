---
{
  "chunk_id": "sp_properties_avalanche__port_provision_list_fd611950669cd19f",
  "source_file": "topics/sp_properties_avalanche.htm",
  "source_original_path": "topics/sp_properties_avalanche.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Session profile property settings for Spirent Avalanche sessions"
  ],
  "heading_path": [
    "Session profile property settings for Spirent Avalanche sessions",
    "Session profile property settings for Spirent Avalanche sessions",
    "Port Provision List"
  ],
  "anchor": "1218428",
  "context_ids": [
    "sp_properties_avalanche"
  ],
  "index_keywords": [
    "Avalanche sessions",
    "property settings",
    "sessions"
  ],
  "index_keyword_paths": [
    "Avalanche sessions",
    "Avalanche sessions > property settings",
    "Spirent Avalanche > sessions",
    "configuring > Avalanche sessions"
  ],
  "related_links": [
    "#1183022",
    "spirent_avalanche.12.htm#1289807",
    "inheritance_property.htm#1128847"
  ],
  "images": [
    "topics/images/spirent_avalanche_3.2.jpg"
  ],
  "content_hash": "fd611950669cd19f",
  "level": 2
}
---

# Session profile property settings for Spirent Avalanche sessions > Session profile property settings for Spirent Avalanche sessions > Port Provision List

The Port Provision List properties are used only for STC mode (device is not an appliance), as described in Advanced > License.

> **Tip:** Tip Be sure to review Specifying cards, slots, port groups, and ports/virtual ports before setting values.

To add a port definition:

1. 1

1. Check Include additional values from list to allow you to add a port definition. (For a discussion on inheriting settings from reference session profiles—the Include inherited values checkbox—see Property values: Inheriting settings.)

1. 2

1. Now, click to add a new port definition. Each new port definition appears in the list.

Specify the following properties.

| Card | Required. Specify the card as an integer number Default: 1 |
| --- | --- |
| Port | Required. Specify the port as an integer number Default: 1 |
| Virtual port | Optional. Specify the virtual port. When specified, the Virtual card of the Server and Client must match with two different virtual port in the Port Provision list. You must create 2 ports with different virtual port. Default: 1 |
| MAC address | Required. MAC address that is assigned to the port by the configuration script (config.tcl). Use x-xx-xx-xx-xx-x format. |
| Port speed | Required. Specify the port speed in Mbps. Default: 1000 |
| Duplex mode | Required. Specify either Full-duplex or Half-duplex Default: Full-duplex |
| Port media | Required. Specify either Copper or Fiber media. Default: Copper |
| Auto negotiation | Optional. Check the box to specify auto-negotiation. |
| Operational mode | Optional. Specify either func (Functional) or perf (Performance) mode. Note Use the Appliance Operational Mode property when Avalanche is running on an appliance The 10Gbps AP card has two 10Gbps ports. Functional mode: Both ports can be reserved and used. Each port will be assigned with three virtual ports (1,2,3 on each port, for example, : 192.168.1.1:2,1,1 through 192.168.1.1:2,1,3 and 192.168.1.1:2,2,1 through 192.168.1.1:2,2,3). This mode allows a tester to use both ports at maximum of 5Gbps port bandwidth per port. Performance mode: Only the first port is activated (for example: 192.168.1.1:2,1) with seven virtual ports. (192.168.1.1:2,1,1 through 192.168.1.1:2,1,7). With only the first port activated, it will achieve 10Gbps bandwidth on the port. Default: func |
| Note | Use the Appliance Operational Mode property when Avalanche is running on an appliance |

![inline_icon](topics/images/spirent_avalanche_3.2.jpg) <!-- image_chunk: img_04c8a729c257e2c6 -->
