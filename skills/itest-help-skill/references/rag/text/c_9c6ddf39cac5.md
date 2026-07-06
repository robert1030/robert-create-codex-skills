# Session Builder > QuickCall definitions validation criteria > Validation rules applied when exporting Quickcall library > Validation rules for allowedPattern, allowedLength, etc., with datatype

The table below lists the properties and the supported datatype. When you use a property that does not match the datatype, a validation conflict occurs and a validation error message displays. For example, using AllowedRange with String (i.e., --datatype=string, allowedRange={3; 5}), displays an error message as follows.

The datatype 'String' does not support the attribute 'AllowedRange'. The supported attributes are AllowedValue, AllowedPattern, AllowedLength, AllowedCount, Marked, isMultiline when exporting a Quickcall library.

| 欄位1 | 欄位2 | 欄位3 | 欄位4 | 欄位5 | 欄位6 | 欄位7 |
| --- | --- | --- | --- | --- | --- | --- |
| Properties/DataType | string | integer | decimal | boolean | datetime | anyURI |
| AllowedValue | x | x | x | x |  | x |
| AllowedPattern | x |  |  |  | x |  |
| AllowedRange |  | x | x |  |  |  |
| AllowedLength | x |  |  |  |  |  |
| AllowedCount | x | x | x | x | x | x |
| Marked | x | x | x |  |  | x |
| isMultiline | x |  |  |  |  |  |
| enablementValue | x | x | x | x | x | x |
