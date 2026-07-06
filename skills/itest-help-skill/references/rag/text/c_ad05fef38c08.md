# Spirent Avalanche sessions > Avalanche API Commands > av_create > Parameters

| 欄位1 | 欄位2 | 欄位3 |
| --- | --- | --- |
| Name | Type | Description |
| handle | handle | Specifies the handle of the parent for the newly created object. |
| relationName or objectTypeName | string | The name of the relation from the parent to the created object, or the name of the object’s type. |
| DDNPath |  | A dotted path name sequence that begins with an object handle, followed by one or more object type names. The path must identify a valid sequence of objects in the data model hierarchy. Avalanche Automation returns data for the object identified by the last name in the sequence. Use index values to identify one of a set of children of the same type. Index values are assigned in the order of creation. An unqualified type name (a name with no index value) indicates the first child object of that type for the parent. |
| DANpath |  | A dotted path name beginning with a sequence of one or more object types, and ending with an attribute name. Avalanche Automation combines the objectHandle (or the directDescendantPath) with the descendantAttributePath to resolve the attribute reference. |
| attr/value |  | The attr portion of the pair is the name of the attribute to be modified. The value portion specifies the new value. You can specify one or more attr/value pairs in a single function call. The attribute name and value must be separated by a space; each name-value pair in a sequence must be separated by a space. |
