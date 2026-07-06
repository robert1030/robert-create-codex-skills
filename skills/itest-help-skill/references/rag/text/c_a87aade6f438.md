# Parameters > Defining and managing parameters > Defining a parameter > 第1段

1. 1 Click the Parameters tab on the appropriate editor: Test Case editor, Session Profile editor, or Parameter editor.

1. 2 Uncheck Show the parameter values that will be used for execution. (see Step 6.)

1. 3 One of the following:

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/parameters.1.jpg) <!-- image_ref -->

- To add the parameter as a child of an existing node, select the node and click Add Child . (Nodes are containers for parameter definitions and are discussed in Creating structure for parameters (working with nodes).)

![*](bullet_blue.jpg) <!-- image_ref -->

![](images/parameters_2.2.jpg) <!-- image_ref -->

- To add a parameter at the same level as an existing parameter (a sibling), select the sibling parameter and click Add . The parameter is added after the sibling in the same node.

1. 4 Double-click in the Name cell to specify the Name. Click in the Value and Description cells to specify settings as described here:

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

![*](bullet_black_small.png) <!-- image_ref -->

- **Name**：Specify a friendly name for the parameter (for example, port, slot, deviceID, or IPaddress). The name appears in the Data view when you execute a test case. In test case steps, to refer to a parameter that is in a container, use container_name/parameter_name syntax. For example, use the following syntax in a param command field replacement of the firmwareRev parameter in the Card_1 node: [param Card_1/firmwareRev]
- **Type**：Select a parameter type from the dropdown list. Options: Text, Boolean, Integer, Double, Secret, or Custom type Default: Text An option that displays in addition to Text, Boolean, Integer, Double, or Secret is a custom type parameter defined via the Custom types tab (see Custom Types). You may also adding a new parameter and select the Type via the Insert Parameter wizard (see Inserting a parameter into a property or test case step). See also About the Parameter Type ‘Secret’.
- **Value**：Specify the value of the parameter. (Nodes cannot have a Value.) Each of the parameter type value are validated to ensure that you have entered an appropriate value allowed for the Type selected. For example, Boolean type accepts a True/False value.

![](images/param_diff_value_to_custom_type.png) <!-- image_ref -->
