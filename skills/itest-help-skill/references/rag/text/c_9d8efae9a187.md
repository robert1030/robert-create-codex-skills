# Parameters > Defining and managing parameters > Defining a parameter > Defining array parameters for use in Velocity

Array parameters in iTest are defined as sets of parameters with duplicated names or paths. Velocity and Network DevOps Agent do not support array parameters defined as sets of parameters with duplicated names or paths.

If you wish to run your testcase on Velocity and Network DevOps Agent, define an array as a single parameter value and then use expressions inside the testcase to split the value into array elements.

For example, a string value with delimiters separating individual elements can be used along with a Python/Tcl expression in the testcase steps to split the single value into multiple elements. iTest built-in actions (for, foreach) may be used to iterate over split values. The testcase and parameter file when exported to Velocity preserves the element order.

The examples below show array parameter definition using single parameter value in Python and Tcl.

Example: Parameter array—Python definition

![](images/array_param_PythonSplit.png) <!-- image_ref -->

Example: Parameter array—Tcl definition.

![](images/array_param_TCLSplit.png) <!-- image_ref -->
