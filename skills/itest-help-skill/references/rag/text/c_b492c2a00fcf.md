# Procedures > Advanced Users: About procedures > Parameters > Parameters in procedures

Parameters are loaded in by call steps, so a parameter’s resolved value depends on the order in which procedures are called. For example, two procedures use the same parameters with different values: If you call a procedure from test case B and then call a procedure from test case A, then the parameter values for B are resolved first. If A is called before B, then A’s values are resolved first.

> **Note：** Note For QuickCalls, parameters are resolved differently. See How QuickCalls execute.
