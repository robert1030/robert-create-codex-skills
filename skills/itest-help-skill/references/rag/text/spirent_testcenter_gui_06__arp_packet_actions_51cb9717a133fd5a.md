---
{
  "chunk_id": "spirent_testcenter_gui_06__arp_packet_actions_51cb9717a133fd5a",
  "source_file": "topics/spirent_testcenter_gui.06.htm",
  "source_original_path": "topics/spirent_testcenter_gui.06.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Device commands"
  ],
  "heading_path": [
    "Device commands",
    "Device commands",
    "ARP packet actions"
  ],
  "anchor": "1357163",
  "context_ids": [],
  "index_keywords": [
    "ARP packets",
    "ARP/ND state"
  ],
  "index_keyword_paths": [
    "ARP packets",
    "ARP/ND state"
  ],
  "related_links": [
    "tgen_cmds_testcenter.htm#1332853",
    "#1358089"
  ],
  "images": [],
  "content_hash": "51cb9717a133fd5a",
  "level": 2
}
---

# Device commands > Device commands > ARP packet actions

For all of the following ARP actions:

- Click the button that captures the action in the main toolbar to apply the action to all ports. Click the button on the “local” toolbar (on pages that enable you to select ports) to apply the action to the selected ports.

- You can specify the listOfPortIdentifiers argument values in any mix of formats separated by spaces. For example, slot:port mixed with sequential portIndex — 1:1 1:2 3 6

See To specify a list of port locations.

- If listOfPortIdentifiers is not specified, then the command is applied to all ports and returns data for all ports.

- The returned ARP/ND state is one of the following:

IDLE — Idle

WAITING — ARP/ND is in progress

SUCCESSFUL — All attempted ARP/NDs were resolved successfully

FAILURE — Some attempted ARP/NDs could not be resolved successfully

CONGESTED — Some attempted ARP/NDs are congested

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| startArpNd | [listOfPortIdentifiers] | Appears in main toolbar for all ports and local toolbar for Port page | Starts ARP/ND packets for the specified ports and returns the ARP/ND state. Example: startArpNd 1:1 1:2 3 |
| stopArpNd | [listOfPortIdentifiers] | Appears in main toolbar for all ports and local toolbar for Port page | Stops ARP/ND packets for the specified ports and returns the ARP/ND state. Returns data for all ports if listOfPortIdentifiers is not specified. Example: stopArpNd 2 3 1:1 |
| startArpNdOnAllStreamBlocks | [listOfPortIdentifiers] | Appears in local toolbar on All Stream Blocks and Traffic Generator pages | Starts ARP/ND packets on all stream blocks for the specified ports and returns the ARP/ND state. Returns data for all ports if listOfPortIdentifiers is not specified. Example: startArpNdOnAllStreamBlocks 1:3 1:4 |
| startArpNdOnAllDevices | [listOfPortIdentifiers] | Appears in local toolbar on All Devices and Devices pages | Starts ARP/ND packets on all devices for the specified ports and returns the ARP/ND state. Returns data for all ports if listOfPortIdentifiers is not specified. Example: startArpNdOnAllDevices 1:3 1:4 |
| showArpNdCache | [listOfPortIdentifiers] | Appears in main toolbar for all ports and local toolbar for Port page | Returns the ARP/ND cache. See Example response for showArpNdCache. Returns data for all ports if listOfPortIdentifiers is not specified. Example: showArpNdCache 1:3 1:4 |
