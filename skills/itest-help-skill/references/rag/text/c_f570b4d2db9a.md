# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/scriptget.html > scriptGet

scriptGet gets the value of a variable from the specified interpreter and sets the specified iTest interpreter variable to the value. (By default, the command gets the value from the global Tcl interpreter, but you have the option to specify the session with the target interpreter.)

scriptGet takes two arguments: the name of an iTest variable to be set; and something that is substituted by the interpreter. Command substitution happens on both arguments before the interpreter is asked to interpret the second argument.

In this example, t2 is the iTest variable to get the value, and var2 is the Tcl variable whose value will populate t2. The braces around $var2 prevent substitution, causing it to be passed to the specified interpreter as the string "$var2".

![](../images/scriptget.jpg) <!-- image_ref -->

For details on arguments and restrictions, see the online help: The scriptGet action.
