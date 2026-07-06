# Executing Tests > Execution: Quick instructions > Replaying captured items from the Capture view > 第1段

In the Capture view: If the group of captured items is all in the same session and does not include an open step, then drop the items into an active session window of the appropriate session type. The items execute immediately. (You cannot include session open steps in the group of captured items.)

![](images/executing_tests.11.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A simple and powerful way to manually execute a series of CLI commands is to save the command text in a text file (for example, a Notepad text file). Copy the commands and then paste them into an active session. The commands execute immediately.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/executing_tests.12.jpg) <!-- image_ref -->

- During an interactive session, click in the toolbar and then select the QuickCall from the drop-down list. iTest then executes all of the steps in the QuickCall as if you had typed them yourself. With a single click (typically), you can execute a QuickCall that performs a complex initialization routine or executes a long sequence of related steps.

QuickCalls will save you a lot of time setting up and tearing down, and, for example, can quickly perform the 20 steps that you usually have to type to bring the device into the proper state for that single crucial test step. See “QuickCalls: Defining and using a library of custom actions”.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/executing_tests.13.jpg) <!-- image_ref -->

- Alternatively, if a session window of the appropriate type is open, then select the items and click .

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/executing_tests.14.jpg) <!-- image_ref -->

- If the selected group of captured items include an open item for each session, then click .



For a single selected item:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If the session from which the item was captured is still active, then the item is immediately executed in that session.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If iTest determines that the item could be executed in any of multiple active sessions, then a dialog box asks you to specify the session in which to execute.

![](images/executing_tests.15.jpg) <!-- image_ref -->
