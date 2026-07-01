---
{
  "chunk_id": "rm_chaining__requirements_for_response_map_chaining_6619ecdce88f2e1c",
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
    "Requirements for response map chaining"
  ],
  "anchor": "1105780",
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
  "images": [
    "topics/images/response_mapping_2.2.jpg",
    "topics/images/response_mapping.3.jpg"
  ],
  "content_hash": "6619ecdce88f2e1c",
  "level": 2
}
---

# Making use of existing response map libraries: Chaining response maps > Making use of existing response map libraries: Chaining response maps > Requirements for response map chaining

A response map is chained only when the following conditions are true:

- The step specifies a particular response map library. That is, for the step in the Test Case editor, the Other Post-processing > Expected Response property is set to Use the response map library configured for the session

- For the session profile associated with the step's session, a response map library is specified on the Session Profile editor's Misc page.

- The response map is applicable to the step. That is, on the Response Map editor's Applicability page, the settings result in the map being applicable to the step

- The response map library project is eligible to be chained. Response map chaining uses iTest Project Natures to determine whether a project is eligible to be chained. Only projects with the following natures can be chained:

- iTest Default Project nature (For this nature, the icon for the project includes the iTest logo )

- iTest Response Map Library nature (For this nature, the icon for the project includes an ‘R’ logo )

![unknown](topics/images/response_mapping_2.2.jpg) <!-- image_chunk: img_6bfb9d2c163c23c3 -->

![unknown](topics/images/response_mapping.3.jpg) <!-- image_chunk: img_3cf60f9eb412e625 -->
