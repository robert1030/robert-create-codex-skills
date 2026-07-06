# Session Builder > Creating a custom session type > Building a new Session type > 第1段

> **Note：** Note Make sure that you have QuickCall libraries defined (Defining a QuickCall) using the required session types, for example, using REST, Tcl, CMD and so on.

Follow these steps to build a custom session type based on the QuickCall library.

Step 1

Export QuickCall Library

These steps describes deriving new session type from native iTest session type and a QuickCall library using REST, Tcl, CMD and other session types.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Select File > Export from iTest GUI, and the Select window opens.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Select option ExportQuickCall Libraries to new session type and click Next.

![](images/session_builder.1.jpg) <!-- image_ref -->

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Click Next and the Select QuickCall Libraries window opens

![*](bullet_blue.jpg) <!-- image_ref -->

Select QuickCall Libraries and location to save

When the Select QuickCall Libraries window opens, select the quick call libraries and specify the location to store the custom session package.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Select the required QuickCall library from its location (All Projects, a specific project, my_project, or resource).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Select the QuickCall library(s) and indicate the export location (Export To:) by selecting iTest resource or Export to directory.

![*](bullet_blue.jpg) <!-- image_ref -->

- Selecting iTest Resource (default):

This is the default location. The custom session will be automatically installed and requires restarting iTest for the installation to take effect.

![*](bullet_blue.jpg) <!-- image_ref -->

- Selecting location as Export to directory:

Browse and select the directory to copy the custom session type. This option does not require you to restart iTest as the custom session is not installed automatically. You are required to User need to install this session Browse to the manually for use. See Manually Installing Custom Session Type within iTest for details.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Click Next and the Define New Session Type wizard displays.

![*](bullet_blue.jpg) <!-- image_ref -->

Define New Session Type wizard—QuickCall definitions validation before export
