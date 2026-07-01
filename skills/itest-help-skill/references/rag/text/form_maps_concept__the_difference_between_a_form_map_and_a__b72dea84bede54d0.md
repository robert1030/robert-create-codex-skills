---
{
  "chunk_id": "form_maps_concept__the_difference_between_a_form_map_and_a__b72dea84bede54d0",
  "source_file": "topics/form_maps_concept.htm",
  "source_original_path": "topics/form_maps_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Form Maps",
    "Overview: Form Maps"
  ],
  "heading_path": [
    "Overview: Form Maps",
    "Overview: Form Maps",
    "The difference between a form map and a response map"
  ],
  "anchor": "1406189",
  "context_ids": [
    "form_maps_concept"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "form maps > defined"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b72dea84bede54d0",
  "level": 2
}
---

# Overview: Form Maps > Overview: Form Maps > The difference between a form map and a response map

It is important to understand the difference between a form map and a response map. They both are tied to XML documents, but they have very different functions.

- A form map describes the elements that make up the page.

- A response map applies queries to the structured XML representation of the response to an executed step.

When you are working in GUI testing sessions, you probably need both form maps and response maps:

- Form maps identify the targets on the page. As a result, an action like click or showTable can act on the intended element (the target) on the page.

- Response maps apply queries to the responses returned by actions like describe or showTable. As a result, you can analyze the data in a response.
