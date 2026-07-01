---
{
  "chunk_id": "form_maps_concept__overview_form_maps_69d40d2c8cce758b",
  "source_file": "topics/form_maps_concept.htm",
  "source_original_path": "topics/form_maps_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Form Maps",
    "Overview: Form Maps"
  ],
  "heading_path": [
    "Overview: Form Maps",
    "Overview: Form Maps"
  ],
  "anchor": "1269211",
  "context_ids": [
    "form_maps_concept"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "form maps > defined"
  ],
  "related_links": [
    "form_map_library_specify.htm#1419527"
  ],
  "images": [
    "topics/images/forms_target_dropDown.png",
    "topics/images/forms_big_picture.png"
  ],
  "content_hash": "69d40d2c8cce758b",
  "level": 1
}
---

# Overview: Form Maps > Overview: Form Maps

Form maps identify the targets (elements like buttons, links, and text boxes) on a graphical user interface (for example, a Web page (Selenium session), Swing form, Flex (Flash) application, and so on). While developing a test case, you will make use of the information in the map to perform an action on a target (for example, to click a particular button on a page).

You have the option to give the targets user-friendly names. Form maps are typically used by applications like Selenium and Swing that perform GUI test automation.

Form maps are stored in fffm files. Typically form maps are collected together for a particular GUI application into a project that is configured to be a form map library.

You use the iTest Form Map editor to edit form map files. In the Test Case editor, on a particular step, if the associated session has a form map library associated with it, the Test Case editor will populate the Context property for the step with a list of candidate form maps. If you select a form map, then the Target property for the step will provide a list of predefined targets from the form map.

> **Note:** Note To associate a form map library with the session profile or device for the session, you specify the form map library on the Misc page of the Session Profile editor or Testbed editor. Details appear in Associating a form map library with a session.

Once you define a form map, test case developers can create steps by selecting a target from a drop-down list. That is, for example, they'll be able to create a step that performs the click action on the Advanced Search link on the google_home page without knowing anything about the HTML of the web page, as shown here (the target name for the Advertising link is link_Advertising):

Typically, you create a form map for each HTML page that test case developers will access.

This example shows the relationship between the page on which testing occurs, the definition of the target in the Form Map editor, and the use of a target in a test case step:

- The GoogleHome form map defines the targets that appear on Google's home page.

- One of the targets on the page is a link named link_Advertising.

- The google_home form map is the context in which the click action takes place on the link_Advanced_Search target.

![screenshot](topics/images/forms_target_dropDown.png) <!-- image_chunk: img_3a75082933f933b3 -->

![screenshot](topics/images/forms_big_picture.png) <!-- image_chunk: img_19e1d1136df0dc11 -->
