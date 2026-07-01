---
{
  "chunk_id": "action_configure__making_quick_changes_to_the_trafficgen_c_7bf75f8399d9eadb",
  "source_file": "topics/action_configure.htm",
  "source_original_path": "topics/action_configure.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Traffic generator actions",
    "The ‘configure’ action: Configure a traffic generator device"
  ],
  "heading_path": [
    "The ‘configure’ action: Configure a traffic generator device",
    "The ‘configure’ action: Configure a traffic generator device",
    "Making quick changes to the TrafficGen configuration settings"
  ],
  "anchor": "1085303",
  "context_ids": [
    "action_configure"
  ],
  "index_keywords": [
    "configure",
    "configure action"
  ],
  "index_keyword_paths": [
    "actions > configure",
    "configure action"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "7bf75f8399d9eadb",
  "level": 2
}
---

# The ‘configure’ action: Configure a traffic generator device > The ‘configure’ action: Configure a traffic generator device > Making quick changes to the TrafficGen configuration settings

You can edit traffic streams or other settings in the TrafficGen configuration script without having to set up the traffic generator again. Follow these steps:

1. Back up the test case so you can recover if the changes do not work as you expect.

1. 2

1. Copy the content of the TrafficGen.Configure step's Command cell into a text editor. In this example, we'll change the vlanId setting from 20 to 90.

Search for the text -vlan:

"vlan config -vlanID 20"

Change the setting as needed, for example:

"vlan config -vlanID 90"
