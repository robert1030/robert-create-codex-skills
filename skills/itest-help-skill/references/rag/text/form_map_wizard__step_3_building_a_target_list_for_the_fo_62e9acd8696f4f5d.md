---
{
  "chunk_id": "form_map_wizard__step_3_building_a_target_list_for_the_fo_62e9acd8696f4f5d",
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
    "Step 3: Building a target list for the form map"
  ],
  "anchor": "1149986",
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
  "related_links": [
    "fme_targets_page.htm#1099561"
  ],
  "images": [
    "topics/images/forms_target_generated_from_sample.png"
  ],
  "content_hash": "62e9acd8696f4f5d",
  "level": 2
}
---

# Creating form maps for use with GUI testing test applications > Creating form maps for use with GUI testing test applications > Step 3: Building a target list for the form map

At this point, iTest has identified targets on the page and auto-added them to the form map definition. Let's take a look at the Targets page.

1. We see that the wizard has identified many of the targets on the page and suggests a commonsense name for each target.

We scrolled through the list and selected the Advanced Search target.

> **Tip:** Tip To improve on the suggested target names, select the target in the list and then edit the name as needed.

1. 2

1. Here's the actual query that finds the target during execution. Because the target has a “friendly” Target name (or alias), the test case developer does not need to work with the query.

1. 3

1. See Form Map editor: Targets page for details on adding arguments.

> **Tip:** Tip The list of targets that test case developers see while adding (for example) a click or setText action, is the list as you see it on the Targets page. To make it easier for them to select targets, move the most popular targets to the top of the list. Let's use Move Up to move link_Advertising to the top of the list.

Save the form map by clicking Save in the main toolbar. (When you edit existing form maps, the dialog box allows you to save the form map into any form map library.)

![screenshot](topics/images/forms_target_generated_from_sample.png) <!-- image_chunk: img_b19ffdbf31f8a35e -->
