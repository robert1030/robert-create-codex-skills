---
{
  "chunk_id": "spe_misc_page__response_map_library_b8ff34e7fb208f97",
  "source_file": "topics/spe_misc_page.htm",
  "source_original_path": "topics/spe_misc_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Session Profile editor: Settings page"
  ],
  "heading_path": [
    "Session Profile editor: Settings page",
    "Session Profile editor: Settings page",
    "Response Map Library"
  ],
  "anchor": "1536988",
  "context_ids": [
    "spe_misc_page"
  ],
  "index_keywords": [
    "Misc page",
    "Session Profile editor",
    "specifying for session"
  ],
  "index_keyword_paths": [
    "Misc page > Session Profile editor",
    "Session Profile editor > Misc page",
    "form map libraries > specifying for session",
    "response map libraries > specifying for session"
  ],
  "related_links": [
    "response_map_concept.htm#",
    "rm_chaining.htm#1139163",
    "emulation.3.htm#1239888",
    "action_details_view.htm#1261910",
    "new_response_map_wizard.htm#1105632"
  ],
  "images": [],
  "content_hash": "b8ff34e7fb208f97",
  "level": 3
}
---

# Session Profile editor: Settings page > Session Profile editor: Settings page > Response Map Library

| Response Map Library | Optional. The response map library that you specify here is searched by any test case step in the session when the step attempts to determine which response map to apply to a response. Note When a session profile (ffsp file) is saved, if Response Map Library is blank, iTest automatically inserts the project address where the session profile is being saved. See “Response Maps: Returning Data from Responses” Tip The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. | Note | When a session profile (ffsp file) is saved, if Response Map Library is blank, iTest automatically inserts the project address where the session profile is being saved. | Tip | The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. |
| --- | --- | --- | --- | --- | --- |
| Note | When a session profile (ffsp file) is saved, if Response Map Library is blank, iTest automatically inserts the project address where the session profile is being saved. |  |  |  |  |
| Tip | The response map chaining feature enables you to specify that, during the mapping process, any response that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. |  |  |  |  |
| External source | Optional. Specify the response map or response map library that contains the sample response that a step should use to emulate the response. The use of this setting is fully described in Step 3: Activate emulation for particular steps or sessions and specify the source of the emulated response. By default, the source that you specify here is inherited by the External source property for the step. If a source is specified in the External source property for the step, the value in the step properties override the setting that you specify here, To enable the test case to dynamically determine the sample response at runtime, field replacements are supported in this field. Note Often, the External source might be the same as the Response Map Library for the session profile. The two properties are distinct because, during emulation, you might want to use different responses than you use during actual execution with response mapping (including error cases). Default: [empty] Tips The response map chaining feature enables you to specify that, during the search for the sample response to use for emulation, any step that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. On the Response view, clicking the Add This Sample to an Existing Response Map is a quick way to add a sample response for use in an emulated step. See Response view and Creating a response map: Instructions. | Note | Often, the External source might be the same as the Response Map Library for the session profile. The two properties are distinct because, during emulation, you might want to use different responses than you use during actual execution with response mapping (including error cases). | Tips | The response map chaining feature enables you to specify that, during the search for the sample response to use for emulation, any step that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. |
| Note | Often, the External source might be the same as the Response Map Library for the session profile. The two properties are distinct because, during emulation, you might want to use different responses than you use during actual execution with response mapping (including error cases). |  |  |  |  |
| Tips | The response map chaining feature enables you to specify that, during the search for the sample response to use for emulation, any step that does not find an applicable map in the specified response map library (or all applicable maps fail) should also check for applicable maps in one or more other libraries. See Making use of existing response map libraries: Chaining response maps. |  |  |  |  |
|  | On the Response view, clicking the Add This Sample to an Existing Response Map is a quick way to add a sample response for use in an emulated step. See Response view and Creating a response map: Instructions. |  |  |  |  |
