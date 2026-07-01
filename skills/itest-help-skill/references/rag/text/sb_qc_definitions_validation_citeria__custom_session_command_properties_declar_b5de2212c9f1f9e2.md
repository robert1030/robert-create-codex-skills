---
{
  "chunk_id": "sb_qc_definitions_validation_citeria__custom_session_command_properties_declar_b5de2212c9f1f9e2",
  "source_file": "topics/sb_qc_definitions_validation_citeria.htm",
  "source_original_path": "topics/sb_qc_definitions_validation_citeria.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Builder",
    "QuickCall definitions validation criteria"
  ],
  "heading_path": [
    "QuickCall definitions validation criteria",
    "QuickCall definitions validation criteria",
    "Custom session command properties declaration"
  ],
  "anchor": "1397742",
  "context_ids": [
    "sb_qc_definitions_validation_citeria"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "b5de2212c9f1f9e2",
  "level": 2
}
---

# QuickCall definitions validation criteria > QuickCall definitions validation criteria > Custom session command properties declaration

iTest parses each argument of a Quickcall as a property of the custom session command. The definition in the argument description helps clarify how it may be used when exporting the Quickcall library. By default, the datat ype of each argument is a string and can be defined to contain different data types. For example, --datatype=integer. In addition, the declaration can also provide subsequent validation rules for an argument such as allowedValue, allowedRange, allowedLength, etc. The table below shows how to specify the validation rules for an argument.

| Properties | Description | Syntax/example |
| --- | --- | --- |
| datatype | Indicates the data type values appropriate for values in this argument. The values must be one of the following: string, integer, boolean, decimal, anyURI, or dateTime. | --datatype=integer |
| masked | True or false. True: indicates that the contents of the argument are sensitive (such as a password) and should normally be hidden from view by users. False:indicates that the value may be visible (not masked) | --datatype=string, masked=true |
| isMultiline | True or false. Applicable Only if the datatype is string. True: indicates that the string is allowed to span multiple lines. False: indicates that the string is not allowed to span muliple lines. | --datatype=string, isMultiline=true |
| allowedValue | In cases where only a certain fixed set of values are appropriate for the datatype, then the allowedValues element will appear once in the parameter declaration for each of these values. | --datatype=string, allowedValue=A|B|C |
| allowedLength | Aplicable for string argument. Establishes a minimum and/or maximum length for the string. | Syntax :allowedLength={min_value;max_value} or allowedLength={min_value; } or allowedLength={ ;max_value} Example: --datatype=string, allowedLength={3;5} |
| allowedCount | Determines whether the given argument may appear multiple times in the container. | Syntax: allowedCount={min_value;max_value} or allowedCount={min_value; } or allowedCount={ ;max_value} Example: --datatype=string, allowedCount={3;5} |
| allowedPattern | Indicates that the string arguments are valid only when they conform to a certain pattern. | --datatype=string, allowedPattern=([\da-fA-F]{2}:){5}[\da-fA-F]{2} |
| allowedRange | Valid for numeric arguments (integer and decimal). The allowedRange indicates the minimum and/or maximum values that will be considered valid. When both minimum and maximum values are specified and if the minimum value is greater than the maximum value, then the range between these values will be invalid. | Syntax: allowedRange={min_value;max_value} or allowedRange={min_value; } or allowedRange={ ;max_value} Example: --datatype=integer, allowedRange={3;5} |
| enablementValue | Indicates that the validity of an argument depends on the presence and/or values of other arguments. That is, if the enablementValue element is specified in the argument description, then you will be allowed to indicate that this argument is valid only when another argument (by name) within the same container carries a specific value. | --enablementValue = { parameter: "param1", value : "", enableOn: "equal"} |
