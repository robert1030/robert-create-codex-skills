# Session Windows > Starting a session using a session profile

You can start an interactive session in any of the following ways:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Double-click the session profile in the Favorites view

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Right-click the session profile in the Project Explorer and select Start

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- Click Start in the Session Profile editor (the New Session page).

The session starts in a new session window, as described in Session windows.

Advanced Users Many of the property settings for session profiles support field replacements to enable you to parameterize settings so they can be determined dynamically at runtime. You might use tcl, param, or profile command field replacements to improve the flexibility and portability of automated test cases. Sometimes, to perform an interactive test, you might need to manually start a session that typically starts only for automated test sessions. To enable you to do this, if any tcl, param, or profile command field replacements are encountered while starting the session, iTest starts a Tcl interpreter so that the field replacement can be resolved.

When the session ends, the Tcl interpreter is disposed. If a Tcl interpreter service is requested on restart, a new interpreter will be created and returned. See Defining a session profile (configuring the session settings).
