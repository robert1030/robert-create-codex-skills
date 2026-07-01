---
{
  "chunk_id": "param_merge_how_it_works__merge_order_2170add03c54b2f7",
  "source_file": "topics/param_merge_how_it_works.htm",
  "source_original_path": "topics/param_merge_how_it_works.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Merging parameter definitions from multiple sources",
    "How parameter definitions from multiple sources are merged at run time"
  ],
  "heading_path": [
    "How parameter definitions from multiple sources are merged at run time",
    "How parameter definitions from multiple sources are merged at run time",
    "Merge order"
  ],
  "anchor": "1120339",
  "context_ids": [
    "param_merge_how_it_works"
  ],
  "index_keywords": [
    "merge order",
    "merging at runtime",
    "parameter definitions",
    "parameter definitions at runtime"
  ],
  "index_keyword_paths": [
    "merge order > parameter definitions",
    "merging > parameter definitions at runtime",
    "parameter definitions > merge order",
    "parameter definitions > merging at runtime"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "2170add03c54b2f7",
  "level": 2
}
---

# How parameter definitions from multiple sources are merged at run time > How parameter definitions from multiple sources are merged at run time > Merge order

Parameters can be defined in several places. iTest combines the parameter definitions from all sources before execution. Here's how it works with default settings:

1. First, parameters defined in the Global parameter file are loaded onto the heap.

1. 2

1. Parameter files that are included with in the Global file are loaded (again, the parameters defined in each file are loaded first, followed by any referenced files, recursively). The files are loaded in the order in which they are listed in the parameter Global file.

1. 3

1. The parameters defined in the test case are loaded.

1. 4

1. The parameters defined in the session profiles to be used for execution are loaded.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |
