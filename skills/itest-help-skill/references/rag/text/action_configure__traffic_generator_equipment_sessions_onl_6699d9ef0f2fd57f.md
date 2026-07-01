---
{
  "chunk_id": "action_configure__traffic_generator_equipment_sessions_onl_6699d9ef0f2fd57f",
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
    "Traffic Generator equipment sessions only"
  ],
  "anchor": "1107749",
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
  "content_hash": "6699d9ef0f2fd57f",
  "level": 2
}
---

# The ‘configure’ action: Configure a traffic generator device > The ‘configure’ action: Configure a traffic generator device > Traffic Generator equipment sessions only

If you use traffic generators in your topology, ensure that the device is correctly configured, and save the configuration so you can quickly replicate it when needed.

To enable a step in a iTest test case to configure a traffic generator to the desired state before performing the automated test, iTest submits the same saved configuration information to the device to configure it. Here's how it works:

1. During an interactive session with the device, you use a configuration get step to obtain the traffic generator device's configuration settings. The response to the configuration get is the text of the configuration file.

1. 2

1. Now, when you save a captured configuration get step into a test case step, iTest converts the configuration get step into a configure step. iTest places the text of the configuration file into the Description cell (actually, the value of the Command property) for the configure step.

1. 3

1. Then, when the test case executes, the configure step submits the configuration settings, thus configuring the device exactly as if you had configured it using its native management console.

The configure action is typically the first step after open in Ixia Traffic and Agilent N2X sessions.
