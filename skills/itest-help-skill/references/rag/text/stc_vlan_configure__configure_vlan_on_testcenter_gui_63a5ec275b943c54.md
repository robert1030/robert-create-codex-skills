---
{
  "chunk_id": "stc_vlan_configure__configure_vlan_on_testcenter_gui_63a5ec275b943c54",
  "source_file": "topics/stc_vlan_configure.htm",
  "source_original_path": "topics/stc_vlan_configure.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Configure VLAN on TestCenter GUI"
  ],
  "heading_path": [
    "Configure VLAN on TestCenter GUI",
    "Configure VLAN on TestCenter GUI"
  ],
  "anchor": "1429820",
  "context_ids": [
    "stc_vlan_configure"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1426404",
    "#1426434"
  ],
  "images": [
    "topics/images/vlan_config.png",
    "topics/images/vlan_editvlan_config_no_of_vlan.png"
  ],
  "content_hash": "63a5ec275b943c54",
  "level": 1
}
---

# Configure VLAN on TestCenter GUI > Configure VLAN on TestCenter GUI

iTest TestCenter session supports configuring VLAN encapsulation for the device. The VLAN configured device can then send and receive packets with another device within the same VLAN ID (for testing quick traffic blasting within VLANs). VLAN encapsulation is supported:

- On devices and bound stream blocks

- In VLAN QinQ

- In REST and TCL-based session types

In addition to supporting configuring VLAN encapsulation settings on the iTest TestCenter GUI, iTest supports viewing and configuring VLAN settings on iTest TestCenter console exactly as you do in the TestCenter. See Configure VLAN on TestCenter Console page and Configure VLAN on TestCenter Testcase step. iTest Spirent TestCenter session editor also allows you to view and configure VLAN settings. On the device page, the column, NumberOfVLAN (button) allows you to view and configure VLAN settings.

To configure VLAN encapsulation, select a device in the device table and configure VLAN Encapsulation for the selected device as follows.

- Encapsulation column: Select type of VLAN (Ethernet/VLAN, Ethernet/VLAN/IPv4, Ethernet/VLAN/IPv6) from the list.

- NumberOfVLAN column: Input number of VLANs to be configured and then click the button to view and configure VLAN settings.

VLAN Encapsulation displays in GUI and console after loading a VLAN configuration in the session. The NumberOfVLAN column displays in the session only when the device is configured with VLAN encapsulation. You can add VLAN encapsulation, configure VLAN encalsulation properties as required.

| Field Name | Type | Default Value | Boundary Value |
| --- | --- | --- | --- |
| VLANs per Port | Integer | 1 | [ 1 ; 4095 ] |
| VLAN ID | Integer | - | [ 0 ; 4095 ] |
| Priority | Integer | 7 | [ 0 ; 7 ] |
| TPID(hex) | String | 8100 | [ 0 ; 9] & [ A ; F ] |

VLAN Modifier

| Field Name | Type | Default Value | Boundary Value |
| --- | --- | --- | --- |
| Modifies Type: Increment | Value | Integer | 100 |
| Step | Integer | - |  |
| Modifies Type: List | Value | Integer | - |
| Step | N/A (Disabled) | 8100 |  |

> **Note:** Note These values are not allowed in the above fields.

- Negative numeric (such as: -999)

- Rational numbers (such as: 9.9)

- Alphabet characters (such as: ABCabc)

- Special characters (such as: !@#$%^&*)

![screenshot](topics/images/vlan_config.png) <!-- image_chunk: img_c4bffca575ca3f78 -->

![screenshot](topics/images/vlan_editvlan_config_no_of_vlan.png) <!-- image_chunk: img_3b6a714d580a6b8d -->
