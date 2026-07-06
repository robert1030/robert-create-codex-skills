# Controlling execution flow: Loops, If/Then, and Switch > Loop control actions > The ‘break’ action: Break out of a loop

There are two distinct kinds of break action:

![](images/loops_5.1.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Break CLI session execution (marked #1 in the example): The break that appears in the first group of actions sends the break character for CLI sessions (typically Ctrl+C). See The break action: Send the break character.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Break out of a loop (marked #2 in the example): The break that appears in the list of EXEC actions breaks out of a for, foreach (in Tcl), or while loop. Use this break action to stop executing a loop and continue executing at the step after the loop.

![*](bullet_blue.jpg) <!-- image_ref -->

- The Start this step in a new thread and proceed to the next step (asynchronous execution) property on a break step is ignored.

![*](bullet_blue.jpg) <!-- image_ref -->

- Steps nested inside a break step are never used.
