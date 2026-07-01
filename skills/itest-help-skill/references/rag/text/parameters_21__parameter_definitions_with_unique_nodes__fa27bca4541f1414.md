---
{
  "chunk_id": "parameters_21__parameter_definitions_with_unique_nodes__fa27bca4541f1414",
  "source_file": "topics/parameters.21.htm",
  "source_original_path": "topics/parameters.21.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Merging parameter definitions from multiple sources",
    "Parameter definitions handling at runtime"
  ],
  "heading_path": [
    "Parameter definitions handling at runtime",
    "Parameter definitions handling at runtime",
    "Parameter definitions with unique nodes are overridden with those in the parameter file"
  ],
  "anchor": "1538528",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/param_UniqueRootDefinitions.png",
    "topics/images/param_FileOverridesUniqueRoots.png",
    "topics/images/param_TclFileOverridesUniqueRoots.png"
  ],
  "content_hash": "fa27bca4541f1414",
  "level": 2
}
---

# Parameter definitions handling at runtime > Parameter definitions handling at runtime > Parameter definitions with unique nodes are overridden with those in the parameter file

If parameters defined in a test case have unique nodes and the parameter file (.ffpt) has the same nodes, then definitions in the parameters file will override the definition in the test case (similar to the parameters from the command line).

Example 1: Parameter definition in the Test Case Editor > Parameters tab and a parameters file (.fftp) which is set as a global parameter file.

Example 2: Test case parameter overridden with the definition from the parameter file.

Python example.

Tcl Example:

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/param_UniqueRootDefinitions.png) <!-- image_chunk: img_eeea9722ef081170 -->

![screenshot](topics/images/param_FileOverridesUniqueRoots.png) <!-- image_chunk: img_5f85638e5df9ed8f -->

![screenshot](topics/images/param_TclFileOverridesUniqueRoots.png) <!-- image_chunk: img_99e4be7ed59b37ae -->
