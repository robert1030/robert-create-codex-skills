---
{
  "chunk_id": "param_merge_how_it_works__overview_3aeda25d3772b624",
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
    "Overview"
  ],
  "anchor": "1131749",
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
  "related_links": [
    "add_parameter_dialog.htm#1144750"
  ],
  "images": [],
  "content_hash": "3aeda25d3772b624",
  "level": 2
}
---

# How parameter definitions from multiple sources are merged at run time > How parameter definitions from multiple sources are merged at run time > Overview

Parameters can be defined in several places in addition to the Global parameter file. iTest combines the parameter definitions from all sources before execution. See Adding a parameter definition while inserting parameters.

You can think of the parameter value that you define in the session profile as the default or base value. At runtime, for an example parameter named param1, the following changes occur:

1. 1

1. If you specified a value for param1 in the test case, iTest uses the value from the test case, and then:

1. 2

1. Finally, if you specified a value for param1 in the Global parameter file, iTest uses the value from the Global parameter file

This clearly defined order (in which a parameter value is overridden) is called the merge order.

So, if you have specified a Global parameter file, then (regardless of any values in the other files) the value specified in the Global parameter file is the value that is used at runtime. Because this is true whenever you have specified a Global parameter file, you do not need to specify that the value in the Global parameter file should be used. That is why the Global parameter file does not appear as a source of parameter values in the Insert Parameter dialog box.
