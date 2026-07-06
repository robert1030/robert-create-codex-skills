# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/subst.html > subst

subst string

Performs backslash, command, and variable substitutions on the string argument. The substitutions are performed in exactly the same way as for Tcl commands. As a result, the string argument is actually substituted twice; once by the Tcl parser in the usual fashion for Tcl commands, and again by the subst command.

Limitation: No additional arguments are allowed. The command is otherwise compatible with its Tcl counterpart as more fully described at: http://www.tcl.tk/man

For details on using this and other iTest interpreter commands, see the online help: Command syntax for test case steps.

Also, see: Field replacements: Substituting values into properties and commands.
