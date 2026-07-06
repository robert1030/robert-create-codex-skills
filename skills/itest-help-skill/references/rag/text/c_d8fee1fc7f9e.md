# CyberFlood Session > Generate iTest test case from captured CyberFlood session

Perform these tasks in iTest Test Case editor window after capturing CyberFlood session.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- In the iTest Session window, open/select, Show View/Capture. This will display all your recorded sessions.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Create a test case with the captured session commands. Select the CyberFlood session to generate an new Test Case, right-click and select Add to new test case.

> **Note：** Note The input argument value in Step properties mirror the Steps Description column.

![](images/cf_testSteps.png) <!-- image_ref -->

> **Tip：** Tip For CyberFlood session, some fields (multi-line arguments) support JSON object and if it (JSON object) has an Array child node, use '\\\[' instead of '['.
