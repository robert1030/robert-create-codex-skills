# Session Builder > Manually Installing Custom Session Type within iTest > Install custom sessions distributed through a Central Server

Sessions built with the Session Builder may be deployed on a central server and distributed to your end-users by setting up the Update Site.

Step 1

Set up Central Site for software distribution

Go to Windows -> Preferences and set up the central site for software distribution as described in Preferences: Install/Update (Chapter , “Configuring iTest Preferences”).

![*](bullet_blue.jpg) <!-- image_ref -->

Install new session types from the central site

Select menu Help > Find and install new session types on top of the iTest window. The iTest Session Settings display with two tabs: Available Session Types and Installed Session Types.

> **Note：** Note You may get to the iTest Session Settings window via iTest > Tools > Browse on iTest store. See Install custom session type using iTest > Tools > Browse on iTest Store

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Available Session Types:

The list is retrieved and populated from a Central Server. The list shows the name of the session type, version, date created, whether licensed, description of the session, and whether includes document, if any.

![](images/07-install-custom-sessions.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

- Select the session type (s) to install and click Install.

![*](bullet_blue.jpg) <!-- image_ref -->

- Click Yes when a message displays saying that iTest needs to restart in order to apply new session type, whether you to restart iTest.

iTest restarts and the installs the selected session (s), which will be available in the list of Session Types in the Start a new session window.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Installed Session Type: Lists all the installed session types. You may uninstall session types as required. Uninstall also requires iTest to be restarted in order to apply the changes.
