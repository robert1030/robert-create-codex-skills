# Procedures > The ‘write’ action: Adding text into the response of a call step

> **Note：** Note The write action is supported for TCL only.

A write step adds text into the response of a call step. In a called procedure, you can use one or multiple write steps to return a response that includes response data from one or more of the procedure's steps.

If you include multiple write steps in a procedure, then you can easily add a line terminator to each response so that the resulting returned response is a multi-line string. In addition, the text that appears in the Description cell of each write step is appended to the response. See Tips on using ‘write’ and ‘return’ steps to prepare useful response data for called procedures.

Contrast write with The ‘return’ action: Returning execution from the current procedure.

> **Note：** Note A write step does not write to files or involve file I/O.
