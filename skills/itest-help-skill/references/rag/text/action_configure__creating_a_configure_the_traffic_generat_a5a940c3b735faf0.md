---
{
  "chunk_id": "action_configure__creating_a_configure_the_traffic_generat_a5a940c3b735faf0",
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
    "Creating a “Configure the traffic generator” step in a test case"
  ],
  "anchor": "1154592",
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
  "content_hash": "a5a940c3b735faf0",
  "level": 2
}
---

# The ‘configure’ action: Configure a traffic generator device > The ‘configure’ action: Configure a traffic generator device > Creating a “Configure the traffic generator” step in a test case

1. Using the traffic generator device's native interface, configure it in the usual way.

1. 2

1. Now, during an interactive iTest session with the device, submit a configuration get command. The configuration setting text is returned as the response to the configuration get command.

1. 3

1. Save the captured configuration get step as a step in the test case. You can save any number of captured steps or the whole captured session, as long as the selection includes the configuration get step.

1. 4

1. iTest converts the configuration get step into a configure step.
