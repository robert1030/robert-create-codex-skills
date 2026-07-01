---
{
  "chunk_id": "form_maps_concept__detailed_discussion_advanced_users_a3ed8777f1534e61",
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
    "Detailed discussion (Advanced users)"
  ],
  "anchor": "1269239",
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
  "content_hash": "a3ed8777f1534e61",
  "level": 2
}
---

# Overview: Form Maps > Overview: Form Maps > Detailed discussion (Advanced users)

A form map is iTest’s method for centralizing the place where you define targets on a given GUI page. For all of iTest's GUI session types, iTest tries to describe the objects on a page as an XML document, where each node in the XML document represents one object on the page, possibly containing other objects. The node also has attributes containing some of the most important properties of that object that you might want to use if you are trying to uniquely identify that object on the page – such as its ID (if any), its location, its text, and so on. The XML document that describes the page is a “map”.

A form map is essentially a set of named XPath queries. XPath is a language for finding a node (or set of nodes) in an XML document. iTest adds one extra optional layer on top of XPath to allow for the idea of a parameterized XPATH query, which allows you to have “arguments” to the query.

In Web sessions, you can identify a Target for each step. This target is a form map query (or direct XPATH) into the current page’s map. That query should find a single node in the map and, if so, it is that corresponding object on the page that will be operated on for that step.

The Context property on the step exists so that you can choose which form map (if any) to use in the case where you want to use one of the form map queries rather than using an XPath directly. At editing time, populating the Context property is helpful because it means that the Target drop-down list will be populated with all of the form map queries from the corresponding map.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
