---
{
  "chunk_id": "quickcalls_form_maps__about_form_maps_in_quickcall_fa543aa6e94000b6",
  "source_file": "topics/quickcalls_form_maps.htm",
  "source_original_path": "topics/quickcalls_form_maps.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Adding a test case step that executes a QuickCall",
    "About Form Maps in QuickCall"
  ],
  "heading_path": [
    "About Form Maps in QuickCall",
    "About Form Maps in QuickCall"
  ],
  "anchor": "1471731",
  "context_ids": [
    "quickcalls_form_maps"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "form_maps_concept.htm#",
    "quickcalls_new_quickcall_library_wizard.htm#1292200"
  ],
  "images": [
    "topics/images/QC_forms_step.png",
    "topics/images/qc_forms_formMap_viaSession.png",
    "topics/images/qc_forms_changeSession_emptyCOntext_and_Target.png"
  ],
  "content_hash": "fa543aa6e94000b6",
  "level": 1
}
---

# About Form Maps in QuickCall > About Form Maps in QuickCall

> **Note:** Note Prerequisite: Ensure that the form map exists in your system See Chapter , “Form Maps” for creating Form Maps.

Create QuickCall as described Defining a QuickCall and define Form Map. The Form Map displays in both the test case and QuickCall as shown below.

> **Note:** Note Define session profile in the Procedure Properties > General > Default session.

Use Form Maps from the library and specify custom targets for different actions in the test case using iTest Selenium session.

When creating a new test case or QuickCall library using $session or [session] associated with the same session profile (e.g., default session), the steps find the appropriate Form Maps in step properties.

If you change the default session in Procedure Properties > General > Default session, then the Context and Target will be empty.

> **Note:** Note If you select the same Session Profile again, the Context and Target fields are populated appropriately.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/QC_forms_step.png) <!-- image_chunk: img_b051a62edc494abe -->

![screenshot](topics/images/qc_forms_formMap_viaSession.png) <!-- image_chunk: img_54afc285c8c1e8a6 -->

![screenshot](topics/images/qc_forms_changeSession_emptyCOntext_and_Target.png) <!-- image_chunk: img_e12d195de17482d1 -->
