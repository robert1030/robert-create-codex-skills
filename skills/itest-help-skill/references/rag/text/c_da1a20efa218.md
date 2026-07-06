# Popups（來源文件無 TOC 對應，依資料夾結構歸類） > popups/linsert.html > linsert

linsert list index element ?element element ...?

The linsert command inserts elements into a list. The command produces a new list from list by inserting all of the element arguments just before the index'th element of list. Each element argument will become a separate element of the new list. If index is less than or equal to zero, then the new elements are inserted at the beginning of the list. The interpretation of the index value is the same as for the command string index, supporting simple index arithmetic and indexes relative to the end of the list.

The linsert command is compatible with its Tcl counterpart as described at: http://www.tcl.tk/man

For details on each iTest command, see the online help: Command syntax for test case steps.
