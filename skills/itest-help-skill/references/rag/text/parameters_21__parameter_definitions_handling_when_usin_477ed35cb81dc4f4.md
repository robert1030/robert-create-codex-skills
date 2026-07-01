---
{
  "chunk_id": "parameters_21__parameter_definitions_handling_when_usin_477ed35cb81dc4f4",
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
    "Parameter definitions handling when using TCL interpreter"
  ],
  "anchor": "1538423",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/param_DuplicateRootDefinitions.png",
    "topics/images/param_PythonTclConcatenatedDuplicateRoots.png"
  ],
  "content_hash": "477ed35cb81dc4f4",
  "level": 2
}
---

# Parameter definitions handling at runtime > Parameter definitions handling at runtime > Parameter definitions handling when using TCL interpreter

If a test case parameter definitions include duplicate nodes (same node names as defined in a parameter file), the parameters are concatenated to form a list when executing the test case.

Example 1: Parameter definition in the Test Case Editor > Parameters tab and a parameters file (.fftp) which is set as a global parameter file.

Example 2: Parameter values are concatenated whenever duplicate nodes are present in parameters definition (Test Case Editor > Parameters tab and a parameter file).

![screenshot](topics/images/param_DuplicateRootDefinitions.png) <!-- image_chunk: img_df33d4abac90d5d0 -->

![screenshot](topics/images/param_PythonTclConcatenatedDuplicateRoots.png) <!-- image_chunk: img_44fe4b3b5f636449 -->
