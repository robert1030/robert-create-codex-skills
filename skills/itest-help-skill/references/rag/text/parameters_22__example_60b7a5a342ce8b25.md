---
{
  "chunk_id": "parameters_22__example_60b7a5a342ce8b25",
  "source_file": "topics/parameters.22.htm",
  "source_original_path": "topics/parameters.22.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Merging parameter definitions from multiple sources",
    "Previewing the runtime parameter settings while you develop a test case"
  ],
  "heading_path": [
    "Previewing the runtime parameter settings while you develop a test case",
    "Previewing the runtime parameter settings while you develop a test case",
    "Example"
  ],
  "anchor": "1329446",
  "context_ids": [],
  "index_keywords": [
    "previewing runtime",
    "previewing runtime parameter"
  ],
  "index_keyword_paths": [
    "parameter values > previewing runtime",
    "values > previewing runtime parameter"
  ],
  "related_links": [],
  "images": [
    "topics/images/parameters_8.1.jpg"
  ],
  "content_hash": "60b7a5a342ce8b25",
  "level": 2
}
---

# Previewing the runtime parameter settings while you develop a test case > Previewing the runtime parameter settings while you develop a test case > Example

- The view opens with all node structures collapsed. Click and as needed to view parameters of interest. In the example, we expanded the slot and card_1 nodes. The card_2 and ports nodes are still collapsed.

- The Resolved From column displays the source of each parameter (which file it is merged from):

- Because cardType and firmwareRev are local parameters (defined in the document that is being edited—a test case in this example), there are no entries in the Resolved From cells for them.

- The pingCount and routerAssignment parameters are defined in the parameter file (it is the local for the test case that we are editing). iTest displays the icon to emphasize that the values are resolved from another file. To view or edit a parameter definition, click the link. The appropriate editor opens to the Parameters page.

![screenshot](topics/images/parameters_8.1.jpg) <!-- image_chunk: img_9aa7d21d506cba1f -->
