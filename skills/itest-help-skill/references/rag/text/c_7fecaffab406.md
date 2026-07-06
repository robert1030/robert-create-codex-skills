# Capturing Manual (Interactive) Sessions > Overview: Creating a test case by capturing interactive sessions > Working in the Capture view > 第1段

iTest always records your interactions with sessions — capturing session open and close actions, the actions that you send to sessions on devices, each session’s responses, and so on. iTest displays the ordered list of captured items in the Capture view.

> **Note：** Note iTest captures sessions regardless of whether the Capture view is open or not.

![](images/capture_tasks.01.jpg) <!-- image_ref -->

In a Telnet session, for example, when you type a command and press Enter, iTest captures both the command that you submitted (for example, show ip traffic) and the device's response (actually, the response from the session running on the device). The command/response pair (and some additional information like timestamp, prompt information, and the session and action identifiers) make up a captured item. As soon as the device responds, iTest adds the captured item as a row in the appropriate session in the Capture view.

![](images/capture_tasks.02.jpg) <!-- image_ref -->

The Capture view displays “today’s” captured items as they occur with the most recent item at the bottom of the list. You have the option to view the list of captured items grouped by session (as shown in the example — click Group By Session/Time ).

> **Tip：** Tip Double-click a tab to maximize the view. Double-click it again to minimize it.

Each top-level row represents one session, marker, or comment. The cells for a session row are populated if all captured items in the session share the same value for the cell. The cells are blank if the steps have different values.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/capture_tasks.03.jpg) <!-- image_ref -->

- You can replay captured items or whole sessions by selecting them (use Ctrl-Click and Shift-Click for multi-select) and then clicking Replay Selected . You also have the option to replay selected captured items by dropping them into an active session window.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The Capture view is a log of your session; it is not the place to edit steps. To edit steps, save the captured items into a test case and use the Test Case editor to modify the steps as needed.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/capture_tasks.04.jpg) <!-- image_ref -->

- Save selected items as a Capture report by clicking Save As Capture Report

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

![](images/capture_tasks.05.jpg) <!-- image_ref -->
