---
{
  "chunk_id": "stc_vlan_configure_2__configure_vlan_and_modify_vlan_header_on_a450c36f5669f269",
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
    "Configure VLAN and Modify VLAN header on TestCase Step"
  ],
  "anchor": "1459586",
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
  "related_links": [],
  "images": [
    "topics/images/stc_rest_set_vlan_encaptsulationIntC.png",
    "topics/images/spirent_testcenter_rest.05.jpg",
    "topics/images/stc_rest_VLAN-Header_basedOnIndex.png",
    "topics/images/stc_rest_VLAN-Header_additionalVLAN.png",
    "topics/images/stc_rest_VLAN-Header_deletedVLAN.png",
    "topics/images/stc_rest_VLAN_Non-defaultValuesApplied.png"
  ],
  "content_hash": "a450c36f5669f269",
  "level": 3
}
---

# Spirent TestCenter Command reference > Spirent TestCenter Command reference > Configure VLAN on TestCenter Testcase step > Configure VLAN and Modify VLAN header on TestCase Step

Open session type Spirent TestCenter. Select the ConfigureDevices Step properties, add VLAN encapsulation and configure properties as required.

Encapsulation and VLAN headers will not be changed by configureDevice step and they use default values (inherited values).

Add VLAN Headers and configure as required. Uncheck the Include inherited values to ensure that the encapsulation and VLAN headers are changed to use the custom values.

The following shows examples modified VLAN Headers.

> **Note:** Note Device VLAN number information is obtained from Spirent TestCenter GUI or from the Spirent TestCenter REST session started with configuration, or inspect XML configuration file. VLAN header size is a list of VLAN that created by you user in testcase.

1. The VLAN headers will be configured based on its index. For example, Device has 2 VLAN headers stacked: Ethernet → VLAN_100 → VLAN_200. If VLAN Header list size equal Device' VLAN number, VLAN header will be configured by it's index.

1. 2

1. If VLAN Header list size is greater than the Device VLAN number, an additional VLAN header will be added.

1. 3

1. If VLAN Header list size is less than Device VLAN number, VLAN header will be unstacked or deleted.

1. 4

1. VLAN non-default properties applied.

![screenshot](topics/images/stc_rest_set_vlan_encaptsulationIntC.png) <!-- image_chunk: img_efc484478d2b5e74 -->

![screenshot](topics/images/spirent_testcenter_rest.05.jpg) <!-- image_chunk: img_162780b694a00896 -->

![screenshot](topics/images/stc_rest_VLAN-Header_basedOnIndex.png) <!-- image_chunk: img_bfe45314654c7f78 -->

![screenshot](topics/images/stc_rest_VLAN-Header_additionalVLAN.png) <!-- image_chunk: img_a11d3240f79af621 -->

![screenshot](topics/images/stc_rest_VLAN-Header_deletedVLAN.png) <!-- image_chunk: img_f67e8672b2181dc2 -->

![screenshot](topics/images/stc_rest_VLAN_Non-defaultValuesApplied.png) <!-- image_chunk: img_b806f9e9732fa356 -->
