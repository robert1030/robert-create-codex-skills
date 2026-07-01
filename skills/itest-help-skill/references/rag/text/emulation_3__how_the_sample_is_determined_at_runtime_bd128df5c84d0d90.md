---
{
  "chunk_id": "emulation_3__how_the_sample_is_determined_at_runtime_bd128df5c84d0d90",
  "source_file": "topics/emulation.3.htm",
  "source_original_path": "topics/emulation.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Emulating sessions in test case steps"
  ],
  "heading_path": [
    "Emulating sessions in test case steps",
    "Emulating sessions in test case steps",
    "How the sample is determined at runtime"
  ],
  "anchor": "1239945",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "rm_chaining.htm#1139163",
    "tl1.1.htm#1152885",
    "preferences_emulation.htm#1297129"
  ],
  "images": [
    "topics/images/emulation.4.jpg"
  ],
  "content_hash": "bd128df5c84d0d90",
  "level": 4
}
---

# Emulating sessions in test case steps > Emulating sessions in test case steps > How the sample is determined at runtime

| If the External source is a response map library, then: iTest first auto-selects a response map based on Applicability and Priority property settings. iTest then selects the particular response from within the response map based on the setting of the Sample name property. If no Sample name value is specified (the field is blank), then iTest uses the first sample response that appears in the appropriate response map. The response map chaining feature enables you to specify that, during the search for the sample response to use for emulation, any step that does not find an applicable map in the specified response map library should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. If iTest cannot identify an appropriate response map based on Applicability and Priority property settings, then iTest uses the step response (as specified by the Emulation > Step Response property group for the step). If the External source is a response map, then iTest selects the particular sample response from within the response map based on the setting of the Sample name property. If no Sample name value is specified, then iTest uses the first sample response that appears in the appropriate response map. For both the response map library and response map options: If the Sample name is specified, but no sample with that name is found, then iTest performs the following actions: Return no response for the step Generate an onEmulationSampleNameNotFound event Set the test case result to Fail If the External source property is empty and no setting is specified in the session profile or device associated with the step, then iTest uses the step response (as specified by the Emulation > Step Response property group for the step). |  | If the External source is a response map library, then: |  | iTest first auto-selects a response map based on Applicability and Priority property settings. iTest then selects the particular response from within the response map based on the setting of the Sample name property. If no Sample name value is specified (the field is blank), then iTest uses the first sample response that appears in the appropriate response map. |  | If iTest cannot identify an appropriate response map based on Applicability and Priority property settings, then iTest uses the step response (as specified by the Emulation > Step Response property group for the step). |  | If the External source is a response map, then iTest selects the particular sample response from within the response map based on the setting of the Sample name property. If no Sample name value is specified, then iTest uses the first sample response that appears in the appropriate response map. |  | For both the response map library and response map options: If the Sample name is specified, but no sample with that name is found, then iTest performs the following actions: |  | Return no response for the step |  | Generate an onEmulationSampleNameNotFound event |  | Set the test case result to Fail |  | If the External source property is empty and no setting is specified in the session profile or device associated with the step, then iTest uses the step response (as specified by the Emulation > Step Response property group for the step). |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | If the External source is a response map library, then: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | iTest first auto-selects a response map based on Applicability and Priority property settings. iTest then selects the particular response from within the response map based on the setting of the Sample name property. If no Sample name value is specified (the field is blank), then iTest uses the first sample response that appears in the appropriate response map. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | If iTest cannot identify an appropriate response map based on Applicability and Priority property settings, then iTest uses the step response (as specified by the Emulation > Step Response property group for the step). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | If the External source is a response map, then iTest selects the particular sample response from within the response map based on the setting of the Sample name property. If no Sample name value is specified, then iTest uses the first sample response that appears in the appropriate response map. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | For both the response map library and response map options: If the Sample name is specified, but no sample with that name is found, then iTest performs the following actions: |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Return no response for the step |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Generate an onEmulationSampleNameNotFound event |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | Set the test case result to Fail |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|  | If the External source property is empty and no setting is specified in the session profile or device associated with the step, then iTest uses the step response (as specified by the Emulation > Step Response property group for the step). |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |



Step 4: Configure the “step response” (the emulated response for the step)

iTest uses the response that you configure in this step in the following cases:

- The Use step response option is selected

- The Use external source option is selected, but the External source is not specified for the step or in the session profile or device associated with the step

- The Use external source option is selected and the External source is a response map library, but iTest cannot identify an appropriate response map based on Applicability and Priority property settings.

On the Emulation > Step Response page for the step, configure the following properties. Remember that iTest can perform runtime substitution for any properties marked by the field replacements indicator .

| Use Latest | Click the button to use the data that the session returned the last time the test case executed. This populates the Response, Structured data, and Duration properties and copies application-specific queries from the last response. The queries are not shown in the emulation properties and cannot be edited, but they will appear in the Query view after a step has been emulated |
| --- | --- |
| Reset | Click the button to clear the property settings.that define the emulated response: Response, Content type, Structured data, Duration and application-specific queries. |
| Response | This multi-line text box holds the text that will be returned for an emulated step. To populate the property with the text of the response returned during the most recent execution, click Use Latest. You can modify the text to meet your needs. For example, if the response text for the show version command for the last execution was “Version 3.4”, and you need to develop the test case for the next version before you get the device software update, you can change the response text to “Version 3.5”. |
| Content type | Specify the format of the response data. This setting ensures that structured responses like XML and TL1 are correctly parsed. Note For more information, see Configuring sessions and test case steps for TL1 devices. Default: text |
| Note | For more information, see Configuring sessions and test case steps for TL1 devices. |
| Structured data | This multi-line text box holds the structured part of the response that will be returned for an emulated step. To populate the property with the structured data returned during the most recent execution, click Use Latest. As with the Response text, you can modify the text to meet your needs Note iTest emulates only the structured data from the response; it does not emulate structured data that is appended by response mapping. The emulated/source element in the structured data identifies where the emulated response actually came from: The value “step” means the response came from the Step Response properties A value of “<source_uri>#<sample_name>” appears when the response came from a sample in a response map |
| Note | iTest emulates only the structured data from the response; it does not emulate structured data that is appended by response mapping. |
|  | The value “step” means the response came from the Step Response properties |
|  | A value of “<source_uri>#<sample_name>” appears when the response came from a sample in a response map |
| Duration | This property is used only if you check Enable emulation duration for the test case on the General page of the Test Case editor. This property specifies how long it will take to execute the emulated step. To populate the property with the time of the latest actual response, click Use Latest. You can modify the setting to change the duration of emulated steps. For example, you can speed up or slow down a reboot step. Specify 0.0 to execute as fast as possible. Default: 0.0 |



Step 5: Emulation is now active for the specified steps

When you execute the test case, the resulting test report indicates the steps that used emulated responses. See Setting preferences for emulation.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/emulation.4.jpg) <!-- image_chunk: img_fb574fefd7bf9e27 -->
