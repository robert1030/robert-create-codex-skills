# Making your test case thread-safe > waitThread: Wait for steps to complete > Creating a waitThread step

![*](bullet_blue.jpg) <!-- image_ref -->

1. For each step that you want to wait for, set the following property values (in the General property group):

![*](bullet_blue.jpg) <!-- image_ref -->

- Specify that the step should execute asynchronously: Check the Start this step (in a new thread) and proceed to the next step box.

![*](bullet_blue.jpg) <!-- image_ref -->

- Specify a name for the thread in the threadName property.

Follow the naming guidelines listed in Naming variables and procedures.

The name need not be unique. If multiple threads share a name, then the waitThread step is activated only when the last thread with the shared name finishes.

Because field replacements are supported in the text, you can define a name that can be generated dynamically (for example, in a loop with the loop count as the replacement text).

1. 2 Create the step that will wait:

![*](bullet_blue.jpg) <!-- image_ref -->

- After the asynch steps, add a step with an EXEC action of waitThread.

![*](bullet_blue.jpg) <!-- image_ref -->

- Specify the threads that the waitThread step should wait for: In the Command property, specify the threadName values of the threads. This can be a wildcarded list and can make use of field substitution.
