---
{
  "chunk_id": "emulation_3__emulating_sessions_in_test_case_steps_c21bcc3bd78f444c",
  "source_file": "topics/emulation.3.htm",
  "source_original_path": "topics/emulation.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Emulating sessions in test case steps"
  ],
  "heading_path": [
    "Emulating sessions in test case steps",
    "Emulating sessions in test case steps"
  ],
  "anchor": "1181970",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "emulation.5.htm#1164772",
    "new_response_map_wizard.htm#1105632",
    "response_mapping.07.htm#1538423",
    "#1239945",
    "rme_samples_page.htm#1564003",
    "rme_samples_page.htm#1106006"
  ],
  "images": [
    "topics/images/emulation.1.jpg",
    "topics/images/emulation.2.jpg"
  ],
  "content_hash": "c21bcc3bd78f444c",
  "level": 1
}
---

# Emulating sessions in test case steps > Emulating sessions in test case steps

> **Note:** Note These instructions describe the basic process of activating emulation. There are many powerful options for this feature — see Emulation: Quick instructions for ideas.



Step 1: (Optional, but typical) Execute the test case

You can generate responses to use when emulating the test in either or both of the following ways:

- Populate all responses for the test case by executing the test case in the normal way (without configuring emulation). This provides iTest with the default responses to use when emulating sessions. You can use these responses as they are or edit them to suit your needs.

Important If you will use a sample response from a response map or response map library to provide the emulated response, then you must first create the response map or add the sample response to an existing response map. See Creating a response map: Instructions and Adding a sample response to an existing response map.

- Create a response manually by typing or pasting it into the Response view for a step.



Step 2: Enable emulation for the test case

When emulation is enabled for the test case, then any step for which emulation is activated will receive an emulated response. Use either of the following methods to enable emulation for the test case:

- In the Test Case menu, select Emulator > Enable Emulation for the Test Case

- On the General page of the Test Case editor: In the Emulation section:

- Check Enable emulation for the test case

- Optional. Check Enable emulation duration for the test case to cause an emulated step to execute in the same amount of time as the actual step. Uncheck to execute emulated steps as fast as possible (default).



Step 3: Activate emulation for particular steps or sessions and specify the source of the emulated response

1. Select one step or multiple steps whose responses should be emulated.

- You can emulate any call or run step and any step in a session.

- To emulate all steps in a particular session, select the open step for the session and continue with these instructions.

1. 2

1. On the Step Properties > Emulation page, set the Emulate property to Always.

| Emulate | No: This is the default setting: Do not emulate the response; send the command to the session in the typical way. IMPORTANT If the open step for a session is emulated, then all steps in the session are emulated, including steps for which Emulate is set to No. Always: Rather than interact with the session, return the response that is specified by the Emulation Source property group. | IMPORTANT | If the open step for a session is emulated, then all steps in the session are emulated, including steps for which Emulate is set to No. |
| --- | --- | --- | --- |
| IMPORTANT | If the open step for a session is emulated, then all steps in the session are emulated, including steps for which Emulate is set to No. |  |  |

1. 3

1. Specify the Emulation Source (where to get the emulated response):

- Use step response causes iTest to use a response that had been returned for an earlier execution of the step (or an edited version of such a response). If you select this option, then click the Edit the step response link to configure the step response. Skip to How the sample is determined at runtime for further instructions.

- Use external source causes iTest to emulate the response using a sample response from a response map or response map library. (To use a sample response as the emulated response, you must have previously configured the sample while defining a response map, as described in Step 3 in Configuring a sample response.)

By default, the External source property is blank and the setting is inherited from the External source setting in the session profile or device associated with the step. To override that setting, you specify a setting here, in the External source property for the step. Follow these steps to specify the external source:

Click Select. In the Specify External source dialog box, specify one of the following:

- The Use the source configured for the session setting is the default when the Use external source check box is not checked. That is, use the setting that is inherited from the External source setting in the session profile or device associated with the step. If no source is specified there, then use the response that is specified by the Emulation > Step Response property group for the step.

- Default: Use the specified response map library (specify either a library project or the catalog for a library)

- Use the specified response map

> **Tip:** Tip We recommend that you specify a response map library rather than an particular response map as the External source. In this way, rather than requiring you to specify a response map for each step in a test case, you can take advantage of iTest’s ability to auto-select the appropriate map based on Applicability and Priority property settings.

1. Set the Sample name property: If you use the External source property to specify a response map library or response map as the external source for the emulated response, then use the Sample name property to specify the name of the response sample to use (that is, the sample from within the appropriate response map).

To enable the test case to dynamically determine the sample response at runtime, field replacements are supported in this field.

![screenshot](topics/images/emulation.1.jpg) <!-- image_chunk: img_1626104a5f579ee4 -->

![screenshot](topics/images/emulation.2.jpg) <!-- image_chunk: img_9db22ef54082ebdb -->
