---
{
  "chunk_id": "action_open__to_add_an_open_step_343c766d4349ced3",
  "source_file": "topics/action_open.htm",
  "source_original_path": "topics/action_open.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Session-control actions: open and close",
    "The open action: Start a session"
  ],
  "heading_path": [
    "The open action: Start a session",
    "The open action: Start a session",
    "To add an open step"
  ],
  "anchor": "1530391",
  "context_ids": [
    "action_open"
  ],
  "index_keywords": [
    "open",
    "open action",
    "starting",
    "starting a session"
  ],
  "index_keyword_paths": [
    "actions > open",
    "open action",
    "sessions > starting",
    "test cases > starting a session"
  ],
  "related_links": [
    "actions_sp_at_runtime.htm#1530423",
    "tce_step_properties_open_step.htm#1716227"
  ],
  "images": [],
  "content_hash": "343c766d4349ced3",
  "level": 2
}
---

# The open action: Start a session > The open action: Start a session > To add an open step



Fastest and Easiest way: Save a captured session

The fast and easy way to add an open step is to save a captured session into a test case. The fully-configured open step is added as the first step in the session. You do not need to do anything else.



Add the open step manually

Alternatively, when you add an open step by selecting open in the Action cell, you will specify additional values in the Session and Description cells, as described here:

1. Identify the session by its Session name:

When you add an open step, the Session name for the step is populated with the Session name property from the session profile (DUT6_Telnet in the example). If the session profile does not specify a value for the Session name property, then you must specify a unique name in the Session cell to identify the session that the open step starts. All steps in the session will use the same Session name. Session names can start with a letter, underscore, or number.

1. 2

1. Specify the session to open. Click in the Description cell to open the Select a Session Profile or Device dialog box. Specify one of the following methods for opening a session:

- Topology device: The box displays each device associated with the current test case (either a global topology or the local topology specified for the test case). Select the device from the list and then click OK.

The text in the Description cell will be a device URI of the format device:device_name. For example, device:telnet_DUT6 means: “From the global topology or the local topology specified for the test case (on the Test Case editor General page), fetch a device definition named telnet_DUT6.”

- Session profile or reference session profile: The box displays a tree of all projects in the current workspace. Navigate to the session profile and then click OK.

The resulting text in the Description cell will be the URI of the session profile that will start the session, for example, project://my_project/session_profiles/telnet_DUT6.ffsp

For instructions on configuring this value to be determined at runtime, see Determining the device or session profile (dynamically) at runtime.

- iTest default session type: This is a powerful option that you can use when generalizing a test case. You can use a parameter in the Session or Description cells for a step so that the session ID, device, or session profile can be determined at runtime. With this option, you must specify a Default session for the step or procedure. See Determining the device or session profile (dynamically) at runtime.

1. 3

1. For additional settings that you can configure and information on using parameters in open steps, see Step Properties section: Session Properties: Overriding device or session profile settings in the open step.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
