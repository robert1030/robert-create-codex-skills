# Procedures > Defining a procedure > Adding a procedure definition manually and modifying procedure properties (like arguments) > 第5段

1. Response: In the Procedure Properties> Inputs and Output tree, click Response. On the Response page, select Enable JSON Response to configure the sample JSON response. Use the text area to edit the JSON string, or use the JSON tree to generate the JSON string.

| 欄位1 | 欄位2 |
| --- | --- |
| Enable JSON Response | Select to enable JSON Response, which allows you to define the JSON response. When enabled, the response node in the Procedure Properties > Inputs and Outputs tree allows you to configure the JSON response for this procedure. When disabled, the sample JSON structure controls (raw text and nested/indented layout) is not available (grayed out). |

You can also get a sample data from response map, if you Enable JSON Response and the sample JSON response is empty (not defined yet). The first sample data from the response map file will be fetched and populated on the Response page.

You may define QuickCall procedures with JSON Response, and insert these calls in a Test Case. The insterted step populates the Response View with the JSON response from the called procedure (the Response View background is light grey before running a test case). It is not necessary to execute the test case to see the format of the response.

> **Note：** Note The response map should use JSON mapper for the data to be populated in the Response window.

![](images/proc_resp_struc_json.png) <!-- image_ref -->
