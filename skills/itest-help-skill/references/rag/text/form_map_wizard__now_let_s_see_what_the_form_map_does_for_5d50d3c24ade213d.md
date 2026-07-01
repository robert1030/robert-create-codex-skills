---
{
  "chunk_id": "form_map_wizard__now_let_s_see_what_the_form_map_does_for_5d50d3c24ade213d",
  "source_file": "topics/form_map_wizard.htm",
  "source_original_path": "topics/form_map_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "Form Maps",
    "Creating form maps for use with GUI testing test applications"
  ],
  "heading_path": [
    "Creating form maps for use with GUI testing test applications",
    "Creating form maps for use with GUI testing test applications",
    "Now let's see what the form map does for the test case developer"
  ],
  "anchor": "1150019",
  "context_ids": [
    "form_map_wizard"
  ],
  "index_keywords": [
    "adding targets to",
    "adding to form maps",
    "creating",
    "form maps",
    "of HTML pages"
  ],
  "index_keyword_paths": [
    "XML maps > of HTML pages",
    "creating > form maps",
    "form maps > adding targets to",
    "form maps > creating",
    "maps > of HTML pages",
    "targets > adding to form maps"
  ],
  "related_links": [],
  "images": [
    "topics/images/forms_tcSteps_targetList.png",
    "topics/images/forms_test_case_steps.png",
    "topics/images/form_maps.14.jpg",
    "topics/images/forms_tc_results_advert.png"
  ],
  "content_hash": "5d50d3c24ade213d",
  "level": 2
}
---

# Creating form maps for use with GUI testing test applications > Creating form maps for use with GUI testing test applications > Now let's see what the form map does for the test case developer

In this example, the developer adds step 2 and specifies the following properties: The step click (Action) the link named link_Advcertising (Target) on the google_home page (the Context is the page where the target lives, as defined by the google_home form map).

Because we associated the google_home form map library with the session profile that started this session, the following actions take place:

- The Context list is populated with google_home (the form map for the home page — the Context box lists all form maps in the specified form map library).

- After the test case developer chooses the Context, the Target list is populated with the targets defined in the form map. Notice that the target named link_Advcertising appears at the top of the list, just as we specified.

So, here's what happens when the test case executes:

Step 1 opens the Google home page.

Step 2 clicks the Advertising link.

Step 3 closes the session.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/forms_tcSteps_targetList.png) <!-- image_chunk: img_a4ff60f7584d8ea9 -->

![screenshot](topics/images/forms_test_case_steps.png) <!-- image_chunk: img_3a6c375bde47e53b -->

![screenshot](topics/images/form_maps.14.jpg) <!-- image_chunk: img_75d2023fe87cc2fd -->

![screenshot](topics/images/forms_tc_results_advert.png) <!-- image_chunk: img_646cc0270dda710e -->
