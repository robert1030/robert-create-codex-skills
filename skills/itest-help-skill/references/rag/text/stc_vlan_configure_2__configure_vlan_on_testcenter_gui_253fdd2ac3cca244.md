---
{
  "chunk_id": "stc_vlan_configure_2__configure_vlan_on_testcenter_gui_253fdd2ac3cca244",
  "source_file": "topics/stc_vlan_configure_2.htm",
  "source_original_path": "topics/stc_vlan_configure_2.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session window",
    "Spirent TestCenter Command reference"
  ],
  "heading_path": [
    "Spirent TestCenter Command reference",
    "Spirent TestCenter Command reference",
    "Configure VLAN on TestCenter Testcase step",
    "Configure VLAN on TestCenter GUI"
  ],
  "anchor": "1453544",
  "context_ids": [
    "STC_rest_command_reference",
    "stc_vlan_configure"
  ],
  "index_keywords": [
    "Spirent TestCenter REST",
    "command set"
  ],
  "index_keyword_paths": [
    "Spirent TestCenter REST > command set",
    "TestCenter > command set",
    "action reference > Spirent TestCenter REST",
    "command reference > Spirent TestCenter REST"
  ],
  "related_links": [
    "#1453674"
  ],
  "images": [
    "topics/images/STC_REST_VLAN.png",
    "topics/images/sct_rest_edit_VLAN_config.png"
  ],
  "content_hash": "253fdd2ac3cca244",
  "level": 3
}
---

# Spirent TestCenter Command reference > Spirent TestCenter Command reference > Configure VLAN on TestCenter Testcase step > Configure VLAN on TestCenter GUI

iTest TestCenter session supports configuring VLAN encapsulation for the device. The VLAN configured device can then send and receive packets with another device within the same VLAN ID (for testing quick traffic blasting within VLANs). VLAN encapsulation is supported:

- On devices and bound stream blocks

- In VLAN QinQ

- In REST and TCL-based session types

In addition to supporting configuring VLAN encapsulation settings on the iTest TestCenter GUI, iTest supports viewing and configuring VLAN settings on iTest TestCenter Rest console exactly as you do in the TestCenter. See Configure VLAN on TestCenter Console page iTest Spirent TestCenter REST session editor also allows you to view and configure VLAN settings. On the device page, the column, NumberOfVLAN (button) allows you to view and configure VLAN settings.

To configure VLAN encapsulation, select a device in the device table and configure VLAN Encapsulation for the selected device as follows.

- Encapsulation column: Select type of VLAN (Ethernet/VLAN, Ethernet/VLAN/IPv4, Ethernet/VLAN/IPv6) from the list.

- NumberOfVLAN column: Input number of VLANs to be configured and then click the button to view and configure VLAN settings.

VLAN Encapsulation displays in GUI and console after loading a VLAN configuration in the session. The NumberOfVLAN column displays in the session only when the device is configured with VLAN encapsulation. You can add VLAN encapsulation, configure VLAN encapsulation properties as required.

| Field Name | Type | Default Value | Boundary Value |
| --- | --- | --- | --- |
| VLAN Number | Integer | 1 | [ 1 ; 4095 ] |
| VLAN ID | Integer | 100 | [ 0 ; 4095 ] |
| Priority | Integer | 1 | [ 0 ; 7 ] |
| TPID(hex) | String | 1100 | [ 0 ; 9] & [ A ; F ] |

VLAN Modifier

| Field Name | Type | Default Value | Boundary Value |
| --- | --- | --- | --- |
| Modifies Type: Increment | Value | Integer | 100 |
| Step | Integer | 1 |  |
| Modifies Type: List | Value | Integer | - |
| Step | N/A (Disabled) | 1100 |  |

> **Note:** Note These values are not allowed in the above fields.

- Negative numeric (such as: -999)

- Rational numbers (such as: 9.9)

- Alphabet characters (such as: ABCabc)

- Special characters (such as: !@#$%^&*)

![screenshot](topics/images/STC_REST_VLAN.png) <!-- image_chunk: img_ea36d6f535a3c853 -->

![screenshot](topics/images/sct_rest_edit_VLAN_config.png) <!-- image_chunk: img_eb6ec7a2b2133ba5 -->
