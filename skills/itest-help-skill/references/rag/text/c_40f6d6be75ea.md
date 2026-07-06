# Parameters > Merging parameter definitions from multiple sources > Parameter merging behavior > Merge Alignment setting

The Merge Behavior table that appears below this table presents a summary of how nodes and parameters are merged based on the Merge Alignment setting.

> **Note：** Note This setting specifies how to merge parameter definitions. Use the Merge Value Update property setting to specify how to merge the values of the parameters.

- **Inherit choice from parent; if no parent, add if missing/multiple**：Default setting. Inherit the Merge Alignment setting for the parent node/parameter. If the setting in the parent is the default setting, then use the Use if present; add if missing/multiple merge behavior.
- **Always add**：Add any node or parameter that appears in the parent and not in the child.
- **Use if present; add if missing/multiple**：Add any node or parameter that appears in the parent and not in the test child. Add any node or parameter that appears in the parent and also in the test child. Use node if present; add if the node does not exist in the child or if multiple nodes are being merged
- **Use if present but do not add if missing**：Use the node if present in the child, but do not add if missing from the child
