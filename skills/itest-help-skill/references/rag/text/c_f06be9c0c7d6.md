# Tcl Shell Sessions > Tcl Shell session window > About the Tcl interpreter that iTest uses

The Tcl interpreter provided with iTest can execute third-party Tcl packages that are pure Tcl (no separate Tcl distribution is required, however).

By default, iTest selects the interpreter using the following process:

1. 1 If an interpreter is specified in the Use the specified Tcl interpreter property on the preferences page, then use that interpreter.

1. 2 Otherwise, launch the first installed Tcl interpreter that iTest finds in the PATH environment variable.

1. 3 If no interpreter is specified in the PATH variable, use iTest's built-in interpreter. The internal interpreter is a JACL Java-based Tcl interpreter. Because JACL does not support any C/C++ extensions, most traffic generator devices will not work in this interpreter.

Preferences for the Tcl interpreter are described in Setting preferences for Tcl Shell sessions and Setting iTest preferences.
