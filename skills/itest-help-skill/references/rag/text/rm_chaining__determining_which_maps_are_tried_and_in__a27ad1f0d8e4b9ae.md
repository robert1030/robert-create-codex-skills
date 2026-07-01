---
{
  "chunk_id": "rm_chaining__determining_which_maps_are_tried_and_in__a27ad1f0d8e4b9ae",
  "source_file": "topics/rm_chaining.htm",
  "source_original_path": "topics/rm_chaining.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Making use of existing response map libraries: Chaining response maps"
  ],
  "heading_path": [
    "Making use of existing response map libraries: Chaining response maps",
    "Making use of existing response map libraries: Chaining response maps",
    "Determining which maps are tried and in what order"
  ],
  "anchor": "1105797",
  "context_ids": [
    "rm_chaining"
  ],
  "index_keywords": [
    "chaining",
    "chaining response maps",
    "reusing"
  ],
  "index_keyword_paths": [
    "chaining response maps",
    "response map libraries > chaining",
    "response map libraries > reusing",
    "response maps > chaining"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "a27ad1f0d8e4b9ae",
  "level": 2
}
---

# Making use of existing response map libraries: Chaining response maps > Making use of existing response map libraries: Chaining response maps > Determining which maps are tried and in what order

The Structure view includes a mappingInfo section that lists the response maps that are applied during execution.

- Response map library projects that are selected in the primary library’s Project References page appear in the projects section.

- Projects appear in the projects list in the order in which they appear on the Project References page. If a referenced project itself has referenced projects, then they are added to the list before adding the next project. For example, if A references B and C, and B references D and E, then the list will be ordered A B D E C.

- In the candidateMaps list, for each project in order, response maps are sorted in priority order (as specified on the Response Map editor's Applicability page)

In this example mappingInfo section in the Response view, while the R5000_router_response_maps library was selected, it contained no applicable maps and the S100_switch_response_maps library was found to include two applicable maps. The show_version map has higher priority than show_version2.

<structure>

<mappingInfo>

<projects>

<project>my_project</project>

<project>R5000_router_response_maps</project>

<project>S100_switch_response_maps</project>

</projects>

<candidateMaps>

<map>project://my_project/show_version.ffrm</map>

<map>project://S100_switch_response_maps/show_version.ffrm</map>

<map>project://S100_switch_response_maps/show_version2.ffrm</map>

</candidateMaps>

<mapped URI="project://my_project/show_version.ffrm">

...

</mapped>

</structure>

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
