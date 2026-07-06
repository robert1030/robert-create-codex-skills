# QuickCalls: Defining and using a library of custom actions > Adding a test case step that executes a QuickCall > About arguments in QuickCall steps > Fixing QuickCall steps with empty description in Python TestCases

Usage of TCL syntax for QuickCalls and call steps in Python test cases display a warning message in the Problems view if a step has empty description as shown below. QuickCall steps with empty descriptions, which correspond to empty argument list in TCL.

![](images/qc_tclSyntax_inPyhton_Warning.png) <!-- image_ref -->

A fix requires manual input or using iTest provided option called Quick Fix to automatically fix QuickCall steps with empty descriptions.

In the Problem view, select a test case or multiple test cases with empty argument list, right-click and then press Quick Fix to display the Quick Fix dialog.

![](images/qc_tclSyntax_inPyhton_QuickFix.png) <!-- image_ref -->

On the Quick Fix dialog, select the required test case listed in the Problems section and click Finish. The Quick Fix updates the relevant steps by adding the correct syntax ‘()’ in the previously empty step description.

![](images/qc_tclSyntax_inPyhton_QuickFixDialog.png) <!-- image_ref -->
