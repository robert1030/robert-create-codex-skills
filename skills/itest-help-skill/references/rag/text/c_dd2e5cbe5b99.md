# Tcl Shell Sessions > Tcl Shell session window > Sourcing the .itesttclshrc file upon session startup

Before starting a iTest Tcl Shell session, the iTest Tcl Shell interpreter sources the .itesttclshrc script located in your home directory (if present). This allows you to initialize the Tcl shell with any startup scripts listed in itesttclshrc. For most .itesttclshrc scripts, the result is to source the standard .tclshrc script located in your home directory (if present).

Because the interpreter sources the .itesttclshrc file, you can use [tcl …] field replacements in the text of session profile property settings to source Tcl initialization code in the script (which can, in turn, affect the resulting value of the substitution).
