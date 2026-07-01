---
{
  "chunk_id": "form_map_wizard__step_2_creating_the_form_map_d58cb61763d93b6f",
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
    "Step 2: Creating the form map"
  ],
  "anchor": "1149944",
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
    "topics/images/form_maps.04.jpg",
    "topics/images/form_maps.05.jpg",
    "topics/images/form_maps.06.jpg",
    "topics/images/form_maps.07.jpg"
  ],
  "content_hash": "d58cb61763d93b6f",
  "level": 2
}
---

# Creating form maps for use with GUI testing test applications > Creating form maps for use with GUI testing test applications > Step 2: Creating the form map

You might typically create a form map for each page that test case developers will work on. In this example, we'll create a form map for the Google home page.

1. In the Response view, click New Form Map .

1. 2

1. iTest opens the New Form Map wizard to ask you whether to save the form map into a new Form Map library or an existing library. (If this is the first form map to be created, then you'll first create a Form Map library and then add the new form map to it. More about Form Map libraries later.)

1. 3

1. In the Form map library field, we type the name for a new library. Form map libraries are iTest projects that hold form maps (more on libraries later).

Because we expect to save the form maps for all of the google pages in this library, we’ll name it google_form_maps.

The page displays the XML map of the page (the DOM) in the Sample box and suggests the default name new_form_map. Because the form map represents the home page, we’ll call it google_home (form maps use the .fffm filename extension).

When you're ready, click Next.

1. 4

1. Now, the wizard offers to auto-generate targets based on the DOM.

In the test case that we plan to write, we'll add a step that clicks the Advanced Search link on the home page, so let's allow the wizard to generate the targets on the page (hopefully, the Advanced Search link target will be included in the set of targets that the wizard generates.).

In addition, let's allow the wizard to associate the Form Map library that we just created with the session profile. This ensures that, whenever we start a session using the session profile, iTest knows to look into the new Form Map library to find the appropriate form map for a step.

1. 5

1. Click Finish to save the new form map. iTest opens the Form Map editor to the Samples page and creates a sample.

iTest populates the XML Data Viewer field with the XML description of the home page that we got with the snapshot. This is where we'll find the targets that appear on the page.

> **Tip:** Tip The sample name is unimportant unless you expect more than one format for this web page (for example, when the page displays one set of configuration options or another, depending on the device model).

![screenshot](topics/images/form_maps.04.jpg) <!-- image_chunk: img_cf115a8433739a59 -->

![screenshot](topics/images/form_maps.05.jpg) <!-- image_chunk: img_0e040e2d0c719bf6 -->

![screenshot](topics/images/form_maps.06.jpg) <!-- image_chunk: img_f59716f70e2bf2c9 -->

![screenshot](topics/images/form_maps.07.jpg) <!-- image_chunk: img_ea07e45b54ed6b07 -->
