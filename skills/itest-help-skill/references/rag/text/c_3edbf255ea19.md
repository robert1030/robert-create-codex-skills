# Session Profiles > Masking passwords during capture and replay

You will typically want to replace password text with * characters to mask them from unauthorized use. By default, iTest replaces commands that the device does not echo with eight * characters (passwords are typically not echoed).

The default setting causes the following behavior: Before creating a Capture report, iTest masks all command text for which no echo was returned.
