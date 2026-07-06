# Response Maps: Returning Data from Responses > Response Map editor: Samples page > Configuring a sample response > Buttons that manage the list of samples: > 第2段

- **Do not map this sample**：When you check the box, iTest will not generate the mapping logic that enables iTest to return data from responses. Default: unchecked
- **Content type**：Specify the format of the response data. This setting ensures that structured responses like XML and TL1 are correctly parsed. See Mapping TL1 responses. Default: text
- **Structured data**：This multi-line text box holds the structured part of the response that will be returned for an emulated step. When the sample was added from a response, this text box displays the structured data that was returned in the response. You can edit this text to check how queries will be mapped for different values (in the Query and Structure views) and to simulate different structured data for emulated responses. As with the Response text, you can modify the text to meet your needs.
- **Duration**：The Duration value shows how long it took for the step to execute (for the sample that was added from a response). You can use the Duration value to simulate the original execution speed when a step is emulated from this sample or modify the setting as needed. To emulate the response with this duration, you must check Enable emulation duration for the test case on the General page of the Test Case editor. Specify 0.0 to execute as fast as possible.

![](images/response_mapping.07.jpg) <!-- image_ref -->

1. 4 At this point, you have configured a sample response for the response map. Save the response map document by clicking Save in the main tool bar.
