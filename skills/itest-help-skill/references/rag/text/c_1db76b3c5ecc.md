# Procedures > The ‘call’ action: Calling a procedure > About arguments in procedure calls

A call action has the following content in the Description cell (all items are separated by spaces).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The procedure name (you can specify the name dynamically using either a variable or a field replacement)

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Optional: Any number of space-separated named arguments in the following format:

```
(Tcl): -arg_1 value1 -arg_2 value2 -arg_3 value3 ...
```

```
(Python): (arg_1 = value1, arg_2 = value2, arg_3 = value3)
```

Important Ensure that you select Python or TCL call syntax for procedure calls according to the test case language. Using Python call syntax in TCL test cases (and vice versa) is not supported. See also Fixing QuickCall steps with empty description in Python TestCases and Fixing steps with empty Argument list in Python testcases.

You can specify a value dynamically using either a field replacement or $varName

> **Note：** Note All named arguments must appear before all numbered arguments.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Optional: Any number of values for numbered arguments

To access the value of a numbered argument, use as follows.

Tcl: ${arg[<number>]}, for example, ${arg[3]}

Python: [arg(<number>)], for example, [arg(3)]
