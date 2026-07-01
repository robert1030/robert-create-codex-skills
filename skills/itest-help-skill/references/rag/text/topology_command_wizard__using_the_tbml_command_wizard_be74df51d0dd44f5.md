---
{
  "chunk_id": "topology_command_wizard__using_the_tbml_command_wizard_be74df51d0dd44f5",
  "source_file": "topics/topology_command_wizard.htm",
  "source_original_path": "topics/topology_command_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Overview: iTest Topologies",
    "TBML Command Wizard"
  ],
  "heading_path": [
    "TBML Command Wizard",
    "TBML Command Wizard",
    "Using the TBML command wizard"
  ],
  "anchor": "1427365",
  "context_ids": [
    "topology_command_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/tbml_wiz_tc_menu.png",
    "topics/images/tbml_wiz_subcommand_find_property.png",
    "topics/images/tbml_wiz_03_Id_res_or_link_select_res_link.png",
    "topics/images/tbml_wiz_04_select_property_vendor.png",
    "topics/images/tbml_wiz_05_finish_command_line.png"
  ],
  "content_hash": "be74df51d0dd44f5",
  "level": 2
}
---

# TBML Command Wizard > TBML Command Wizard > Using the TBML command wizard

After defining the topology, open the General page on the Test Case editor and specify the Local topology for the test case.

- For open steps in the test case, select any of the devices in the topology from a drop‑down list.

- Add a Step to access the Parameters defined in topology session profiles, for example on a new Step, right-click, select Insert > TBML Command option.

> **Note:** Note The following steps are included as an example and the options displayed on the TBML Command Wizard dialogs may vary depending on your selection.

- The TBML Commands Wizard opens. Select a Subcommand and click Next and select a property on the Find a Property dialog.

> **Note:** Note Selecting the option Find anything via TBML query displays the TBML command on the Finish dialog, which may be inserted in the Test Case Step.

- Click Next to Open the Identify the Resource or Link dialog and click Next and select the required resource or link.

> **Note:** Note The Next button appears only when you select a resource or link.

Click Next on the Select a resource dialog.

- Select a property on the dialog or select from a predefined properties or enter a property name. Click Next, define the Vendor and Default Property value if required, and click Next again.

- The TBML Command Wizard displays the command line generated based on your selection on the Finish dialog. Click Finish to insert the dialog into the Test Case Step.

You may execute this Test Case as all other test and see the result.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/tbml_wiz_tc_menu.png) <!-- image_chunk: img_482e3d486a84fcc4 -->

![screenshot](topics/images/tbml_wiz_subcommand_find_property.png) <!-- image_chunk: img_d63475628813e9fe -->

![screenshot](topics/images/tbml_wiz_03_Id_res_or_link_select_res_link.png) <!-- image_chunk: img_9abbd17a94c9328d -->

![screenshot](topics/images/tbml_wiz_04_select_property_vendor.png) <!-- image_chunk: img_2249e7edc9dca624 -->

![screenshot](topics/images/tbml_wiz_05_finish_command_line.png) <!-- image_chunk: img_5b5bf96a78538311 -->
