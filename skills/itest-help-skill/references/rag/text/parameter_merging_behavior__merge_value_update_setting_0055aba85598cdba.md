---
{
  "chunk_id": "parameter_merging_behavior__merge_value_update_setting_0055aba85598cdba",
  "source_file": "topics/parameter_merging_behavior.htm",
  "source_original_path": "topics/parameter_merging_behavior.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Merging parameter definitions from multiple sources",
    "Parameter merging behavior"
  ],
  "heading_path": [
    "Parameter merging behavior",
    "Parameter merging behavior",
    "Merge Value Update setting"
  ],
  "anchor": "1136357",
  "context_ids": [
    "parameter_merging_behavior"
  ],
  "index_keywords": [
    "Merge Alignment",
    "Merge Behavior table",
    "Merge Value Update",
    "Value Overwrite Behavior",
    "advanced inheritance",
    "advanced merging behavior",
    "parameters"
  ],
  "index_keyword_paths": [
    "Advanced Merging Behavior > parameters",
    "Merge Alignment",
    "Merge Behavior table",
    "Merge Value Update",
    "Value Overwrite Behavior",
    "merging > parameters",
    "parameters > advanced inheritance",
    "parameters > advanced merging behavior"
  ],
  "related_links": [
    "parameters.06.htm#1135311"
  ],
  "images": [],
  "content_hash": "0055aba85598cdba",
  "level": 2
}
---

# Parameter merging behavior > Parameter merging behavior > Merge Value Update setting

The Value Overwrite Behavior table that appears below this table presents summary of how values are set based on the Merge Value Update setting. For the definition of node, see Creating structure for parameters (working with nodes).

> **Note:** Note This setting specifies how to merge parameter values. Use the Merge Alignment property setting to specify how to merge parameter definitions.

| Inherit choice from parent; if no parent, update only if missing | Default setting. Inherit the Value Update setting for the parent node/parameter. If the setting in the parent is the default setting, then use the Update value only if missing behavior. |
| --- | --- |
| Do not update value | The value specified for the Value property on this page takes precedence. Do not overwrite the value. |
| Update value only if missing | If the current document does not define a parameter value that is defined in the merging document, then overwrite the parameter values. |
| Update value only if present | If the merging document includes a parameter with the same name, then overwrite the values. |
| Always update value | If the merging document includes a parameter with the same name, then overwrite the values. |
