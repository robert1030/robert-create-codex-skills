# Session Builder > Creating a custom session type > Building a new Session type > 第3段

- Not selected (default). When Extends the existing session is not selected, the custom Session Builder hides the native session type, and provides a command line interface and allows using the console.

> **Note：** Note Selecting Extends the existing session disables any selection in the Session Initialization option.

![*](bullet_blue.jpg) <!-- image_ref -->

- Selected. When Extends the existing session is selected, the Session Builder extends the native session type (using the GUI). For example, use this option to extend REST API with custom commands tailored for a particular need.

> **Note：** Note Both options hide the native libraries.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Inherits license from based session: Selected by default and re-uses license from the based session.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- License ID: Becomes available only when Inherits license from based session is not selected. This option allows you to add a new license to the new session type.

Tip Contact Spirent customer support to request generating a custom license for your custom session and provide the license key string you wish to use. For example string iTESTOPENSTACK#33.10.2016 for custom OpenStack Neutron session.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Select the required QuickCall or Select All from the list of usable session type in the Wizard.

When you also select a single procedure to export, from a list of displayed procedures, all the selected procedure’s dependencies will also be exported automatically as session specific commands in the custom session, if any and not selected.

For example, in a Quickcall with 3 procedures A, B, C, where C calls B, B calls A, and A contains a single step to display the Help command, selecting only procedure C to export, also exports procedures A and B as session specific commands.

![](images/session_builder.4.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- The Back, Next, Finish, and Cancel buttons become available only after you complete all the above information. The Next button allows you to attach a document to the new custom session.

![*](bullet_blue.jpg) <!-- image_ref -->

Attach User document to the new custom session

If the Next button is available, click Next to select the Document for the new session type.

![*](bullet_blue.jpg) <!-- image_ref -->

- Attach document as follows:

![*](bullet_blue.jpg) <!-- image_ref -->
