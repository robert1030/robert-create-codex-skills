---
{
  "chunk_id": "parameters_03__defining_a_parameter_f301048f28b4162f",
  "source_file": "topics/parameters.03.htm",
  "source_original_path": "topics/parameters.03.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Defining and managing parameters",
    "Defining a parameter"
  ],
  "heading_path": [
    "Defining a parameter",
    "Defining a parameter"
  ],
  "anchor": "1466510",
  "context_ids": [],
  "index_keywords": [
    "defining",
    "multiple values",
    "multiple values for parameter",
    "setting values"
  ],
  "index_keyword_paths": [
    "multiple values for parameter",
    "parameter > multiple values",
    "parameters > defining",
    "parameters > setting values"
  ],
  "related_links": [
    "#1323155",
    "parameters.06.htm#1135311",
    "insert_parameter_dialog.htm#1135987",
    "param_parameters_type_secret.htm#1554375",
    "parameters.10.htm#1144740",
    "param_merge_how_it_works.htm#1120320",
    "parameters.22.htm#1329140",
    "new_parameter_file_wizard.htm#1323746"
  ],
  "images": [
    "topics/images/parameters.1.jpg",
    "topics/images/parameters_2.2.jpg",
    "topics/images/param_diff_value_to_custom_type.png",
    "topics/images/parameters_2.4.jpg",
    "topics/images/param_find_required.png"
  ],
  "content_hash": "f301048f28b4162f",
  "level": 1
}
---

# Defining a parameter > Defining a parameter

1. 1

1. Click the Parameters tab on the appropriate editor: Test Case editor, Session Profile editor, or Parameter editor.

1. 2

1. Uncheck Show the parameter values that will be used for execution. (see Step 6.)

1. 3

1. One of the following:

- To add the parameter as a child of an existing node, select the node and click Add Child . (Nodes are containers for parameter definitions and are discussed in Creating structure for parameters (working with nodes).)

- To add a parameter at the same level as an existing parameter (a sibling), select the sibling parameter and click Add . The parameter is added after the sibling in the same node.

1. 4

1. Double-click in the Name cell to specify the Name. Click in the Value and Description cells to specify settings as described here:

| Name | Specify a friendly name for the parameter (for example, port, slot, deviceID, or IPaddress). The name appears in the Data view when you execute a test case. In test case steps, to refer to a parameter that is in a container, use container_name/parameter_name syntax. For example, use the following syntax in a param command field replacement of the firmwareRev parameter in the Card_1 node: [param Card_1/firmwareRev] |
| --- | --- |
| Type | Select a parameter type from the dropdown list. Options: Text, Boolean, Integer, Double, Secret, or Custom type Default: Text An option that displays in addition to Text, Boolean, Integer, Double, or Secret is a custom type parameter defined via the Custom types tab (see Custom Types). You may also adding a new parameter and select the Type via the Insert Parameter wizard (see Inserting a parameter into a property or test case step). See also About the Parameter Type ‘Secret’. |
| Value | Specify the value of the parameter. (Nodes cannot have a Value.) Each of the parameter type value are validated to ensure that you have entered an appropriate value allowed for the Type selected. For example, Boolean type accepts a True/False value. Note The parameter values are always type string. When language is Python, variables must be type casted when used as any other type. You cannot enter a value when parameter Type is Secret. If you have selected a custom Type, the Value dropdown list shows the values you entered for the custom type. (see Custom Types). You may also enter an undefined value for the type. An information icon and message (tool tip) displays when you enter an invalid value (as shown below). |
| Note | The parameter values are always type string. When language is Python, variables must be type casted when used as any other type. |
|  | You cannot enter a value when parameter Type is Secret. |
|  | If you have selected a custom Type, the Value dropdown list shows the values you entered for the custom type. (see Custom Types). |
|  | You may also enter an undefined value for the type. An information icon and message (tool tip) displays when you enter an invalid value (as shown below). |

