---
{
  "chunk_id": "rme_samples_page__buttons_that_manage_the_list_of_samples_6b71001ddbd82b08",
  "source_file": "topics/rme_samples_page.htm",
  "source_original_path": "topics/rme_samples_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Samples page"
  ],
  "heading_path": [
    "Response Map editor: Samples page",
    "Response Map editor: Samples page",
    "Configuring a sample response",
    "Buttons that manage the list of samples:"
  ],
  "anchor": "1106020",
  "context_ids": [
    "rme_samples_page"
  ],
  "index_keywords": [
    "Response Map editor",
    "Samples page",
    "adding sample responses to",
    "adding to response maps",
    "sample responses to response maps"
  ],
  "index_keyword_paths": [
    "Response Map editor > Samples page",
    "Samples page > Response Map editor",
    "adding > sample responses to response maps",
    "response maps > adding sample responses to",
    "sample responses > adding to response maps"
  ],
  "related_links": [
    "mapping_tl1.htm#1153843"
  ],
  "images": [
    "topics/images/response_mapping.06.jpg"
  ],
  "content_hash": "6b71001ddbd82b08",
  "level": 4
}
---

# Response Map editor: Samples page > Response Map editor: Samples page > Configuring a sample response > Buttons that manage the list of samples:

| Add | Add a new response sample. You can use this button to add the first sample or to provide additional samples for an existing response map. |
| --- | --- |
| Remove | Delete the selected response sample. Any maps that you created using the deleted sample are still in place and will be used when mapping a response. |
| Move Up / Move Down | Use these buttons to organize the samples in the list. Note This feature is purely for your convenience and has no bearing on mapping (all response maps are applied to each response regardless of the order of the samples in the list). |
| Note | This feature is purely for your convenience and has no bearing on mapping (all response maps are applied to each response regardless of the order of the samples in the list). |
| Cut | Cut the selected response sample definition (typically for pasting into a different response map document). |

1. 3

1. If you intend to use the sample as an emulated response, then open the Advanced section (click the arrow) and set the following properties. If not, then skip this step.

| Do not map this sample | When you check the box, iTest will not generate the mapping logic that enables iTest to return data from responses. If you edit a sample response so that it will no longer map a response (for example to provide a different emulated response) then you can check the box to prevent a mapping error when the response map is validated. If you intend to use the sample only as the source for emulated steps, then check the box to avoid mapping errors during execution. Default: unchecked |  | If you edit a sample response so that it will no longer map a response (for example to provide a different emulated response) then you can check the box to prevent a mapping error when the response map is validated. |  | If you intend to use the sample only as the source for emulated steps, then check the box to avoid mapping errors during execution. |
| --- | --- | --- | --- | --- | --- |
|  | If you edit a sample response so that it will no longer map a response (for example to provide a different emulated response) then you can check the box to prevent a mapping error when the response map is validated. |  |  |  |  |
|  | If you intend to use the sample only as the source for emulated steps, then check the box to avoid mapping errors during execution. |  |  |  |  |
| Content type | Specify the format of the response data. This setting ensures that structured responses like XML and TL1 are correctly parsed. See Mapping TL1 responses. Default: text |  |  |  |  |
| Structured data | This multi-line text box holds the structured part of the response that will be returned for an emulated step. When the sample was added from a response, this text box displays the structured data that was returned in the response. You can edit this text to check how queries will be mapped for different values (in the Query and Structure views) and to simulate different structured data for emulated responses. If you created the response map using the wizard, iTest uses the structured data from the response that you used when starting the wizard. If you added the sample by clicking Add in the Response Map editor, then this property is blank and you must provide a value. As with the Response text, you can modify the text to meet your needs. Note During execution, iTest emulates only structured data from the response; it does not emulate structured data that is appended by response mapping. |  | If you created the response map using the wizard, iTest uses the structured data from the response that you used when starting the wizard. |  | If you added the sample by clicking Add in the Response Map editor, then this property is blank and you must provide a value. |
|  | If you created the response map using the wizard, iTest uses the structured data from the response that you used when starting the wizard. |  |  |  |  |
|  | If you added the sample by clicking Add in the Response Map editor, then this property is blank and you must provide a value. |  |  |  |  |
| Note | During execution, iTest emulates only structured data from the response; it does not emulate structured data that is appended by response mapping. |  |  |  |  |
| Duration | The Duration value shows how long it took for the step to execute (for the sample that was added from a response). You can use the Duration value to simulate the original execution speed when a step is emulated from this sample or modify the setting as needed. To emulate the response with this duration, you must check Enable emulation duration for the test case on the General page of the Test Case editor. Specify 0.0 to execute as fast as possible. |  |  |  |  |

1. 4

1. At this point, you have configured a sample response for the response map. Save the response map document by clicking Save in the main tool bar.

![unknown](topics/images/response_mapping.06.jpg) <!-- image_chunk: img_991bb117374b0b5b -->
