---
{
  "chunk_id": "new_response_map_wizard__creating_a_response_map_instructions_c710963ccd106c51",
  "source_file": "topics/new_response_map_wizard.htm",
  "source_original_path": "topics/new_response_map_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Creating a response map: Instructions"
  ],
  "heading_path": [
    "Creating a response map: Instructions",
    "Creating a response map: Instructions"
  ],
  "anchor": "1105632",
  "context_ids": [
    "new_response_map_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "response_mapping.03.htm#1157418",
    "filtering_responses.1.htm#",
    "rme_applicability_page.htm#1106102",
    "rme_overview_page.htm#1127952",
    "rme_samples_page.htm#1106000"
  ],
  "images": [
    "topics/images/rm_wiz_02_filename.png",
    "topics/images/rm_wiz_03.png"
  ],
  "content_hash": "c710963ccd106c51",
  "level": 1
}
---

# Creating a response map: Instructions > Creating a response map: Instructions

Watch a short video to learn nearly everything you need to know to get started on the Spirent Knowledge Base

> **Note:** Note One of the options for emulation feature is that you can specify an external source for the emulated response to a step or session. You specify the source response as a particular sample in a response map. If you plan to use a response map solely to supply an emulated response, then the process of creating the response map document is simpler. The following instructions include notes on options you can skip.

Use the Response Map wizard to create a response map based on the current command/response pair. When you create a response map, you create queries that can reliably return particular values from any response (based on the structured sample response that you used to create the response map).

1. When you manually submit a command or a test case executes a command, the command/response pair appears in the Response view. If a response looks “good” (that is, it is in the format that you expect other users will see), you can click Add Response Map to start the Response Map wizard.

Alternatively, in the Capture view, select the step that generates the response. Right-click and select New Response Map.

> **Note:** Note If you need to filter the response text to make it easier to map (as described in Step 1B: Optional: Filter the response if needed), follow the instructions in “Filtering Unwanted Text from Responses”.

1. 2

1. The New Response Map wizard starts and opens the Specify File Location page. On the Specify File Location page, you may modify the default values and specify the following properties for the new map. Click Next.

| Response map library | iTest discovers the project in which the new response map is created (based on the location of the test case), and selects the response_maps folder within that project (if it exists), as the default location. If you chose to add a new response map library, then specify a name for the new library. The new library will be added to the project and will appear in the Project Explorer. If you chose to add the map to an existing response map library, then select the library from the list. |
| --- | --- |
| File name | iTest proposes multiple response map file names based on the command sent (command that produced the response). The multiple file names are suggested as a drop-down list, from most specific to least specific tokens within the command (contents of the file). See the example screenshot above. Select a name from the drop-down list or specify a name for the new response map. We recommend that you select a name from the list, e.g., the default name, which is the text of the command (with underscore characters for spaces). |
| Sample | Populated with the new response text. |

1. 3

1. On the Response Map Applicability page, specify when the map can be used. The settings on this wizard page are identical to the Applicability page on the Response Map editor (as described in Response Map editor: Applicability page). Configure the settings and then click Next.

1. 4

1. Use the Automatic Response Map Generation page to have iTest use automatic response mappers to take a first try at generating a map.

Important If you plan to use the response map only to supply an emulated response, then uncheck this option and click Finish.

> **Note:** Note To use this feature, you must check out an Automatic Response Map Generation license. To check out a license, click Help > Configure iTest Licensing.

In many cases the process generates a map and queries that you can use immediately. In some cases, you may have to rename particular queries. In other cases, the map will not meet your needs and you will have to generate a map using the Response Map editor.

Important Because we are continuously improving the auto-mapping and auto-query technologies, the maps and queries that it generates will change from one release of iTest to the next. For this reason, do not use the auto-mapping feature in test case steps to generate queries. Instead, use auto-mapping to generate a map and then save the resulting response map. In the test case, use the response map instead of the auto-mapping feature to obtain data from the response. This ensures that the test case will continue to work as you upgrade iTest.

1. 5

1. Click Finish.

The wizard will auto check whether the session profile links to the response map library (project) specified and displays a dialog asking you to confirm whether you wish to configure the session profile to use the project specified as its response map library.

iTest places the new response map file into the specified response map library and then opens the response map file in the Response Map editor. You will now configure mappers and continue configuring the response map. See Response Map editor: Overview page.

If you plan to use the response map only to supply an emulated response, then you will not configure mappers. Open the editor’s Samples page and continue as described in Response Map editor: Samples page.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/rm_wiz_02_filename.png) <!-- image_chunk: img_85a3afca0ff8c998 -->

![screenshot](topics/images/rm_wiz_03.png) <!-- image_chunk: img_c044b04d132d9d54 -->
