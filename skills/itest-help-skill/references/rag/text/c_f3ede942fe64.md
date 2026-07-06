# Capturing Manual (Interactive) Sessions > Overview: Creating a test case by capturing interactive sessions > Captured items

In both manual (interactive) sessions and automatically executed test cases, a session typically returns a response to each command that you send. iTest captures the command, response, and other identifying information (like the session and action identifiers and timestamp) as a captured item.

The Capture view displays basic information about each captured item and lists each item in the order in which it was captured. In this example, we have selected a single captured item (the show ip traffic command that we submitted to the device).

![](images/capture_tasks_9.1.jpg) <!-- image_ref -->

You can save any or all of the captured items that currently appear in the Capture view as a Capture report or a procedure in a test case. Capture reports preserve and display all of the information about all captured items.

The Capture view is a log of your session; it's not the place to edit steps. To edit steps, save the captured items into a test case and use the Test Case editor to modify the steps as needed.Captured items include the session's response, but the Capture view does not display responses. To view a response, open the Response view or view the items in a Capture report. Double-click an item to display it in the Response view.

On startup, iTest will automatically discard old captured sessions when the size of the capture database exceeds a certain limit. You can change this limit using Window > Preferences.
