---
{
  "chunk_id": "tce_step_properties_other_postprocessing__expected_response_980884a2f3f8d548",
  "source_file": "topics/tce_step_properties_other_postprocessing.htm",
  "source_original_path": "topics/tce_step_properties_other_postprocessing.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Steps page on the Test Case Editor",
    "Step Properties section: Other Post-processing properties group"
  ],
  "heading_path": [
    "Step Properties section: Other Post-processing properties group",
    "Step Properties section: Other Post-processing properties group",
    "Expected Response"
  ],
  "anchor": "1716159",
  "context_ids": [
    "tce_step_properties_other_postprocessing"
  ],
  "index_keywords": [
    "Other Postprocessing properties group",
    "Step Properties section",
    "specifying for steps"
  ],
  "index_keyword_paths": [
    "Other Postprocessing properties group > Step Properties section",
    "Step Properties section > Other Postprocessing properties group",
    "global analysis rules > specifying for steps",
    "response maps > specifying for steps"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "980884a2f3f8d548",
  "level": 2
}
---

# Step Properties section: Other Post-processing properties group > Step Properties section: Other Post-processing properties group > Expected Response

| Do not use a response map for this step | Do not use a response map for the step. Use this setting when the response might match a response map due to the map's Applicability setting and you do not want the response to map Note Even if you select this option, iTest will apply an auto-generated response map if you check the Use an auto-generated response map if no other map is available property. | Note | Even if you select this option, iTest will apply an auto-generated response map if you check the Use an auto-generated response map if no other map is available property. |
| --- | --- | --- | --- |
| Note | Even if you select this option, iTest will apply an auto-generated response map if you check the Use an auto-generated response map if no other map is available property. |  |  |
| Use the response map library configured for the session | Use the response map library specified in the session profile associated with the step. iTest searches the library and applies the first map with appropriate Applicability settings. |  |  |
| Use a response map file | Use the response map specified for the Response Map file property. If you check Use a response map file, then specify the file in the Response Map file text box. Once you specify a response map, the Response Map file label becomes a link. Click the link to edit or review the response map. |  |  |
| Find the response map by name in response map library configured for the session | Response map name When you select this option, iTest searches the response map library associated with the step’s session for the specified response map that you specify in the Response map name text box. iTest applies the first map with the correct name and with appropriate Applicability settings. If the response map is not found, then an OnResponseMapNotFound event occurs. Response map to use at design time Note If you do not use variables or field substitution in the Response map name value, then you cannot specify a value for Response map to use at design time If you use field replacement in the Response map name setting to determine the response map to use at runtime, then, at design time (while you are working in the Test Case editor), this property setting enables you to test how various response maps will work. When you specify a particular response map (from the associated response map library), iTest applies the map to the response. You can then preview the blue boxes in the Response view and the results of queries in the Queries view. During test case execution, the value specified for Response map name is used and the Response map to use at design time setting is ignored. | Note | If you do not use variables or field substitution in the Response map name value, then you cannot specify a value for Response map to use at design time |
| Note | If you do not use variables or field substitution in the Response map name value, then you cannot specify a value for Response map to use at design time |  |  |
| Use an auto-generated response map if no other map is available | Check the box to cause iTest to apply auto-mappers to the response in the case that no applicable map is found. Note Even if you select the Do not use a response map for this step option, iTest will apply an auto-generated response map if you check the Use an auto-generated response map if no other map is available property. | Note | Even if you select the Do not use a response map for this step option, iTest will apply an auto-generated response map if you check the Use an auto-generated response map if no other map is available property. |
| Note | Even if you select the Do not use a response map for this step option, iTest will apply an auto-generated response map if you check the Use an auto-generated response map if no other map is available property. |  |  |