|  | Once you specify a value, it also appears in the Data view, where you can modify it when execution is paused or loaded for execution. You can create an empty parameter (that is, a parameter with no value). Multiple values for a single parameter are useful, for example, in foreach loops. To create a parameter with multiple values, do either of the following: Create multiple parameters with the same name. For a single variable name, type each value and separate the values using spaces. If any single value contains a space, then use double quotes around the value. |  | Once you specify a value, it also appears in the Data view, where you can modify it when execution is paused or loaded for execution. |  | Create multiple parameters with the same name. |  | For a single variable name, type each value and separate the values using spaces. If any single value contains a space, then use double quotes around the value. |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | Once you specify a value, it also appears in the Data view, where you can modify it when execution is paused or loaded for execution. |  |  |  |  |  |  |
|  | Create multiple parameters with the same name. |  |  |  |  |  |  |
|  | For a single variable name, type each value and separate the values using spaces. If any single value contains a space, then use double quotes around the value. |  |  |  |  |  |  |
| Dynamic test case parameter value: You may want to use a query language for defining a test case parameter, which is resolved to a resource property (concrete value) when the test case is run. For example: Name=resParameter and Value=$(topology/resources/PC/inventoryName) is resolved to the resource property when running a test case. See details of using the Property Query Language below. |  |  |  |  |  |  |  |
| Property Query Language Dynamic property value is a placeholder, which is substituted with the value of a resolved property query: ${property_query} Structure of a query: <LOCATION>/resources/<RESOURCE_NAME>/[PORT_NAME/]<PROPERTY_NAME> Where parameters are following: LOCATION - a data origin, available options: inventory; topology. RESOURCE_NAME - a name of a resource; PORT_NAME - optional, a name of resource port; PROPERTY_NAME - a name of a property. Escape character '\': Use the backslash character to escape a single character or symbol. Only the character immediately following the backslash is escaped. To use the forward slash (/), use the backslash (\)t o escape. For example, “A/B” is escaped to “A\/B”. To use a backslash (\) character, use a backslash (\) to escape. For example, “A/B” is escaped to “A//B”. Examples: ${inventory/resources/Server #1/ipAddress} ${inventory/resources/Cisco Switch #1/Fa0\/1/Port Speed} ${topology/resources/My Virtual Machine/OS Family} Resolving of Property Query Depending on the LOCATION, a search for resources, ports and properties is performed in different places: inventory: search is performed against Inventory; topology: search is performed against a topology TBML file which is associated with a reservation. If a property is not found by a query then a test case execution is failed. Resolution restrictions for inventory's resource: Password properties are not resolved for a security reason. Attachment properties are not resolved as well. |  | LOCATION - a data origin, available options: |  | inventory; |  | topology. |  |
|  | LOCATION - a data origin, available options: |  |  |  |  |  |  |
|  | inventory; |  |  |  |  |  |  |
|  | topology. |  |  |  |  |  |  |
|  | RESOURCE_NAME - a name of a resource; |  |  |  |  |  |  |
|  | PORT_NAME - optional, a name of resource port; |  |  |  |  |  |  |
|  | PROPERTY_NAME - a name of a property. |  |  |  |  |  |  |
|  | Escape character '\': |  |  |  |  |  |  |
|  | To use the forward slash (/), use the backslash (\)t o escape. For example, “A/B” is escaped to “A\/B”. |  |  |  |  |  |  |
|  | To use a backslash (\) character, use a backslash (\) to escape. For example, “A/B” is escaped to “A//B”. |  |  |  |  |  |  |
|  | Depending on the LOCATION, a search for resources, ports and properties is performed in different places: |  |  |  |  |  |  |
|  | inventory: search is performed against Inventory; |  |  |  |  |  |  |
|  | topology: search is performed against a topology TBML file which is associated with a reservation. |  |  |  |  |  |  |
|  | Resolution restrictions for inventory's resource: |  |  |  |  |  |  |
|  | Password properties are not resolved for a security reason. |  |  |  |  |  |  |
|  | Attachment properties are not resolved as well. |  |  |  |  |  |  |
| Description | Optional. Describe the function and use of the parameter. The text also appears in the Data view to help you when setting parameter values while executing, pausing, or single-stepping the test case. |  |  |  |  |  |  |

1. 5

1. Optional. Mask the value. Check the box for sensitive information (for example, a password) that should be hidden from view in any user-visible windows. See Masking a parameter’s value.

For Secret parameter type, Mask the value is automatically enabled and masked by default, which you may uncheck.

1. 6

1. Optional. Specify Advance Merge settings.

Merge settings specify, for example, which value to use for a particular parameter when the test case includes a parameter with the same name but with different values. The set of parameters and values that result after merging is the set that is used for execution. Typically, you do not need to change the default settings. See How parameter definitions from multiple sources are merged at run time.

To view the parameter and values that iTest will use at runtime, check Show the parameter values that will be used for execution.

The page view switches to a read-only table of parameters and values. For details, see Previewing the runtime parameter settings while you develop a test case.

1. 7

1. Optional. Save the parameter definitions as a parameter file. One powerful way to cause iTest to use a particular set of parameter definitions when executing any test case is to create a parameter file. A parameter file is a collection of parameter definitions and (optionally) references to additional parameter files. See Creating a parameter file.

The Search field on the Parameters page allows you to search for the parameters find your required parameters.

> **Note:** Note The Search does not return anything if it contains invalid characters. For example: \, :, ;, ', ", ( ), { }.

![inline_icon](topics/images/parameters.1.jpg) <!-- image_chunk: img_3f084c02e59b4220 -->

![inline_icon](topics/images/parameters_2.2.jpg) <!-- image_chunk: img_770fd8a9de651bed -->

![screenshot](topics/images/param_diff_value_to_custom_type.png) <!-- image_chunk: img_faaffd4b6b3026f3 -->

![screenshot](topics/images/parameters_2.4.jpg) <!-- image_chunk: img_26fcb3dd1a80aba5 -->

![screenshot](topics/images/param_find_required.png) <!-- image_chunk: img_2d85378d3eb1eccf -->
