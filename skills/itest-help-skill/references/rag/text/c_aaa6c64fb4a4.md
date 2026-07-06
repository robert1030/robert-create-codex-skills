# Spirent TestCenter REST sessions > Spirent TestCenter REST session window > To create a test case that includes Spirent TestCenter REST sessions > 第1段

You typically save captured manual steps as a test case. Follow these steps:

![*](bullet_blue.jpg) <!-- image_ref -->

1. Ensure that the TestCenter REST session profile or device is properly configured. See Session profile property settings for Spirent TestCenter REST sessions.

![](images/spirent_testcenter_rest_2.1.jpg) <!-- image_ref -->

1. 2 Click to begin the direct-to-test process of saving the interactive session as a test case.

1. 3 Start the TestCenter REST session and perform the test as needed. You work in the iTest TestCenter REST session the same way you work in TestCenter. When you interact with a TestCenter component, iTest performs a TestCenter action and captures both the action and the response from TestCenter. For example:

![](images/spirent_testcenter_rest.2.jpg) <!-- image_ref -->

You first select Port 1. When you click Auto Negotiate, iTest opens the Auto Negotiate Editor to view or create session (just like TestCenter). Then, click OK in the editor.

You may select Port 1 and change the default settings, for example, MIMO Configuration (option 4x4:4), Power Settings, Channel Frequency (option Dual Band), and Mode options. Click Apply and the action ConfigurePort reflects your changes on the Console. Then click Apply in the editor.

iTest submits command to TestCenter REST on the Spirent device (e.g., add a stream block on the generator’s port 1, configure port, and so on).

In the TestCenter REST Console window, iTest displays the command you entered. The response from TestCenter includes settings that were implemented on the Spirent device.

> **Note：** Note While not all TestCenter commands are available using buttons or other controls on the page, you can perform any TestCenter REST command by entering it on the iTest Console view (as described in Spirent TestCenter Command reference).

You may also select an object, right-click (for e.g., on Device) to view the properties and perform a required function.

![](images/stc_rest_object_view_dropdown.png) <!-- image_ref -->

In addition, you may select an object (e.g., Port 1) and right-click, to view the object handlers and their properties, and perform the required action.

![](images/stc_rest_object_action_dropdown.png) <!-- image_ref -->

![](images/spirent_testcenter_rest.5.jpg) <!-- image_ref -->
