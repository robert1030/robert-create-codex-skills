# Python Automation Library > Overview

Note iTest installer includes PyDev (Python IDE) and RED (Robot Editor) plugins for ease of your work. See the following links for more details:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- PyDev: https://marketplace.eclipse.org/content/pydev-python-ide-eclipse

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- RED: https://marketplace.eclipse.org/content/red-robot-editor

Spirent provides a Python Automation Library allowing step level interaction with iTest sessions. The library can be leveraged in your Python-based automation scripts and suites to drive commands and quick calls on multiple concurrent sessions. The library is a thin client for the following two iTest server instances:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- iTest GUI running on the local machine or on a remote host

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- A Velocity agent running on the local machine or on a remote host.

The Python library controls iTest sessions on the (GUI or agent) and enables iTest services to be consumed within Python scripts, e.g., quick calls and response maps. See Python Session Level Control Library. In addition, the iTest GUI can be used to generate example Python code from captured steps. See Python Script Generation.

The following lists the use cases of Python Automation Library:

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- To open existing session profiles (inside or outside a topology) so your Python script can:

![*](bullet_blue.jpg) <!-- image_ref -->

- Invoke quick calls with arguments.

![*](bullet_blue.jpg) <!-- image_ref -->

- Parse responses from quick calls (auto-mapped or explicitly-mapped).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- To issue native commands for CLI sessions so your Python script can:

![*](bullet_blue.jpg) <!-- image_ref -->

- Send any arbitrary command to an open session.

![*](bullet_blue.jpg) <!-- image_ref -->

- Parse responses from commands (auto-mapped or explicitly-mapped).

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- To open and control built-in session independent of a pre-existing session profile.

![*](bullet_blue_rectangle.jpg) <!-- image_ref -->

- To use Python Automation Library commands with special step properties in an opened session profile.
