# QuickCalls: Defining and using a library of custom actions > Adding a test case step that executes a QuickCall > About arguments in QuickCall steps > Example:

This example call to the ExercisePorts QuickCall includes two named arguments and one numbered argument. Here is the form of the call:

<QuickCallName> -slot slotNumber -port portNumber numberOfRepetitions

Here is the actual QuickCall step: The value of the port argument is determined dynamically by the return value of a param command.The numbered argument has the value 75.

![](images/quickcalls_2.01.jpg) <!-- image_ref -->

Ensure that you select Python or TCL call syntax for procedure calls according to the test case language. Using Python call syntax in TCL test cases (and vice versa) is not supported. See Fixing steps with empty Argument list in Python testcases.
