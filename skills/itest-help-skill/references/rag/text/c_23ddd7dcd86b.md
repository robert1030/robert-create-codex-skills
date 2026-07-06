# Parameters > Merging parameter definitions from multiple sources > Parameter merging behavior > Merge Value Update setting

The Value Overwrite Behavior table that appears below this table presents summary of how values are set based on the Merge Value Update setting. For the definition of node, see Creating structure for parameters (working with nodes).

> **Note：** Note This setting specifies how to merge parameter values. Use the Merge Alignment property setting to specify how to merge parameter definitions.

- **Inherit choice from parent; if no parent, update only if missing**：Default setting. Inherit the Value Update setting for the parent node/parameter. If the setting in the parent is the default setting, then use the Update value only if missing behavior.
- **Do not update value**：The value specified for the Value property on this page takes precedence. Do not overwrite the value.
- **Update value only if missing**：If the current document does not define a parameter value that is defined in the merging document, then overwrite the parameter values.
- **Update value only if present**：If the merging document includes a parameter with the same name, then overwrite the values.
- **Always update value**：If the merging document includes a parameter with the same name, then overwrite the values.
