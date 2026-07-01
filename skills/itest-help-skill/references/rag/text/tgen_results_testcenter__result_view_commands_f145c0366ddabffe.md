---
{
  "chunk_id": "tgen_results_testcenter__result_view_commands_f145c0366ddabffe",
  "source_file": "topics/tgen_results_testcenter.htm",
  "source_original_path": "topics/tgen_results_testcenter.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Results commands"
  ],
  "heading_path": [
    "Results commands",
    "Results commands",
    "Result View commands"
  ],
  "anchor": "1379481",
  "context_ids": [
    "stc_results_commands",
    "tgen_results_testcenter"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_4.01.jpg",
    "topics/images/spirent_testcenter_gui_4.02.jpg",
    "topics/images/spirent_testcenter_gui_4.03.jpg",
    "topics/images/spirent_testcenter_gui_4.04.jpg",
    "topics/images/spirent_testcenter_gui_4.05.jpg",
    "topics/images/spirent_testcenter_gui_4.06.jpg",
    "topics/images/spirent_testcenter_gui_4.07.jpg",
    "topics/images/spirent_testcenter_gui_4.08.jpg",
    "topics/images/spirent_testcenter_gui_3.09.jpg",
    "topics/images/spirent_testcenter_gui_3.10.jpg",
    "topics/images/spirent_testcenter_gui_4.11.jpg",
    "topics/images/spirent_testcenter_gui_4.12.jpg",
    "topics/images/spirent_testcenter_gui_4.13.jpg",
    "topics/images/spirent_testcenter_gui_4.14.jpg"
  ],
  "content_hash": "f145c0366ddabffe",
  "level": 2
}
---

# Results commands > Results commands > Result View commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| clearResults | [resultType] | resultType | Clears statistics for specified result type. If not specified, statistics for all view types are cleared. Example: clearResults DetailedStreamResults |
| saveResults | fileURI resultType [tabname] [pagenumber] | resultType tabName | Saves the statistics for the specified result type to an XML file. Example: saveResults file:/C:/temp/basic_counters.xml BasicTrafficResults "Basic Counters" 1 |
| showResults | fileURI resultType [tabname] [pagenumber] | resultType tabName | Shows the results for the specified result type. The result type must be subscribed. Example: showResults DetailedStreamResults "Basic Counters" 1 |
| showSubscriptionViews | — None — |  | Lists all available result types and subcribed status. |
| subscribeView | resultTypeList | resultTypes | Add the specified result types to the subscribed views. Example: subscribeView BasicTrafficResults DetailedStreamResults |
| unsubscribeView | resultTypeList | resultTypes | Remove specified result types from subscribed views. Example: unsubscribeView BasicTrafficResults |

![unknown](topics/images/spirent_testcenter_gui_4.01.jpg) <!-- image_chunk: img_7c7bf2ea5390f23e -->

![unknown](topics/images/spirent_testcenter_gui_4.02.jpg) <!-- image_chunk: img_72d711a71a175e27 -->

![unknown](topics/images/spirent_testcenter_gui_4.03.jpg) <!-- image_chunk: img_a87d5d2bdeba7bcf -->

![unknown](topics/images/spirent_testcenter_gui_4.04.jpg) <!-- image_chunk: img_94bdb917f8c05e80 -->

![unknown](topics/images/spirent_testcenter_gui_4.05.jpg) <!-- image_chunk: img_db83243cdae7550b -->

![unknown](topics/images/spirent_testcenter_gui_4.06.jpg) <!-- image_chunk: img_4cb78e5f91153d4a -->

![unknown](topics/images/spirent_testcenter_gui_4.07.jpg) <!-- image_chunk: img_dc6e8a9aba177963 -->

![unknown](topics/images/spirent_testcenter_gui_4.08.jpg) <!-- image_chunk: img_b6aa3aa400022ae0 -->

![unknown](topics/images/spirent_testcenter_gui_3.09.jpg) <!-- image_chunk: img_01368f1de3ed6d43 -->

![unknown](topics/images/spirent_testcenter_gui_3.10.jpg) <!-- image_chunk: img_5fe40d01abd2d624 -->

![unknown](topics/images/spirent_testcenter_gui_4.11.jpg) <!-- image_chunk: img_867e82b7abb29611 -->

![unknown](topics/images/spirent_testcenter_gui_4.12.jpg) <!-- image_chunk: img_d9c5a561c066b46c -->

![unknown](topics/images/spirent_testcenter_gui_4.13.jpg) <!-- image_chunk: img_4605b94a99bf562b -->

![unknown](topics/images/spirent_testcenter_gui_4.14.jpg) <!-- image_chunk: img_aa8f12b7af04bd24 -->
