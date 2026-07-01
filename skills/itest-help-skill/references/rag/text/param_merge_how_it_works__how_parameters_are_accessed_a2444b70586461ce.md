---
{
  "chunk_id": "param_merge_how_it_works__how_parameters_are_accessed_a2444b70586461ce",
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
    "How parameters are accessed"
  ],
  "anchor": "1131797",
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
    "parameter_merging_behavior.htm#1136184"
  ],
  "images": [],
  "content_hash": "a2444b70586461ce",
  "level": 2
}
---

# How parameter definitions from multiple sources are merged at run time > How parameter definitions from multiple sources are merged at run time > How parameters are accessed

Based on where they are defined, parameters are accessed as follows (using the default inheritance settings). You also have the option to specify Parameter merging behavior.

| Session Profile editor (also called the New Session page) | When you create a session profile and base it on an existing profile, the new profile inherits the parameter definitions in the existing profile. When you specify a session profile in an open step in a test case, any step in the session that was opened with the profile uses the parameters and values defined in the profile. |
| --- | --- |
| Test Case editor | Parameters that you define for a test case can be accessed by any step in the current test case. Test case steps can make use of param field replacements (the [param paramName] command) to overwrite settings made in session profiles. |
