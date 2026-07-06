# QuickCalls: Defining and using a library of custom actions > Defining QuickCalls > Defining a QuickCall > Tip You might include text that warns developers that this test case is not intended for execution. Make the QuickCalls “public” and associate them with a topology device or session profile: > 第1段

- **Include this test case when listing QuickCall libraries**：Check the Include this test case check box to make the library “public”, that is, to cause iTest to display the test case name whenever a user asks to see a list of available QuickCall libraries. This settings adds the QuickCall library to the drop-down list when you edit a session profile or device to associate with the library. Default: checked for QuickCall libraries and procedure libraries, unchecked otherwise
- **Session profile or device**：Specify the topology device or session profile to associate with the QuickCalls that are defined in the library. Once you have specified a device or profile, the link becomes active and opens the item in the appropriate editor.

![*](bullet_blue.jpg) <!-- image_ref -->

Define the QuickCalls that make up the library

Use the following instructions to add as many QuickCalls as needed to the QuickCall library. You define a QuickCall in either of the following ways:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/quickcalls.04.jpg) <!-- image_ref -->

- The easiest way to add a QuickCall is to manually execute the steps that you want to include in the QuickCall and then, using the capture-to-test feature or from the Capture view, save the captured session as a procedure in a test case. The QuickCall is added as a procedure definition after the last step in the test case.

![*](bullet_blue.jpg) <!-- image_ref -->

- Drag captured items into the Test Case Editor of a new QuickCall definition or an existing QuickCall).

OR

![*](bullet_blue.jpg) <!-- image_ref -->

- Right-click on the selected captured session item, select Add to iTest Test Case and follow the steps in Adding captured sessions or steps into a procedure in a iTest Test Case “Capturing Manual (Interactive) Sessions”.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Alternatively, while working in the Test Case editor, you can add a QuickCall “manually” by adding a procedure definition and then adding steps to the procedure or copy Test Case steps (not a QuickCall) and paste them into a QuickCall test case.

> **Tip：** Tip While working on QuickCall definitions on the Test Case editor Steps page, click Collapse All to view only the QuickCall names and not the individual steps. You can then work on a single QuickCall definition without the clutter.

> **Caution：** CAUTION Do not use the open action (open a session) in a QuickCall.

![*](bullet_blue.jpg) <!-- image_ref -->
