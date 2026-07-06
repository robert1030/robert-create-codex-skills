# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/lsearch.html > lsearch

lsearch ?switches? list pattern

lsearch determines whether a list contains a specified element. If found, returns the zero-based index of the matching item. If you provide the optional -inline switch, then returns the matching item. If not found, returns -1. pattern supports regex matching, exact matching, and wildcard (glob-style) matching (using the * and ? wildcard characters)). The [chars] and \x options are not supported.

The lsearch command is compatible with its Tcl counterpart. The command and optional switches are more fully described at: http://www.tcl.tk/man

For details on each iTest command, see the online help: Command syntax for test case steps.
