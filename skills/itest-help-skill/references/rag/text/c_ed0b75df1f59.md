# Controlling execution flow: Loops, If/Then, and Switch > Loop control actions > The ‘continue’ action: Interrupt a loop iteration

The continue action causes the current script to be aborted out to the innermost containing for, foreach, or while loop command. The loop then continues with the next iteration of the loop.

> **Note：** Note Python does not use foreach construct in a loop.

Use the continue action when you want to execute particular steps for some iterations of the loop, but not for other iterations.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The Start this step in a new thread and proceed to the next step property (asynchronous execution) on a continue step is ignored.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Steps nested inside a continue step are never used.

The ‘if’ action: Element of an if/then or if-elif-else construct

The ‘then’ action: Element of an if/then construct (Tcl)

The ‘else’ action: Element of an if/then or if-else-elif construct

The ‘elseif’/‘elif’ action: Element of an if/then or if-elif-else construct
