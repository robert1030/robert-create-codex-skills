# Capturing Manual (Interactive) Sessions > Overview: Creating a test case by capturing interactive sessions > Adding captured steps into a test case or Python Script

> **Note：** Note For generating Python Scripts from the captured steps, see “Python Automation Library”, section Capturing Manual (Interactive) Sessions.

While you can add a procedure to a test case manually by typing it into the Test Case editor, the fastest way to add a procedure is to perform the steps manually, select the captured steps or sessions in the Capture view, and then use the Add to iTest Test Case wizard.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- If you select multiple sessions, they are saved together in capture order as a single procedure.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Comments and makers are converted into EXEC comment actions.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- When you add a captured session to a iTest test case, each QuickCall that you performed during the manual session becomes a single step in the test case (regardless of how many actions the QuickCall actually performed). This improves readability, portability, and consistency. See “QuickCalls: Defining and using a library of custom actions”.
